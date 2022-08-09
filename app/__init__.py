from flask import Flask
from app.config import Config
from flask_uploads import configure_uploads, IMAGES, UploadSet


app = Flask(__name__)
app.config.from_object(Config)

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

from app import routes