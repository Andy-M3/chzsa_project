from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Machine, Maintenance, Claim
from django.http import HttpResponseRedirect

@login_required
@permission_required('view_machine', raise_exception=True)
def machine_list(request):
    machines = Machine.objects.all()
    model = request.GET.get('model')
    engine_model = request.GET.get('engine_model')
    sort_by = request.GET.get('sort_by')
    
    if model:
        machines = machines.filter(model__icontains=model)
    if engine_model:
        machines = machines.filter(engine_model__icontains=engine_model)
    if sort_by:
        machines = machines.order_by(sort_by)
    
    return render(request, 'chzsa_app/machine_list.html', {'machines': machines})

@login_required
@permission_required('view_maintenance', raise_exception=True)
def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    type = request.GET.get('type')
    organization = request.GET.get('organization')
    sort_by = request.GET.get('sort_by')
    
    if type:
        maintenances = maintenances.filter(type__icontains=type)
    if organization:
        maintenances = maintenances.filter(organization__icontains=organization)
    if sort_by:
        maintenances = maintenances.order_by(sort_by)
    
    return render(request, 'chzsa_app/maintenance_list.html', {'maintenances': maintenances})

@login_required
@permission_required('view_claim', raise_exception=True)
def claim_list(request):
    claims = Claim.objects.all()
    failure_node = request.GET.get('failure_node')
    organization = request.GET.get('organization')
    sort_by = request.GET.get('sort_by')
    
    if failure_node:
        claims = claims.filter(failure_node__icontains=failure_node)
    if organization:
        claims = claims.filter(organization__icontains=organization)
    if sort_by:
        claims = claims.order_by(sort_by)
    
    return render(request, 'chzsa_app/claim_list.html', {'claims': claims})

def home(request):
    return HttpResponseRedirect('/machines/')

def search_machine(request):
    if request.method == 'GET':
        serial_number = request.GET.get('serial_number')
        try:
            machine = Machine.objects.get(serial_number=serial_number)
            return render(request, 'chzsa_app/machine_detail.html', {'machine': machine})
        except Machine.DoesNotExist:
            return render(request, 'chzsa_app/machine_not_found.html')
    return render(request, 'chzsa_app/machine_search.html')
