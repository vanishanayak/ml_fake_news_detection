# 📰 Fake News Detection Using Machine Learning

> A Machine Learning-based web application that classifies news articles as **Fake** or **Real** using **TF-IDF Vectorization**, **Logistic Regression**, and **Streamlit**.

<p align="center">
  <img width="1224" height="603" alt="image" src="https://github.com/user-attachments/assets/dcb797a3-a6e2-49d8-98f7-4a2ae1d5964a" />


</p>

<p align="center">
  <b>Python • Machine Learning • NLP • Streamlit</b>
</p>

---

# 📖 Overview

Fake news spreads rapidly across online platforms, making it difficult to identify reliable information. This project presents a Machine Learning solution that analyzes the textual content of a news article and predicts whether it is **Fake** or **Real**.

The model is trained using Natural Language Processing (NLP) techniques with **TF-IDF Vectorization** and **Logistic Regression**, then deployed through an interactive <b>Streamlit</b> web application.

---

# ✨ Features

- 📰 Detects Fake and Real news articles
- 🤖 Logistic Regression based Machine Learning model
- 📄 TF-IDF text feature extraction
- 🌐 Interactive Streamlit web interface
- ⚡ Fast prediction with approximately **98% accuracy**
- 💾 Saved trained model for future predictions
- 🎯 Simple and user-friendly interface

---

# 📂 Dataset

The model is trained using two publicly available datasets.

| Dataset | Description | Records |
|---------|-------------|---------:|
| Fake.csv | Fake News Articles | 23,481 |
| True.csv | Real News Articles | 21,417 |

**Total Dataset Size:** **44,898 Articles**

### 📸 Dataset Overview

<p align="center">
<img width="580" height="373" alt="{691CE529-1871-4B9D-8150-E861643195EE}" src="https://github.com/user-attachments/assets/784277aa-a0f9-44ea-9f1a-b7eef0d9d2e6" />


</p>

---

# 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Regular Expressions (re)
- Visual Studio Code
- Git & GitHub

---

# ⚙️ Workflow

```
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Train-Test Split
   │
   ▼
Logistic Regression
   │
   ▼
Model Evaluation
   │
   ▼
Save Model
   │
   ▼
Streamlit Web Application
```

---

# 📊 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Logistic Regression |
| Feature Extraction | TF-IDF |
| Accuracy | **98%** |

### 📸 Model Performance

<p align="center">
<img width="772" height="348" alt="{5055D99C-90FF-4E8E-A12E-6AA844764749}" src="https://github.com/user-attachments/assets/2d4bf476-44dd-42f3-80fb-817b69c586fb" />

</p>

---

# 🖥 Application Screenshots

## ✅ Real News Prediction

The screenshot below demonstrates the model successfully identifying a genuine news article.

<p align="center">
  <img width="1032" height="610" alt="image" src="https://github.com/user-attachments/assets/6c326db0-31ef-47b7-bfff-cd453a601699" />

</p>

---

## ❌ Fake News Prediction

The screenshot below demonstrates the model successfully identifying a fake news article.

<p align="center">
  <img width="1048" height="604" alt="image" src="https://github.com/user-attachments/assets/00d87ea5-7df4-456c-bd8d-298d99829948" />

</p>

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/fake-news-detection-using-machine-learning.git
```

Move into the project folder

```bash
cd fake-news-detection-using-machine-learning
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model (Skip if `model.pkl` already exists)

```bash
python train.py
```

Run the application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

# 📁 Project Structure

```
fake-news-detection-using-machine-learning
│
├── dataset
│   ├── Fake.csv
│   └── True.csv
│
├── images
│   ├── home-page.png
│   ├── dataset-overview.png
│   ├── model-results.png
│   └── prediction-output.png
│
├── train.py
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

# 🎯 Future Scope

- Improve preprocessing using advanced NLP techniques.
- Train on larger and more diverse datasets.
- Implement transformer-based models such as **BERT**.
- Add multilingual news detection.
- Integrate live news APIs.
- Deploy the application on cloud platforms.

---

# 👨‍💻 Author

**Vanisha Nayak**

B.Tech (3rd Year)

Computer Science & Engineering(Artificial Intelligence and Machine learning)

---

<p align="center">
⭐ If you found this project useful, consider giving it a Star!
</p>