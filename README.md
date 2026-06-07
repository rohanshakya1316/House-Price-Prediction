# 🏠 House Price Prediction System

A Machine Learning-powered web application built using **Flask** that predicts house prices based on various property characteristics. The application leverages machine learning algorithms to analyze housing data and provide accurate property price estimations through a simple and user-friendly web interface.

---

## 📖 Overview

The House Price Prediction System is an end-to-end machine learning project that follows the complete data science lifecycle, from data preprocessing and model training to deployment using Flask.

The system analyzes property-related features and predicts the estimated market price of a house. Multiple machine learning models were trained and evaluated, and the best-performing model was selected for deployment.

---

## 🎯 Project Objectives

* Predict house prices based on property features.
* Compare multiple machine learning algorithms.
* Select the best-performing model using evaluation metrics.
* Deploy the trained model using Flask.
* Provide a simple and interactive web interface for users.

---

## 🏗️ Project Structure

```bash
HOUSE-PRICE-PREDICTION/
│
├── dataset/
│   └── dataset.csv
│
├── notebook/
│   ├── house_price_prediction.ipynb
│   └── house_price_model_final.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Information

The dataset contains housing-related information used for training and testing the machine learning models.

### Features

| Feature       | Description                              |
| ------------- | ---------------------------------------- |
| Property_ID   | Unique identifier for each property      |
| Area          | Total area of the property               |
| Bedrooms      | Number of bedrooms                       |
| Bathrooms     | Number of bathrooms                      |
| Age           | Age of the property                      |
| Location      | Property location                        |
| Property_Type | Type of property                         |
| Price         | Property selling price (Target Variable) |

### Target Variable

```text
Price
```

The goal of the model is to predict the **Price** of a property based on the provided features.

---

## 🤖 Machine Learning Models Used

The following regression algorithms were trained and evaluated:

### 1. Linear Regression

A statistical model that establishes a linear relationship between independent variables and the target variable.

**Advantages:**

* Fast training
* Easy interpretation
* Strong baseline model

---

### 2. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

**Advantages:**

* Handles nonlinear relationships
* Reduces overfitting
* Robust and reliable performance

---

### 3. Gradient Boosting Regressor

A boosting algorithm that builds decision trees sequentially to minimize prediction errors.

**Advantages:**

* High prediction accuracy
* Handles complex data patterns
* Excellent performance on structured datasets

---

## 📈 Model Evaluation

The models were compared using standard regression evaluation metrics:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

After evaluating all three models, the best-performing model was selected and deployed.

---

## 💾 Model Persistence

The final trained model was serialized using Python Pickle and saved as:

```text
house_price_model_final.pkl
```

> **Note:** The model file is intentionally excluded from this GitHub repository and added to `.gitignore`. To run the application locally, place the trained model file inside the `notebook/` directory.

---

## 🌐 Web Application

The project uses **Flask** to serve the machine learning model and provide real-time predictions through a web interface.

### Features

* Real-time house price prediction
* User-friendly interface
* Fast prediction response
* Machine learning model integration
* Responsive design

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
```

### Navigate to Project Directory

```bash
cd house-price-prediction
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add the Trained Model

Place the file:

```text
house_price_model_final.pkl
```

inside:

```text
notebook/
```

### Run the Flask Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🔄 System Workflow

```text
Dataset Collection
       │
       ▼
Data Preprocessing
       │
       ▼
Feature Engineering
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Best Model Selection
       │
       ▼
Model Serialization (.pkl)
       │
       ▼
Flask Deployment
       │
       ▼
User Prediction Interface
```

---

## 🖥️ Input Parameters

Users provide the following property details:

* Area
* Bedrooms
* Bathrooms
* Age
* Location
* Property Type

The system processes the information and predicts the estimated property price.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning Libraries

* Scikit-Learn
* Pandas
* NumPy

### Backend Framework

* Flask

### Frontend Technologies

* HTML5
* CSS3

### Development Tools

* Jupyter Notebook
* Visual Studio Code

---

## 🚀 Future Enhancements

* Property image analysis
* Interactive analytics dashboard
* Cloud deployment (AWS, Azure, Render)
* Real estate API integration
* User authentication system
* Advanced feature engineering

---

## 👨‍💻 Author

**Rohan Shakya**


---

## ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.

Your support motivates continuous improvement and future open-source contributions.

---

### "Predicting House Prices Using Machine Learning and Flask"

An end-to-end Machine Learning Deployment Project demonstrating data preprocessing, model training, model evaluation, and web application deployment.
