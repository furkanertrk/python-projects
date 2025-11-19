import time
import psutil
import pynvml  # NVIDIA GPU verileri için
from datetime import datetime
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Console
from rich import box

# --- GPU Başlatma (Hata yönetimi ile) ---
GPU_AVAILABLE = False
try:
    pynvml.nvmlInit()
    GPU_AVAILABLE = True
except:
    pass

def get_size(bytes, suffix="B"):
    """Bayt cinsinden veriyi okunabilir formata çevirir (1024KB, 10MB vs)"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_cpu_panel():
    """İşlemci Bilgileri"""
    cpu_usage = psutil.cpu_percent(interval=0)
    cpu_freq = psutil.cpu_freq()
    
    # Çekirdek bazlı kullanım (Bar grafiği)
    per_cpu = psutil.cpu_percent(interval=0, percpu=True)
    
    table = Table(box=None, expand=True)
    table.add_column("Çekirdek", style="cyan")
    table.add_column("Yük", style="magenta")
    table.add_column("Grafik", style="green")

    # İlk 8 çekirdeği gösterelim (Yer kaplamasın diye)
    for i, usage in enumerate(per_cpu[:8]):
        bar_count = int(usage / 10)  # 10 blokluk bar
        bar = "█" * bar_count + "░" * (10 - bar_count)
        table.add_row(f"Core {i+1}", f"%{usage:.1f}", bar)

    if len(per_cpu) > 8:
         table.add_row("...", "...", "...")

    freq_text = f"{cpu_freq.current:.0f} MHz" if cpu_freq else "N/A"
    
    summary = f"\n[bold cyan]Genel Kullanım:[/bold cyan] [bold green]%{cpu_usage}[/bold green]\n" \
              f"[bold cyan]Frekans:[/bold cyan] {freq_text}\n" \
              f"[bold cyan]Mantıksal Çekirdek:[/bold cyan] {psutil.cpu_count()}"
              
    return Panel(
        Text.from_markup(summary) + table, 
        title="[b]⚡ CPU (İşlemci)[/b]",
        border_style="blue"
    )

def generate_cpu_table():
    cpu_freq = psutil.cpu_freq()
    table = Table(expand=True, border_style="blue", box=box.ROUNDED)
    table.add_column("CPU Metrik", style="cyan")
    table.add_column("Değer", style="green", justify="right")
    
    table.add_row("Genel Kullanım", f"%{psutil.cpu_percent()}")
    if cpu_freq:
        table.add_row("Frekans", f"{cpu_freq.current:.0f} MHz")
    table.add_row("Çekirdek Sayısı", str(psutil.cpu_count()))
    table.add_row("İşlem Sayısı", str(len(psutil.pids())))
    
    return Panel(table, title="⚡ CPU Monitörü", border_style="blue")

def generate_ram_table():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    table = Table(expand=True, border_style="magenta", box=box.ROUNDED)
    table.add_column("Bellek", style="magenta")
    table.add_column("Durum", justify="right")
    
    # Görsel Bar
    used_percent = mem.percent
    bar_length = 20
    filled = int(bar_length * used_percent / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    table.add_row("RAM Kullanımı", f"{bar} %{used_percent}")
    table.add_row("Toplam", get_size(mem.total))
    table.add_row("Kullanılan", get_size(mem.used))
    table.add_row("Boşta", get_size(mem.available))
    
    return Panel(table, title="💾 RAM (Bellek)", border_style="magenta")

def generate_gpu_table():
    if not GPU_AVAILABLE:
        return Panel("NVIDIA Sürücüsü Bulunamadı", title="🎮 GPU", border_style="red")
    
    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(0) # İlk ekran kartı
        
        name = pynvml.nvmlDeviceGetName(handle)
        
        if isinstance(name, bytes):
            name = name.decode('utf-8')
        # -----------------------

        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
        
        table = Table(expand=True, border_style="green", box=box.ROUNDED)
        table.add_column("GPU Metrik", style="green")
        table.add_column("Değer", style="white", justify="right")
        
        table.add_row("Model", name)
        table.add_row("GPU Yükü", f"%{util.gpu}")
        table.add_row("Sıcaklık", f"{temp}°C")
        table.add_row("VRAM Kullanımı", f"{get_size(mem_info.used)} / {get_size(mem_info.total)}")
        
        return Panel(table, title="🎮 GPU (NVIDIA)", border_style="green")
    except Exception as e:
        return Panel(f"GPU Okuma Hatası: {e}", title="🎮 GPU", border_style="red")

def generate_network_panel(last_sent, last_recv):
    net = psutil.net_io_counters()
    
    # Anlık hız hesabı (Bytes per second)
    # Bu fonksiyon her 1 saniyede bir çağrıldığı için fark direkt hızı verir
    speed_sent = net.bytes_sent - last_sent
    speed_recv = net.bytes_recv - last_recv
    
    table = Table(expand=True, border_style="yellow", box=box.ROUNDED)
    table.add_column("Ağ", style="yellow")
    table.add_column("Hız / Toplam", justify="right")
    
    table.add_row("⬇️ İndirme Hızı", f"[bold green]{get_size(speed_recv)}/s[/bold green]")
    table.add_row("⬆️ Yükleme Hızı", f"[bold blue]{get_size(speed_sent)}/s[/bold blue]")
    table.add_row("Toplam İndirilen", get_size(net.bytes_recv))
    table.add_row("Toplam Yüklenen", get_size(net.bytes_sent))
    
    return Panel(table, title="🌐 Ağ Trafiği", border_style="yellow"), net.bytes_sent, net.bytes_recv

def make_layout():
    """Ekran düzenini oluşturur"""
    layout = Layout(name="root")
    
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    
    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    
    layout["left"].split_column(
        Layout(name="cpu"),
        Layout(name="ram")
    )
    
    layout["right"].split_column(
        Layout(name="gpu"),
        Layout(name="network")
    )
    
    return layout

def main():
    layout = make_layout()
    
    # Header
    layout["header"].update(Panel(Text("🚀 Sistem Monitörü (Dashboard)", justify="center", style="bold white on blue"), style="blue"))
    
    # Footer
    layout["footer"].update(Panel(Text("Çıkış için Ctrl+C'ye basın...", justify="center", style="italic grey50"), style="grey50"))

    # Ağ hızı için başlangıç değerleri
    net_init = psutil.net_io_counters()
    last_sent = net_init.bytes_sent
    last_recv = net_init.bytes_recv

    # Live Context Manager: Ekranı sürekli yeniler
    with Live(layout, refresh_per_second=1, screen=True) as live:
        while True:
            try:
                # Panelleri Güncelle
                layout["cpu"].update(generate_cpu_table())
                layout["ram"].update(generate_ram_table())
                layout["gpu"].update(generate_gpu_table())
                
                net_panel, new_sent, new_recv = generate_network_panel(last_sent, last_recv)
                layout["network"].update(net_panel)
                
                # Değerleri güncelle
                last_sent = new_sent
                last_recv = new_recv
                
                time.sleep(1)
                
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    main()