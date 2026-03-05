from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Create a folder to store the voice recordings
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 1. ROUTE: Home Page (Dashboard)
@app.route('/')
def index():
    return render_template('index.html')

# 2. ROUTE: Voice Analysis Page
@app.route('/voice')
def voice_page():
    return render_template('voice.html')

# 3. ROUTE: Face Recognition Page
@app.route('/face')
def face_page():
    return render_template('face.html')

# 4. API: Receive Voice Data from the Browser
@app.route('/api/upload-voice', methods=['POST'])
def upload_voice():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file found"}), 400
    
    audio_file = request.files['audio']
    file_path = os.path.join(UPLOAD_FOLDER, "latest_recording.wav")
    audio_file.save(file_path)
    
    # This is where you would link an AI model to analyze the voice
    return jsonify({
        "status": "Success",
        "message": "Voice analysis complete",
        "result": "Normal hormonal pattern"
    })

if __name__ == '__main__':
    app.run(debug=True)