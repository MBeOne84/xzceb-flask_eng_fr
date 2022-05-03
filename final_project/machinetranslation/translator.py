
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(englishtext):
    """
    This function translates from english to french
    """
    french_translation=language_translator.translate(
    text=englishtext, model_id='en-fr').get_result()
    frenchtext = french_translation['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    """
    This function translates from french to english
    """
    english_translation=language_translator.translate(
    text=frenchtext, model_id='fr-en').get_result()
    englishtext = english_translation['translations'][0]['translation']
    return englishtext
