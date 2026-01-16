# Rainfall–Runoff Modeling for Niger Delta River Basins Using Hydrological ML

This project applies machine learning to simulate rainfall–runoff processes in Niger Delta river basins using realistic synthetic hydro-meteorological data. It integrates data generation, predictive modeling, and GIS-based runoff and flood-risk mapping.

## 📌 Features
- Synthetic rainfall–runoff dataset generation
- Random Forest–based runoff prediction
- Model evaluation (RMSE, R²)
- GIS runoff mapping (GeoTIFF)
- Flood-prone zone extraction (Shapefiles)

## 🧪 Technologies Used
- Python
- NumPy, Pandas
- Scikit-learn
- Matplotlib
- Rasterio, Fiona (GIS)

## 📂 Dataset
Synthetic daily data includes:
- Rainfall (mm)
- Temperature (°C)
- Evapotranspiration (mm)
- Soil moisture index
- River discharge (m³/s)

## 🗺️ GIS Outputs
- Runoff intensity raster (GeoTIFF)
- Flood-risk polygons (Shapefile)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/rainfall_runoff_niger_delta_ml.py
📊 Applications
Flood risk assessment

Basin-scale hydrological analysis

Climate and land-use impact studies

Academic research and ML demonstrations

⚠️ Disclaimer
All data used are synthetic and intended for research, teaching, and model prototyping only.

👤 Author
Ebingiye Nelvin Agbozu

yaml
Copy code

---

## 📁 Recommended Project Structure

Rainfall-Runoff-Niger-Delta-ML/
│
├── README.md
├── requirements.txt
│
├── data/
│ ├── raw/
│ │ └── niger_delta_rainfall_runoff_dataset.xlsx
│ └── processed/
│
├── src/
│ ├── rainfall_runoff_niger_delta_ml.py
│ ├── gis_runoff_mapping.py
│
├── outputs/
│ ├── figures/
│ │ ├── runoff_timeseries.png
│ │ └── feature_importance.png
│ │
│ └── gis/
│ ├── niger_delta_runoff_map.tif
│ └── niger_delta_flood_zones.shp
│
├── notebooks/
│ └── exploratory_analysis.ipynb
│
└── docs/
└── methodology.md

yaml
Copy code

---

## 🧾 `requirements.txt` (optional)
```txt
numpy
pandas
matplotlib
scikit-learn
rasterio
fiona
