from ibm_watson import LanguageTranslatorV3


#service instance
url_lt=''

# api key
apikey_lt=''

version_lt='2018-05-01'

#language translator object
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

#list of languages
from pandas import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

# english - spanish
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')

#result as dict
translation=translation_response.get_result() 

#result as string
spanish_translation =translation['translations'][0]['translation']