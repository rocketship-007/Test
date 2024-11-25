from fastapi import FastAPI
import parser


app = FastAPI()

@app.get('/spacecraft_names')
def root():
    spacecraft_names = parser.get_spacecraft_name()
    return {'name': spacecraft_names}


# @app.get('/docking_ports_filled')
# def root():
#     filled_in_ports = parser.get_docking_port()
#     return {'docked': filled_in_ports}



