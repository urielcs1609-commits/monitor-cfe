import requests
from bs4 import BeautifulSoup
import os

def enviar_telegram(mensaje):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": mensaje}
    
    try:
        response = requests.post(url, data=payload)
        # Esto nos dirá en la consola si Telegram aceptó el mensaje
        print(f"Respuesta de Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al enviar a Telegram: {e}")

def check_cfe():
    url = "https://apps.cfe.mx/SolicitudesEmpleo"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tablas = soup.find_all('table')
    
        if len(tablas) > 0: 
        print("¡HAY CONVOCATORIAS DETECTADAS!")
        # ESTA ES LA LÍNEA QUE FALTABA CONECTAR:
        enviar_telegram("🚀 ¡Nueva convocatoria en CFE! Revisa aquí: https://apps.cfe.mx/SolicitudesEmpleo")
    else:
        print("Sin novedades.")

if __name__ == "__main__":
    check_cfe()
