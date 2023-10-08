from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_data', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(gender=request.form.get('gender'),
                          race_ethnicity=request.form.get('race_ethnicity'),
                          parental_level_of_education=request.form.get(
                              'parental_level_of_education'),
                          lunch=request.form.get('lunch'),
                          test_preparation_course=request.form.get(
                              'test_preparation_course'),
                          reading_score=float(request.form.get('reading_score')),
                          writing_score=float(request.form.get('writing_score'))
                          )
        # print(data)
        dataframe = data.get_data_As_dataframe()
        pred_pipeline = PredictPipeline()

        predictions = pred_pipeline.predict(dataframe)
        return render_template('home.html', results=predictions[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
