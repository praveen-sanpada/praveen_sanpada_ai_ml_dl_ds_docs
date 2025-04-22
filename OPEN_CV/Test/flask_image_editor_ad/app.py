import os
import cv2
import datetime
from flask import Flask, render_template, request, send_from_directory

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def generate_filename(prefix="processed"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.png"

@app.route("/", methods=["GET", "POST"])
def index():
    original_path = None
    processed_path = None

    if request.method == "POST":
        file = request.files["image"]
        if not file:
            return "❌ No file uploaded"

        filename = generate_filename("original")
        original_full_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(original_full_path)
        original_path = f"uploads/{filename}"

        img = cv2.imread(original_full_path)
        action = request.form.get("action")

        # Handle actions
        if action == "grayscale":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        elif action == "resize":
            width = int(request.form.get("width", 300))
            height = int(request.form.get("height", 300))
            img = cv2.resize(img, (width, height))

        elif action == "crop":
            x = int(request.form.get("x", 0))
            y = int(request.form.get("y", 0))
            w = int(request.form.get("w", 100))
            h = int(request.form.get("h", 100))
            img = img[y:y+h, x:x+w]

        processed_filename = generate_filename("processed")
        processed_full_path = os.path.join(UPLOAD_FOLDER, processed_filename)
        processed_path = f"uploads/{processed_filename}"

        cv2.imwrite(processed_full_path, img)

        return render_template("index.html", original=original_path, processed=processed_path, download=processed_filename)

    return render_template("index.html")

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
