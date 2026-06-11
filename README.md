# 🌸 Iris Flower Species Prediction System

## Overview

The Iris Flower Species Prediction System is a Machine Learning web application that predicts the species of an Iris flower based on its physical measurements.

The application uses a trained Random Forest Classifier model and provides an interactive web interface built with Streamlit, allowing users to enter flower measurements and receive real-time predictions.

---

## Features

* Predicts Iris flower species instantly
* Interactive web interface using Streamlit
* Random Forest Machine Learning model
* Real-time predictions
* User-friendly sliders for feature input
* GitHub version controlled
* Deployment-ready application

---

## Technologies Used

* Python
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Streamlit
* Git & GitHub

---

## Dataset

This project uses the famous Iris Dataset, which contains measurements of three Iris flower species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

Features used:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

---

## Machine Learning Model

Algorithm Used:

* Random Forest Classifier

Model Workflow:

1. Load Iris Dataset
2. Preprocess Data
3. Split Dataset into Training and Testing Sets
4. Train Random Forest Model
5. Evaluate Model Performance
6. Save Model using Joblib
7. Deploy using Streamlit

---

## Project Structure

```text
iris-classification-ml/
│
├── data/
├── models/
├── src/
├── app.py
├── iris_model.pkl
├── iris_classification.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Trishi-rajeev/iris-classification-ml.git
cd iris-classification-ml
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Usage

1. Open the Streamlit application.
2. Adjust flower measurements using sliders.
3. Click the Predict button.
4. View the predicted Iris species.

---

## Sample Prediction

Input:

* Sepal Length: 5.8
* Sepal Width: 3.0
* Petal Length: 4.0
* Petal Width: 1.2

Output:

```text
Predicted Species: Versicolor
```

---

## Future Enhancements

* Deploy on Streamlit Cloud
* Add model performance visualization
* Add probability scores
* Compare multiple machine learning algorithms
* Improve UI/UX design

---

## Learning Outcomes

Through this project, I gained experience in:

* Machine Learning Model Development
* Classification Algorithms
* Model Serialization using Joblib
* Web Application Development with Streamlit
* Git and GitHub Workflow
* Model Deployment

---

## Author

Trishi Rajeev

GitHub:
https://github.com/Trishi-rajeev

```
```
