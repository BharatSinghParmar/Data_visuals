Weather Data Visualization for Indian Cities 🌦️📊

Project Overview

This project provides an interactive web platform to visualize 10 years of weather data (2014-2023) for Indian cities, focusing on:
	•	Temperature at 2 Metres (t2m)
	•	Surface Pressure (sp)

The project extracts and processes large NetCDF4 datasets and visualizes the data using Bokeh for interactive scatter and line plots, served through a Flask web application.

⸻

Features ✨
	•	📈 Scatter and Line Plot Visualizations for each city.
	•	🕑 Hourly, Daily, Monthly, Yearly filtering using sliders.
	•	🌆 City Selection Dashboard to pick different Indian cities.
	•	🔄 Real-time Interactivity with dynamic updates.
	•	💾 Download-ready CSVs for processed city-specific data.
	•	🌐 Lightweight Web Application using Flask.
	•	📊 Historical trend analysis for weather researchers, students, and planners.

⸻

Tech Stack 🔧

Layer	Tools/Technologies
Backend	Flask (Python)
Data Handling	NetCDF4, Pandas, NumPy, glob, os
Frontend	Bokeh, HTML5, CSS3, JavaScript (Flask Jinja2)
Data Source	Copernicus Climate Data Store (ERA5 reanalysis)



⸻

Installation Instructions 🚀
	1.	Clone this repository:

git clone https://github.com/yourusername/weather-data-visualization.git
cd weather-data-visualization


	2.	Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


	3.	Install required packages:

pip install -r requirements.txt


	4.	(Optional): Install additional packages if missing:

pip install netCDF4 pandas bokeh flask numpy


	5.	Run the application:

python app.py


	6.	Open in browser:
Visit http://127.0.0.1:5000/

⸻

Project Structure 📁

weather-data-visualization/
├── app.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── index.html
│   ├── city_list.html
│   ├── plot_choice.html
│   ├── display.html
│   └── error.html
├── data/
│   └── CSVs for each city
├── plots/
│   └── Generated Bokeh HTML files
├── README.md
└── requirements.txt



⸻

How It Works 🛠️
	1.	Data Extraction:
Fetches NetCDF4 files from the Copernicus Climate Data Store (ERA5 dataset).
	2.	Data Processing:
	•	Reads hourly data for surface pressure and 2m temperature.
	•	Converts it into city-specific CSV files.
	•	Organizes the data for Bokeh visualizations.
	3.	Visualization:
	•	Bokeh plots are generated for scatter and line graphs.
	•	Interactive filters (Year, Month, Day, Hour) allow dynamic exploration.
	4.	Flask Web App:
	•	Renders webpages where users can select a city, plot type, and explore graphs.

⸻

Screenshots 📸

Homepage	City Selection	Plot Selection	Scatter Plot Example	Line Plot Example
				



⸻

Future Enhancements 🔮
	•	📡 Real-time weather API integration (live updates).
	•	📈 3D visualizations using Plotly or WebGL.
	•	🌍 Interactive map-based selection for cities.
	•	🤖 ML-based anomaly detection in weather patterns.
	•	📱 Mobile app version using React Native or Flutter.

⸻

Acknowledgements 🙏
	•	Copernicus Climate Data Store
	•	Bokeh Documentation
	•	Flask Documentation
	•	Python NetCDF4 Library
