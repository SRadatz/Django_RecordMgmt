from django.shortcuts import render
from django.http import HttpResponse
from .models import * 



# Create your views here.

def index(request):
    return render(request, 'index.html')
def grant_create(request):
    return render(request, "grant_creation.html")
def employee_creation(request):
    return render(request, "employee_creation.html")
def grant_creation(request):
    return render(request, "grant_creation.html")

def emp_delete(request):
    EID = request.GET['employee_id']
    EID = int(EID)
    delete_rec = Employee.objects.get(employee_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def employee(request):
    query_set = Employee.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'employee.html', context)

def emp_edit(request):
    EID = request.GET['employee_id']
    EID = int(EID)
    edit_rec = Employee.objects.get(employee_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "emp_edit.html", content)



def emp_conf(request):
    ID = request.GET['employee_id']
    UN = request.GET['username']
    EM = request.GET['email']
    PD = request.GET['password']
    CT ='2020-01-01 12:30:00' 
    OID = request.GET['organization_nonprofit']
    OID = int(OID)

    ON = Organization.objects.get(nonprofit_id = OID)
    insert_data = Employee.objects.create(employee_id= int(ID),
                                            username= UN,
                                            email= EM,
                                            password= PD,
                                            create_time= CT,
                                            organization_nonprofit= ON)
    query_set_product_price_filtered = []
    query_set_product_price = Employee.objects.all()

    for obj in query_set_product_price:
        query_set_product_price_filtered.append(obj)

    context = {
    'object_instance' : query_set_product_price_filtered
    }

    return render(request, "Confirm.html")

def emp_edit_conf(request):
    ID = request.GET['employee_id']
    UN = request.GET['username']
    EM = request.GET['email']
    PD = request.GET['password']
 
    EID = request.GET['employee_id']
    edit_rec = Employee.objects.get(employee_id= EID)

    edit_rec.employee_id = ID
    edit_rec.username = UN
    edit_rec.email = EM
    edit_rec.password = PD
    edit_rec.save()

    return render(request, "Confirm.html")    

def Confirm(request):
    grant_organization_nonprofit = request.GET['organization_nonprofit']
    grant_organization_nonprofit = int(organization_nonprofit)
    grant_grant = request.GET['grant_id']
    grant_grant = int(grant_id)
    grantee_id = request.GET['grantee_id']
    grantee_id = int(grantee_id)
    name = request.GET['name']
    address = address.GET['address']
    city = city.GET['city']
    state = state.GET['state']
    postal_code = postal_code.GET['postal_code']

    query_grantee_filtered = []
    query_grantee_value = Grantee.objects.all()

    for object in query_grantee_value:
        query_grantee_filtered.append(object)

    context = {
        'object_instance' : query_grantee_filtered
    }

    return render(request, 'Confirm.html', context)

def dashboard(request):
    query_set = Grant.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'Grant.html', context)

def grant_conf(request):
    GrantID = request.GET['grant_id']
    Appr = request.GET['approve_deny']
    ApprD = request.GET['approval_date']
    ApprM = request.GET['approval_manager']
    Val = request.GET['value']
    Allo = request.GET['allocated']
    StartD = request.GET['start_date']
    EndD = request.GET['end_date']
    OID = request.GET['organization_nonprofit']

    OID = int(OID)
    ON = Organization.objects.get(nonprofit_id = OID)

    insert_data = Grant.objects.create(grant_id= int(GrantID),
                                            approve_deny= int(Appr),
                                            approval_date= ApprD,
                                            approval_manager= ApprM,
                                            value= Val,
                                            allocated= Allo,
                                            start_date= StartD,
                                            end_date= EndD,
                                            organization_nonprofit= ON)

    return render(request, "Confirm.html")

