# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Auditor(models.Model):
    auditor_id = models.IntegerField(db_column='Auditor_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time', blank=True, null=True)  # Field name made lowercase.
    grant_grant = models.ForeignKey('Grant', models.DO_NOTHING, db_column='Grant_Grant_ID',related_name='Auditor_grant_grant')  # Field name made lowercase.
    grant_organization_nonprofit = models.ForeignKey('Grant', models.DO_NOTHING, db_column='Grant_Organization_Nonprofit_ID', related_name='Auditor_grant_organization_nonprofit')
    class Meta:
        managed = False
        db_table = 'auditor'
        unique_together = (('auditor_id', 'grant_grant', 'grant_organization_nonprofit'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employee_id = models.IntegerField(db_column='Employee_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_time', blank=True, null=True)  # Field name made lowercase.
    organization_nonprofit = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_Nonprofit_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'
        unique_together = (('employee_id', 'organization_nonprofit'),)


class Grant(models.Model):
    grant_id = models.IntegerField(db_column='Grant_ID', primary_key=True)  # Field name made lowercase.
    approve_deny = models.IntegerField(db_column='Approve/Deny', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approval_date = models.DateField(db_column='Approval_date', blank=True, null=True)  # Field name made lowercase.
    approval_manager = models.CharField(db_column='Approval_manager', max_length=45, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=45, blank=True, null=True)  # Field name made lowercase.
    allocated = models.CharField(db_column='Allocated', max_length=45, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date', blank=True, null=True)  # Field name made lowercase.
    organization_nonprofit = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_Nonprofit_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grant'
        unique_together = (('grant_id', 'organization_nonprofit'),)


class Grantee(models.Model):
    grantee_id = models.IntegerField(db_column='Grantee_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grant_grant = models.ForeignKey(Grant, models.DO_NOTHING, db_column='Grant_Grant_ID', related_name='Grantee_grant_grant')  # Field name made lowercase.
    grant_organization_nonprofit = models.ForeignKey(Grant, models.DO_NOTHING, db_column='Grant_Organization_Nonprofit_ID', related_name='Grantee_grant_organization_nonprofit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grantee'
        unique_together = (('grantee_id', 'grant_grant', 'grant_organization_nonprofit'),)


class GranteeBank(models.Model):
    bank_id = models.IntegerField(db_column='Bank_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    account_number = models.CharField(db_column='Account_number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    routing_number = models.CharField(db_column='Routing_number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grantee_grantee = models.ForeignKey(Grantee, models.DO_NOTHING, db_column='Grantee_Grantee_ID', related_name='GranteeBank_grantee_grantee') # Field name made lowercase.
    grantee_grant_grant = models.ForeignKey(Grantee, models.DO_NOTHING, db_column='Grantee_Grant_Grant_ID', related_name='GranteeBank_grantee_grant_grant') # Field name made lowercase.
    grantee_grant_organization_nonprofit = models.ForeignKey(Grantee, models.DO_NOTHING, db_column='Grantee_Grant_Organization_Nonprofit_ID', related_name='GranteeBank_grantee_grant_organization_nonprofit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grantee_bank'
        unique_together = (('bank_id', 'grantee_grantee', 'grantee_grant_grant', 'grantee_grant_organization_nonprofit'),)


class Managers(models.Model):
    manager_id = models.IntegerField(db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    grants_approved = models.CharField(db_column='Grants_approved', max_length=45, blank=True, null=True)  # Field name made lowercase.
    organization_nonprofit = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_Nonprofit_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managers'
        unique_together = (('manager_id', 'organization_nonprofit'),)


class Organization(models.Model):
    nonprofit_id = models.IntegerField(db_column='Nonprofit_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_Code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class Status(models.Model):
    status_id = models.IntegerField(db_column='Status_ID', primary_key=True)  # Field name made lowercase.
    applied = models.IntegerField(db_column='Applied', blank=True, null=True)  # Field name made lowercase.
    loi = models.IntegerField(db_column='Loi', blank=True, null=True)  # Field name made lowercase.
    review = models.IntegerField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    approved = models.IntegerField(db_column='Approved', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    archived = models.IntegerField(db_column='Archived', blank=True, null=True)  # Field name made lowercase.
    grant_grant = models.ForeignKey(Grant, models.DO_NOTHING, db_column='Grant_Grant_ID', related_name='Status_grant_grant')  # Field name made lowercase.
    grant_organization_nonprofit = models.ForeignKey(Grant, models.DO_NOTHING, db_column='Grant_Organization_Nonprofit_ID',related_name='Status_grant_organization_nonprofit')   # Field name made lowercase.
        

    class Meta:
        managed = False
        db_table = 'status'
        unique_together = (('status_id', 'grant_grant', 'grant_organization_nonprofit'),)
