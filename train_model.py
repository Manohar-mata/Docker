# train_model.py
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
data = {'text': ['I love this!', 'This is bad.', 'Amazing product!', 'Worst experience ever.'],
        'label': ['positive', 'negative', 'positive', 'negative']}

# Create feature and label
df = pd.DataFrame(data)
X = df['text']
y = df['label']

# Text vectorization
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save model and vectorizer
with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
