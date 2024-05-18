import undetected_chromedriver as uc
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.by import By
import pandas as pd

def obtener_informacion(url_info_dict, url_infojobs, browser):
    browser.get(url_infojobs)
    time.sleep(10)
    html = browser.page_source
    soup2 = bs(html, 'lxml')
    
    #título
    titulo_elem = soup2.find('div', {'class': 'heading-addons'}).find('h1', {'id': 'prefijoPuesto'})
    url_info_dict['titulo'] = titulo_elem.strip() if isinstance(titulo_elem, str) else titulo_elem.text.strip() if titulo_elem else None
    
    #postulaciones
    postulacion_elem = soup2.find('strong', {'id': 'candidate_application_message'})
    numero = postulacion_elem.text.strip() if postulacion_elem else None
    if numero:
        numero_re = re.search(r'\d+', numero) #se aplica una expresion regular para encontrar el número
        url_info_dict['postulacion'] = numero_re.group() if numero_re else None
    else:
        url_info_dict['postulacion'] = None

    #descripción
    descripcion_elem = soup2.find('div', {'id': 'prefijoDescripcion1'})
    url_info_dict['descripcion'] = descripcion_elem.strip() if isinstance(descripcion_elem, str) else descripcion_elem.text.strip() if descripcion_elem else None

    #experiencia_minima
    experiencia_minima = soup2.find('span', string=lambda text: text and 'Experiencia mínima:' in text)
    experiencia_minima = experiencia_minima.get_text(strip=True)
    url_info_dict['experiencia_minima'] = experiencia_minima.split(":", 1)[-1].strip() #nos quedamos con la parte de después de los 2 puntos ":", "Experiencia minima: al menos 4 años --> al menos 4 años"

browser = uc.Chrome()
browser.implicitly_wait(10)
url = "https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=&segmentId=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&sinceDate=ANY"
browser.get(url)

html = browser.page_source #Obtenemos el html de la página

soup = bs(html, 'lxml') # Parsear el HTML con BeautifulSoup


links = [] 

for link in soup.find_all('a', {'class': 'ij-OfferCardContent-description-title-link'}):
    links.append(link["href"])


url_info_dict = {'titulo': None, 'postulacion': None, 'descripcion': None, 'experiencia_minima': None, 'ciudad': None, 'provincia': None, 'pais': None, 
                'jornada_laboral': None, 'link': None, 'requisitos_minimos': None, 'salario_descripcion': None, 'salario_maximo': None, 'salario_minimo': None, 
                'vacantes': None, 'categoria_nombre': None, 'subcategoria_nombre': None, 'idioma_nombre': None, 'estudios_nombre': None, 'habilidades': None, 'compania': None, 'creationDate': None}


df_data = pd.DataFrame(columns=["oferta_id", "titulo", "postulacion", "descripcion", "experiencia_minima", "ciudad", "provincia", "pais", "jornada_laboral", "link", "requisitos_minimos", 
                                "salario_descripcion", "salario_maximo", "salario_minimo", "vacantes", "categoria_nombre", "subcategoria_nombre", "idioma_nombre", 
                                "estudios_nombre", "habilidades", "compania", "creationDate"])

for url in links:
    print(url)
    url_info_dict = obtener_informacion(url_info_dict, url, browser) # Obtener información de las URLs de las ofertas