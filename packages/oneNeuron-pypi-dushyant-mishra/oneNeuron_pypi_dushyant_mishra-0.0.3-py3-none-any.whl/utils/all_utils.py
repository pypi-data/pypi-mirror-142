import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import joblib # for saving my model as a binary file
from matplotlib.colors import ListedColormap
import os
import logging
plt.style.use("fivethirtyeight") # this is the style of the plot

def prepare_data(df, target_col="y"):

  """it is used to separate the dependent and independent variables

  Args:
      df (pd.DataFrame): its the pandas dataframe from the dataset
      
  Returns:
      tuple: it returns tuples of dependent and independent variables
  """
  logging.info("Preparing the data by segregating the dependent and independent variables")

  X = df.drop(target_col, axis=1) #axis=1 means that it will drop the y column in this case

  y = df[target_col]

  return X, y


def save_model(model, filename):
  """This saves the trained model

  Args:
      model (python object): trained model
      filename (str): path to save the trained model
  """
  logging.info("saving the trained model")
  model_dir = "models"
  os.makedirs(model_dir, exist_ok=True) # Only create a new directory if model_dir does not exist
  filePath = os.path.join(model_dir, filename) # models/filename
  joblib.dump(model, filePath)
  logging.info(f"saved the trained model to {filePath}")


def save_plot(df, file_name, model):
  """saves the plots

  Args:
      df: its a dataFrame
      file_name: its a path to save the plots
      model: trained model
  """
  def _create_base_plot(df):           #plots the data points and creates a base plot
    logging.info("creating the base plot")
    df.plot(kind="scatter", x="x1", y="x2", c="y", s=100, cmap="winter")
    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)
    plt.axvline(x=0, color="black", linestyle="--", linewidth=1)
    figure = plt.gcf()    # get current figure
    figure.set_size_inches(10, 8)

  def _plot_decision_regions(X, y, classfier, resolution=0.02):  #plots the decision boundaries
    logging.info("plotting the decision regions")
    colors = ("magenta", "green", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))]) # since we have a binary classifier (perceptron) but listed 4 colors above it will take the first two colors for y output values

    X = X.values # this is the x1 and x2 values as an array
    x1 = X[:, 0] # first column 
    x2 = X[:, 1] # second column
    x1_min, x1_max = x1.min() -1 , x1.max() + 1
    x2_min, x2_max = x2.min() -1 , x2.max() + 1  

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), 
                           np.arange(x2_min, x2_max, resolution))
    #print(xx1)
    #print(xx1.ravel(), end='\n')
    #print(xx1.ravel().T, end='\n')
    #print(xx1.shape, end='\n')
    
    Z = classfier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  #ravel converts to 1D array
    Z = Z.reshape(xx1.shape)
    #print(Z.reshape(xx1.shape), end='\n')

    plt.contourf(xx1, xx2, Z, alpha=0.2, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    plt.plot()

  X, y = prepare_data(df)
  
  _create_base_plot(df)
  _plot_decision_regions(X, y, model)

  plot_dir = "plots"
  os.makedirs(plot_dir, exist_ok=True) # Only create if plot_dir doesen't exist
  plotPath = os.path.join(plot_dir, file_name) # models/filename
  plt.savefig(plotPath)
  logging.info(f"saving the plot at {plotPath}")