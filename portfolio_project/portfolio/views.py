from django.shortcuts import render
from .models import UnidadeCurricular, Docente, SobreMim


def portfolio_view(request):

    sobre = SobreMim.objects.first()

    return render(
        request,
        'portfolio/main.html',
        {'sobre': sobre}
    )


def ucs_view(request):

    ucs = UnidadeCurricular.objects \
        .prefetch_related('docente_set') \
        .select_related('licenciatura') \
        .all()

    return render(request, 'portfolio/ucs.html', {'ucs': ucs})


def docentes_view(request):

    docentes = Docente.objects \
        .prefetch_related('unidades') \
        .all()

    return render(request, 'portfolio/docentes.html', {'docentes': docentes})