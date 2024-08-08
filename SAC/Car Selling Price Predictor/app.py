from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('car_price_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    mileage = int(request.form['mileage'])
    
    # Make a prediction using the model
    prediction = model.predict(np.array([[age, mileage]]))
    selling_price = prediction[0]
    
    return render_template('result.html', price=selling_price)

if __name__ == '__main__':
    app.run(debug=True)
