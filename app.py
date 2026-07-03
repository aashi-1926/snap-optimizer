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
        prompt = request.form["prompt"].lower()

        result = cloudinary.uploader.upload(image)

        public_id = result["public_id"]

        original_url = result["secure_url"]

        original_bytes = result["bytes"]
        original_width = result["width"]
        original_height = result["height"]

        image_url = original_url

        transformed_width = original_width
        transformed_height = original_height
        transformed_bytes = original_bytes

        # ENHANCE
        if (
                "enhance" in prompt
                or "bright" in prompt
                or "brighter" in prompt
                or "sharp" in prompt
                or "professional" in prompt
                or "improve" in prompt
                or "better quality" in prompt
        ):

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="brightness:50",
                quality="auto",
                fetch_format="auto"
            )

            transformed_bytes = int(original_bytes * 0.8)

        elif "sharp" in prompt or "sharpen" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="sharpen"
            )

        # REMOVE BACKGROUND
        elif "remove background" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="background_removal"
            )

            transformed_bytes = int(original_bytes * 0.7)

        # INSTAGRAM STORY
        elif "story" in prompt:

            transformed_width = 1080
            transformed_height = 1920

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=1080,
                height=1920,
                crop="fill"
            )

            transformed_bytes = int(original_bytes * 0.7)
        # PASSPORT PHOTO
        elif "passport" in prompt:

            transformed_width = 600
            transformed_height = 600

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=600,
                height=600,
                crop="fill"
            )

            transformed_bytes = int(original_bytes * 0.6)

        # INSTAGRAM
        elif "instagram" in prompt:

            transformed_width = 1080
            transformed_height = 1080

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=1080,
                height=1080,
                crop="fill"
            )

            transformed_bytes = int(original_bytes * 0.7)

        # PROFILE PICTURE
        elif "profile" in prompt:

            transformed_width = 500
            transformed_height = 500

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=500,
                height=500,
                crop="thumb",
                gravity="face"
            )

            transformed_bytes = int(original_bytes * 0.7)

        elif "youtube" in prompt or "thumbnail" in prompt:

            transformed_width = 1280
            transformed_height = 720

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=1280,
                height=720,
                crop="fill"
            )

            transformed_bytes = int(original_bytes * 0.8)

        elif "linkedin banner" in prompt:

            transformed_width = 1584
            transformed_height = 396

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=1584,
                height=396,
                crop="fill"
            )

        elif "black" in prompt or "grayscale" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="grayscale"
            )

        elif "blur" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="blur:300"
            )

        # LINKEDIN PROFILE PHOTO
        elif "linkedin profile" in prompt:

            transformed_width = 400
            transformed_height = 400

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                width=400,
                height=400,
                crop="thumb",
                gravity="face"
            )

            transformed_bytes = int(original_bytes * 0.7)

        # VINTAGE EFFECT
        elif "vintage" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="sepia"
            )

        # HDR EFFECT
        elif "hdr" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                effect="sharpen:100"
            )



        # COMPRESS
        elif "compress" in prompt:

            image_url = cloudinary.CloudinaryImage(
                public_id
            ).build_url(
                quality="auto:low"
            )

            transformed_bytes = int(original_bytes * 0.4)

        return render_template(
            "result.html",
            image_url=image_url,
            original_url=original_url,
            prompt=prompt,

            original_bytes=original_bytes,
            original_width=original_width,
            original_height=original_height,

            transformed_bytes=transformed_bytes,
            transformed_width=transformed_width,
            transformed_height=transformed_height
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)