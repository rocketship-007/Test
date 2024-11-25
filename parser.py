import json
import urllib.request

def get_spacecraft_name():
    url = 'https://corquaid.github.io/international-space-station-APIs/JSON/iss-docked-spacecraft.json'
    response = urllib.request.urlopen(url)
    spacecraft = json.loads(response.read())
    crafts = spacecraft.get('spacecraft', "")

    spacecraft_name = {c.get('name') for c in crafts}
    return spacecraft_name

# def get_docking_port():
#     url = 'https://corquaid.github.io/international-space-station-APIs/JSON/iss-docked-spacecraft.json'
#     response = urllib.request.urlopen(url)
#     spacecraft = json.loads(response.read())
#     crafts = spacecraft.get('spacecraft', "")
#
#     docking_ports = {c.get('docking_port') for c in crafts}
#     return docking_ports