def grant_delete(request):
    EID = request.GET['grant_id']
    EID = int(EID)
    delete_rec = Grant.objects.get(grant_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def grant_edit(request):
    EID = request.GET['grant_id']
    EID = int(EID)
    edit_rec = Grant.objects.get(grant_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "grant_edit.html", content)

def grant_edit_conf(request):
    GrantID = request.GET.get('grant_id')
    ApprD = request.GET.get('approval_date')
    ApprM = request.GET.get('approval_manager')
    Val = request.GET.get('value')
    Allo = request.GET.get('allocated')
    StartD = request.GET.get('start_date')
    EndD = request.GET.get('end_date')

    edit_rec = Grant.objects.get(grant_id= GrantID)

    edit_rec.grant_id = GrantID
    # edit_rec.approve_deny = Appr
    edit_rec.approval_date = ApprD
    edit_rec.approval_manager = ApprM
    edit_rec.value = Val
    edit_rec.allocated =Allo
    edit_rec.start_date = StartD
    edit_rec.end_date = EndD
    edit_rec.save()

    return render(request, "Confirm.html")

def auditor_creation(request):
    return render(request, "auditor_creation.html")

def Auditor_home(request):
    query_set = Auditor.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'Auditor.html', context)

def auditor_conf(request):
    auditorID = request.GET['auditor_id']
    User = request.GET['username']
    Email = request.GET['email']
    Pass = request.GET['password']
    Time = request.GET['create_time']
    grant = request.GET['grant_grant']
    OID = request.GET['organization_nonprofit']

    OID = int(OID)
    ON = Organization.objects.get(nonprofit_id = OID)
    GT = int(grant)
    Grant_obj = Grant.objects.get(grant_id = GT)

    insert_data = Auditor.objects.create(auditor_id= int(auditorID),
                                            username= User,
                                            email= Email,
                                            password= Pass,
                                            create_time= Time,
                                            grant_grant= Grant_obj,
                                            grant_organization_nonprofit= ON)

    return render(request, "Confirm.html")

def auditor_delete(request):
    EID = request.GET['auditor_id']
    EID = int(EID)
    delete_rec = Auditor.objects.get(auditor_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def auditor_edit_conf(request):
    auditorID = request.GET['auditor_id']
    User = request.GET['username']
    Email = request.GET['email']
    Pass = request.GET['password']

    edit_rec = Auditor.objects.get(auditor_id= auditorID)

    edit_rec.auditor_id = auditorID
    edit_rec.username = User
    edit_rec.email = Email
    edit_rec.password = Pass
    edit_rec.save()

    return render(request, "Confirm.html")

def auditor_edit(request):
    EID = request.GET['auditor_id']
    EID = int(EID)
    edit_rec = Auditor.objects.get(auditor_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "auditor_edit.html", content)

def grantee_home(request):
    query_set = Grantee.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'grantee.html', context)

def grantee_delete(request):
    EID = request.GET['grantee_id']
    EID = int(EID)
    delete_rec = Grantee.objects.get(grantee_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def grantee_edit_conf(request):
    granteeID = request.GET['grantee_id']
    Name = request.GET['name']
    Address = request.GET['address']
    City = request.GET['city']
    State = request.GET['state']
    Postal_Code = request.GET['postal_code']
    granteeID = int(granteeID)

    edit_rec = Grantee.objects.get(grantee_id= granteeID)

    edit_rec.grantee_id = granteeID
    edit_rec.name = Name
    edit_rec.address = Address
    edit_rec.city = City
    edit_rec.state = State
    edit_rec.postal_code = Postal_Code
    edit_rec.save()

    return render(request, "Confirm.html")

def grantee_edit(request):
    EID = request.GET['grantee_id']
    EID = int(EID)
    edit_rec = Grantee.objects.get(grantee_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "grantee_edit.html", content)

def manager_creation(request):
    return render(request, "manager_creation.html")

def manager_home(request):
    query_set = Managers.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'manager.html', context)

