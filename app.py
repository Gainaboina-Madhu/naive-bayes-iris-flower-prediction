from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

model = pickle.load(open("iris_model (1).pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        float(data["sepal_length"]),
        float(data["sepal_width"]),
        float(data["petal_length"]),
        float(data["petal_width"])
    ]])

    prediction = model.predict(features)[0]

    species = ["Setosa", "Versicolor", "Virginica"]
    return jsonify({"prediction": species[prediction]})

if __name__ == "__main__":
    app.run(debug=True)