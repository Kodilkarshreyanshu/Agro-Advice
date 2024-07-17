from logging.handlers import DEFAULT_HTTP_LOGGING_PORT
import pickle
import re
from django.shortcuts import render, redirect

import requests
from django.http import JsonResponse,HttpResponse
import pandas as pd
from app.fertilizer import fertilizer_dic
from app.crop_info import crop_dict
import numpy as np
import logging
from django.utils.translation import activate




from django.utils import translation




# loading our ML model for Crop  Recommendation system
with open('./saved_models/RandomForest2.pkl', 'rb') as file:
    crop_model = pickle.load(file)



# render Home Page
def home(request):
    
    return render(request, 'index.html')





# render Predtion Page
def predictor(request):
    return render(request, 'crop.html')

def fetch_weather(city_name):
    api_key = '98ccbfd03418f5e0e724cfc4d789fddd'  
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    complete_url = base_url + "?q=" + city_name + "&appid=" + api_key 
    response = requests.get(complete_url)
    data = response.json()

    if 'main' in data and 'temp' in data['main'] and 'humidity' in data['main']:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        return (temperature-273.15),(humidity)
    else:
        return None, None



# Import the logging module at the top of your views.py file


# Set up logging configuration (you can adjust the level based on your needs)
logging.basicConfig(level=logging.DEBUG)

# ...






# views.py
from django.http import HttpResponse
from django.shortcuts import render
from google.cloud import texttospeech
import pandas as pd
import numpy as np
from io import BytesIO

import pyttsx3

import threading

def text_to_speech(text, lang='en'):
    def speak():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # Start speech synthesis in a separate thread to avoid blocking the main thread
    threading.Thread(target=speak).start()

# Adjust your view functions accordingly to delay the text-to-speech conversion
import threading
from django.shortcuts import render
from translate import Translator
import speech_recognition as sr

def formInfo(request):
    context = {}

    if request.method == 'POST':
        try:
            recognizer = sr.Recognizer()

            # Capture audio from the user's microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            text = ""

        # Your existing code to retrieve input data
        N = float(request.POST.get('N'))
        P = float(request.POST.get('P'))
        K = float(request.POST.get('K'))
        ph = float(request.POST.get('ph'))
        R = float(request.POST.get('R'))
        city_name = request.POST.get("city_name")

        # Your existing code to fetch weather data
        temperature, humidity = fetch_weather(city_name)

        # Create a DataFrame with feature names
        input_data = pd.DataFrame({
            'N': [N],
            'P': [P],
            'K': [K],
            'temperature': [temperature],
            'humidity': [humidity],
            'ph': [ph],
            'rainfall': [R]
        })

        if temperature is not None and humidity is not None:
            crop_prediction = crop_model.predict(input_data)

            # Get top three predicted classes
            proba = crop_model.predict_proba(input_data)
            top_three_classes = np.argsort(proba[0])[::-1][:3]

            if top_three_classes.size > 0:
                top_three_crops = [crop_model.classes_[idx] for idx in top_three_classes]

                # Default language is English
                lang = 'en'
                # Check if user selected a language
                if 'language' in request.POST:
                    lang = request.POST.get('language')

                # Translate the crop prediction and top three crops
                translator = Translator(to_lang=lang)
                crop_prediction_translated = translator.translate(crop_prediction[0])
                top_three_crops_translated = [translator.translate(crop) for crop in top_three_crops]

                # Construct the response
                context = {
                    'crop_result': f"You should grow {crop_prediction_translated}",
                    'top_three_crops': top_three_crops_translated,
                    'selected_language': lang  # Pass the selected language to the template
                }

                # If the output language is English, convert the result to speech
                if lang == 'en':
                    # Convert the result to speech after a delay
                    speech_text = f"You should grow {crop_prediction_translated}"
                    for idx, crop in enumerate(top_three_crops_translated):
                        if idx != 0:  # Exclude the first crop
                            speech_text += f", {crop}"  # Add each crop to the speech text
                    # Delay the speech synthesis by 1 second
                    threading.Timer(1, text_to_speech, args=[speech_text, lang]).start()

            else:
                context = {'crop_result': 'Unable to determine recommended crops.'}

            return render(request, 'crop.html', context)
        
        else:
            return render(request, 'try_again.html')

    return render(request, 'crop.html', context)







