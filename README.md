# Machine Learning: Notes, Notebooks, and Projects

A hands-on machine-learning curriculum that moves from data preparation and classical models to
advanced topics such as time series, NLP, recommender systems, responsible AI, and model deployment.

Every advanced module is a self-contained Jupyter notebook with explanations, runnable code,
executed outputs, and exercises. The notebooks use small built-in or synthetic datasets so they run
quickly and reproducibly on a laptop.

## What is inside

| Path | Contents |
| --- | --- |
| [`Core_ML/`](Core_ML/) | Mathematical foundations plus data cleaning, encoding, scaling, feature selection, regression, classification |
| [`Advanced_ML/`](Advanced_ML/) | 22 advanced modules, from k-NN and SVM to causal inference and topic modeling |
| [`docs/`](docs/) | Curriculum, setup, dataset guide, and study plan |
| `*.csv`, `*.xlsx` | Datasets used by the foundation notebooks |

## Core_ML modules

The `Core_ML` collection covers the prerequisites for the advanced modules: the mathematics behind
the algorithms, data cleaning, encoding, scaling, feature selection, and the classical regression and
classification algorithms. The data-preparation and classical-model notebooks are working notes from
the learning process; the advanced modules revisit the same ideas with cleaner pipelines and stronger
evaluation.

### Mathematical and statistical foundations

| # | Notebook | Topics |
| --- | --- | --- |
| f1 | [Linear Algebra](Core_ML/f1_linear_algebra.ipynb) | Vectors, matrices, least squares, rank, eigenvalues, PCA, SVD |
| f2 | [Probability](Core_ML/f2_probability.ipynb) | Distributions, expectation, Bayes, maximum likelihood, Monte Carlo |
| f3 | [Optimization](Core_ML/f3_optimization.ipynb) | Gradients, gradient descent, learning rates, SGD, momentum, early stopping |
| f4 | [Regression Diagnostics](Core_ML/f4_regression_diagnostics.ipynb) | Residual analysis, multicollinearity, leverage, Cook's distance, robust regression |

### Data preparation and feature engineering

| # | Notebook | Topics |
| --- | --- | --- |
| p1 | [Data Cleaning](Core_ML/p1.ipynb) | Loading data, inspecting structure, and fixing basic quality issues |
| p2 | [Dropping Missing Values](Core_ML/p2.ipynb) | Dropping null rows and columns, and the trade-offs |
| p3 | [Filling Missing Values](Core_ML/p3.ipynb) | Constant and statistic-based imputation |
| p4 | [Scikit-learn Imputation](Core_ML/p4.ipynb) | `SimpleImputer` and pipeline-safe imputation |
| p5 | [One-Hot Encoding](Core_ML/p5.ipynb) | Nominal categories and dummy variables |
| p6 | [Label Encoding](Core_ML/p6.ipynb) | Integer labels and when not to use them |
| p7 | [Ordinal Encoding](Core_ML/p7.ipynb) | Encoding ordered categories |
| p8 | [Outlier Handling](Core_ML/p8.ipynb) | IQR detection, removal, and capping |
| p9 | [Feature Scaling](Core_ML/p9.ipynb) | Standardization vs min-max normalization |
| p10 | [Duplicates and Data Types](Core_ML/p10.ipynb) | Duplicate rows, mixed types, and type conversion |
| p11 | [Feature Selection](Core_ML/p11.ipynb) | Forward and backward elimination with cross-validation |

### Classical machine learning

