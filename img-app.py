from flask import Flask, render_template, request
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import os

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        image = request.files["image"]

        result = cloudinary.uploader.upload(image)

        image_url = result["secure_url"]

        return render_template(
            "result.html",
            image_url=image_url
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)