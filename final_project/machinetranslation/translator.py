import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2022-06-19",
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    if english_text == "":
        return ""

    result = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = result["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    if french_text == "":
        return ""

    result = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = result["translations"][0]["translation"]
    return english_text
