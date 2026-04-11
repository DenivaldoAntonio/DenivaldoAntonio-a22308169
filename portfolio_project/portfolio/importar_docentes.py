import requests
from bs4 import BeautifulSoup

from portfolio.models import Docente


url = "https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/docentes"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# encontrar nomes (estrutura simples do site)
nomes = soup.get_text().split("\n")

for nome in nomes:

    nome = nome.strip()

    if len(nome) > 5 and " " in nome:

        Docente.objects.get_or_create(

            nome=nome

        )

print("Docentes importados com sucesso")