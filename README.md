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

 # 🧠 2️⃣ Why It Is Called “Naive”?

    It assumes:
    
    All features are independent of each other.
    
    Example:
    
    It assumes:
    
    Sepal length does NOT depend on petal length
    
    Petal width does NOT depend on sepal width
    
    In real life, this may not be 100% true.
    
    That’s why it is called “Naive” assumption of independence.

# Gaussian Naive Bayes

    Since Iris features are continuous numbers, we use:
    
    👉 Gaussian Naive Bayes
    
    It assumes features follow normal distribution.

    The model calculates the probability of each flower species using Bayes’ theorem       and assumes feature independence. 
    
    It selects the species with the highest posterior probability."
      
