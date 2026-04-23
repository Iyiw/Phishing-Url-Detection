# 🔐 Phishing URL Detection using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-RandomForest-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Overview

This project detects **phishing URLs** using machine learning by analyzing URL structure, domain patterns, and lexical features.

Unlike basic implementations, this model avoids dataset leakage and focuses on **real-world generalization**, making it more reliable in practical cybersecurity scenarios.

---

## 🎯 Key Features

* URL-based feature engineering
* Domain & subdomain analysis
* IP address detection
* Random Forest classifier
* Cross-validation for robustness

---

## 🧠 Model Details

* Algorithm: Random Forest
* Trees: 200
* Train/Test Split: 70/30
* Focus: Reducing overfitting & improving real-world detection

---

## 📊 Sample Results

### 🔹 Confusion Matrix

> *(Add image in assets folder and link here)*

```
assets/confusion_matrix.png
```

---

### 🔹 Feature Importance

> *(Add image in assets folder and link here)*

```
assets/feature_importance.png
```

---

## 📂 Project Structure

```bash
Phishing-Url-Detection/
│
├── src/        # Source code
├── model/      # Trained model
├── assets/     # Visualizations
├── README.md
├── requirements.txt
```
# EXPLORE CODE

- Full Model Implementation ->
- [phishing.py](phishing.py)
---

##  How it Works

1. Extract features from URL  
2. Convert to numerical format  
3. Pass into trained Random Forest model  
4. Output prediction (Phishing / Legitimate)



## ▶️ How to Run

python phishing.py

## 🔍 Example

**Input:**

```text
http://secure-login-paypal.xyz
```

**Output:**

```text
⚠️ Phishing URL Detected
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and may not detect highly sophisticated phishing attacks used in real-world environments.

---

## 👨‍💻 Author

**Subhabrata**

---

## ⭐ Support

If you found this useful, consider giving the repo a ⭐ to support the project!

