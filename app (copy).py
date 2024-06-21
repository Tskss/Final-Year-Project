# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import csv
import requests
import config
import pickle
import io
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from chat import get_response
import os
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model

disease_dic= ["Benign","Melignant"]



from model_predict  import pred_leaf_disease

# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------
import random
import string

# Generate three random alphabets
random_alphabets = ''.join(random.choices(string.ascii_uppercase, k=3))

# Generate three random integers
random_integers = ''.join(random.choices(string.digits, k=3))

# Combine alphabets and integers
random_combination = random_alphabets + random_integers

print(random_combination)



app = Flask(__name__)

# render home page

# Function to initialize or load chat history
def load_chat_history():
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                chat_history.append({'random_combination':[0],'user_message': row[1], 'bot_response': row[2]})

    return chat_history

def load_chat_history2(target_combination):
    chat_history = []
    file_path = 'chat_history.csv'

    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the 'random_combination' field is in the second column (index 1)
                if len(row) > 1 and row[0] == target_combination:
                    chat_history.append({'random_combination': [0], 'user_message': row[1], 'bot_response': row[2]})

    return chat_history

# Function to save a new message to the chat history
def save_to_chat_history(random_combination,user_message, bot_response):
    file_path = 'chat_history.csv'

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([random_combination,user_message, bot_response])
@ app.route('/')
def home():
    title = 'Coalbot'
    return render_template('index4.html', title=title)

# render crop recommendation form page



@app.route('/chatboat', methods=['GET', 'POST'])
def chatboat():
   
    return render_template('chatbot.html')


@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Coalboat'

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

            if prediction=="Benign":
                precaution="Cancer is Not Melanoma"
 
            else:

                precaution="Cancer is Melanoma"
            patient_id = request.form.get('patient_id')
            patient_name = request.form.get('patient_name')
            age = request.form.get('age')
            date = request.form.get('date')
            gender = request.form.get('gender')

            print(patient_id,patient_name,age,date,gender)
                    
        # Your code to process the uploaded image and text inputs goes here

    #return render_template('disease.html', title=title)

            # Set up the canvas and page size

            import os

            # Create a folder with the patient name and ID
            folder_name = f"{patient_name}_{patient_id}"
            os.makedirs(folder_name, exist_ok=True)

            # Set up the canvas and page size
            pdf_file_name = f"{folder_name}/medical_report.pdf"
            c = canvas.Canvas(pdf_file_name, pagesize=letter)

 #           c = canvas.Canvas("medical_report.pdf", pagesize=letter)

            # Define the patient data
            #patient_id = '1232'
            #patient_name = 'Ravi'
            #age = '24'
            #date = '1898-12-11'
            #gender = 'male'
            skin_cancer = prediction

            # Write the report title
            c.setFontSize(16)
            c.drawString(50, 750, "Medical Report")

            # Write the patient information
            c.setFontSize(12)
            c.drawString(50, 700, "Patient ID: " + patient_id)
            c.drawString(50, 680, "Patient Name: " + patient_name)
            c.drawString(50, 660, "Age: " + age)
            c.drawString(50, 640, "Date: " + date)
            c.drawString(50, 620, "Gender: " + gender)
            c.drawString(50, 600, "Skin Cancer Diagnosis: " + skin_cancer)

            # Save the PDF file
            c.save()

            return render_template('disease-result.html', prediction=prediction,precaution=precaution,title=title)
        #except:
         #   pass
    return render_template('disease.html', title=title)

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # You can replace the next line with a call to an AI model for generating responses
    bot_response =get_response(user_message)

    save_to_chat_history(random_combination,user_message, bot_response)

    chat_history = load_chat_history2(random_combination)
    #return render_template('index.html', user_message=user_message, bot_response=bot_response)

    return render_template('chatbot.html', user_message=user_message, bot_response=bot_response, chat_history=chat_history)

# render disease prediction result page


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
