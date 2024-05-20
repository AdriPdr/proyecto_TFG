import undetected_chromedriver as uc
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver.common.by import By
import pandas as pd
import re
import pandas as pd
import datetime
import hashlib

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

    #ciudad
    ciudad = soup2.find('span', {'id': 'prefijoPoblacion'})
    if ciudad:
        ciudad = ciudad.text
        url_info_dict['ciudad'] = re.sub(r',\s*$', '', ciudad) #eliminamos la coma del final, Madrid, --> Madrid
    else: 
        url_info_dict['ciudad'] = None

    #provincia
    provincia = soup2.find('a', {'id': 'prefijoProvincia'})
    if provincia: 
        url_info_dict['provincia'] = provincia.text
    else: 
        url_info_dict['provincia'] = None

    #país
    pais = soup2.find('span', {'id': 'prefijoPais'})
    if pais: 
        pais = pais.text
        url_info_dict['pais'] = re.sub(r'\(([^)]+)\)', r'\1', pais) #Eliminamos los paréntesis del país, (España) --> España
    else: 
        url_info_dict['pais'] = None

    #jornada_laboral
    jornada_laboral = soup2.find('span', {'id': 'prefijoJornada'}).text
    if jornada_laboral: 
        jornada_laboral = jornada_laboral.split(',')[1].strip()
        url_info_dict['jornada_laboral'] = jornada_laboral
    else:
        url_info_dict['jornada_laboral'] = None

    #link
    url_info_dict['link'] = url_infojobs

    #requisitos_minimos
    requisitos_minimos_global = soup2.find('h3', class_='list-default-title', string='Requisitos mínimos')
    if requisitos_minimos_global: 
        requisitos_minimos = requisitos_minimos_global.find_next('p')    
        url_info_dict['requisitos_minimos'] = requisitos_minimos.text
    else: 
        url_info_dict['requisitos_minimos'] = None

    #salario_descripcion
    salario_global = soup2.find('h3', class_= 'list-default-title', string='Salario')
    if salario_global: 
        salario_descripcion = salario_global.find_next('span')
        salario_descripcion = salario_descripcion.text.split(":", 1)[-1].strip()
        url_info_dict['salario_descripcion'] = salario_descripcion
    else: 
        url_info_dict['salario_descripcion'] = None

    #salario_maximo
    salario_maximo_y_minimo = re.findall(r'\d{1,3}(?:\.\d{3})*(?:,\d+)?', salario_descripcion) 
    if len(salario_maximo_y_minimo) == 2:  
        salario_maximo = salario_maximo_y_minimo[1]
        url_info_dict['salario_maximo'] = salario_maximo 
    else: 
        url_info_dict['salario_maximo'] = None
    
    #salario_minimo
    if salario_maximo_y_minimo:                        
        salario_minimo = salario_maximo_y_minimo[0]
        url_info_dict['salario_minimo'] = salario_minimo
    else: 
        url_info_dict['salario_minimo'] = None

    #vacantes
    numero_vacantes = soup2.find('span', {'id': 'prefijoVacantes'})
    if numero_vacantes:
        numero_vacantes = numero_vacantes.text
        url_info_dict['vacantes'] = numero_vacantes
    else: 
        url_info_dict['vacantes'] = None

    #categoria_nombre
    categoria = soup2.find('a', {'id': 'prefijoCat'})
    if categoria:
        categoria = categoria.text 
        url_info_dict['categoria_nombre'] = categoria
    else:
        url_info_dict['categoria_nombre'] = None
    
    #subcategoria_nombre
    subcategoria = soup2.find('a', {'id': 'prefijoSubCat'})
    if subcategoria:
        subcategoria = subcategoria.text
        url_info_dict['subcategoria_nombre'] = subcategoria

    #idioma_nombre
    idioma = soup2.find('h3', class_='list-default-title', string='Idiomas requeridos') 
    if idioma: 
        idioma = idioma.find_next('span', class_='list-default-text').text.split('-')[0].strip()
        url_info_dict['idioma_nombre'] = idioma
    else:
        url_info_dict['idioma_nombre'] = None

    #estudios_nombre
    estudios_minimos = soup2.find('span', {'id': 'prefijoEstMin'})
    if estudios_minimos:
        estudios_minimos = estudios_minimos.text
        url_info_dict['estudios_nombre'] = estudios_minimos
    else: 
        url_info_dict['estudios_nombre'] = None

    #habilidades
    lista_habilidades = soup2.find('ul', {'class': 'list-default list-inline'})
    if lista_habilidades:
        lista_habilidades = lista_habilidades.find_all('a')
        habilidades = [habilidad.text.strip() for habilidad in lista_habilidades]
        habilidades_limpias = ', '.join(habilidades)
        url_info_dict['habilidades'] = habilidades_limpias
    else:
        url_info_dict['habilidades'] = None

    #compania
    compania = soup2.find('a', {'class': 'link'})
    if compania: 
        compania = compania.text
        url_info_dict['compania'] = compania
    else: 
        url_info_dict['compania'] = None 

    return url_info_dict

