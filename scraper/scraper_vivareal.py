import requests
from bs4 import BeautifulSoup

header = {
        'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }

##Request apartamento

def get_imovel_link(initial_url = r'https://www.vivareal.com.br/venda/pernambuco/recife/apartamento_residencial/'):
    header = {
        'Accept-Language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

    base_url = r'https://www.vivareal.com.br'
    r = requests.get(initial_url, header = header)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = soup.find_all('a')
    link_imovel_list = []
    for link in links:
        if (r'/imovel' in link['href']):
            link_imovel = base_url + link['href']
            link_imovel_list.append(link_imovel)
            print(link_imovel)
    return link_imovel_list
    

r = requests.get(r'https://www.vivareal.com.br/imovel/imovel-comercial-4-quartos-madalena-bairros-recife-98m2-aluguel-RS2700-id-2565601570/')
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')
#ads_title = soup.find_all('h1')['title__title js-title-view'] #Anuncio
ads_title = soup.find(class_ = 'title__title js-title-view') #Anuncio
#address = soup.find_all('p')['title__address js-address'] #Endereço
address = soup.find(class_ = 'title__address js-address') #Endereço
#description = soup.find_all('p')['description__text'] #Endereço
description = soup.find(class_ = 'description__text') #Endereço
#map_address = soup.find_all('p')['map__address'] #Endereço
map_address = soup.find(class_ = 'map__address') #Endereço

h3_soup = soup.find_all('h3') #Valores
addit = soup.find_all('li') #Elementos extras
span_c = soup.find_all('span') #Condominio e IPTU

for image in images:
    name = image['alt']
    link = image['src']
    print(name, link)

print(ads_title, address, description, map_address)
print('\n')
print(h3_soup)
print('\n')
print(addit)
print('\n')
print(span_c)
print('\n')




