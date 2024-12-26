from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the saved model and vectorizer
with open('sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('index.html', result="Please enter some text.")
        
        # Transform input text and make prediction
        vectorized_text = vectorizer.transform([text])
        prediction = model.predict(vectorized_text)[0]
        return render_template('index.html', result=f'The sentiment is: {prediction}')
    return render_template('index.html', result="Invalid request.")

if __name__ == '__main__':
    app.run(debug=True)
