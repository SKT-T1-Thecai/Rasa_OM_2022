# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionSearchWeather(Action):

    def name(self) -> Text:
        return "action_search_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        if city is None:

            dispatcher.utter_message(text="请先告诉我要查哪个城市")
            return [SlotSet("city", "Shanghai")]
        else:
            dispatcher.utter_message(text="你问的是"+city+"的天气吗？")
            return []

class ActionCPUHighUsage(Action):

    def name(self) -> Text:
        return "action_cpu_high_usage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="知道cpu使用率高了")
        return []


class ActionGetAlarmInSystem(Action):
    def name(self) -> Text:
        return "action_get_alarm_in_system"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="知道平台报警了")
        return []

class ActionGetPeopleInSystem(Action):
    def name(self) -> Text:
        return "action_get_people_in_system"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        system = tracker.get_slot("system")
        dispatcher.utter_message(text="你问的是"+system+"的平台吗")
        return []