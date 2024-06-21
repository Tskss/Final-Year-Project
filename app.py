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

from flask import Flask, render_template, request, redirect, url_for
import sounddevice as sd
import numpy as np
import librosa
from flask import Flask, render_template, request, redirect, url_for
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write, read
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr




import joblib
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import random



import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
from final_app_for_plant_disease_detection.model_predict import pred_leaf_disease

from crop_yield.yield_code import yield_fn

from crop_recommendation.recemmendation_code import recondation_fn


from fertiliser_recommendation.fertiliser_recommendation import recondation_fertiliser_fn

features_list4=['Temparature', 'Humidity ', 'Moisture', 'Nitrogen', 'Potassium',
       'Phosphorous', 'Black', 'Clayey', 'Loamy', 'Red',
       'Sandy', 'Barley', 'Cotton', 'Ground Nuts', 'Maize', 'Millets',
       'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane', 'Tobacco', 'Wheat']

features_list3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Load column names from the pickle file
with open('column_names2.pkl', 'rb') as file:
    loaded_column_names = pickle.load(file)

# Print the loaded column names
print(loaded_column_names)


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

#from model_predict  import pred_leaf_disease
#yield_inputs=[]

features_list=loaded_column_names
# Load the list from the pickle file
with open('zero_list2.pkl', 'rb') as file:
    loaded_list = pickle.load(file)

# Print the loaded list
print(loaded_list)

features_list1=loaded_list

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading plant disease classification model

#disease_dic= ["Benign","Melignant"]



#from model_predict  import pred_leaf_disease

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
#@ app.route('/')
#def home():
#    title = 'Coalbot'
#    return render_template('index4.html', title=title)

# render crop recommendation form page
@app.route('/')
def home():
    return render_template('index5.html') 

@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()
              #print(result1)
              #print(gmail1)
    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('chatbot.html')
    else:
        return jsonify({'result':'use proper  gmail and password'})
                  
                                               



                          
                     # print(value1[0:])
    
    
    
    

              
              # int_features3[0]==12345 and int_features3[1]==12345:
               #                      return render_template('index.html')
        
@app.route('/register',methods=['POST'])
def register():
    

    int_features2 = [str(x) for x in request.form.values()]
    #print(int_features2)
    #print(int_features2[0])
    #print(int_features2[1])
    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0]
    passw1=int_features2[1]
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root",'',"ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list1)
    if logu1 in gmail_list1:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                 # return jsonify({'result':'succesfully registered'})
                  return render_template('login44.html')

                      



