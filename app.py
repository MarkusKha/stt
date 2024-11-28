import os
from flask import Flask, request, render_template, jsonify
import whisper
import tempfile

app = Flask(__name__)
model = None

def load_model():
    global model
    if model is None:
        # Using the 'base' model for good balance of speed and accuracy
        model = whisper.load_model("base")
    return model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        # Load model if not already loaded
        model = load_model()
        
        # Transcribe the audio
        result = model.transcribe(tmp_path)
        
        # Clean up the temporary file
        os.unlink(tmp_path)
        
        return jsonify({'text': result['text']})
    except Exception as e:
        # Clean up the temporary file in case of error
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Load the model when starting the server
    load_model()
    app.run(debug=True, port=5000)
