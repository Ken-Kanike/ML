# Advanced Machine Learning Modules

This folder contains 22 self-contained notebooks that extend the foundation material in
[`Core_ML/`](../Core_ML/) into modern, practical machine-learning topics.

Each module includes:

- learning objectives and concept explanations,
- runnable code with visible outputs,
- evaluation and interpretation,
- a summary and exercises.

The notebooks use built-in scikit-learn datasets, synthetic data, or small generated examples, so
they execute quickly and do not require downloads. The focus is classical and applied machine
learning; deep-learning frameworks and large models are out of scope. Module 13 builds a small
multilayer perceptron from scratch with NumPy.

## Module index

| # | Notebook | Topics |
| --- | --- | --- |
| 01 | [k-NN and SVM](01_knn_svm/01_knn_svm.ipynb) | Distance metrics, feature scaling, decision boundaries, kernels, margin and regularization |
| 02 | [Trees and Ensembles](02_trees_ensembles/02_trees_ensembles.ipynb) | Decision trees, pruning, bagging, random forests, gradient boosting |
| 03 | [Model Evaluation](03_model_evaluation/03_model_evaluation.ipynb) | Train/validation/test splits, cross-validation, classification and regression metrics, ROC and PR curves |
| 04 | [Pipelines and Tuning](04_pipelines_tuning/04_pipelines_tuning.ipynb) | ColumnTransformer, preprocessing pipelines, grid search, randomized search, nested cross-validation |
| 05 | [Clustering](05_clustering/05_clustering.ipynb) | K-means, elbow and silhouette methods, hierarchical clustering, DBSCAN, cluster evaluation |
| 06 | [Dimensionality Reduction](06_dimensionality_reduction/06_dimensionality_reduction.ipynb) | PCA, explained variance, t-SNE, visualization, downstream model performance |
| 07 | [Imbalanced Learning](07_imbalanced_learning/07_imbalanced_learning.ipynb) | Class weights, random over/under-sampling, SMOTE, precision-recall AUC, threshold selection |
| 08 | [Time Series](08_time_series/08_time_series.ipynb) | Decomposition, stationarity, ACF/PACF, lag features, ARIMA, walk-forward validation |
| 09 | [NLP Basics](09_nlp_basics/09_nlp_basics.ipynb) | Text normalization, tokenization, bag-of-words, TF-IDF, linear text classifiers |
| 10 | [Recommender Systems](10_recommender_systems/10_recommender_systems.ipynb) | Content-based filtering, item-item collaborative filtering, matrix factorization with SVD |
| 11 | [Anomaly Detection](11_anomaly_detection/11_anomaly_detection.ipynb) | Isolation Forest, Local Outlier Factor, One-Class SVM, contamination and evaluation |
| 12 | [Model Interpretability](12_model_interpretability/12_model_interpretability.ipynb) | Coefficients, impurity importance, permutation importance, partial dependence |
| 13 | [Neural Networks](13_neural_networks/13_neural_networks.ipynb) | Perceptron intuition, MLP, activations, backpropagation overview, regularization |
| 14 | [Deployment](14_deployment/14_deployment.ipynb) | Model persistence, FastAPI service, request schemas, tests, monitoring |
| 15 | [Association Rules](15_association_rules/15_association_rules.ipynb) | Transactions, support, confidence, lift, Apriori, FP-Growth |
| 16 | [Feature Engineering](16_feature_engineering/16_feature_engineering.ipynb) | Date features, ratios, interactions, binning, polynomial features, target encoding, leakage |
| 17 | [Fairness and Responsible AI](17_fairness_responsible_ai/17_fairness_responsible_ai.ipynb) | Bias sources, demographic parity, equal opportunity, mitigation, model cards |
| 18 | [Statistics Foundations](18_statistics_foundations/18_statistics_foundations.ipynb) | Sampling distributions, central limit theorem, confidence intervals, hypothesis tests, bootstrap |
| 19 | [Exploratory Data Analysis](19_exploratory_data_analysis/19_exploratory_data_analysis.ipynb) | Data quality, univariate and target analysis, correlation, outliers, modelling implications |
| 20 | [Causal Inference](20_causal_inference/20_causal_inference.ipynb) | Potential outcomes, confounding, randomized experiments, adjustment, propensity scores, difference-in-differences |
| 21 | [Model Calibration](21_model_calibration/21_model_calibration.ipynb) | Reliability diagrams, Brier score, log loss, ECE, sigmoid and isotonic calibration, cost-sensitive thresholds, bootstrap |
| 22 | [Topic Modeling](22_topic_modeling/22_topic_modeling.ipynb) | Count and TF-IDF features, LDA, NMF, perplexity, document-topic mixtures, topic evaluation |

## Recommended order

If you are new to the advanced material:

1. **19 Exploratory Data Analysis**, **18 Statistics Foundations**, and **20 Causal Inference** for
   the analytical toolkit.
2. **16 Feature Engineering** for representation design.
3. **01 k-NN and SVM**, **02 Trees and Ensembles**, **03 Model Evaluation**, **04 Pipelines and Tuning**,
   **07 Imbalanced Learning**, and **21 Model Calibration** for supervised learning.
4. **05 Clustering** and **06 Dimensionality Reduction** for unsupervised learning.
5. **08 Time Series**, **09 NLP Basics**, **22 Topic Modeling**, **10 Recommender Systems**,
   **11 Anomaly Detection**, **12 Model Interpretability**, **13 Neural Networks**, and
   **15 Association Rules** for breadth.
6. **14 Deployment** and **17 Fairness and Responsible AI** for professional practice.

The numbered folders are a reference index, not a strict dependency chain.

## How to run

From the repository root:

```bash
pip install -r requirements.txt
jupyter lab
```

Open any notebook and run the cells from top to bottom. Each notebook is standalone. To re-execute a
notebook from the command line:

```bash
jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=600 \
  Advanced_ML/01_knn_svm/01_knn_svm.ipynb
```

## Conventions

- All notebooks are executed before commit, so outputs are visible on GitHub.
- Code uses `RANDOM_STATE = 42` or a fixed NumPy generator for reproducibility.
- Examples are small enough to run on a laptop CPU.
- Datasets are built in or generated; no private or licensed data is required.
- Each notebook ends with exercises for further practice.

## Related documentation

- [Repository README](../README.md)
- [Curriculum](../docs/CURRICULUM.md)
- [Setup and troubleshooting](../docs/SETUP.md)
- [Dataset guide](../docs/DATASETS.md)
- [Study plan](../docs/STUDY_PLAN.md)
