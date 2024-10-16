import json
from xml.parsers.expat import ParserCreate
from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class DefaultSaxHandler(object):

    def __init__(self):

        self.pointer = ""

        self.city = ""

        self.forecast = []

    def start_element(self, name, attrs):
        self.pointer = name
        
        if name == "cast":
            
            self.weather = {"date": "", "high": "", "low": ""}

    def end_element(self, name):

        if name == "cast":

            self.forecast.append(self.weather)

    def char_data(self, text):

        if self.pointer == "province":

            self.city = text

        elif self.pointer == "date":

            self.weather["date"] = text

        elif self.pointer == "daytemp_float":

            self.weather["high"] = text

        elif self.pointer == "nighttemp_float":

            self.weather["low"] = text

    def toJSON(self):

        return {"city": self.city, "weather": self.forecast}


def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)

    return handler.toJSON()


# ceshi

KEY = "2a0408d476372dda05c5e0fcee590afc"

URL = (
    "https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=%s&output=xml&extensions=all"
    % KEY
)

with request.urlopen(URL, timeout=4) as f:

    data = f.read()

    result = parseXml(data.decode("utf-8"))
    formatted_result = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)

    print(formatted_result)

assert result["city"] == "北京"

print("OK!")
