# demucs_utils.py
import subprocess
import os
import uuid

def demucs_split(audio_path, output_base_dir='static/results'):
    track_id = str(uuid.uuid4())
    output_dir = os.path.join(output_base_dir, track_id)
    os.makedirs(output_dir, exist_ok=True)

    # Demucs 실행
    try:
        subprocess.run([
            'demucs', '-o', output_base_dir, audio_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Demucs 실행 실패: {e}")
        return None, []

    # Demucs는 'htdemucs/{파일명}' 폴더에 결과 저장
    filename_wo_ext = os.path.splitext(os.path.basename(audio_path))[0]
    stem_folder = os.path.join(output_base_dir, 'htdemucs', filename_wo_ext)
    
    if not os.path.exists(stem_folder):
        print(f"[ERROR] 분리된 stem 폴더를 찾을 수 없습니다: {stem_folder}")
        return None, []

    stems = [f for f in os.listdir(stem_folder) if f.endswith('.wav')]

    return stem_folder, stems
