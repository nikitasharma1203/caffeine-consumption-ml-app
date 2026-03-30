![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Deployed-success)

### 🌐 Live Demo
https://caffeine-consumption-ml-app-cswxdgjaeyhngcyhzq9atk.streamlit.app/

# Caffeine Consumption Analysis & ML-Based Intake Calculator
End-to-end data science project that evolved from a statistical research study into a machine learning powered Python application with an interactive Streamlit dashboard.

This project demonstrates skills across data collection, statistical analysis, machine learning, and deployment.

### Project Summary and Problem Statement
Conducted a large-scale survey-based statistical study on caffeine consumption among university students

Applied hypothesis testing, non-parametric statistics, and data visualization in R

Upgraded the project into a machine learning workflow in Python and used clustering, PCA, regression, classification and outlier detection

Built and deployed a real-time caffeine intake calculator web app

### Live Application – Caffeine Intake Calculator
#### Features:
* Multi-drink session tracking
* Brand-wise caffeine estimation
* Personalized safe caffeine limit based on body weight
* Visual feedback for safe vs excessive intake

## Machine Learning 
Analyzed caffeine intake patterns across demographics

Exam vs regular day consumption modeling

Feature-driven prediction and behavior analysis

Model evaluation using appropriate metrics

## Repository structure
caffeine-consumption-ml/ 
│ 
├── caffeine_calculator/ 
│ └── app.py # solo 
│ 
├── machine_learning/
│ └── ml.ipynb # solo 
│ 
├── data/ 
│ ├── analysis.csv # group 
│ ├── market data.xlsx 
│ └── Pilot Study.Data.xlsx │ 
├── statistical-analysis/ # group 
│ ├── REPORT.pdf 
│ └── Questionnaire.docx
│ 
├── requirements.txt 
└── README.md


## Contribution & Project Ownership

This repository represents a **two-phase project**:

### Phase 1 – Statistical Analysis (Group Project)
- Conducted as a **group academic project** during the previous academic year
- Included survey design, data collection, questionnaire development, and statistical analysis
- Group report, datasets, and questionnaires are included **for academic context and continuity**
- Investigates caffeine consumption among science faculty students through surveys, market data, and chemical analysis. It explores brand preferences, intake patterns across genders and academic years, and the impact on sleep and focus. Statistical methods such as reliability testing, normality checks, parametric and non-parametric tests were applied to validate findings. Results show higher caffeine intake during exams, significant links between consumption and reduced sleep quality, and taste, focus, and staying awake as primary drivers of use. The study highlights both lifestyle influences and health concerns, offering evidence-based insights for student wellness monitoring.


### Phase 2 – Machine Learning & Application (Solo Work)
- Independently upgraded and extended the project in the current academic year
- Designed and implemented:
  - Machine learning workflows in Python
  - Feature engineering and modeling
  - Streamlit-based caffeine intake calculator
- Responsible for **all code, app development, deployment, and documentation** in this phase
- This machine learning extension analyzes caffeine consumption patterns among 320 university students. The pipeline covers regression, classification, clustering, PCA, and outlier detection. Regression models predict exam-day intake from regular habits with strong performance (R² ≈ 0.75), showing tea and spending as key drivers. Classification experiments grouped students into Very Low, Low, Medium, and High consumers, with linear SVM achieving ~70% accuracy and outperforming tree-based models. PCA reduced six beverage features to two components, retaining ~43% variance, highlighting mainstream vs. alternative choices and intensity of preference. K-Means clustering (k=5, silhouette ≈ 0.52) revealed personas: Light Consumers, Moderate Consumers, Exam Spikers, and rare Extreme Consumers. Outlier detection flagged ~10% of students with unusually high exam spending (up to ₹210/day). Together, these methods provide predictive insights, behavioral segmentation, and wellness-oriented recommendations for caffeine use under academic stress.

**All Python ML code, Streamlit app, README, and deployment are solely my individual work.**
