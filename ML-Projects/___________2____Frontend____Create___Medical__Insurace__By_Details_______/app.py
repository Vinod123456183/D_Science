from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # Ensure this method is set to POST
def predict():
    # Get input data from form
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])
    
    # Prepare the input for prediction
    input_data = (age, sex, bmi, children, smoker, region)
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data_as_numpy_array)
    
    return render_template('result.html', prediction=prediction[0] , 2)

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found!", 404  # Basic error message for debugging

if __name__ == '__main__':
    app.run(debug=True)
