# Study Plan

This plan assumes 6-8 hours per week for 10 weeks. If you already know Python, pandas, and basic
statistics, compress the first two weeks and spend more time on the projects.

## Weekly rhythm

- **Read** the notebook markdown before running code.
- **Run** every cell and change at least one parameter.
- **Do** the exercises at the end of the notebook.
- **Write** a five-line learning log: what you tried, what happened, why, and what you would test next.
- **Commit** your work regularly if you keep a personal fork.

## Week 0: Mathematical foundations (recommended)

**Goal:** build the linear algebra, probability, and optimization background used throughout the
course. Skip or skim this week if you already have it.

- Run `Core_ML/f1_linear_algebra.ipynb` and `Core_ML/f1b_linear_algebra_advanced.ipynb`.
- Run `Core_ML/f2_probability.ipynb`, `f3_optimization.ipynb`, and `f4_regression_diagnostics.ipynb`.
- Practise: derive a least-squares solution, project a vector, compute a determinant and trace,
  diagonalize a covariance matrix, compute a posterior probability, implement one gradient step,
  and interpret a residual plot.

**Deliverable:** a one-page note connecting dot products, likelihood, gradients, and linear
regression.

## Week 1: Setup and data fluency

**Goal:** get the environment running and learn to inspect a dataset.

- Read [`SETUP.md`](SETUP.md) and install the environment.
- Run [`Advanced_ML/19_exploratory_data_analysis`](../Advanced_ML/19_exploratory_data_analysis/19_exploratory_data_analysis.ipynb).
- Skim `Core_ML/p1.ipynb` through `p4.ipynb`.
- Practise: load a CSV, check shape, types, missing values, duplicates, and summary statistics.

**Deliverable:** a short EDA of a dataset you choose, with five findings and three modelling
recommendations.

## Week 2: Statistics and data preparation

**Goal:** understand uncertainty and prepare clean features.

- Run [`Advanced_ML/18_statistics_foundations`](../Advanced_ML/18_statistics_foundations/18_statistics_foundations.ipynb).
- Work through `Core_ML/p5.ipynb` through `p11.ipynb`.
- Run [`Advanced_ML/16_feature_engineering`](../Advanced_ML/16_feature_engineering/16_feature_engineering.ipynb).
- Practise: confidence interval, t-test, one-hot encoding, scaling, and a leakage check.

**Deliverable:** a preprocessing pipeline with imputation, encoding, scaling, and a written note on
which steps must be fitted inside cross-validation.

## Week 3: Supervised learning foundations

**Goal:** train and evaluate core classifiers.

- Run [`Advanced_ML/01_knn_svm`](../Advanced_ML/01_knn_svm/01_knn_svm.ipynb).
- Run [`Advanced_ML/02_trees_ensembles`](../Advanced_ML/02_trees_ensembles/02_trees_ensembles.ipynb).
- Review `Core_ML/m1.ipynb` and run `Core_ML/m1a_ml_workflow.ipynb` for the project workflow.
- Review `Core_ML/m2.ipynb` through `m4.ipynb` for regression basics, and run
  `Core_ML/m3a_stepwise_regression.ipynb` for model selection.
- Run `Core_ML/m6a_least_squares_classification.ipynb` and `Core_ML/m7a_logistic_glm.ipynb` to
  connect regression to classification and interpret odds ratios.
- Practise: compare k-NN, SVM, a decision tree, and a random forest on one dataset.

**Deliverable:** a model comparison table with accuracy, precision, recall, specificity, F1, and a
short discussion of which errors matter most, plus a selected regression model with its validation
error and an odds-ratio interpretation.

## Week 4: Evaluation and tuning

**Goal:** build trustworthy model-selection workflows.

- Run [`Advanced_ML/03_model_evaluation`](../Advanced_ML/03_model_evaluation/03_model_evaluation.ipynb).
- Run [`Advanced_ML/04_pipelines_tuning`](../Advanced_ML/04_pipelines_tuning/04_pipelines_tuning.ipynb).
- Review `Core_ML/m5.ipynb` for cost functions and regularization.
- Optional: run [`Advanced_ML/21_model_calibration`](../Advanced_ML/21_model_calibration/21_model_calibration.ipynb)
  when your model outputs probabilities.
- Practise: nested cross-validation and a small hyperparameter search.

**Deliverable:** an end-to-end pipeline with a held-out test set that was touched only once.

## Week 5: Imbalanced data and unsupervised learning

**Goal:** handle skewed targets and find structure without labels.