| # | Notebook | Topics |
| --- | --- | --- |
| m1 | [Supervised Learning Overview](Core_ML/m1.ipynb) | Regression vs classification and the algorithm landscape |
| m1a | [ML Workflow](Core_ML/m1a_ml_workflow.ipynb) | ML issues, applications, project steps, train/validation/test workflow, specificity |
| m2 | [Simple Linear Regression](Core_ML/m2.ipynb) | One feature, line fitting, and prediction |
| m3 | [Multiple Linear Regression](Core_ML/m3.ipynb) | Several features, coefficients, and model evaluation |
| m4 | [Polynomial Regression](Core_ML/m4.ipynb) | Non-linear relationships with polynomial features |
| m5 | [Cost Functions and Regularization](Core_ML/m5.ipynb) | MSE, MAE, RMSE, R2, Lasso, Ridge, and ElasticNet |
| m6 | [Classification Overview](Core_ML/m6.ipynb) | Linear and non-linear classifiers, and evaluation metrics |
| m7 | [Logistic Regression](Core_ML/m7.ipynb) | Sigmoid, binary and multiclass classification, decision boundaries |
| m8 | [Confusion Matrix](Core_ML/m8.ipynb) | Precision, recall, F1, and classification error analysis |
| m9 | [Imbalanced Data](Core_ML/m9.ipynb) | Random over/under-sampling and evaluation under imbalance |
| m10 | [Naive Bayes](Core_ML/m10.ipynb) | Bayes theorem, independence assumptions, and text classification |

Start with `f1.ipynb` to `f4.ipynb` for the mathematical foundations, then `p1.ipynb` to `p11.ipynb`,
then `m1.ipynb`, `m1a_ml_workflow.ipynb`, and `m2.ipynb` to `m10.ipynb`. The data-preparation and classical-model notebooks read datasets from
the repository root, so launch Jupyter from the root or pass the correct path. The foundation notebooks
use synthetic or built-in data. `Core_ML/data_mal.py` contains the scripts used to generate and
deliberately degrade the practice datasets, and `Core_ML/NOTE.txt` plus `Core_ML/NOTE2.txt` contain the
longer study notes.

## Advanced modules

| # | Module | Focus |
| --- | --- | --- |
| 01 | [k-NN and SVM](Advanced_ML/01_knn_svm/01_knn_svm.ipynb) | Distance-based and margin-based classification, scaling, kernels |
| 02 | [Trees and Ensembles](Advanced_ML/02_trees_ensembles/02_trees_ensembles.ipynb) | Decision trees, bagging, random forests, gradient boosting |
| 03 | [Model Evaluation](Advanced_ML/03_model_evaluation/03_model_evaluation.ipynb) | Splits, cross-validation, classification and regression metrics |
| 04 | [Pipelines and Tuning](Advanced_ML/04_pipelines_tuning/04_pipelines_tuning.ipynb) | ColumnTransformer, pipelines, grid and randomized search |
| 05 | [Clustering](Advanced_ML/05_clustering/05_clustering.ipynb) | K-means, hierarchical clustering, DBSCAN, cluster validation |
| 06 | [Dimensionality Reduction](Advanced_ML/06_dimensionality_reduction/06_dimensionality_reduction.ipynb) | PCA, t-SNE, explained variance, visualization |
| 07 | [Imbalanced Learning](Advanced_ML/07_imbalanced_learning/07_imbalanced_learning.ipynb) | Resampling, SMOTE, class weights, precision-recall |
| 08 | [Time Series](Advanced_ML/08_time_series/08_time_series.ipynb) | Decomposition, stationarity, lag features, ARIMA |
| 09 | [NLP Basics](Advanced_ML/09_nlp_basics/09_nlp_basics.ipynb) | Text cleaning, bag-of-words, TF-IDF, text classification |
| 10 | [Recommender Systems](Advanced_ML/10_recommender_systems/10_recommender_systems.ipynb) | Content-based and collaborative filtering, SVD |
| 11 | [Anomaly Detection](Advanced_ML/11_anomaly_detection/11_anomaly_detection.ipynb) | Isolation Forest, LOF, One-Class SVM |
| 12 | [Model Interpretability](Advanced_ML/12_model_interpretability/12_model_interpretability.ipynb) | Permutation importance, partial dependence, coefficients |
| 13 | [Neural Networks](Advanced_ML/13_neural_networks/13_neural_networks.ipynb) | Perceptrons, MLPs, activations, regularization, decision boundaries |
| 14 | [Deployment](Advanced_ML/14_deployment/14_deployment.ipynb) | Model serialization, FastAPI, schema validation, testing |
| 15 | [Association Rules](Advanced_ML/15_association_rules/15_association_rules.ipynb) | Apriori, FP-Growth, support, confidence, lift |
| 16 | [Feature Engineering](Advanced_ML/16_feature_engineering/16_feature_engineering.ipynb) | Dates, ratios, interactions, binning, target encoding, leakage |
| 17 | [Fairness and Responsible AI](Advanced_ML/17_fairness_responsible_ai/17_fairness_responsible_ai.ipynb) | Bias, fairness metrics, mitigation, model cards |
| 18 | [Statistics Foundations](Advanced_ML/18_statistics_foundations/18_statistics_foundations.ipynb) | Sampling, confidence intervals, hypothesis tests, power, bootstrap |
| 19 | [Exploratory Data Analysis](Advanced_ML/19_exploratory_data_analysis/19_exploratory_data_analysis.ipynb) | Data quality, distributions, target analysis, outliers |
| 20 | [Causal Inference](Advanced_ML/20_causal_inference/20_causal_inference.ipynb) | Potential outcomes, confounding, randomized experiments, propensity scores, difference-in-differences |
| 21 | [Model Calibration](Advanced_ML/21_model_calibration/21_model_calibration.ipynb) | Reliability diagrams, Brier score, ECE, sigmoid and isotonic calibration, cost-sensitive thresholds |
| 22 | [Topic Modeling](Advanced_ML/22_topic_modeling/22_topic_modeling.ipynb) | Count and TF-IDF features, LDA, NMF, perplexity, document-topic mixtures |

