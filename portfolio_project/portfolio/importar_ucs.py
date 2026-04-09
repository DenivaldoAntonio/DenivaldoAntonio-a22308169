import json
import os

from portfolio.models import Licenciatura, UnidadeCurricular

PASTA = "files"

# ficheiro principal do curso
ficheiro_curso = os.path.join(PASTA, "ULHT260-PT.json")

with open(ficheiro_curso, encoding="utf-8") as f:

    dados = json.load(f)

    # verificar se courseName existe
    print("Curso encontrado:", dados.get("courseName"))

    licenciatura = Licenciatura.objects.create(

        nome=dados.get("courseName", "Engenharia Informática"),

        sigla="LEI",

        instituicao="Universidade Lusófona",

        descricao="Importado automaticamente da API Lusófona"

    )

    for uc in dados.get("courseFlatPlan", []):

        UnidadeCurricular.objects.create(

            nome=uc.get("curricularUnitName"),

            codigo=uc.get("curricularIUnitReadableCode"),

            ects=uc.get("ects", 0),

            semestre=1,
            
            licenciatura=licenciatura

        )

print("Importação concluída com sucesso")