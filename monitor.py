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
        print(f"Respuesta de Telegram: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar a Telegram: {e}")

def check_cfe():
    url = "https://apps.cfe.mx/SolicitudesEmpleo"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tablas = soup.find_all('table')
    
    # Esta es la parte que dio el error. 
    # Asegúrate de que el "if" esté alineado con la "r" de "response" arriba.
    if len(tablas) > 0:
        print("¡HAY CONVOCATORIAS DETECTADAS!")
        enviar_telegram("🚀 ¡Nueva convocatoria en CFE! Revisa aquí: https://apps.cfe.mx/SolicitudesEmpleo")
    else:
        print("Sin novedades.")

if __name__ == "__main__":
    check_cfe()