See [`Advanced_ML/README.md`](Advanced_ML/README.md) for module descriptions and a recommended order.

## Recommended learning path

1. **Mathematical foundations**: `Core_ML/f1` to `f4`.
2. **Core ML**: `Core_ML/p1` to `p11`, then `m1` to `m10`.
3. **Analytical toolkit**: modules 19, 18, and 20.
4. **Supervised learning and evaluation**: modules 16, 01, 02, 03, 04, 07, and 21.
5. **Unsupervised learning and text**: modules 05, 06, and 22.
6. **Specialized topics**: modules 08, 09, 10, 11, 12, 13, and 15.
7. **Professional practice**: modules 14 and 17.

The numeric module order is a reference index, not a strict prerequisite chain. See
[`docs/STUDY_PLAN.md`](docs/STUDY_PLAN.md) for a week-by-week schedule.

## Quick start

Requirements: Python 3.10 or newer, Git, and Jupyter. The notebooks were tested with Python 3.12.

### Windows PowerShell

```powershell
git clone https://github.com/Ken-Kanike/ML.git
cd ML
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

### macOS and Linux

```bash
git clone https://github.com/Ken-Kanike/ML.git
cd ML
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Open a notebook and run the cells from top to bottom. The advanced notebooks are self-contained and
can be run from their own folder.

## Running notebooks

The committed notebooks already contain executed outputs. To re-execute one:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=600 \
  Advanced_ML/01_knn_svm/01_knn_svm.ipynb
```

On Windows PowerShell, put the command on one line or use a backtick for continuation.

If Jupyter asks for a kernel, select the Python environment where `requirements.txt` was installed.

## Datasets

- Advanced modules use scikit-learn built-in datasets, synthetic data, or small generated examples.
- `Core_ML` mathematical foundation notebooks use synthetic or built-in data.
- `Core_ML` data-preparation and classical-model notebooks use the CSV and Excel files in the
  repository root.
- See [`docs/DATASETS.md`](docs/DATASETS.md) for the full mapping.

No real personal data or credentials are included. Synthetic examples are used where privacy or
licensing would otherwise be a concern.

## Documentation

- [Advanced module guide](Advanced_ML/README.md)
- [Curriculum](docs/CURRICULUM.md)
- [Setup and troubleshooting](docs/SETUP.md)
- [Dataset guide](docs/DATASETS.md)
- [Study plan](docs/STUDY_PLAN.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## Contributing

Corrections, clearer explanations, additional exercises, and new notebooks are welcome. Please read
[`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## License

Released under the [MIT License](LICENSE).

## Acknowledgements

The foundation material was built while learning from public courses and documentation, including
scikit-learn, pandas, seaborn, statsmodels, imbalanced-learn, and mlxtend. The advanced modules were
written as a structured extension of that foundation for learners who want a broader, project-ready
view of machine learning.