def manager_delete(request):
    EID = request.GET['manager_id']
    EID = int(EID)
    delete_rec = Managers.objects.get(manager_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def manager_edit_conf(request):
    managerID = request.GET['manager_id']
    User = request.GET['username']
    Email = request.GET['email']
    Pass = request.GET['password']
    Name = request.GET['name']
    Grants = request.GET['grants_approved']

    edit_rec = Managers.objects.get(manager_id= managerID)

    edit_rec.manager_id = managerID
    edit_rec.name = Name
    edit_rec.username = User
    edit_rec.email = Email
    edit_rec.password = Pass
    edit_rec.grants_approved = Grants
    edit_rec.save()

    return render(request, "Confirm.html")

def manager_edit(request):
    EID = request.GET['manager_id']
    EID = int(EID)
    edit_rec = Managers.objects.get(manager_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "manager_edit.html", content)

def manager_conf(request):
    ID = request.GET['manager_id']
    User = request.GET['username']
    Pass = request.GET['password']
    Name = request.GET['name']
    Email = request.GET['email']
    Grants = request.GET['grants_approved']
    OID = request.GET['organization_nonprofit']

    OID = int(OID)
    ON = Organization.objects.get(nonprofit_id = OID)

    insert_data = Managers.objects.create(manager_id= int(ID),
                                            username= User,
                                            password= Pass,
                                            name= Name,
                                            email= Email,
                                            grants_approved= Grants,
                                            organization_nonprofit= ON)

    return render(request, "Confirm.html")

def organization_creation(request):
    return render(request, "organization_creation.html")

def organization_home(request):
    query_set = Organization.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'organization.html', context)

def organization_delete(request):
    EID = request.GET['nonprofit_id']
    EID = int(EID)
    delete_rec = Organization.objects.get(nonprofit_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def organization_edit_conf(request):
    organizationID = request.GET['nonprofit_id']
    Name = request.GET['name']
    Address = request.GET['address']
    City = request.GET['city']
    State = request.GET['state']
    Postal_Code = request.GET['postal_code']
    Country = request.GET['country']

    edit_rec = Organization.objects.get(nonprofit_id= organizationID)

    edit_rec.organization_id = organizationID
    edit_rec.name = Name
    edit_rec.address = Address
    edit_rec.city = City
    edit_rec.state = State
    edit_rec.postal_code = Postal_Code
    edit_rec.country = Country
    edit_rec.save()

    return render(request, "Confirm.html")

def organization_edit(request):
    EID = request.GET['nonprofit_id']
    EID = int(EID)
    edit_rec = Organization.objects.get(nonprofit_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "organization_edit.html", content)

def organization_conf(request):
    ID = request.GET['nonprofit_id']
    Name = request.GET['name']
    Address = request.GET['address']
    City = request.GET['city']
    State = request.GET['state']
    Postal_Code = request.GET['postal_code']
    Country = request.GET['country']

    insert_data = Organization.objects.create(nonprofit_id= int(ID),
                                            name= Name,
                                            address= Address,
                                            city= City,
                                            state= State,
                                            postal_code= Postal_Code,
                                            country= Country)

    return render(request, "Confirm.html")


def status_home(request):
    query_set = Status.objects.all()
    context = {
        'object_instance' : query_set
    }
    return render(request, 'status.html', context)

def status_delete(request):
    EID = request.GET['status_id']
    EID = int(EID)
    delete_rec = Status.objects.get(status_id= EID)
    delete_rec.delete()

    return render(request, "record_delete.html")

def status_edit_conf(request):
    statusID = request.GET['status_id']
    Applied = request.GET['applied']
    LOI = request.GET['loi']
    Review = request.GET['review']
    Approved = request.GET['approved']
    Active = request.GET['active']
    Archived = request.GET['archived']

    edit_rec = Status.objects.get(status_id= statusID)

    edit_rec.status_id = statusID
    edit_rec.applied = Applied
    edit_rec.loi = LOI
    edit_rec.review = Review
    edit_rec.approved = Approved
    edit_rec.active = Active
    edit_rec.archived = Archived
    edit_rec.save()

    return render(request, "Confirm.html")

def status_edit(request):
    EID = request.GET['status_id']
    EID = int(EID)
    edit_rec = Status.objects.get(status_id= EID)

    content = {
        'object_instance' : edit_rec
    }

    return render(request, "status_edit.html", content)
