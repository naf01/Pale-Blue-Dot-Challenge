import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndvi(red_band_path, nir_band_path):
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

    # Calculate the average NDVI for the entire area
    ndvi_average = np.nanmean(ndvi)

    return ndvi, ndvi_average

# Example usage
red_band_path = input('Band4 locate : ')  # Replace with the actual path to Landsat 8 Red band
nir_band_path = input('Band5 locate : ')  # Replace with the actual path to Landsat 8 NIR band

# Calculate average NDVI for the entire area
ndvi, ndvi_average = calculate_ndvi(red_band_path, nir_band_path)

# Print the average NDVI value
print(f'Average NDVI for the entire area: {ndvi_average}')

# Write the NDVI raster to a new GeoTIFF file
output_ndvi_path = 'output_ndvi.tif'  # Replace with the desired output path
with rasterio.open(red_band_path) as src:
    profile = src.profile
    profile.update(dtype=rasterio.float32)

with rasterio.open(output_ndvi_path, 'w', **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

# Visualize the NDVI result
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
s = input('title : ')
plt.title('Normalized Difference Vegetation Index (NDVI) '+s)
plt.show()
