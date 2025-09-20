def load_words_from_file(filename):
    """Dosyadan kelimeleri ve karşılıklarını yükler."""
    words_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line or ':' in line:
                # ':' veya '=' karakterine göre ayır
                if '=' in line:
                    word, translation = line.strip().split('=', 1)
                else:
                    word, translation = line.strip().split(':', 1)
                # Sözlüğe ekle
                words_dict[word.strip()] = translation.strip()
    return words_dict

def extract_english_words(words_dict):
    """Sözlükten İngilizce kelimeleri ayıklar."""
    return list(words_dict.keys())

def save_words_to_file(words_list, output_filename):
    """İngilizce kelimeleri belirtilen dosyaya kaydeder."""
    with open(output_filename, 'w', encoding='utf-8') as file:
        for word in words_list:
            file.write(word + '\n')

# Kelimeleri yükle
input_filename = 'words.txt'
words_dict = load_words_from_file(input_filename)

# İngilizce kelimeleri ayıkla
english_words = extract_english_words(words_dict)

# İngilizce kelimeleri başka bir dosyaya kaydet
output_filename = 'english_words.txt'
save_words_to_file(english_words, output_filename)

print(f"Ingilizce kelimeler '{output_filename}' dosyasına kaydedildi.")