@app.route('/chatboat', methods=['GET', 'POST'])
def chatboat(): 
   
    return render_template('login44.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # You can replace the next line with a call to an AI model for generating responses
    bot_response ,predicted_tag=get_response(user_message)

    #save_to_chat_history(random_combination,user_message, bot_response)

    #chat_history = load_chat_history2(random_combination)

  #  print("the random generated result is ",chat_history)





    # Extract 'bot_response' value
    #bot_response_value = chat_history[0]['bot_response']

    
    from gtts import gTTS
    from pydub import AudioSegment
    import pygame
    import os

    text = str(bot_response)
    language = 'en'

    try:
        # Create gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio in a file
        tts.save("output.mp3")
        print("Audio file saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Play the saved audio file using pygame
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("output.mp3")

        # Play the audio file
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value as needed

        # Close the mixer
        pygame.mixer.quit()

    except Exception as e:
        print(f"Error playing audio: {e}")
    if predicted_tag=="crop_yield_prediction":
        print("it is crop yield problem")
        import tkinter as tk
        from tkinter import simpledialog

        def get_user_input():
            # Create a Toplevel window for the popup form
            popup = tk.Toplevel(root)
            popup.title("Popup Form")

            # HTML-like input fields
            fields = [
                ("State name", "experience", None),
                ("District name", "test_score", None),
                ("Select Season Type", "interview_score2", ["Autumn     ", "Kharif     ", "Rabi       ", "Summer     ", "Whole Year ", "Winter     "]),
                ("Crop", "interview_score3", None),
                ("Area", "interview_score4", None),
                ("Select Soil Type", "interview_score9", ["chalky", "clay", "loamy", "peaty", "sandy", "silt", "silty"]),
                ("Temperature", "temperature", None),
                ("Wind Speed", "wind_speed", None),
                ("Precipitation", "precipitation", None),
                ("Humidity", "humidity", None),
                ("N", "N", None),
                ("P", "P", None),
                ("K", "K", None),
                ("Pressure", "pressure", None),
            ]

            # Function to handle form submission
            def submit_form():
                user_inputs = {}
                for label, name, options in fields:
                    if options:
                        user_inputs[name] = option_var[name].get()
                    else:
                        user_inputs[name] = entry_var[name].get()

                print("User entered:", user_inputs)
                all_values=[]
                all_values = [value if not value.isdigit() else float(value) for value in user_inputs.values()]

                print("these are the values  you enterd in form",all_values)
                int_features =all_values


               # print("output from web page  ",int_features)

                #features_list1[83]=int_features[0]
                print("these are the inputs feeding to the application",int_features)



                state_ind=features_list.index(int_features[0])

                print(state_ind)

                features_list1[state_ind]=1



                print(int_features[1])


                


                #print(features_list.index('DHULE'))


                dist_ind=features_list.index(int_features[1])

                print(dist_ind)

                features_list1[dist_ind]=1

                season_ind=features_list.index(int_features[2])

                features_list1[season_ind]=1

                crop_ind=features_list.index(int_features[3])

                features_list1[crop_ind]=1

                crop_ind=features_list.index(int_features[5])

                features_list1[crop_ind]=1


                features_list1[0]=float(int_features[4])

               




                a=features_list1


                print(a)

                output_yield=yield_fn(features_list1)

                #features_list1=loaded_list

                random_float = round(random.uniform(0,0.09), 2)



                output_yield=random_float+output_yield
                text_data = "total crop yield will be  " +str(output_yield[0])+ "  quintols for hectare"
                with open('crop_yield.pkl', 'wb') as file:
                    pickle.dump(text_data, file)

                print("total yield will be ",output_yield)
                #yield_inputs=all_values
                popup.destroy()

            # Create and pack input fields
            entry_var = {}
            option_var = {}
            for label, name, options in fields:
                if options:
                    option_var[name] = tk.StringVar(value=options[0])
                    option_menu = tk.OptionMenu(popup, option_var[name], *options)
                    option_menu.pack(pady=5)
                else:
                    entry_var[name] = tk.StringVar()
                    
                    entry = tk.Entry(popup, textvariable=entry_var[name], width=30)

                    entry.pack(pady=5)
                tk.Label(popup, text=label).pack()

            # Create and pack submit button
            submit_button = tk.Button(popup, text="Submit", command=submit_form)
            submit_button.pack(pady=10)

        # Create the main window
        root = tk.Tk()
        root.title("Popup Form Example")

        # Trigger the popup form immediately
        get_user_input()

        # Start the main loop
        root.mainloop()

        from translate import Translator

        def translate_text(text, target_language):
            translator= Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
        # Load the data from the pickle file
        with open('crop_yield.pkl', 'rb') as file:
            loaded_data_yield = pickle.load(file)
        text_to_translate =loaded_data_yield
        # Translate to Kannada
        english_translation=text_to_translate
        kannada_translation = translate_text(text_to_translate, "kn")
        print(f"Kannada: {kannada_translation}")

        # Translate to Hindi
        hindi_translation = translate_text(text_to_translate, "hi")
        print(f"Hindi: {hindi_translation}")

        # Translate to Tamil
        tamil_translation = translate_text(text_to_translate, "ta")
        print(f"Tamil: {tamil_translation}")

        # Translate to Malayalam
        malayalam_translation = translate_text(text_to_translate, "ml")
        print(f"Malayalam: {malayalam_translation}")


        marathi_translation = translate_text(text_to_translate, "mr")
        print(f"marathi: {marathi_translation}")

        # Print the result
        print("this is the text response for present question",loaded_data_yield)
        #return render_template('index.html', user_message=user_message, bot_response=bot_response)
        save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

        chat_history = load_chat_history2(random_combination)

        #bot_response_value = chat_history[0]['bot_response']

        return render_template('chatbot.html', user_message=user_message, bot_response=loaded_data_yield, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)

 
 
 

    elif predicted_tag=="crop_recommendation":
        print("it is recommendation problem")

    #if predicted_tag=="crop_yield_prediction":
        #print("it is crop yield problem")
        import tkinter as tk
        from tkinter import simpledialog

        def get_user_input():
            # Create a Toplevel window for the popup form
            popup = tk.Toplevel(root)
            popup.title("Popup Form")

            # HTML-like input fields
            fields = [
                ("temperature", "experience", None),
                ("Humidity", "test_score", None),
                ("Rain falle", "test_score4", None),

                ("Select Soil Type", "interview_score9", ["chalky", "clay", "loamy", "peaty", "sandy", "silt", "silty"]),
               
            ]

            # Function to handle form submission
            def submit_form():
                user_inputs = {}
                for label, name, options in fields:
                    if options:
                        user_inputs[name] = option_var[name].get()
                    else:
                        user_inputs[name] = entry_var[name].get()

                print("User entered:", user_inputs)
                all_values=[]
                all_values = [value if not value.isdigit() else float(value) for value in user_inputs.values()]

                print("these are the values  you enterd in form",all_values)
                int_features =all_values


               # print("output from web page  ",int_features)

                #features_list1[83]=int_features[0]
                print("these are the inputs feeding to the application",int_features)

                a1=int_features[0]
                a2=int_features[1]
                a3=int_features[2]


                output1 = recondation_fn(a1,a2,a3)
                print(output1)               


                #output_yield=recondation_fn(a1,a2,a3)

                #features_list1=loaded_list

                #random_float = round(random.uniform(0,0.09), 2)



                #output_yield=random_float+output_yield
                text_data2 = "The Best Plant That you can Cultivate is   " +str(output1[0])
                with open('recommendation.pkl', 'wb') as file:
                    pickle.dump(text_data2, file)

                print("total yield will be ",output1)
                #yield_inputs=all_values
                popup.destroy()

            # Create and pack input fields
            entry_var = {}
            option_var = {}
            for label, name, options in fields:
                if options:
                    option_var[name] = tk.StringVar(value=options[0])
                    option_menu = tk.OptionMenu(popup, option_var[name], *options)
                    option_menu.pack(pady=5)
                else:
                    entry_var[name] = tk.StringVar()
                    
                    entry = tk.Entry(popup, textvariable=entry_var[name], width=30)

                    entry.pack(pady=5)
                tk.Label(popup, text=label).pack()

            # Create and pack submit button
            submit_button = tk.Button(popup, text="Submit", command=submit_form)
            submit_button.pack(pady=10)

        # Create the main window
        root = tk.Tk()
        root.title("Popup Form Example")

        # Trigger the popup form immediately
        get_user_input()

        # Start the main loop
        root.mainloop()

        from translate import Translator

        def translate_text(text, target_language):
            translator= Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
        # Load the data from the pickle file
        with open('recommendation.pkl', 'rb') as file:
            loaded_data_rcmd = pickle.load(file)
        text_to_translate =loaded_data_rcmd
        # Translate to Kannada


        english_translation=text_to_translate
        kannada_translation = translate_text(text_to_translate, "kn")
        print(f"Kannada: {kannada_translation}")

        # Translate to Hindi
        hindi_translation = translate_text(text_to_translate, "hi")
        print(f"Hindi: {hindi_translation}")

        # Translate to Tamil
        tamil_translation = translate_text(text_to_translate, "ta")
        print(f"Tamil: {tamil_translation}")

        # Translate to Malayalam
        malayalam_translation = translate_text(text_to_translate, "ml")
        print(f"Malayalam: {malayalam_translation}")
        marathi_translation = translate_text(text_to_translate, "mr")
        print(f"marathi: {marathi_translation}")

        # Print the result
        print("this is the text response for present question",loaded_data_rcmd )
        #return render_template('index.html', user_message=user_message, bot_response=bot_response)
        save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

        chat_history = load_chat_history2(random_combination)
        return render_template('chatbot.html', user_message=user_message, bot_response=text_to_translate, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)


    elif predicted_tag=="unknown":
        #print("it is recommendation problem")

   



                #output_yield=random_float+output_yield
        text_data2 = "Please ask valid questions .this is agribot we can help you resolve problem related to agriculture."


        from translate import Translator

        def translate_text(text, target_language):
            translator= Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
        # Load the data from the pickle file
       # with open('recommendation.pkl', 'rb') as file:
        #    loaded_data_rcmd = pickle.load(file)
        text_to_translate =text_data2 
        # Translate to Kannada


        english_translation=text_to_translate
        kannada_translation = translate_text(text_to_translate, "kn")
        print(f"Kannada: {kannada_translation}")

        # Translate to Hindi
        hindi_translation = translate_text(text_to_translate, "hi")
        print(f"Hindi: {hindi_translation}")

        # Translate to Tamil
        tamil_translation = translate_text(text_to_translate, "ta")
        print(f"Tamil: {tamil_translation}")

        # Translate to Malayalam
        malayalam_translation = translate_text(text_to_translate, "ml")
        print(f"Malayalam: {malayalam_translation}")
        marathi_translation = translate_text(text_to_translate, "mr")
        print(f"marathi: {marathi_translation}")

        # Print the result
        #print("this is the text response for present question",loaded_data_rcmd )
        #return render_template('index.html', user_message=user_message, bot_response=bot_response)
        save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

        chat_history = load_chat_history2(random_combination)
        return render_template('chatbot.html', user_message=user_message, bot_response=text_to_translate, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)




    elif  predicted_tag=="fertilizer_recommendation":
        print("it is Fertiliser recommendation problem")
        print("it is crop yield problem")
        import tkinter as tk
        from tkinter import simpledialog

        def get_user_input():
            # Create a Toplevel window for the popup form
            popup = tk.Toplevel(root)
            popup.title("Popup Form")

            # HTML-like input fields
            fields =fields_fertilizer = [
    ("Temperature", "temperature", None),
    ("Humidity", "humidity", None),
    ("Moisture", "moisture", None),
    ("Nitrogen", "nitrogen", None),
    ("Potassium", "potassium", None),
    ("Phosphorus", "phosphorus", None),
    ("Soil Type", "soil_type", ["Black", "Clayey", "Loamy", "Red", "Sandy"]),
    ("Crop", "crop", ['Barley', 'Cotton', 'Ground Nuts', 'Maize', 'Millets', 'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane', 'Tobacco', 'Wheat'])
]

            # Function to handle form submission
            def submit_form():
                user_inputs = {}
                for label, name, options in fields:
                    if options:
                        user_inputs[name] = option_var[name].get()
                    else:
                        user_inputs[name] = entry_var[name].get()

                print("User entered:", user_inputs)
                all_values=[]
                all_values = [value if not value.isdigit() else float(value) for value in user_inputs.values()]

                print("these are the values  you enterd in form",all_values)
                int_features =all_values


               # print("output from web page  ",int_features)

                #features_list1[83]=int_features[0]
                print("these are the inputs feeding to the application",int_features)




                features_list3[0]=float(int_features[0])
                features_list3[1]=float(int_features[1])
                features_list3[2]=float(int_features[2])
                features_list3[3]=float(int_features[3])
                features_list3[4]=float(int_features[4])
                features_list3[5]=float(int_features[5])

                crop_ind=features_list4.index(int_features[6])

                features_list3[crop_ind]=1

                crop_ind=features_list4.index(int_features[7])

                features_list3[crop_ind]=1               




                a=features_list3


                print(a)
                from fertiliser_recommendation.fertiliser_recommendation import recondation_fertiliser_fn

                output_yield=recondation_fertiliser_fn(features_list3)

                #features_list1=loaded_list

                #random_float = round(random.uniform(0,0.09), 2)



                output_yield=output_yield
                text_data = "The best fertiliser you need to use is     " +str(output_yield[0])
                with open('crop_yield.pkl', 'wb') as file:
                    pickle.dump(text_data, file)

                print("total yield will be ",output_yield)
                #yield_inputs=all_values
                popup.destroy()

            # Create and pack input fields
            entry_var = {}
            option_var = {}
            for label, name, options in fields:
                if options:
                    option_var[name] = tk.StringVar(value=options[0])
                    option_menu = tk.OptionMenu(popup, option_var[name], *options)
                    option_menu.pack(pady=5)
                else:
                    entry_var[name] = tk.StringVar()
                    
                    entry = tk.Entry(popup, textvariable=entry_var[name], width=30)

                    entry.pack(pady=5)
                tk.Label(popup, text=label).pack()

            # Create and pack submit button
            submit_button = tk.Button(popup, text="Submit", command=submit_form)
            submit_button.pack(pady=10)

        # Create the main window
        root = tk.Tk()
        root.title("Popup Form Example")

        # Trigger the popup form immediately
        get_user_input()

        # Start the main loop
        root.mainloop()

        from translate import Translator

        def translate_text(text, target_language):
            translator= Translator(to_lang=target_language)
            translation = translator.translate(text)
            return translation
        # Load the data from the pickle file
        with open('crop_yield.pkl', 'rb') as file:
            loaded_data_yield = pickle.load(file)
        text_to_translate =loaded_data_yield
        # Translate to Kannada
        english_translation=text_to_translate 
        kannada_translation = translate_text(text_to_translate, "kn")
        print(f"Kannada: {kannada_translation}")

        # Translate to Hindi
        hindi_translation = translate_text(text_to_translate, "hi")
        print(f"Hindi: {hindi_translation}")

        # Translate to Tamil
        tamil_translation = translate_text(text_to_translate, "ta")
        print(f"Tamil: {tamil_translation}")

        # Translate to Malayalam
        malayalam_translation = translate_text(text_to_translate, "ml")
        print(f"Malayalam: {malayalam_translation}")
        marathi_translation = translate_text(text_to_translate, "mr")
        print(f"marathi: {marathi_translation}")

        # Print the result
        print("this is the text response for present question",loaded_data_yield)
        #return render_template('index.html', user_message=user_message, bot_response=bot_response)
        save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

        chat_history = load_chat_history2(random_combination)
        return render_template('chatbot.html', user_message=user_message, bot_response=loaded_data_yield, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)

 
    elif predicted_tag=="plant_disease_solution":
                import tkinter as tk
                from tkinter import filedialog
                from PIL import Image, ImageTk
                import os

                # Function for fertilizer recommendation (replace with your actual implementation)
                def recondation_fertiliser_fn(features_list):
                    # Replace this with your actual implementation
                    return [0]  # Placeholder for demonstration

                def get_user_input():
                    def upload_file():
                        file_path = filedialog.askopenfilename()
                        if file_path:
                            # Displaying the file path (you can remove or modify this line)
                            file_path_label.config(text=f"Selected file: {file_path}")
                            # Perform any further processing with the file as needed
                            save_image_as_png(file_path)

                    def save_image_as_png(file_path):
                        #image = Image.open(file_path)
                        #print("complete image path is ")
                        #output_path = os.path.join(os.path.dirname(file_path), "output2.png")
                        #image.save(output_path, "PNG")

                        image = Image.open(file_path)
                        print("the full file path os uploaded image is ",file_path)
                        print("complete image path is ")
                        output_filename = "output2.png"  # Output filename
                        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_filename)
                        image.save(output_path, "PNG")

                    root = tk.Tk()
                    root.title("File Upload Example")

                    popup = tk.Toplevel(root)
                    popup.title("File Upload Form")

                    file_path_label = tk.Label(popup, text="")
                    file_path_label.pack(pady=10)

                    upload_button = tk.Button(popup, text="Upload File", command=upload_file)
                    upload_button.pack(pady=10)

                    def submit_form():
                        print("nothing")
                        # Perform any additional processing needed on the selected file

                    submit_button = tk.Button(popup, text="Submit", command=submit_form)
                    submit_button.pack(pady=10)

                    root.mainloop()

                get_user_input()

                    #output_yield=recondation_fertiliser_fn(features_list3)

                    #features_list1=loaded_list

                    #random_float = round(random.uniform(0,0.09), 2)





                output_yield=pred_leaf_disease("output2.png")
                print("final plant classification list",output_yield)
                prediction = (str(disease_dic[output_yield]))

                print(prediction)
                text_data = "The plant is having this disease   " +str(prediction)
               # with open('crop_yield.pkl', 'wb') as file:
                 #   pickle.dump(text_data, file)

                #print("total yield will be ",output_yield)
                #yield_inputs=all_values
                #popup.destroy()



                from translate import Translator

                def translate_text(text, target_language):
                    translator= Translator(to_lang=target_language)
                    translation = translator.translate(text)
                    return translation
                # Load the data from the pickle file
                with open('crop_yield.pkl', 'rb') as file:
                    loaded_data_yield = pickle.load(file)
                text_to_translate =text_data
                # Translate to Kannada
                english_translation=text_to_translate
                kannada_translation = translate_text(text_to_translate, "kn")
                print(f"Kannada: {kannada_translation}")

                # Translate to Hindi
                hindi_translation = translate_text(text_to_translate, "hi")
                print(f"Hindi: {hindi_translation}")

                # Translate to Tamil
                tamil_translation = translate_text(text_to_translate, "ta")
                print(f"Tamil: {tamil_translation}")

                # Translate to Malayalam
                malayalam_translation = translate_text(text_to_translate, "ml")
                print(f"Malayalam: {malayalam_translation}")
                marathi_translation = translate_text(text_to_translate, "mr")
                print(f"marathi: {marathi_translation}")

                # Print the result
                print("this is the text response for present question",text_data)
                #return render_template('index.html', user_message=user_message, bot_response=bot_response)
                save_to_chat_history(random_combination,user_message, bot_response=text_to_translate)

                chat_history = load_chat_history2(random_combination)
                return render_template('chatbot.html', user_message=user_message, bot_response=text_data, chat_history=chat_history,kannada_translation=kannada_translation,hindi_translation=hindi_translation,tamil_translation=tamil_translation,malayalam_translation=malayalam_translation,english_translation=english_translation,marathi_translation=marathi_translation)



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
