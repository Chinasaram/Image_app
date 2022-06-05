from fastapi import FastAPI, UploadFile

from . import models
from .database import engine
from .schema import Image

models.Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/upload_image")
def upload_image(image: UploadFile):
    """Uploads an image to the server"""
    return {"filename": image.filename}


@app.get("/get_image/all")
def get_all_images():
    """Gets all images from the server"""
    pass


@app.put("/update_image/{image_id}")
def update_image():
    """Updates an image on the server"""
    pass


@app.delete("/delete_image/{image_id}")
def delete_image(image_id: str, Image: Image):
    """Deletes an image from the server"""
    pass


@app.get("/get_image/{image_id}")
def get_image(image_id: str, Image: Image):
    """Gets an image from the server"""
    pass
