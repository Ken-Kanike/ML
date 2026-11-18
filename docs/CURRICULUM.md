# Curriculum

This curriculum is designed for learners who want a broad, practical foundation in machine learning.
It combines the mathematical foundations, data-preparation, and classical-algorithm notebooks in
`Core_ML/` with the 22 advanced modules in `Advanced_ML/`.

## Who this is for

- Learners who know basic Python and want a structured ML path.
- Students who want runnable examples rather than only theory.
- Developers moving from software engineering into data science.
- Anyone preparing a portfolio of applied ML work.

## Learning outcomes

By the end, you should be able to:

- use the linear algebra, probability, and optimization ideas behind ML algorithms;
- clean, explore, and prepare tabular data;
- choose and evaluate supervised and unsupervised models;
- build reproducible pipelines and tune hyperparameters;
- handle imbalanced data, time series, text, and recommendations;
- distinguish prediction from causal effect estimation;
- measure and improve probability calibration;
- discover topics in unlabeled text;
- interpret models and communicate their limitations;
- detect and mitigate bias;
- package a model behind an API;
- explain statistical uncertainty and avoid common inference errors.

## Prerequisites

- Python basics: variables, functions, loops, lists, dictionaries.
- Familiarity with NumPy and pandas is helpful but not required.
- Basic algebra and comfort with plots. The `f1`, `f1b`, and `f2`-`f4` notebooks build the linear
  algebra, probability, optimization, and regression-diagnostics background you need.
- No deep-learning or statistics background is assumed.

## Track 1: Foundations

### Mathematical and statistical foundations (`Core_ML/f1`, `f1b`, `f2`-`f4`)

| Notebook | Topic |
| --- | --- |
| `f1_linear_algebra.ipynb` | Vectors, matrices, least squares, eigenvalues, PCA, SVD |
| `f1b_linear_algebra_advanced.ipynb` | Inner products, projections, determinants, traces, positive definite matrices, diagonalization |
| `f2_probability.ipynb` | Distributions, expectation, Bayes, maximum likelihood, Monte Carlo |
| `f3_optimization.ipynb` | Gradients, gradient descent, learning rates, SGD, momentum, early stopping |
| `f4_regression_diagnostics.ipynb` | Residual analysis, multicollinearity, influence, robust regression |

### Data preparation (`Core_ML/p1`-`p11`)

| Notebook | Topic |
| --- | --- |
| `p1.ipynb` | Data cleaning |
| `p2.ipynb` | Dropping missing values |
| `p3.ipynb` | Filling missing values |
| `p4.ipynb` | Scikit-learn imputation |
| `p5.ipynb` | One-hot encoding |
| `p6.ipynb` | Label encoding |
| `p7.ipynb` | Ordinal encoding |
| `p8.ipynb` | Outlier handling |
| `p9.ipynb` | Feature scaling |
| `p10.ipynb` | Duplicates and data-type fixes |
| `p11.ipynb` | Feature selection and train/test splitting |

### Classical algorithms (`Core_ML/m1`-`m10` plus statistical companions)

| Notebook | Topic |
| --- | --- |
| `m1.ipynb` | Supervised learning overview |
| `m1a_ml_workflow.ipynb` | ML issues, applications, project steps, and validation workflow |
| `m2.ipynb` | Simple linear regression |
| `m3.ipynb` | Multiple linear regression |
| `m3a_stepwise_regression.ipynb` | Forward, backward, and bidirectional selection with AIC, BIC, adjusted R2, and cross-validation |
| `m4.ipynb` | Polynomial regression |
| `m5.ipynb` | Cost functions and regularization |
| `m6.ipynb` | Classification overview |
| `m6a_least_squares_classification.ipynb` | Least-squares classification, linear boundaries, and comparison with logistic regression |
| `m7.ipynb` | Logistic regression |
| `m7a_logistic_glm.ipynb` | Logit link, odds ratios, GLM formulation, marginal effects, and assessment |
| `m8.ipynb` | Confusion matrix, accuracy, precision, recall, specificity, and F1 |
| `m9.ipynb` | Imbalanced datasets and resampling |
| `m10.ipynb` | Naive Bayes |

The foundation notebooks are working notes. They are intentionally kept close to the original
learning process. The advanced modules revisit several of these ideas with cleaner, reproducible
code and stronger evaluation.

## Track 2: Analytical toolkit

Build the habits that make modelling reliable.

| Module | Why it matters |
| --- | --- |
| [19 Exploratory Data Analysis](../Advanced_ML/19_exploratory_data_analysis/19_exploratory_data_analysis.ipynb) | Understand the data before choosing a model |
| [18 Statistics Foundations](../Advanced_ML/18_statistics_foundations/18_statistics_foundations.ipynb) | Quantify uncertainty and interpret experiments |
| [20 Causal Inference](../Advanced_ML/20_causal_inference/20_causal_inference.ipynb) | Separate association from intervention effects |
| [16 Feature Engineering](../Advanced_ML/16_feature_engineering/16_feature_engineering.ipynb) | Represent the problem well and avoid leakage |

