import cv2
import os
from app import app, images
from app.forms import ImageForm
from flask import request, render_template, url_for, redirect,flash
from werkzeug.utils import secure_filename


def make_sketch(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(grayed)
    blurred = cv2.GaussianBlur(inverted, (19, 19), sigmaX=0, sigmaY=0)
    final_result = cv2.divide(grayed, 255 - blurred, scale=256)
    return final_result


@app.route('/', methods=['GET', 'POST'])
@app.route('/sketch', methods=['GET', 'POST'])
def sketch():
    form = ImageForm()

    if request.method == 'POST' and form.validate_on_submit():
        filename = form.image.data.filename
        images.save(form.image.data)
        img = cv2.imread(app.config['UPLOADED_IMAGES_DEST']+'/'+filename)
        try:
            sketch_img = make_sketch(img)
            sketch_img_name = filename.split('.')[0]+"_sketch.jpg"
            sketch_location = cv2.imwrite(app.config['UPLOADED_IMAGES_DEST']+'/'+sketch_img_name, sketch_img)
            return render_template('base.html', form=form, org_img=filename, sketch_img=sketch_img_name, show=True)
        except:
            flash('This file is not an image!')

    return render_template('base.html', form=form, show=False)