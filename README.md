# naive-bayes-iris-flower-prediction

# 🌸 How This Project Works
# 🔹 1️⃣ What Problem It Solves

This project predicts the species of an Iris flower using machine learning.

**Based on four measurements:**

      Sepal Length
      Sepal Width
      Petal Length
      Petal Width
  
**The system classifies the flower into one of three species:**

      Iris Setosa
      Iris Versicolor
      Iris Virginica
  
 # 🔹 2️⃣ Why We Used Machine Learning
**We use a machine learning model because:**
  It automatically learns patterns from data
  It provides better accuracy
  It works for complex feature relationships
  It can generalize to new unseen data

# 🌸 What is Naive Bayes?
  Naive Bayes is a probability-based classification algorithm based on Bayes’ Theorem.
  It predicts the class (species) with the highest probability given the inputfeatures.

 # 📐 1️⃣ Bayes Theorem Formula

          The core formula is:
          
          P(A | B) = ( P(B | A) × P(A) ) / P(B)
          
          Where:
          
          P(A | B) → Probability of class A given features B
          
          P(B | A) → Probability of features given class A
          
          P(A) → Prior probability of class
          
          P(B) → Total probability of features



# Gaussian Naive Bayes

    Since Iris features are continuous numbers, we use:
    
    👉 Gaussian Naive Bayes
    
    It assumes features follow normal distribution.

    The model calculates the probability of each flower species using Bayes’ theorem       and assumes feature independence. 
    
    It selects the species with the highest posterior probability."

# Multi Level Classification
# 1️⃣ Data Loading

 - The first step in this project is loading the Iris dataset into the system.
 - If the dataset includes any unrelated columns such as an Id column, those are          removed because they do not contribute to prediction and may negatively affect         model performance.

# 2️⃣ Data Understanding and Exploration

 - Check the number of rows and columns
 - Verify data types of each feature
 - Ensure there are no missing values
 - Understand statistical properties like mean and standard deviation
      
# 3️⃣ Feature and Target Separation

 - The dataset is divided into two parts:
 - **Independent Variables (X)**
 - These are the input features used to make predictions:
 - Sepal Length
 - Sepal Width
 - Petal Length
 - Petal Width
 - **Dependent Variable (y)**
 - This is the output label:
 - Setosa
 - Versicolor
 - Virginica

# 4️⃣ Train-Test Split

 - To properly evaluate the model’s performance, the dataset is split into:
 - **Training Data (80%) – Used to train the model**
 - **Testing Data (20%) – Used to evaluate model performance**

# 5️⃣ Applying Naive Bayes Algorithm

 - In this project, Gaussian Naive Bayes is used because the features are continuous      numerical values.
 - Naive Bayes works based on Bayes’ Theorem and assumes that all features are            independent of each other.

# 6️⃣ Model Training

 - During training, the model learns:
 - Mean of each feature for each class
 - Variance of each feature for each class
 - Prior probability of each class

# 7️⃣ Model Prediction

 - After training, the model is used to predict the species of flowers in the test        dataset.

 - **For each flower:**
 - The algorithm calculates probability for each class
 - Compares probabilities
 - Selects the class with the highest probability

# 8️⃣ Model Evaluation

 - To measure performance, several evaluation metrics are used:
 - **🔹 Accuracy Score**
 - Measures how many predictions are correct out of total predictions.
 - 
# 🔹 Confusion Matrix

 - True Positives
 - True Negatives
 - False Positives
 - False Negatives
 - It helps understand where the model makes mistakes.

# 🔹 Classification Report

 - Precision
 - Recall
 - F1-Score
 - Support

# 9️⃣ Model Performance

 - **Gaussian Naive Bayes performs very well on the Iris dataset.**
 - Typical performance:
 - **Training Accuracy: Around 95–98%**
 - **Testing Accuracy: Around 93–97%**

# 🎯 Why Naive Bayes Was Chosen

 - Simple and fast algorithm
 - Works well for classification tasks
 - Suitable for small datasets
 - Requires less computational power
 - Produces good accuracy
