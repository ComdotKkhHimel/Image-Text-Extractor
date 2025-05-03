from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
