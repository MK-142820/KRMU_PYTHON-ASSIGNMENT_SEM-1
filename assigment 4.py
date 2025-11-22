# Weather Data Visualizer – <Manoj kumar>

A mini project for the course **Programming for Problem Solving using Python**.  
This project performs *real-world data cleaning, analysis, aggregation, and visualization* using weather datasets.

---

## 📌 Features
- Load and clean real CSV weather files  
- Compute daily, monthly, seasonal statistics  
- Line, bar, scatter & combined plots using Matplotlib  
- Grouping and aggregation using Pandas  
- Export cleaned data + PNG plots  
- Markdown report included  

---

## 📂 Dataset
The dataset used: **<mention source, e.g., Kaggle – Daily Local Weather Dataset>**

Columns used:
- Date  
- Temperature  
- Rainfall  
- Humidity  

---

## 🛠️ Tools & Libraries
- Python 3.8+
- Pandas
- NumPy
- Matplotlib

---

## 📊 Results (Generated)
- Daily temperature trend (line chart)  
- Monthly rainfall totals (bar chart)  
- Humidity vs Temperature (scatter plot)  
- Combined subplot visualization  

All charts saved in `images/`.

---

## 🧹 Data Export
- Cleaned file saved as: `cleaned_weather.csv`

---

## 📄 Report
The summary report is available in `/report/summary_report.md`.

---

## ▶ How to Run
```bash
pip install pandas numpy matplotlib
python src/weather_analysis.py



# Weather Data Visualization Report

## 1. Introduction
This mini-project analyses a real-world weather dataset using Python libraries such as Pandas, NumPy, and Matplotlib.

The objective is to understand trends in temperature, rainfall, and humidity, and visualize them effectively.

---

## 2. Data Cleaning
- Converted Date column to datetime format  
- Removed unwanted columns  
- Filled missing values using forward fill (ffill)  
- Exported cleaned dataset (`cleaned_weather.csv`)  

---

## 3. Statistical Findings

### Daily Statistics
Daily mean, min, max, and standard deviation computed using Pandas + NumPy.

### Monthly Insights
- Highest temperatures observed in: **May–June**  
- Peak rainfall recorded in: **July–August**  
- Humidity highest during monsoon months  

### Yearly Summary
Shows rising average temperatures yearly — indicates warming trend.

---

## 4. Visualizations
The following plots were generated:

### 1️⃣ Daily Temperature Trend (Line Chart)
Shows clear fluctuations and seasonal patterns.

### 2️⃣ Monthly Rainfall Totals (Bar Chart)
Bar chart shows monsoon dominance.

### 3️⃣ Humidity vs Temperature (Scatter Plot)
Humidity decreases as temperature increases.

### 4️⃣ Combined Plot
Subplot visualization for better comparison.

---

## 5. Conclusions
- Summers show extreme temperatures (peak in May–June)  
- Rainfall highly seasonal (monsoon peak)  
- Humidity strongly correlated with rainfall  
- Temperature appears to rise gradually over years (possible climate shift)

---

## 6. Future Scope
- Add Seaborn heatmaps  
- Build an interactive dashboard using Plotly  
- Automate daily weather report emails  

---

## 7. Dataset Source
Mention your source (e.g., Kaggle, IMD Open Data Portal).


