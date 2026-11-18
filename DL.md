# Deep Learning (Deferred)

This file is a placeholder roadmap for deep-learning topics. The current focus is the
classical-ML portion of the Semester 6 syllabus (`CSC604` / `CSL604`). Neural-network
foundations from the ML syllabus are listed here so they are not lost, but they are
intentionally parked until the DL phase starts.

Status: **not started**. Update this file when the official DL syllabus is available.

## 1. Neural-network foundations deferred from CSC604 / CSL604

These are the neural-network parts of the ML syllabus. A basic MLP + backpropagation
notebook already exists in `Advanced_ML/13_neural_networks/`, but the following need a
dedicated treatment later.

- [ ] Biological neuron vs artificial neuron
- [ ] Evolution of neural networks and ANN architecture
- [ ] McCulloch-Pitts model
- [ ] Perceptron model with bias
- [ ] Non-separable patterns and limitations of the perceptron
- [ ] Activation functions: binary, bipolar, continuous, ramp, sigmoid, tanh, ReLU, softmax
- [ ] Perceptron learning rule (step-by-step, from scratch)
- [ ] Delta learning rule / LMS / Widrow-Hoff rule
- [ ] Multi-layer perceptron architecture
- [ ] Hidden-layer weight adjustment
- [ ] Error backpropagation derivation and implementation
- [ ] Simple network design and training diagnostics

## 2. Deep-learning core

- [ ] Training deep networks: epochs, batches, learning-rate schedules
- [ ] Optimizers: SGD, momentum, RMSProp, Adam
- [ ] Weight initialization: Xavier and He
- [ ] Vanishing and exploding gradients
- [ ] Regularization: weight decay, dropout, batch normalization, early stopping
- [ ] Hyperparameter tuning and experiment tracking
- [ ] Loss functions for regression, binary, multi-class, and multi-label tasks
- [ ] GPU basics and mixed precision

## 3. Architectures

- [ ] Convolutional neural networks (CNNs)
- [ ] Recurrent networks: RNN, LSTM, GRU
- [ ] Attention and transformers
- [ ] Autoencoders and representation learning
- [ ] Generative models: GANs and diffusion models
- [ ] Transfer learning and fine-tuning
- [ ] Embeddings and vector search

## 4. Applied projects

- [ ] Image classification with a CNN
- [ ] Text classification with an RNN or transformer
- [ ] Time-series forecasting with a sequence model
- [ ] Fine-tuning a pretrained model
- [ ] Building and serving a small DL model

## 5. Prerequisites already in this repo

- Linear algebra: `Core_ML/f1_linear_algebra.ipynb`
- Probability: `Core_ML/f2_probability.ipynb`
- Optimization and gradient descent: `Core_ML/f3_optimization.ipynb`
- Introductory MLP/backprop: `Advanced_ML/13_neural_networks/13_neural_networks.ipynb`
- Evaluation: `Advanced_ML/03_model_evaluation/03_model_evaluation.ipynb`

## Notes

- Do not add DL notebooks to the current ML gap-filling pass.
- When the DL phase begins, convert each checklist item into either a notebook section or
  a standalone notebook, then update this file with links.
