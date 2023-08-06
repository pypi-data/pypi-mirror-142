import numpy as np
import logging
from tqdm import tqdm

class Perceptron:
  def __init__(self, eta: float=None, epochs: int=None):
    self.weights = np.random.randn(3) * 1e-4 # Small Weight Initialization
    logging.info(f"initial weights before training: \n{self.weights}")
    self.eta = eta # Learning Rate
    self.epochs = epochs #Iterations
  
  def _z_outcome(self, inputs, weights):
    return np.dot(inputs, weights) # z = w * x

  def activationFunction(self, z):
    return np.where(z > 0, 1, 0) # Condition, if true, else

  def fit(self, X, y):
    self.X = X
    self.y = y

    X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))] # Concatenate
    logging.info(f"X with bias: \n{X_with_bias}")

    for epoch in tqdm(range(self.epochs), total=self.epochs, desc="training the model"):  #tqdm adds a progress bar
      logging.info("--"*10)
      logging.info(f"for epoch: {epoch}")
      logging.info("--"*10)

      z = self._z_outcome(X_with_bias, self.weights)
      y_hat = self.activationFunction(z) # foward propagation
      logging.info(f"predicted value after forward pass: \n{y_hat}")

      self.error = self.y - y_hat
      logging.info(f"error: \n{self.error}")

      total_loss = np.sum(self.error)
      logging.info(f"total loss: {total_loss}")      # returns the sum of all the errors 

      self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error) # backward propagation
      logging.info(f"updated weights after epoch:\n{epoch}/{self.epochs} : \n{self.weights}")
      logging.info("#####"*10)

  def predict(self, X):
    X_with_bias = np.c_[X, -np.ones((len(X), 1))]  #prediction is same as forward pass without the backward pass
    z= self._z_outcome(X_with_bias, self.weights)
    return self.activationFunction(z)

  def total_loss(self):
    total_loss = np.sum(self.error)
    logging.info(f"total loss: {total_loss}")
    return total_loss