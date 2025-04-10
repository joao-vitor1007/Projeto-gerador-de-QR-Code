from flask import Flask, render_template, request, send_from_directory
import qrcode
import os
import uuid


app = Flask(__name__)
QR_FOLDER = 'qrcodes'
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None

    if request.method == "POST":
        data = request.form["link"]
        filename = f"{uuid.uuid4().hex}.png"
        filepath = os.path.join(QR_FOLDER, filename)

        # Gerar o QR Code
        img = qrcode.make(data)
        img.save(filepath)

        qr_image = filename

    return render_template("index.html", qr_image=qr_image)

@app.route("/qrcodes/<filename>")
def get_qrcode(filename):
    return send_from_directory(QR_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)



