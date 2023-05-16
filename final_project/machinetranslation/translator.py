""" Module for text translation using IBM Watson Translator. """
import os
# import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

url = os.environ['url']
apikey = os.environ['apikey']
version = os.environ['version']


# create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


# language_translator.set_disable_ssl_verification(True)
# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))


def english_to_french(english_text=None):
    """ This function returns the text translated from English to French """
    if english_text is None or english_text == "":
        return ""
    try:
        output = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        return output["translations"][0]["translation"]
    except: # pylint: disable=bare-except
    # except KeyError:
        return ""


def french_to_english(french_text=None):
    """ This function returns the text translated from French to English """
    if french_text is None or french_text == "":
        return ""
    try:
        output = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        return output["translations"][0]["translation"]
    except: # pylint: disable=bare-except
        return ""
