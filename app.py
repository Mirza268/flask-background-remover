from flask import Flask, render_template, request, send_file
from rembg import remove
import os
import time
import threading  # <- threading and time at top

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file = request.files['image']
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(PROCESSED_FOLDER, 'removed_' + file.filename)
    
    file.save(input_path)

    with open(input_path, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)

    with open(output_path, 'wb') as o:
        o.write(output_data)

    # ✅ Temporary file delete function inside the route
    def delete_temp_files():
        time.sleep(10)  # wait 10 seconds
        os.remove(input_path)
        os.remove(output_path)

    threading.Thread(target=delete_temp_files).start()

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
