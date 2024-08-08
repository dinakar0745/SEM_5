from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('logistic_model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the form
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        profile_score = float(request.form['profile_score'])

        # Create a numpy array with the input values
        input_data = np.array([[cgpa, iq, profile_score]])

        # Standardize the input values
        input_data_scaled = scaler.transform(input_data)

        # Make a prediction
        prediction = model.predict(input_data_scaled)

        # Return the result
        if prediction[0] == 1:
            result = "The candidate is likely to be placed."
        else:
            result = "The candidate is unlikely to be placed."
    except Exception as e:
        result = f"An error occurred: {e}"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