## Track 3: Core supervised learning

| Module | Key ideas |
| --- | --- |
| [01 k-NN and SVM](../Advanced_ML/01_knn_svm/01_knn_svm.ipynb) | Scaling, distances, margins, kernels |
| [02 Trees and Ensembles](../Advanced_ML/02_trees_ensembles/02_trees_ensembles.ipynb) | Trees, bagging, random forests, boosting |
| [03 Model Evaluation](../Advanced_ML/03_model_evaluation/03_model_evaluation.ipynb) | Honest splits, cross-validation, metrics |
| [04 Pipelines and Tuning](../Advanced_ML/04_pipelines_tuning/04_pipelines_tuning.ipynb) | Reproducible preprocessing and search |
| [07 Imbalanced Learning](../Advanced_ML/07_imbalanced_learning/07_imbalanced_learning.ipynb) | Resampling, class weights, PR-AUC, thresholds |
| [21 Model Calibration](../Advanced_ML/21_model_calibration/21_model_calibration.ipynb) | Probability quality, reliability diagrams, calibration, cost-sensitive decisions |

## Track 4: Unsupervised learning

| Module | Key ideas |
| --- | --- |
| [05 Clustering](../Advanced_ML/05_clustering/05_clustering.ipynb) | K-means, hierarchical, density-based clustering |
| [06 Dimensionality Reduction](../Advanced_ML/06_dimensionality_reduction/06_dimensionality_reduction.ipynb) | PCA, t-SNE, visualization, compression |

## Track 5: Specialized applications

| Module | Key ideas |
| --- | --- |
| [08 Time Series](../Advanced_ML/08_time_series/08_time_series.ipynb) | Temporal validation, stationarity, ARIMA |
| [09 NLP Basics](../Advanced_ML/09_nlp_basics/09_nlp_basics.ipynb) | Text features and classification |
| [22 Topic Modeling](../Advanced_ML/22_topic_modeling/22_topic_modeling.ipynb) | Unsupervised discovery of themes in text |
| [10 Recommender Systems](../Advanced_ML/10_recommender_systems/10_recommender_systems.ipynb) | Content and collaborative filtering |
| [11 Anomaly Detection](../Advanced_ML/11_anomaly_detection/11_anomaly_detection.ipynb) | Outlier detection without balanced labels |
| [12 Model Interpretability](../Advanced_ML/12_model_interpretability/12_model_interpretability.ipynb) | Global and local explanations |
| [13 Neural Networks](../Advanced_ML/13_neural_networks/13_neural_networks.ipynb) | MLPs from first principles |
| [15 Association Rules](../Advanced_ML/15_association_rules/15_association_rules.ipynb) | Market-basket analysis with Apriori and FP-Growth |

## Track 6: Professional practice

| Module | Key ideas |
| --- | --- |
| [14 Deployment](../Advanced_ML/14_deployment/14_deployment.ipynb) | Serialization, API design, validation, monitoring |
| [17 Fairness and Responsible AI](../Advanced_ML/17_fairness_responsible_ai/17_fairness_responsible_ai.ipynb) | Bias, fairness metrics, mitigation, model cards |

## Suggested projects

1. **Tabular prediction pipeline**: build an end-to-end pipeline with preprocessing, feature
   engineering, cross-validation, and a final report on a dataset of your choice.
2. **Forecasting study**: compare a naive baseline, regression on lags, and ARIMA on a public time
   series; report walk-forward error.
3. **Text classifier**: collect or use a public text dataset, compare TF-IDF with a simple embedding
   baseline, and analyse errors.
4. **Recommendation prototype**: build a content-based and a collaborative recommender; evaluate
   ranking quality and discuss cold start.
5. **Responsible AI audit**: choose a public model or dataset, compute group-level metrics, and write
   a model card with mitigation recommendations.
6. **Deployment project**: package a model behind FastAPI, add validation and tests, and document the
   API contract.
7. **Causal effect study**: define a treatment, draw a DAG, choose an identification strategy, and
   report the estimate with its assumptions and sensitivity checks.
8. **Topic-model exploration**: collect a public text corpus, compare LDA and NMF, and evaluate topics
   with top words, stability, and a downstream task.

## How to use the notebooks

- Run the code, then change one thing and observe the effect.
- Complete the exercises at the end of each notebook.
- Keep a short learning log: what you tried, what happened, and why.
- Prefer a small, well-evaluated model over a complex model with a leaky validation setup.

## Assessment ideas

- A portfolio notebook with a clear question, data provenance, validation strategy, results, and
  limitations.
- A short written explanation of a fairness or leakage issue.
- A code review of another learner's pipeline.
- A final presentation of a project with error analysis, not only accuracy.
