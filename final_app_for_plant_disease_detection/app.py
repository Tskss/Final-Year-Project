# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd

import requests
import config
import pickle
import io
from PIL import Image


# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model

disease_dic= ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___healthy',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']



from model_predict  import pred_leaf_disease

# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Plant Disease Detector'
    return render_template('index.html', title=title)

# render crop recommendation form page

@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Plant Disease Detection'

    if request.method == 'POST':
        #if 'file' not in request.files:
         #   return redirect(request.url)
            file = request.files.get('file')

            print(file)
        #if not file:
         #   return render_template('disease.html', title=title)
        #try:
            img1 = file.read()

            #print(img)

            prediction =pred_leaf_disease(img1)

            prediction = (str(disease_dic[prediction]))

            print(prediction)

            if prediction=="Apple___Apple_scab":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Apple___Black_rot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Apple___Cedar_apple_rust":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Corn___Cercospora_leaf_spot Gray_leaf_spot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Corn___Common_rust":

                 precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"  

            elif prediction=="Corn___Northern_Leaf_Blight":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Grape___Black_rot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Grape___Esca_(Black_Measles)":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Strawberry___Leaf_scorch":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Bacterial_spot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Early_blight":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Late_blight":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Leaf_Mold":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Septoria_leaf_spot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Spider_mites Two-spotted_spider_mite":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Target_Spot":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Tomato_mosaic_virus":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"
            elif prediction=="Tomato___Tomato_Yellow_Leaf_Curl_Virus":
                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"

            else:

                precaution="Contact : Expert X ,Contact Number :xxxxxxxxxx"




            return render_template('disease-result.html', prediction=prediction,precaution=precaution,title=title)
        #except:
         #   pass
    return render_template('disease.html', title=title)


# render disease prediction result page


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