# ...





import pandas as pd
from django.shortcuts import render
from django.utils.safestring import mark_safe
import os
from django.conf import settings

import os
import pandas as pd
from django.shortcuts import render
from django.conf import settings


import os
import pandas as pd
import pyttsx3
import logging
import numpy as np
from django.shortcuts import render
from django.conf import settings
from app.fertilizer import fertilizer_dic
from gtts import gTTS

# Function for text-to-speech conversion


# Existing fert_recommend view with text-to-speech
import os
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import activate
import pyttsx3
import threading

# Define your text-to-speech function


# Modify your view function to include a delay before text-to-speech
def fert_recommend(request):
    if request.method == 'POST':
        try:
            recognizer = sr.Recognizer()

            # Capture audio from the user's microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            text = ""

        crop_name = str(request.POST.get('crop_name'))
        N = float(request.POST.get('N'))
        P = float(request.POST.get('P'))
        K = float(request.POST.get('K'))

        file_path = os.path.join(settings.BASE_DIR, 'static', 'Dataset', 'fertilizer.csv')
        df = pd.read_csv(file_path)

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K

        recommendations = {}

        if n != 0:
            recommendations['n'] = f"{abs(n)} units {'less' if n > 0 else 'more'} than the desired value: {fertilizer_dic['NHigh' if n < 0 else 'Nlow']}"
        if p != 0:
            recommendations['p'] = f"{abs(p)} units {'less' if p > 0 else 'more'} than the desired value: {fertilizer_dic['PHigh' if p < 0 else 'Plow']}"
        if k != 0:
            recommendations['k'] = f"{abs(k)} units {'less' if k > 0 else 'more'} than the desired value: {fertilizer_dic['KHigh' if k < 0 else 'Klow']}"

        if not recommendations:
            response = "No fertilizer needed. You are good to go!!"
        else:
            response = {'recommendation': recommendations}

        return render(request, 'fertilizer_result.html', response)

    # Default response for GET method
    return render(request, 'fertilizer.html')









def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





def pair_crop_page(request):
    return render(request, 'pair_crop_page.html')

# Function for text-to-speech conversion
from django.shortcuts import render
from django.http import HttpResponse
import joblib
import threading
import pyttsx3
from translate import Translator

# Load the machine learning models
nitrogen_model = joblib.load('./saved_models/nitrogen.pkl')
pest_model = joblib.load('./saved_models/pest.pkl')
shade_model = joblib.load('./saved_models/shade.pkl')

# Define your text-to-speech function
def text_to_speech(text, lang='en'):
    if lang == 'en':
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
        engine.say(text)
        engine.runAndWait()

# Modify your view function to include a delay before text-to-speech
def input_data(request, option):
    if option not in ['nitrogen', 'pest', 'shade']:
        return HttpResponse("Invalid option")

    if request.method == 'POST':
        try:
            recognizer = sr.Recognizer()

            # Capture audio from the user's microphone
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            text = ""
        
        ph = float(request.POST.get('ph'))
        temperature = float(request.POST.get('temperature'))
        rainfall = float(request.POST.get('rainfall'))

        # Perform prediction based on the selected option
        if option == 'nitrogen':
            model = nitrogen_model
        elif option == 'pest':
            model = pest_model
        elif option == 'shade':
            model = shade_model

        # Perform prediction using the loaded model
        input_data = [[temperature, ph, rainfall]]
        result = model.predict(input_data)[0]

        # Construct the speech text
        speech_text = f"The predicted crop pair based on {option} is {result}."

        # Translate the speech text to Hindi or Marathi if required
        selected_language = request.POST.get('language', 'en')
        if selected_language in ['hi', 'mr']:
            try:
                translator = Translator(to_lang=selected_language)
                translated_text = translator.translate(speech_text)
                speech_text = translated_text
            except Exception as e:
                print(f"Translation error: {e}")

        # Delay the speech synthesis by 1 second before triggering it
        threading.Timer(1, text_to_speech, args=[speech_text]).start()

        # Return the result to the template
        return render(request, 'result.html', {'result': speech_text})

    # If the request method is not POST, render the input form
    return render(request, 'input_data.html', {'option': option})

























