import geopandas as gpd
import matplotlib.pyplot as plt

# Dosya yolunun doğru belirtildiğinden emin olun
gdf = gpd.read_file(r'Bu kısmı kendinize göre ayarlamanız gerkeiyor. Tam dosya yolu olmmayınca bazen sıorun olabiliyor\geo-pandas\data\TUR_adm1.shp')

# Veri çerçevesini görüntüleyin
print(gdf.head())

# Geometrileri haritalandırın
gdf.plot()

plt.show()
