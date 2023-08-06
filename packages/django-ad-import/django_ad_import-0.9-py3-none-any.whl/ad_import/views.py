from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from ad_import.models import Server, User, Workstation


@permission_required('ad_import.view_user', raise_exception=True)
def view_user(request):
    user_id = request.GET.get('id')
    user = User.objects.get(id=user_id)
    return render(request, 'ad_import/user.html', {'user': user})


@permission_required('ad_import.view_workstation', raise_exception=True)
def view_workstation(request):
    computer_id = request.GET.get('id')
    computer = Workstation.objects.get(id=computer_id)
    return render(request, 'ad_import/computer.html', {'computer': computer})


@permission_required('ad_import.view_server', raise_exception=True)
def view_server(request):
    computer_id = request.GET.get('id')
    computer = Server.objects.get(id=computer_id)
    return render(request, 'ad_import/computer.html', {'computer': computer})