- Run [`Advanced_ML/07_imbalanced_learning`](../Advanced_ML/07_imbalanced_learning/07_imbalanced_learning.ipynb).
- Run [`Advanced_ML/05_clustering`](../Advanced_ML/05_clustering/05_clustering.ipynb).
- Run [`Advanced_ML/05a_hebbian_learning`](../Advanced_ML/05a_hebbian_learning/05a_hebbian_learning.ipynb)
  and [`Advanced_ML/05b_em_clustering`](../Advanced_ML/05b_em_clustering/05b_em_clustering.ipynb).
- Run [`Advanced_ML/06_dimensionality_reduction`](../Advanced_ML/06_dimensionality_reduction/06_dimensionality_reduction.ipynb).
- Practise: precision-recall curves, SMOTE inside a pipeline, silhouette analysis, a Hebbian
  principal-direction learner, and EM responsibilities on boundary points.

**Deliverable:** an imbalanced-classification report and a cluster analysis with a validation metric,
including a comparison of k-means and a Gaussian mixture.

## Week 6: Time series and text

**Goal:** apply ML to ordered and unstructured data.

- Run [`Advanced_ML/08_time_series`](../Advanced_ML/08_time_series/08_time_series.ipynb).
- Run [`Advanced_ML/09_nlp_basics`](../Advanced_ML/09_nlp_basics/09_nlp_basics.ipynb) and
  [`Advanced_ML/09a_text_analytics_workflow`](../Advanced_ML/09a_text_analytics_workflow/09a_text_analytics_workflow.ipynb).
- Optional: run [`Advanced_ML/22_topic_modeling`](../Advanced_ML/22_topic_modeling/22_topic_modeling.ipynb)
  for unlabeled text.
- Practise: a chronological split, a naive forecast baseline, TF-IDF, a confusion matrix for text,
  and an extractive summary.

**Deliverable:** a forecast comparison, a text-classification error analysis, and a short
text-analytics project brief naming the practice area and evaluation metric.

## Week 7: Recommenders, anomalies, and interpretation

**Goal:** cover three common applied problems.

- Run [`Advanced_ML/10_recommender_systems`](../Advanced_ML/10_recommender_systems/10_recommender_systems.ipynb).
- Run [`Advanced_ML/11_anomaly_detection`](../Advanced_ML/11_anomaly_detection/11_anomaly_detection.ipynb).
- Run [`Advanced_ML/12_model_interpretability`](../Advanced_ML/12_model_interpretability/12_model_interpretability.ipynb).
- Optional: run [`Advanced_ML/20_causal_inference`](../Advanced_ML/20_causal_inference/20_causal_inference.ipynb)
  when the question is about an intervention rather than a prediction.
- Practise: precision@k, contamination sensitivity, permutation importance.

**Deliverable:** a short report explaining one model's global and local behaviour.

## Week 8: Neural networks, rules, and responsible AI

**Goal:** understand flexible models and their risks.

- Run [`Advanced_ML/13_neural_networks`](../Advanced_ML/13_neural_networks/13_neural_networks.ipynb).
- Run [`Advanced_ML/15_association_rules`](../Advanced_ML/15_association_rules/15_association_rules.ipynb).
- Run [`Advanced_ML/17_fairness_responsible_ai`](../Advanced_ML/17_fairness_responsible_ai/17_fairness_responsible_ai.ipynb).
- Practise: a small MLP, association-rule filtering, and a group-level fairness report.

**Deliverable:** a model card for a model of your choice, including limitations and monitoring ideas.

## Week 9: Deployment

**Goal:** serve a model and test the contract.

- Run [`Advanced_ML/14_deployment`](../Advanced_ML/14_deployment/14_deployment.ipynb).
- Review FastAPI request validation, model persistence, and error handling.
- Practise: add a second endpoint or a batch-prediction route.

**Deliverable:** a working local API with example requests and a short README.

## Week 10: Capstone

**Goal:** produce a portfolio-quality project.

- Choose a question and dataset.
- Write the data provenance and limitations.
- Build a reproducible pipeline.
- Evaluate with the correct validation strategy.
- Perform error analysis and a fairness or robustness check where relevant.
- Present results with clear visuals.

**Deliverable:** a notebook or repository with code, results, limitations, and next steps.

## Four-week fast track

If you have limited time:

1. **Week 1:** modules 19, 18, 16; foundation `p1`-`p11`.
2. **Week 2:** modules 01, 02, 03, 04, 07.
3. **Week 3:** modules 05, 06, 08, 09, 12.
4. **Week 4:** modules 14, 17, plus a small capstone.

Skip topics that are outside your goals, but do not skip evaluation, leakage, or error analysis.

## Study tips

- Type code instead of only reading it.
- Change one variable at a time and predict the result before running.
- Keep a list of assumptions and check them.
- When a score looks too good, look for leakage.
- Explain each metric in plain language before using it.
- Prefer a baseline first; compare every model to it.
- Revisit earlier notebooks after finishing later ones; the connections become clearer.
