import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_ndmi(nir_band_path, swir_band_path):
    # Open the NIR band raster
    with rasterio.open(nir_band_path) as nir_src:
        nir = nir_src.read(1).astype(float)
    
    # Open the SWIR band raster
    with rasterio.open(swir_band_path) as swir_src:
        swir = swir_src.read(1).astype(float)

    # Calculate NDMI (Normalized Difference Moisture Index)
    ndmi = (nir - swir) / (nir + swir)

    return ndmi

def calculate_average(ndmi):
    # Calculate the average value for the entire area
    ndmi_average = np.nanmean(ndmi)

    return ndmi_average

# Example usage
nir_band_path = input('NIR Band locate: ')  # Replace with the actual path to Landsat 8 NIR band
swir_band_path = input('SWIR Band locate: ')  # Replace with the actual path to Landsat 8 SWIR band

# Calculate NDMI
ndmi_result = calculate_ndmi(nir_band_path, swir_band_path)

# Print the average NDMI value
ndmi_average = calculate_average(ndmi_result)
print(f'Average NDMI for the entire area: {ndmi_average}')

# Visualize the NDMI result
# plt.imshow(ndmi_result, cmap='RdYlBu', vmin=-1, vmax=1)
# plt.colorbar(label='NDMI')
# s = input('title : ')
# plt.title('Normalized Difference Moisture Index (NDMI) ' + s)
# plt.show()