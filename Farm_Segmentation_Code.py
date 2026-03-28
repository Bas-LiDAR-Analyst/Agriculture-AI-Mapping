# Step 1: Install the necessary geospatial AI libraries
!pip install segment-geospatial

import os
from samgeo import SamGeo

# Step 2: Initialize the Segment Anything Model (SAM) 
# We use the 'vit_h' (Vision Transformer Huge) model on the GPU (cuda)
sam = SamGeo(model_type="vit_h", device='cuda')

# Step 3: Define file paths
# Ensure the input file was uploaded to the /content/ directory in Colab
input_raster = "/content/Ganga_Farms_SAM_Ready.tif"
output_raster = "Ganga_Final_Farms_Map.tif"

# Step 4: Run the automated segmentation
if os.path.exists(input_raster):
    print("Input file detected. Starting AI boundary extraction...")
    # This process analyzes pixels and generates vector-like masks for farm plots
    sam.generate(input_raster, output=output_raster, foreground=True, unique=True)
    print(f"Success! The segmented map has been saved as: {output_raster}")
else:
    print("Error: Input file not found. Please upload the GeoTIFF to the sidebar.")
  
  import rasterio
import numpy as np
import pandas as pd

# Load the segmented map you created
file_path = "/content/Ganga_Final_Check.tif"

with rasterio.open(file_path) as src:
    # Read the raster data
    data = src.read(1)
    # Get pixel resolution (size of one pixel in meters)
    res = src.res[0] 
    
    # Identify unique farm IDs and count pixels for each
    unique, counts = np.unique(data, return_counts=True)
    
    # Calculate area: (Number of pixels * Area of one pixel)
    # Area of one pixel = resolution * resolution
    pixel_area = res * res
    areas = counts * pixel_area
    
    # Create a table (DataFrame) for easy viewing
    # We skip ID 0 as it usually represents the background
    df = pd.DataFrame({'Farm_ID': unique[1:], 'Area_SqMeters': areas[1:]})

print("Calculated Farm Areas Successfully!")
# Display first 10 farm areas
print(df.head(10))

# Save this data as a CSV file to download
df.to_csv("Ganga_Farm_Areas.csv", index=False)
