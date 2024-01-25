import rasterio
import numpy as np
import matplotlib.pyplot as plt

def calculate_esi(thermal_band_path_10):
    # Open the thermal infrared band 10
    with rasterio.open(thermal_band_path_10) as tirs10_src:
        tirs10 = tirs10_src.read(1).astype(float)

    # Calculate Land Surface Temperature (LST) using the brightness temperature formula
    lst = tirs10 / 1260.56 - 1.0

    # Calculate ESI (Evaporative Stress Index)
    esi = (1.5 * (tirs10 - lst)) / (tirs10 + 15)

    # Set any potential division by zero to NaN
    esi[np.isinf(esi)] = np.nan

    # Calculate the average ESI for the entire area
    esi_average = np.nanmean(esi)

    return esi, esi_average

def perform():
    # Example usage
    thermal_band_path_10 = input('Thermal Band 10 locate: ')  # Replace with the actual path to Landsat 8 Thermal Band 10

    # Calculate ESI and average ESI for the entire area
    esi, esi_average = calculate_esi(thermal_band_path_10)

    # Print the average ESI value
    print(f'Average Evaporative Stress Index (ESI) for the entire area: {esi_average}')

    # Visualize the ESI result
    plt.imshow(esi, cmap='RdYlBu_r', vmin=-1, vmax=1)
    plt.colorbar(label='ESI')
    s = input('title : ')
    plt.title('Evaporative Stress Index (ESI) ' + s)
    plt.show()

for i in range(7):
    perform()