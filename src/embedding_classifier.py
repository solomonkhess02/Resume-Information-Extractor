from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
import joblib

model = SentenceTransformer("all-MiniLM-L6-v2")
clf = LogisticRegression()

def embed(texts):
    return model.encode(texts)

def train(texts, labels):
    X = embed(texts)
    clf.fit(X, labels)
    joblib.dump(clf, "resume_clf.pkl")

def predict(text):
    X = embed([text])
    return clf.predict(X)[0]
