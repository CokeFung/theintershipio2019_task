import xmltodict
import json
def main():
    f = open("./xml_data.xml")
    xml_data = f.read()
    json_data = xmltodict.parse(xml_data)
    json_data = json.dumps(json_data)

    with open("json_data.json", "w") as out:
        json.dump(json_data, out)
main()
