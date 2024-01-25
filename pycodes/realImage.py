import rasterio
import numpy as np
import matplotlib.pyplot as plt

def create_enhanced_true_color_image(nir_band_path, red_band_path, green_band_path, blue_band_path, output_image_path, brightness_factors=None, output_size_factor=2):
    # Open the bands
    with rasterio.open(nir_band_path) as nir_src, rasterio.open(red_band_path) as red_src, rasterio.open(green_band_path) as green_src, rasterio.open(blue_band_path) as blue_src:
        nir = nir_src.read(1).astype(float)
        red = red_src.read(1).astype(float)
        green = green_src.read(1).astype(float)
        blue = blue_src.read(1).astype(float)

    # Apply brightness adjustment if provided
    if brightness_factors is not None:
        red *= brightness_factors.get('red', 1.0)
        green *= brightness_factors.get('green', 1.0)
        blue *= brightness_factors.get('blue', 1.0)

    # Normalize the bands to the 0-1 range
    nir = nir / 65535.0
    red = red / 65535.0
    green = green / 65535.0
    blue = blue / 65535.0

    # Stack the bands to create an enhanced true color image
    enhanced_true_color_image = np.stack([red, green, blue], axis=-1)

    # Clip values to the valid range [0, 1]
    enhanced_true_color_image = np.clip(enhanced_true_color_image, 0, 1)

    # Double the image size
    output_size = (enhanced_true_color_image.shape[1] * output_size_factor, enhanced_true_color_image.shape[0] * output_size_factor)

    # Save the enhanced true color image with doubled size
    plt.figure(figsize=(output_size[0]/100, output_size[1]/100))  # Set figure size in inches
    plt.imsave(output_image_path, enhanced_true_color_image)

    # Display the enhanced true color image
    plt.imshow(enhanced_true_color_image)
    plt.title('Enhanced True Color Image')
    plt.show()

# Example usage
nir_band_path = r'D:\Research\PlaeBlueDot\landsat-8\CL\CLRT_LC08_L2SP_191054_20210223_20210303_02_T1_SR_B5.tif'  # Replace with the actual path to Landsat 8 NIR band
red_band_path = r'D:\Research\PlaeBlueDot\landsat-8\CL\CLRT_LC08_L2SP_191054_20210223_20210303_02_T1_SR_B4.tif'  # Replace with the actual path to Landsat 8 Red band
green_band_path = r'D:\Research\PlaeBlueDot\landsat-8\CL\CLRT_LC08_L2SP_191054_20210223_20210303_02_T1_SR_B3.tif'  # Replace with the actual path to Landsat 8 Green band
blue_band_path = r'D:\Research\PlaeBlueDot\landsat-8\CL\CLRT_LC08_L2SP_191054_20210223_20210303_02_T1_SR_B2.tif'  # Replace with the actual path to Landsat 8 Blue band
output_image_path = 'enhanced_true_color_image.png'  # Replace with the desired output image path

# Adjust brightness factors to increase brightness
brightness_factors = {'red': 5, 'green': 5, 'blue': 5}

# Set the output size factor (e.g., 2 for doubling the size)
output_size_factor = 2

create_enhanced_true_color_image(nir_band_path, red_band_path, green_band_path, blue_band_path, output_image_path, brightness_factors, output_size_factor)