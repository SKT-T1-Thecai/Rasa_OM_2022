# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from py2neo import Graph
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from scheme_search.scheme_search import PlatformScheme

platform_scheme = PlatformScheme()
neo4j_link =Graph(
            host="127.0.0.1",
            port=7687,
            user="neo4j",
            password="123456"
        )
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
        business_system = tracker.get_slot("system")
        try:
            result = platform_scheme.get_bussiness_system_by_name(business_system)
            dispatcher.utter_message(text="业务系统"+business_system+"的负责人是"+result["department_director"]
        +",它所选用的厂商是"+result["manufactor"]+",厂商负责人是"+result["manufactor_director"]+"。")
        except:
            dispatcher.utter_message(text="不好意思没有查到业务系统"+business_system+"的负责人")
        return []


class ActionGetVirtualMachinesInSystem(Action):
    def name(self) -> Text:
        return "action_get_virtual_machines_in_system"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        business_system = tracker.get_slot("system")
        if business_system is None:
            dispatcher.utter_message("请您先输入业务系统名称。")
            return []
        try:
            result = platform_scheme.get_virtual_machines_of_business_system(business_system)
            dispatcher.utter_message(text=str(result))
        except:
            dispatcher.utter_message(text="不好意思没有查到业务系统"+business_system+"对应的虚拟机")
        return []