import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndwi(nir_band_path, green_band_path):
    # Open the NIR band raster
    with rasterio.open(nir_band_path) as nir_src:
        nir = nir_src.read(1).astype(float)
    
    # Open the green band raster
    with rasterio.open(green_band_path) as green_src:
        green = green_src.read(1).astype(float)

    # Calculate NDWI (Normalized Difference Water Index)
    ndwi = (green - nir) / (green + nir)

    return ndwi

def detect_water(ndwi, threshold=0):
    # Thresholding NDWI to detect water
    water_mask = ndwi > threshold
    return water_mask

# Example usage
nir_band_path = input('NIR Band locate: ')  # Replace with the actual path to Landsat 8 NIR band
green_band_path = input('Green Band locate: ')  # Replace with the actual path to Landsat 8 Green band

# Calculate NDWI
ndwi_result = calculate_ndwi(nir_band_path, green_band_path)

# Detect water using NDWI
water_mask = detect_water(ndwi_result)

# Visualize the water mask
plt.imshow(water_mask, cmap='Blues', vmin=0, vmax=1)
plt.colorbar(label='Water Mask')
plt.title('Surface Water Detection using NDWI')
plt.show()
