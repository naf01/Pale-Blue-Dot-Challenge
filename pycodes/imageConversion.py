import rasterio
import numpy as np
import matplotlib.pyplot as plt

def convert_land_water(red_band_path, nir_band_path, output_path):
    # Open the red band raster
    with rasterio.open(red_band_path) as red_src:
        red = red_src.read(1).astype(float)

    # Open the near-infrared (NIR) band raster
    with rasterio.open(nir_band_path) as nir_src:
        nir = nir_src.read(1).astype(float)

    # Calculate the Normalized Difference Vegetation Index (NDVI)
    ndvi = (nir - red) / (nir + red)

    # Threshold NDVI to identify land and water
    threshold = 0.2
    land_mask = ndvi > threshold

    # Create a binary mask where land is True and water is False
    binary_mask = np.zeros_like(land_mask, dtype=np.uint8)
    binary_mask[land_mask] = 255  # Set land areas to white (255)

    # Write the binary mask to a new GeoTIFF file
    with rasterio.open(output_path, 'w', driver='GTiff', width=red_src.width, height=red_src.height,
                       count=1, crs=red_src.crs, transform=red_src.transform, dtype='uint8') as dst:
        dst.write(binary_mask, 1)

# Example usage
red_band_path = r'D:\Research\PlaeBlueDot\CLIP\CLIP\clipLC08_L2SP_138043_20201218_20210309_02_T1_SR_B4.tif'  # Replace with the actual path to Landsat 8 Red band
nir_band_path = r'D:\Research\PlaeBlueDot\CLIP\CLIP\clipLC08_L2SP_138043_20201218_20210309_02_T1_SR_B5.tif'  # Replace with the actual path to Landsat 8 NIR band
output_mask_path = 'land_water_mask.tif'  # Replace with the desired output path

convert_land_water(red_band_path, nir_band_path, output_mask_path)

# Visualize the result
with rasterio.open(output_mask_path) as mask_src:
    plt.imshow(mask_src.read(1), cmap='gray')
    plt.title('Land (White) and Water (Black) Mask')
    plt.show()
