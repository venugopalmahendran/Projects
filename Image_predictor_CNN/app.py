from flask import Flask, request, jsonify, render_template
import os
from transferlearning import model


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/imageslist')
def list():
    return render_template('imageslist.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"response": "ERROR: No image file found in request."})
    img_file=request.files['image']
    img_path=img_file.filename
    img_file.save(img_path)
    decoded=model.transform([img_path])
    return jsonify({"result": decoded})

if __name__ == "__main__":
    print("🚀 Server starting at http://127.0.0.1:5000")
    app.run(debug=True)
