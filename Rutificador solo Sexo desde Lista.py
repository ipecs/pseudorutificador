import requests
import time

ruta_carpeta = input("Ingresa la ruta de la carpeta donde se encuentra el archivo RUTS.txt: ")
ruta_archivo = ruta_carpeta + "/RUTS.txt"

with open(ruta_archivo, "r") as f:
    for line in f:
        numero = line.strip()
        url = f"https://r.rutificador.co/pr/{numero}"
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"
        }
        
        response = requests.post(url, headers=headers)
        
        if response.status_code == 200:
            # Se ha recibido una respuesta exitosa
            response_text = response.text
            if "VAR" in response_text:
                print("Hombre")
            elif "MUJ" in response_text:
                print("Mujer")
            else:
                print("No se pudo determinar el género.")
        else:
            print(f"Ha ocurrido un error. Código de estado: {response.status_code}")
        
        time.sleep(4)
