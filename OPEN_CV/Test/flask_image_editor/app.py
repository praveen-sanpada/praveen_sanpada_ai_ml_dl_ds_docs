import os
from flask import Flask, render_template, request, send_file
import cv2
import numpy as np

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if not file:
            return "❌ No file uploaded"

        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)

        action = request.form.get("action")

        img = cv2.imread(filename)

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

        # Save processed image
        output_path = os.path.join(UPLOAD_FOLDER, "processed.png")
        cv2.imwrite(output_path, img)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
