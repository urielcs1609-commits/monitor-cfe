import requests
from bs4 import BeautifulSoup

def check_cfe():
    url = "https://apps.cfe.mx/SolicitudesEmpleo"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscamos cualquier tabla en la página
    tablas = soup.find_all('table')
    
    if len(tablas) > 0:
        print("¡HAY CONVOCATORIAS DETECTADAS!")
        # Aquí es donde podrías agregar lógica de envío de mail
        return True
    else:
        print("Aún no hay vacantes publicadas.")
        return False

if __name__ == "__main__":
    check_cfe()
