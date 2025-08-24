Background Remover Tool

A simple and efficient Background Remover Web Application built with HTML, CSS, JavaScript, and Flask (Python). This tool allows users to upload an image, automatically removes its background using AI (rembg & Pillow libraries), and provides an option to download the processed image.

Features :

- Upload images directly from your device
- Automatically remove image background
- Replace the background with white (default)
- Download the processed image instantly
- Lightweight and easy-to-use interface
- Runs locally with Flask backend

Tech Stack :

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Libraries Used:
  rembg :
    – AI-based background removal
  Pillow :
    – Image processing

Project Structure :

<img width="510" height="224" alt="image" src="https://github.com/user-attachments/assets/85cbbd6e-8199-4bfb-8aca-316da1b0618a" />


Installation & Setup :

- Clone the repository
- git clone https://github.com/yourusername/bg-remover-tool.git
  cd bg-remover-tool

- Create & activate virtual environment.
<img width="494" height="90" alt="image" src="https://github.com/user-attachments/assets/809598e0-0cd1-469d-b8a1-78b3a9745111" />


- Install dependencies
- pip install -r requirements.txt
  
- Run the Flask app
python app.py

- Open your browser and go to:
http://127.0.0.1:5000/

Usage :
- Upload an image from your device.
- The tool will remove the background automatically.
- Download the processed image in a single click.

Demo :
<img width="1261" height="887" alt="pic1" src="https://github.com/user-attachments/assets/e6f3b855-0c6d-49cc-987a-9d733f8528e0" />
<img width="1265" height="827" alt="pic2" src="https://github.com/user-attachments/assets/53784ea5-c88d-44ed-8b59-30cdfa85799a" />
<img width="1258" height="723" alt="pic3" src="https://github.com/user-attachments/assets/725398f2-57cb-42ab-a180-9e797fc85255" />
<img width="1265" height="733" alt="pic4" src="https://github.com/user-attachments/assets/b8f5e02f-4b79-412d-b438-48cafe15bace" />
<img width="1267" height="182" alt="pic5" src="https://github.com/user-attachments/assets/b9a94f87-fed4-45ab-92e1-a9f63ce12b5e" />


Contributing :

Contributions are welcome! If you’d like to improve the tool, feel free to:
-Fork the repo
-Create a new branch (feature-xyz)
-Commit your changes
-Open a pull request

License :

This project is licensed under the MIT License – free to use, modify, and distribute.

Acknowledgements :
- rembg
- Pillow
- Flask
