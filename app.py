from flask import Flask, render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application


@app.route('./')
def index():
    return render_template('index.html')
