# HyPySpectral - Hyperspectral Image Analysis Toolbox for Python

## Introduction
HyPySpectral is a Python package for reading, processing, analysing, and visualising hyperspectral images. Many of these tools are suitable for remote sensing and feature selection tasks, however, requests for new features in other fields are encouraged.

## Planned Features
### Input and Output
- AVIRIS 
- ENVI Standard reading and writing from and to header and binary
- ASD file import (i.e., USGS Spectral Library)
- GeoTIFF
- Generic multiband image loading

### Visualisation and Utilities
- Rendering of VNIR to RGB 
- Psedo and False Colouration 
- Hyperspectral datacube 3D rendering
- Radiometric Correction
- Save visualisations to file

### Classification
- K-means Clustering
- K-nearest neighbour Clustering
- LibSVM support

### Dimensionality Reduction
- Principal Component Analysis (PCA)
  - PCA Variants
- Linear Discriminant Analysis (LDA)
- Maximum/Minimum Noise Fraction (MNF)
- Independent Component Analysis (ICA-DR)

### Band Selection
- WaLuMi 
- WaLuDi 

### Target/Anomaly Detection
- Adaptive Cosine/Coherence Estimator (ACE)
- Matched Filter (MF)
- Constrained Energy Minimisation (CEM)
- Generalised Likelihood Ratio Test (GLRT)
- Orthogonal Subspace Detector (OSP)
- Reed-Xiaoli Detector (RXD)
  - RXD Variants

### Endmember Estimation
- SMACC
- VCA
- ICA-EEA
- Harsanyi-Farrand-Chang Virtual Dimensionality (HFC-VD)

### Spectral Comparison
- Spectral Angle Mapper (SAM)
- Spectral Information Divergence (SID)
- SID-SAM Hybrid Method

### Remote Sensing Indices
- Normalised Difference Vegetation Index (NDVI)
  - NDVI variants
- Normalised Difference Water Index (NDWI)
- Normalised Difference Snow Index (NDSI)
- Built-up Indices
- Soil Indices

### Georectification
- GLT referencing


## Installation
HyPySpectral is hosted on ```PyPi``` so can be installed simply using the following:

```
pip install HyPySpectral
```

## Contact
Feel free to report any bugs/request new features by contacting us at XX.XX.