from .crop_info import crop_dict  # Importing crop_dict from crop_info.py

def crop_search(request):
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name', '')
        selected_crop = find_matching_crop(crop_name)
        if selected_crop:
            crop_info = crop_dict[selected_crop]
            # Preprocess the description
            if 'description' in crop_info:
                description = crop_info['description']
                # Remove unwanted characters and split into separate lines
                cleaned_description = [line.strip() for line in description.split('<br>') if line.strip()]
                crop_info['description'] = cleaned_description
            crop_image_url = crop_info.get('crop_image_url', '')  # Extracting the image URL
            return render(request, 'crop_search_result.html', {'crop_name': selected_crop, 'crop_info': crop_info, 'crop_image_url': crop_image_url})
        else:
            return render(request, 'crop_search_result.html', {'crop_name': crop_name, 'crop_info': None, 'crop_image_url': None})
    return render(request, 'crop_search.html')






def find_matching_crop(user_input):
    # Iterate through crop_dict keys and find a case-insensitive match
    for crop in crop_dict:
        if crop.lower() == user_input.lower():
            return crop
    return None


# myapp/views.py

# myapp/views.py

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm

@csrf_exempt
def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Your email address
        to_email = 'kodilkarshreyanshu@gmail.com'

        # Formulate the email subject and message
        subject = 'New Contact Form Submission'
        email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

        try:
            # Send the email
            send_mail(subject, email_message, 'sender@example.com', [to_email], fail_silently=False)

            # Return a success response
            return JsonResponse({'status': 'success'})
        except Exception as e:
            # Return an error response
            return JsonResponse({'status': 'error', 'message': str(e)})

    # Return an error response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def contact_view(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})



from django.shortcuts import render, redirect
import pickle

def crop_selection(request):
    if request.method == 'POST':
        selected_crop = request.POST.get('crop')
        if selected_crop:
            return redirect('enter_environment_data', selected_crop=selected_crop)
    return render(request, 'crop_selection.html')

import os


def enter_environment_data(request, selected_crop):
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        ph = float(request.POST.get('ph'))
        rainfall = float(request.POST.get('rainfall'))
        
        # Determine the path to the pickle file based on the selected crop
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_dir, 'saved_models', f'{selected_crop.upper()}.pkl')
        
        # Load corresponding model based on selected crop
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # Make prediction using the model and input data
        prediction = model.predict([[temperature, ph, rainfall]])
        
        return render(request, 'result.html', {'prediction': prediction})
    
    return render(request, 'enter_environment_data.html', {'selected_crop': selected_crop})

import requests
from django.shortcuts import render

# Function to fetch live agriculture news using NewsAPI
def get_agriculture_news():
    api_key = '2a42f23b6b1a4876abe0ee3ec2beb776'  # Your NewsAPI key
    url = f'https://newsapi.org/v2/everything?q=farmer+agriculture+india&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            agriculture_articles = [article for article in articles if 'agriculture' in article['title'].lower() or 'agriculture' in article['description'].lower()]
            return agriculture_articles
        else:
            return []
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
    
def news(request):
    # Fetch live agriculture news
    agriculture_news = get_agriculture_news()
    context = {'agriculture_news': agriculture_news}
    return render(request, 'news.html', context)








# views.py

