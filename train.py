import  pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

fake = pd.read_csv("dataset/Fake.csv")
true = pd.read_csv("dataset/True.csv")

print("Fake Dataset Information")
print(fake.info())

print("\nTrue Dataset Information")
print(true.info())

print("\nFake Dataset Shape:", fake.shape)
print("True Dataset Shape:", true.shape)

print("\nFake Dataset Columns:")
print(fake.columns)

print("\nTrue Dataset Columns:")
print(true.columns)

print("\nMissing Values in Fake Dataset:")
print(fake.isnull().sum())

print("\nMissing Values in True Dataset:")
print(true.isnull().sum()) 
fake["label"] = 0
true["label"] = 1


data = pd.concat([fake, true], ignore_index=True)

print("\nCombined Dataset Shape:")
print(data.shape)

print("\nLast 5 rows of Combined Dataset:")
print(data.tail())
# Shuffle the dataset
data = data.sample(frac=1, random_state=42)


data.reset_index(drop=True, inplace=True)

print("\nFirst 5 rows after shuffling:")
print(data.head())


data["text"] = data["text"].apply(clean_text)

print("\nCleaned News Text:")
print(data["text"].head())


X = data["text"]
y = data["label"]

print("\nFirst 5 Input Values (X):")
print(X.head())

print("\nFirst 5 Output Values (y):")
print(y.head())


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))


vectorizer = TfidfVectorizer(stop_words="english")

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("\nTraining Data Shape after TF-IDF:", X_train.shape)
print("Testing Data Shape after TF-IDF:", X_test.shape)


model = LogisticRegression()


model.fit(X_train, y_train)

print("\nModel training completed successfully!")


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


print("\nClassification Report:")
print(classification_report(y_test, y_pred))


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)


with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("\nModel and Vectorizer saved successfully!")