# Residential Investment Walkability Analysis

A data-driven approach to identifying high-potential residential investment opportunities through walkability and livability metrics.

## 📊 Project Overview

This analysis examines the relationship between walkability scores, property values, and livability indicators to help residential investors make informed decisions. The project uses mock data simulating real-world urban metrics to identify investment-worthy suburbs.

## 🎯 Key Objectives

- Analyze correlations between walkability and property values
- Identify top-performing suburbs based on combined metrics
- Cluster neighborhoods into investment profiles
- Provide actionable insights for residential investors

## 📁 Project Structure

walkability-analysis/
├── data/
│ └── walkability_scores.csv
├── notebooks/
│ └── walkability_analysis.ipynb
├── media/
│ ├── Figure_1.png
│ ├── Figure_2.png
│ ├── Figure_3.png
│ └── Figure_4.png
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## 🛠️ Installation & Requirements

```bash
pip install pandas numpy matplotlib scikit-learn jupyter

```

## 📈 Methodology
### Data Processing
- Created combined score: 60% walk_score + 40% distance_to_transit

- Standardized features for clustering analysis

- Correlation analysis across all numeric variables

### Analytical Techniques
- Descriptive statistics and ranking

- Correlation heatmap visualization

- K-means clustering (3 clusters)

- Comparative scatter plots

## 🔍 Key Findings
### Top Performers
- Fortitude Valley: Highest walk score (92), premium property values

- South Brisbane: Strong walkability (88) with high livability (95)

- Clear correlation between walkability and property values

### Investment Clusters
- Cluster 0: High walkability, premium suburbs

- Cluster 1: Moderate walkability, balanced value

- Cluster 2: Lower walkability, potential opportunities

### Strong Correlations
- Walk score positively correlates with livability index

- Inverse relationship between transit distance and walkability

## 🎯 Business Implications
### For Investors:

- Target high-walk-score suburbs for premium returns

- Consider transit access as key value driver

- Use clustering to identify neighborhood profiles

**Tagline:** "Walkable neighborhoods drive valuable investments—discover where to buy next."

## ⚠️ Assumptions & Limitations
- Combined score weights: 60% walkability, 40% transit access

- Mock data used for demonstration purposes

- Linear relationships assumed between metrics

- Limited to 5 sample suburbs in current dataset

🚀 Usage
python
# Run the analysis
```bash
python src/__init__.py
```

📊 Sample Results
[Link](https://docs.google.com/document/d/1pnPSvSB-bAxJKnLF6Zkx9ETHSBTcBlde3VJW8vfBk2o/edit?tab=t.0)

## 🤝 Contributing
This is a mock analysis for educational and demonstration purposes. Real-world applications would require more comprehensive data and validation.

## 📄 License
MIT License - feel free to adapt for your investment analysis needs.

## Quick Insights:

**Investor Interpretation:** Target high-walk-score suburbs like Fortitude Valley where walkability correlates with higher property values and livability

**Accuracy Note:** Limited by mock data but illustrates realistic urban trends for strategic insight

**Key Assumption:** Walk score (60%) and transit distance (40%) directly influence property appeal and value