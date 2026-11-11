# Dataset Guide

This repository uses small public, built-in, or synthetic datasets. Nothing here contains real
personal data, credentials, or licensed material.

## Advanced modules

Most advanced notebooks create their data inside the notebook or load a scikit-learn built-in dataset.
This keeps execution fast and avoids external downloads.

| Module | Data source |
| --- | --- |
| 01 k-NN and SVM | Breast Cancer Wisconsin dataset (`load_breast_cancer`) |
| 02 Trees and Ensembles | Breast Cancer Wisconsin dataset (`load_breast_cancer`) |
| 03 Model Evaluation | Breast Cancer and Diabetes datasets (`load_breast_cancer`, `load_diabetes`) |
| 04 Pipelines and Tuning | Synthetic classification data (`make_classification`) |
| 05 Clustering | Synthetic blobs and moons (`make_blobs`, `make_moons`) |
| 06 Dimensionality Reduction | Breast Cancer and handwritten digits (`load_breast_cancer`, `load_digits`) |
| 07 Imbalanced Learning | Synthetic imbalanced classification data (`make_classification`) |
| 08 Time Series | Synthetic trend, seasonal, and noise series generated in the notebook |
| 09 NLP Basics | Small synthetic corpus of positive and negative product reviews |
| 10 Recommender Systems | Synthetic movie catalogue and user ratings |
| 11 Anomaly Detection | Synthetic normal points plus injected anomalies |
| 12 Model Interpretability | Breast Cancer Wisconsin dataset (`load_breast_cancer`) |
| 13 Neural Networks | Synthetic two-moons dataset (`make_moons`) |
| 14 Deployment | Breast Cancer Wisconsin dataset (`load_breast_cancer`) |
| 15 Association Rules | Synthetic grocery transactions with planted item associations |
| 16 Feature Engineering | Synthetic customer-churn data generated in the notebook |
| 17 Fairness and Responsible AI | Synthetic hiring data with an explicit group bias |
| 18 Statistics Foundations | Simulated populations, samples, experiments, and A/B tests |
| 19 Exploratory Data Analysis | Wine recognition dataset (`load_wine`) |

## Foundation datasets

The `WsCubeTech` notebooks read files from the repository root. Start Jupyter from the root directory
so the relative paths resolve.

| File | Description | Used by |
| --- | --- | --- |
| `accurate_subscription_data.csv` | Age, estimated salary, and purchase outcome | `m7.ipynb` |
| `catg_data.xlsx` | Categorical data with missing values | `p3.ipynb` |
| `flowers.csv` | Flower measurements for classification | `m7.ipynb` |
| `gender_cat_data.xlsx` | Categorical gender data for encoding practice | `p5.ipynb`, `p6.ipynb`, `p7.ipynb` |
| `house_prices_data.csv` | Housing features and price | `m5.ipynb` |
| `mixed_data.xlsx` | Mixed types, including age values such as `18+` | `p10.ipynb` |
| `student_data.csv` | Experience and salary | `m3.ipynb`, `m4.ipynb` |
| `student_placements.csv` | CGPA and placement package | `m2.ipynb` |
| `student_placement_data.csv` | CGPA, test score, and placement status | `m7.ipynb`, `m8.ipynb`, `m10.ipynb` |
| `subscription_data.csv` | Age, salary, and purchase outcome for imbalance practice | `m9.ipynb` |
| `uncleaned_data.xlsx` | Data with missing values | `p2.ipynb`, `p4.ipynb` |
| `yahoo_data.xlsx` | Historical financial time-series data for cleaning and feature work | `p1.ipynb`, `p8.ipynb`, `p9.ipynb`, `p10.ipynb`, `p11.ipynb` |

Column names and semantics are introduced in the notebooks where the files are used.

## Reproducibility

- Notebooks set `RANDOM_STATE = 42` or use a seeded NumPy generator.
- Synthetic data is generated deterministically from that seed.
- Built-in scikit-learn datasets are bundled with scikit-learn and do not require network access.
- The notebooks do not download data at runtime.

## Licensing and privacy

- The built-in scikit-learn datasets are distributed with scikit-learn under its BSD license.
- The synthetic datasets are generated for teaching and may be reused freely with attribution.
- The CSV and Excel files are small educational samples. Review the original source before reusing
  them in a public or commercial project.
- If you add a dataset, document its source, license, and any privacy considerations. Do not add
  personal, confidential, or identifiable data.

## Adding a dataset

1. Prefer a built-in dataset or a small synthetic example.
2. Keep the file small enough for a Git repository.
3. Document the source and license in this file.
4. Use relative paths and avoid machine-specific absolute paths.
5. Do not commit secrets, credentials, or personal information.
