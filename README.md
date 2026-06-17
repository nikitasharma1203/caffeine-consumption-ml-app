# Caffeine Consumption Analytics & Intake Calculator

<p align="center">

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://caffeine-consumption-ml-app-cswxdgjaeyhngcyhzq9atk.streamlit.app)

</p>

An end-to-end analytics project studying caffeine consumption among university students, combining survey statistics, chemical assays, machine learning, and an interactive Streamlit application.

</p>

<p align="center">

**Phase 1 (Group Thesis)**  
Survey design • Sampling • Chemical assays • Statistical inference

**Phase 2 (Independent Extension)**  
Machine Learning • Clustering • PCA • Outlier Detection • Streamlit Application

---

## Demo

<p align="center">

<!-- Replace with screenshots -->

<img src="caffeine_calculator/app_dash.png" width="750"/>

</p>

---

## Key Highlights

- Collected and analyzed survey responses from **320 university students**.
- Conducted **iodometric back-titration assays** to estimate caffeine concentrations of popular campus beverages.
- Applied non-parametric statistical methods including:
  - Wilcoxon Rank Sum Test
  - Kruskal-Wallis Test
  - Jonckheere-Terpstra Trend Test
  - Shapiro-Wilk Normality Test
- Built machine learning pipelines for:
  - Regression
  - Multi-class Classification
  - PCA
  - K-Means Clustering
  - Outlier Detection
- Developed a Streamlit caffeine calculator using lab-verified caffeine concentrations and personalized intake thresholds.

---

## Repository Structure

```text
caffeine-consumption-ml/

├── statistical-analysis/
│   ├── REPORT.pdf
│   └── Questionnaire.docx

├── data/
│   ├── analysis.csv
│   ├── market_data.xlsx
│   └── Pilot_study_Data.xlsx

├── machine_learning/
│   └── ml.ipynb

└── caffeine_calculator/
    └── app.py
```

---

## Background

This project originated as a **B.Sc. (Hons.) Statistics thesis** at **The Maharaja Sayajirao University of Baroda** titled:

> **The ABC Insights: Analyzing Brewed Chai Coffee Caffeine**

The original group thesis focused on:

- Survey design and questionnaire development
- Stratified sampling
- Chemical assays for caffeine estimation
- Classical statistical analysis

I later extended the project independently to transform the research into an analytics application by developing:

- Machine learning pipelines
- Predictive models
- PCA and clustering analyses
- Outlier detection
- An interactive Streamlit caffeine calculator

---

## Phase 1 — Statistical Analysis

### Sample Design

| Metric | Value |
|-------|------:|
| Pilot Study | 30 respondents |
| Estimated Proportion | 0.70 |
| Required Sample Size | 298 |
| Final Sample Size | **320** |
| Population Size | 3,829 students |

Sampling was performed using a stratified design based on academic year.

### Reliability

Cronbach's alpha was computed on the behavioral survey items after excluding demographic variables.

- One behavioral sub-scale showed acceptable internal consistency.
- Another showed very weak consistency, representing a limitation of the survey instrument.
- Overall reliability was reported in the thesis as acceptable, though findings should be interpreted cautiously.

### Caffeine Content Verification

Instead of relying solely on self-reported consumption, caffeine concentrations were experimentally estimated using **iodometric back-titration assays** on beverages from popular campus vendors including:

- Nescafé
- K.G. Patel
- Dwarkesh
- Other local brands

These laboratory measurements were later integrated into the Streamlit calculator.

### Key Findings

| Research Question | Test Used | Result |
|---|---|---|
| Regular vs Exam Intake | Wilcoxon Rank Sum | Exam-day consumption significantly higher |
| Sleep vs Intake | Kruskal-Wallis + Jonckheere-Terpstra | Higher caffeine associated with shorter sleep |
| Focus vs Intake | Jonckheere-Terpstra | Significant positive trend during exams |
| CGPA vs Exam Intake | Jonckheere-Terpstra | Positive association |
| Gender vs Intake | Wilcoxon Rank Sum | Significant difference on regular days |

The CGPA-caffeine relationship is associative rather than causal and may reflect self-selection effects.

---

## Phase 2 — Machine Learning Pipeline

