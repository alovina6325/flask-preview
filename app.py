# app.py
from flask import Flask, request, render_template, send_from_directory
from demucs_utils import demucs_split
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['music']
    if not file:
        return "파일이 없습니다.", 400

    filename = file.filename
    track_id = str(uuid.uuid4())
    upload_dir = os.path.join('static/uploads', track_id)
    os.makedirs(upload_dir, exist_ok=True)

    input_path = os.path.join(upload_dir, filename)
    file.save(input_path)

    stem_folder, stems = demucs_split(input_path)

    if not stem_folder:
        return "Demucs 분리 실패", 500

    return render_template('stems.html',
                           stems=stems,
                           stem_folder_name=os.path.basename(stem_folder),
                           track_id=track_id)
