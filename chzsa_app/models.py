from django.db import models
from django.contrib.auth.models import User

class Machine(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    engine_model = models.CharField(max_length=100)
    engine_serial_number = models.CharField(max_length=100)
    transmission_model = models.CharField(max_length=100)
    transmission_serial_number = models.CharField(max_length=100)
    drive_axle_model = models.CharField(max_length=100)
    drive_axle_serial_number = models.CharField(max_length=100)
    steer_axle_model = models.CharField(max_length=100)
    steer_axle_serial_number = models.CharField(max_length=100)
    contract_number_date = models.CharField(max_length=100)
    shipment_date = models.DateField()
    end_user = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    additional_options = models.TextField()
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='client_machines')
    service_company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='service_company_machines')

class Maintenance(models.Model):
    type = models.CharField(max_length=100)
    date = models.DateField()
    operating_hours = models.IntegerField()
    order_number = models.CharField(max_length=100)
    order_date = models.DateField()
    organization = models.CharField(max_length=255)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='service_company_maintenances')

class Claim(models.Model):
    failure_date = models.DateField()
    operating_hours = models.IntegerField()
    failure_node = models.CharField(max_length=255)
    failure_description = models.TextField()
    recovery_method = models.CharField(max_length=255)
    spare_parts_used = models.TextField()
    recovery_date = models.DateField()
    downtime = models.IntegerField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='service_company_claims')
