

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden

from .models import (
    UnidadeCurricular,
    Docente,
    SobreMim
)

from .forms import (
    UnidadeCurricularForm,
    DocenteForm
)



def portfolio_view(request):

    sobre = SobreMim.objects.first()

    return render(
        request,
        'portfolio/main.html',
        {'sobre': sobre}
    )


def is_gestor(user):

    return user.groups.filter(
        name='gestor_portfolio'
    ).exists()



def ucs_view(request):

    ucs = UnidadeCurricular.objects \
        .prefetch_related('docente_set') \
        .select_related('licenciatura') \
        .all()

    return render(
        request,
        'portfolio/ucs.html',
        {'ucs': ucs}
    )


@login_required
def criar_uc(request):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    form = UnidadeCurricularForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        return redirect('ucs')

    return render(
        request,
        'portfolio/crud/uc_form.html',
        {'form': form}
    )


@login_required
def editar_uc(request, id):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    uc = get_object_or_404(
        UnidadeCurricular,
        id=id
    )

    form = UnidadeCurricularForm(
        request.POST or None,
        request.FILES or None,
        instance=uc
    )

    if form.is_valid():

        form.save()

        return redirect('ucs')

    return render(
        request,
        'portfolio/crud/uc_form.html',
        {
            'form': form,
            'uc': uc
        }
    )


@login_required
def apagar_uc(request, id):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    uc = get_object_or_404(
        UnidadeCurricular,
        id=id
    )

    if request.method == 'POST':

        uc.delete()

        return redirect('ucs')

    return render(
        request,
        'portfolio/crud/uc_delete.html',
        {'uc': uc}
    )




def docentes_view(request):

    docentes = Docente.objects \
        .prefetch_related('unidades') \
        .all()

    return render(
        request,
        'portfolio/docentes.html',
        {'docentes': docentes}
    )


@login_required
def criar_docente(request):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    form = DocenteForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('docentes')

    return render(
        request,
        'portfolio/crud/docente_form.html',
        {'form': form}
    )


@login_required
def editar_docente(request, id):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    docente = get_object_or_404(
        Docente,
        id=id
    )

    form = DocenteForm(
        request.POST or None,
        instance=docente
    )

    if form.is_valid():

        form.save()

        return redirect('docentes')

    return render(
        request,
        'portfolio/crud/docente_form.html',
        {
            'form': form,
            'docente': docente
        }
    )


@login_required
def apagar_docente(request, id):

    if not is_gestor(request.user):

        return HttpResponseForbidden()

    docente = get_object_or_404(
        Docente,
        id=id
    )

    if request.method == 'POST':

        docente.delete()

        return redirect('docentes')

    return render(
        request,
        'portfolio/crud/docente_delete.html',
        {'docente': docente}
    )