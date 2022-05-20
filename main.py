
from fastapi import FastApi


app = FastApi()


@app.post("/upload_image")
def upload_image():
    """Uploads an image to the server"""
    pass



@app.put("/update_image")
def update_image():
    """Updates an image on the server"""
    pass


@app.delete("/delete_image")
def delete_image():
    """Deletes an image from the server"""
    pass


@app.get("/get_image")
def get_image():
    """Gets an image from the server"""
    pass


@app.get("/all_images")
def get_all_images():
    """Gets all images from the server"""
    pass

