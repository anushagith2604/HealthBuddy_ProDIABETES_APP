
# 🩸 A1C Pathology Test – Diabetes Prediction App

A lightweight machine learning-based web application built using **Streamlit** to predict whether a patient is diabetic, based on clinical input data including glucose level, blood pressure, BMI, and more.

---

## 🧠 Overview

This app uses a trained machine learning model (saved in `.sav` format) to predict **diabetes status** from key health indicators derived from A1C and related pathology tests. Users can enter test values through a simple web form, and get an instant prediction result.

---

## 🔍 Key Features

* 🩺 Predicts if a patient is **diabetic or not**
* 📊 Uses 8 important input features (from Pima Indian dataset or similar)
* 🖥️ Built with **Streamlit** – deployable on local or cloud
* 🧠 Uses a pre-trained model saved as `trained_model.sav`

---

## 🧪 Inputs

| Feature                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| Pregnancies              | Number of times pregnant                                             |
| Glucose                  | Plasma glucose concentration                                         |
| BloodPressure            | Diastolic blood pressure (mm Hg)                                     |
| SkinThickness            | Triceps skin fold thickness (mm)                                     |
| Insulin                  | 2-Hour serum insulin (mu U/ml)                                       |
| BMI                      | Body mass index (weight in kg/(height in m)^2)                       |
| DiabetesPedigreeFunction | Function which scores likelihood of diabetes based on family history |
| Age                      | Age of the patient (in years)                                        |

---

## 🧾 Output

* **Prediction:**

  * ✅ "The patient is not diabetic"
  * ❌ "The patient is diabetic"

---

## 🚀 How to Run the App

### 1. Clone the repository or download the `.py` script

```bash
git clone https://github.com/yourusername/a1c-diabetes-predictor.git
cd a1c-diabetes-predictor
```

### 2. Install Dependencies

```bash
pip install streamlit numpy scikit-learn
```

### 3. Place your trained model

Place your `trained_model.sav` in the correct path. (Update the code if needed — ideally avoid hardcoding Windows paths.)

```bash
# Example: Save the model in the current directory
.
├── trained_model.sav
├── app.py
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🛠️ File Structure

```
a1c-diabetes-predictor/
├── app.py                 # Streamlit main app file
├── trained_model.sav      # Pre-trained ML model (pickle format)
└── README.md
```

---

## 🧠 Model Info

The model can be trained using the **Pima Indian Diabetes Dataset** from Kaggle/UCI. It is serialized using `pickle` as `trained_model.sav`.

> **Note:** Always normalize/scale data the same way it was during training.

---

## ⚠️ Issues in Current Code

You need to fix these small errors:

### 1. Fix `if __name__ == '__main__'` line:

```python
if __name__ == '__main__':
    main()
```

### 2. Convert inputs to `float` before prediction:

```python
diagnosis = diabetes_prediction([float(Pregnancies), float(Glucose), ...])
```

---

## 📜 License

MIT License — Free to use for academic and research purposes.

---

Let me know if you’d like:

* A training script for `trained_model.sav`
* Streamlit cloud deployment guide
* Support for saving predictions to CSV or database
