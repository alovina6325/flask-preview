from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'music' not in request.files:
        return "음악 파일이 없습니다."

    file = request.files['music']
    if file.filename == '':
        return "선택된 파일이 없습니다."

    # 저장
    filename = str(uuid.uuid4()) + "_" + file.filename
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)

    return f"✅ 업로드 성공: {filename}"