browser = uc.Chrome()
browser.implicitly_wait(10)
url = "https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=&segmentId=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&sinceDate=ANY"
browser.get(url)

cookies = browser.find_element(By.ID, 'didomi-notice-agree-button') #Buscamos el botón de aceptar cookies
cookies.click() #Clicamos en él

time.sleep(5) # Esperar un tiempo después del clic


scroll_step = 1000 #desplazamiento inicial
max_height = browser.execute_script("return document.body.scrollHeight") # Obtener la altura inicial de la página

num_steps = 10 # Número de pasos para el desplazamiento

while True: #scroll hacia abajo 
    browser.execute_script("window.scrollBy(0, {});".format(scroll_step))
    time.sleep(2)
    new_height = browser.execute_script("return document.body.scrollHeight") #actualizar altura página (menos lo que ya se ha explorado)

    if new_height == max_height: 
        break

    max_height = new_height

    scroll_step = max_height // num_steps #Altura total entre número pasos

html = browser.page_source #Obtenemos el html de la página

soup = bs(html, 'lxml') # Parsear el HTML con BeautifulSoup


links = [] 

for link in soup.find_all('a', {'class': 'ij-OfferCardContent-description-title-link'}):
    links.append(link["href"])

for i in range(len(links)):
    if not links[i].startswith("http"):
        links[i] = "https:" + links[i]


url_info_dict = {'titulo': None, 'postulacion': None, 'descripcion': None, 'experiencia_minima': None, 'ciudad': None, 'provincia': None, 'pais': None, 
                'jornada_laboral': None, 'link': None, 'requisitos_minimos': None, 'salario_descripcion': None, 'salario_maximo': None, 'salario_minimo': None, 
                'vacantes': None, 'categoria_nombre': None, 'subcategoria_nombre': None, 'idioma_nombre': None, 'estudios_nombre': None, 'habilidades': None, 'compania': None, 'creationDate': None}


df_data = pd.DataFrame(columns=["oferta_id", "titulo", "postulacion", "descripcion", "experiencia_minima", "ciudad", "provincia", "pais", "jornada_laboral", "link", "requisitos_minimos", 
                                "salario_descripcion", "salario_maximo", "salario_minimo", "vacantes", "categoria_nombre", "subcategoria_nombre", "idioma_nombre", 
                                "estudios_nombre", "habilidades", "compania", "creationDate"])

contador = 0
indice = 0
time.sleep(5)

for url in links:
    print(url)
    url_info_dict = obtener_informacion(url_info_dict, url, browser) # Obtener información de las URLs de las ofertas
    indice = str(indice).encode()
    url_info_dict['oferta_id'] = hashlib.md5(indice).hexdigest()
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%dT%H:%M:%S.000+0000")
    url_info_dict['creationDate'] = date
    indice = int(indice)
    indice += 1 
    df_data = df_data._append(url_info_dict, ignore_index = True)
browser.quit() # Cerrar el navegador
df_data.to_csv("C:/Users/apedr/OneDrive/Escritorio/TFG/BRONZE/infoInfojobs.csv")