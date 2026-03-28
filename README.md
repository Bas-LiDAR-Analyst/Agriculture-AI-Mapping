# Agriculture-AI-Mapping
Automated Agricultural Land Segmentation & Area Analysis
📌 Project Overview
This project demonstrates an advanced geospatial workflow to automate the identification and measurement of agricultural land parcels. Using Satellite Imagery (Sentinel-2), Google Earth Engine (GEE), and AI-driven segmentation (Segment Anything Model - SAM), the system extracts precise farm boundaries and calculates their spatial area automatically.

🚀 Features
Data Acquisition: Automated retrieval of Sentinel-2 Level-2A surface reflectance data via Google Earth Engine.

AI Segmentation: Implementation of Meta's Segment Anything Model (SAM) with a Vision Transformer (ViT-H) backbone for zero-shot boundary detection.

High-Resolution Upscaling: Processing imagery at 1m/px resolution to ensure accuracy in small-scale farming plots.

Automated Mensuration: Python-based calculation of farm areas in both Square Meters and Acres.

GIS Integration: Seamless export to QGIS for symbology and Felt.com for interactive web mapping.

🛠️ Tech Stack
Languages: Python (Rasterio, NumPy, Pandas)

Cloud Platforms: Google Earth Engine, Google Colab (GPU: NVIDIA T4)

AI Models: segment-geospatial (SAM)

GIS Tools: QGIS 3.x, Felt.com

📊 Methodology
Preprocessing: Filtered Sentinel-2 imagery for low cloud cover and applied a visualization parameters (visualize()) to convert multi-spectral data into AI-ready RGB format.

Inference: Loaded the SAM model on a CUDA-enabled environment to generate high-fidelity masks.

Data Extraction: Converted AI masks into geospatial raster/vector formats.

Analysis: Ran a custom Python script to iterate through unique Farm IDs and compute geometric area based on pixel resolution.

📈 Results
Successfully delineated complex farm boundaries in the Ganges River Basin.

Generated a comprehensive CSV report containing unique IDs and corresponding area measurements.

Produced an interactive map ready for stakeholder review on Felt.com.

📬 Contact
Bhaskar Geospatial Analyst & AI Enthusiast https://www.upwork.com/freelancers/~01eba65a57237b10a7 | https://www.linkedin.com/in/bhaskar-m-00b7283b6/
