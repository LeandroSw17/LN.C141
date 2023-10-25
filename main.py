import requests
from bs4 import BeautifulSoup
import csv

START_URL = "URL_DO_SITE_AQUI"
headers = {
    "User-Agent": "Seu Agente de Usuário Aqui"
}
star_data = []

response = requests.get(START_URL, headers=headers)

if response.status_code == 200:
    page_content = response.text
else:
    print("Falha ao obter a página. Verifique a URL e os cabeçalhos.")

soup = BeautifulSoup(page_content, "html.parser")

star_table = soup.find("table", {"class": "classe-da-tabela"})
rows = star_table.find_all("tr")
for row in rows:
with open("stars.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Nome da estrela", "Distância", "Massa", "Raio"])
    for star in star_data:
        csv_writer.writerow(star)
