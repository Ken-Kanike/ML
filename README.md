# Machine Learning: Notes, Notebooks, and Projects

A hands-on machine-learning curriculum that moves from data preparation and classical models to
advanced topics such as time series, NLP, recommender systems, responsible AI, and model deployment.

Every advanced module is a self-contained Jupyter notebook with explanations, runnable code,
executed outputs, and exercises. The notebooks use small built-in or synthetic datasets so they run
quickly and reproducibly on a laptop.

## What is inside

| Path | Contents |
| --- | --- |
| [`Advanced_ML/`](Advanced_ML/) | 19 advanced modules, from k-NN and SVM to deployment and responsible AI |
| [`Core_ML/`](Core_ML/) | Foundations: data cleaning, encoding, scaling, feature selection, regression, classification |
| [`docs/`](docs/) | Curriculum, setup, dataset guide, and study plan |
| `*.csv`, `*.xlsx` | Datasets used by the foundation notebooks |

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

See [`Advanced_ML/README.md`](Advanced_ML/README.md) for module descriptions and a recommended order.

## Foundation notebooks

The `Core_ML` collection covers the prerequisites for the advanced modules:

- **Data preparation**: cleaning, missing values, imputation, duplicates, encoding, scaling.
- **Feature work**: outlier handling, transformations, feature selection.
- **Regression**: simple, multiple, polynomial, cost functions, regularization.
- **Classification**: logistic regression, confusion matrix, imbalanced data, naive Bayes.

Start with `p1.ipynb` and continue through `p11.ipynb`, then work through `m1.ipynb` to `m10.ipynb`.
The foundation notebooks read datasets from the repository root, so launch Jupyter from the root or
pass the correct path.

## Recommended learning path

1. **Foundations**: `Core_ML/p1` to `p11`, then `m1` to `m10`.
2. **Statistics and EDA**: modules 19 and 18.
3. **Feature engineering and core models**: modules 16, 01, 02, 03, 04, 07.
4. **Unsupervised learning**: modules 05 and 06.
5. **Specialized topics**: modules 08, 09, 10, 11, 12, 13, 15.
6. **Professional practice**: modules 14 and 17.

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
- Foundation notebooks use the CSV and Excel files in the repository root.
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
