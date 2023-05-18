"""
This module will:
    - Translate English text to French
    - Translate French text to English
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """
    This function translates english text to french.
    """
    french_translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    translated_response = json.loads(json.dumps(french_translation))
    french_text = translated_response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates french text to english.
    """
    english_translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    translated_response = json.loads(json.dumps(english_translation))
    english_text = translated_response['translations'][0]['translation']
    return english_text
