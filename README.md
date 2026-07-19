# 📰 Fake News Detection Using Machine Learning

> A Machine Learning-based web application that classifies news articles as **Fake** or **Real** using **TF-IDF Vectorization**, **Logistic Regression**, and **Streamlit**.

<p align="center">
  <img width="1100" height="573" alt="image" src="https://github.com/user-attachments/assets/a9019fa0-ae7e-49c3-b10d-f1dacbbd75c5" />


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
<img width="654" height="430" alt="image" src="https://github.com/user-attachments/assets/c1ba5acc-97e6-4390-b2d0-741c971a7823" />




</p>
<p align="center">
<img width="751" height="413" alt="image" src="https://github.com/user-attachments/assets/75a510da-54fb-4f40-9b72-8de1d46c5c58" />





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
<img width="770" height="340" alt="image" src="https://github.com/user-attachments/assets/604ffc52-85ae-4c69-907b-339db41df7e5" />


</p>

---

# 🖥 Application Screenshots

## ✅ Real News Prediction

The screenshot below demonstrates the model successfully identifying a genuine news article.

<p align="center">
 
<img width="1030" height="608" alt="image" src="https://github.com/user-attachments/assets/8f3c89ef-1e40-41e8-9290-59d29c936fc5" />



</p>

---

## ❌ Fake News Prediction

The screenshot below demonstrates the model successfully identifying a fake news article.

<p align="center">
 
<img width="1118" height="610" alt="image" src="https://github.com/user-attachments/assets/06f7bdc9-f895-4238-af3c-7a76f7d6a558" />



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
