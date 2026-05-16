import os

from django.core.files import File

from portfolio.models import SobreMim


for obj in SobreMim.objects.all():



            print(f"Migrado: {obj}")