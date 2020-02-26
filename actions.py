# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime
import time
import requests as req
import json
# from rasa_sdk.events import events


def checkTime():
    now = datetime.now()
    if str(now)[11:19] == '10:43:00':
        # notif = Notify()
        notify(CollectingDispatcher)
        time.sleep(1)
    else :
        time.sleep(0.5)
    print(str(now))
    checkTime()


def notify(dispatcher: CollectingDispatcher):
    app_key = '9KHVLZP0'
    url = 'https://random-word-api.herokuapp.com' + '/word?key='+ app_key + '&number=' + str(1)
    r = req.get(url)
    word = r.json()[0]
    from translate import Translator
    translator = Translator(from_lang='en', to_lang='vi')
    translation = translator.translate(word)
    output = word + " có nghĩa là \"" + translation + "\"\n"
    dispatcher.utter_message(text=output)
    return []


# Notify()

# class Notify(Action):

#     def __init__(self):
#         return 
    
#     def name(self): 
#         return "null"
    
#     def run(self, dispatcher: CollectingDispatcher):
#         app_key = '9KHVLZP0'
#         url = 'https://random-word-api.herokuapp.com' + '/word?key='+ app_key + '&number=' + str(1)
#         r = req.get(url)
#         word = r.json()[0]
#         from translate import Translator
#         translator = Translator(from_lang='en', to_lang='vi')
#         translation = translator.translate(word)
#         output = word + " có nghĩa là \"" + translation + "\"\n"

    
#         dispatcher.utter_message(text=output)

class Translate(Action):
    
    def name(self):
        return "give_translation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        word = tracker.get_slot('word').lower()
        print(word)
        from translate import Translator
        from bs4 import BeautifulSoup
        translator = Translator(from_lang='vi', to_lang='en')
        translation = translator.translate(word)
        out = word + " có nghĩa là \"" + translation + "\"\n"

        url = 'http://vndic.net/index.php?word=' + translation + '&dict=en_vi'
        r = req.get(url)
        if r.status_code != 404:
            soup = BeautifulSoup(res.content, 'html.parser')
            content = soup.find(style="display:inline;").contents
            general_meaning = content[0].contents[-1]
            out += "Example: \'" + general_meaning + "\'\n"

        app_key = '8e54f160325cbca75695a8000348f913'
        app_id = '7fa4175c'
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/en/' + translation
        r = req.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

        if r.status_code != 404:
            result = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]
            if 'definitions' in result:
                out += "Nghĩa tiếng Anh: " + result['definitions'][0] + "\n"
            # pprint(result['definitions'][0]) từ ngày nghĩa là gì nhỉ 
            if 'subsenses' in result:
                out += "Other definnitions:\n"
                for defi in result['subsenses']:
                    if 'definitions' in defi: 
                        out += " - " + defi['definitions'][0] + "\n"
                        # print(defi['definitions'][0])
        dispatcher.utter_message(text=out)
        return []

# từ bóng bàn nghĩa là gì nhỉ 
# adv: no conflict, mems commit one by one.

class Give_vi_to_en(Action) :
    def name(self) :
        return "give_vi_to_en"
        
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        word = tracker.get_slot('word').lower()
        print(word)
        from translate import Translator
        translator = Translator(from_lang='vi', to_lang='en')
        translation = translator.translate(word)
        output = word + " có nghĩa là \"" + translation + "\"\n"
        dispatcher.utter_message(text=output)
        return []

        
class Give_en_to_vi(Action) :
    def name(self) :
        return "give_en_to_vi"
        
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        word = tracker.get_slot('word').lower()
        print(word)
        from translate import Translator
        translator = Translator(from_lang='en', to_lang='vi')
        translation = translator.translate(word)
        output = word + " có nghĩa là \"" + translation + "\"\n"
        dispatcher.utter_message(text=output)
        return []

        
class Give_en_to_en(Action) :
    def name(self) :
        return "give_en_to_en"
        
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        word = tracker.get_slot('word').lower()
        import requests as req
        import json
        app_key = '8e54f160325cbca75695a8000348f913'
        app_id = '7fa4175c'
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/en/' + word
        r = req.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

        if r.status_code != 404:
            result = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]
            if 'definitions' in result:
                out += "Nghĩa tiếng Anh: " + result['definitions'][0] + "\n"
            # pprint(result['definitions'][0]) từ ngày nghĩa là gì nhỉ 
            if 'subsenses' in result:
                out += "Other definnitions:\n"
                for defi in result['subsenses']:
                    if 'definitions' in defi: 
                        out += " - " + defi['definitions'][0] + "\n"
                        # print(defi['definitions'][0])
        dispatcher.utter_message(text=out)
        return []

# checkTime()
