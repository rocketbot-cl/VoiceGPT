# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys
import requests

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'VoiceGPT' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

global mod_voice_session

try:
    if not mod_air_session : #type:ignore
        mod_air_session = {}
except NameError:
    mod_air_session = {}


module = GetParams("module")

try:
    if module == "get_analysis":
        template = GetParams("template")
        files = GetParams("files")
        api_key = GetParams("api_key")
        result = GetParams("result")

        try:
            url = "https://api-voicegpt.rocketbot.com/api/sounds/getAnalysis"

            payload = {'template': template}
            files=[('file',(files, open(files,'rb'), 'audio/mpeg'))]

            headers = {'x-api-key': api_key}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)
           
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            import traceback
            traceback.print_exc
            PrintException()
            raise e
        
except Exception as e:
            import traceback
            traceback.print_exc
            PrintException()
            raise e