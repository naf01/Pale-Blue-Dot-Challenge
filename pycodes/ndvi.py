import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndvi(red_band_path, nir_band_path, output_ndvi_path):
    # Open the red band raster
    with rasterio.open(red_band_path) as red_src:
        red = red_src.read(1).astype(float)
    
    # Open the near-infrared (NIR) band raster
    with rasterio.open(nir_band_path) as nir_src:
        nir = nir_src.read(1).astype(float)

    # Calculate NDVI
    ndvi = (nir - red) / (nir + red)

    # Set any potential division by zero to NaN (e.g., when both NIR and Red are 0)
    ndvi[np.isinf(ndvi)] = np.nan

    # Write the NDVI raster to a new GeoTIFF file
    with rasterio.open(output_ndvi_path, 'w', driver='GTiff', width=red_src.width, height=red_src.height, 
                       count=1, crs=red_src.crs, transform=red_src.transform, dtype='float32') as dst:
        dst.write(ndvi, 1)

    return ndvi

# Example usage
red_band_path = input('Band4 locate : ')  # Replace with the actual path to Landsat 8 Red band
nir_band_path = input('Band5 locate : ')  # Replace with the actual path to Landsat 8 NIR band
output_ndvi_path = 'output_ndvi.tif'  # Replace with the desired output path

ndvi_result = calculate_ndvi(red_band_path, nir_band_path, output_ndvi_path)

# Visualize the NDVI result
plt.imshow(ndvi_result, cmap='RdYlGn')
plt.colorbar(label='NDVI')
s = input('title : ')
plt.title('Normalized Difference Vegetation Index (NDVI) '+s)
plt.show()