The machine learning pipeline was developed independently using the cleaned survey dataset (`analysis.csv`, n = 320).

### Performance Summary

| Task | Best Model | Metric |
|------|-----------|-------|
| Regression | Linear Regression | R² = **0.752** |
| Classification | Linear SVM | Accuracy = **69.8%** |
| PCA | 2 Components | 43.4% Variance Retained |
| Clustering | K-Means (k=5) | Silhouette Score = **0.521** |
| Outlier Detection | Z-Score & IQR | 11 and 31 observations flagged |

### Regression

Predicted exam-day caffeine intake using:

- Regular tea consumption
- Regular coffee consumption
- Chocolate intake
- Spending habits

**Results**

- R² = 0.752
- MAE = 0.59 cups/day
- Regular tea consumption was the strongest predictor.

### Classification

Students were categorized into four balanced intake groups:

- Very Low
- Low
- Medium
- High

Models evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Support Vector Machine
- KNN
- Naive Bayes
- XGBoost

The best-performing model was a **Linear SVM**:

- Test Accuracy = 69.8%
- Train Accuracy = 70.5%
- Minimal overfitting

### Principal Component Analysis

Reduced six beverage consumption variables into two principal components.

| Component | Variance Explained |
|------|------:|
| PC1 | 23.6% |
| PC2 | 19.8% |
| Total | **43.4%** |

The modest variance retention suggests beverage preferences are inherently multi-dimensional.

### K-Means Clustering

Applied K-Means clustering using:

- Regular caffeine intake
- Exam-day intake
- Spending behavior

**Silhouette Score**

```text
0.521
```

Five behavioral groups emerged:

- Light consumers
- Moderate consumers
- Exam-driven spenders
- High habitual consumers
- High-intake fixed-spend consumers

The smallest clusters should be interpreted cautiously due to their limited sample sizes.

### Outlier Detection

Two approaches were used:

| Method | Outliers |
|------|------:|
| Z-Score (>3σ) | 11 |
| IQR Method | 31 |

Outliers primarily reflected unusually large changes in caffeine spending during examination periods.

---

## Streamlit Application

The project includes an interactive caffeine intake tracker built using Streamlit.

### Features

- Brand-specific caffeine estimates derived from laboratory assays
- Serving-size based intake calculation
- Weight-based intake thresholds
- Sleep and focus tracking
- Session history and undo support
- Rule-based wellness alerts

The application uses session state to enable live recalculation as drinks are added or removed.

---

## Project Pipeline

```text
Survey + Pilot Study
        │
        ▼
Data Cleaning
        │
        ▼
Statistical Analysis
        │
        ▼
Machine Learning
├── Regression
├── Classification
├── PCA
├── Clustering
└── Outlier Detection
        │
        ▼
Streamlit Application
        │
        ▼
Personalized Intake Calculator
```

---

## Setup

```bash
git clone https://github.com/nikitasharma1203/caffeine-consumption-ml-app.git

cd caffeine-consumption-ml-app

python -m venv venv

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

streamlit run caffeine_calculator/app.py
```

---

## Limitations

- Findings are based on students from a single university and are not nationally representative.
- Caffeine consumption is self-reported.
- Statistical and machine learning analyses identify associations rather than causal relationships.
- Classification and clustering results should be treated as exploratory due to the modest sample size.
- Chemical assays estimated caffeine concentration by brand rather than individual consumption.

---

## Attribution

### Phase 1 — Group Thesis

**The ABC Insights: Analyzing Brewed Chai Coffee Caffeine**

Contributors:

- Jamil Mahida
- Nikita Sharma
- Rajvee Shah
- Savantsinh Rathod
- Tanya Chaurasia

Faculty Advisors:

- Dr. (Mrs.) M.N. Shah
- Mr. Vijay K. Gupta

Department of Statistics  
The Maharaja Sayajirao University of Baroda

### Phase 2 — Independent Extension

Developed independently by **Nikita Sharma**

Contributions include:

- Data preprocessing
- Machine learning pipeline
- Regression and classification models
- PCA and clustering
- Outlier detection
- Streamlit caffeine calculator
- Repository maintenance

---

## License

MIT License
