# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms


class Booking(models.Model):
    status = (('Booked', 'Booked'),('Check In', 'Check In'),('Check Out', 'Check Out'))
    bookingid = models.AutoField(db_column='BookingID', primary_key=True)  # Field name made lowercase.
    checkindate = models.DateField(db_column='CheckInDate')  # Field name made lowercase.
    checkoutdate = models.DateField(db_column='CheckOutDate')  # Field name made lowercase.
    userid = models.ForeignKey('Memberinfo', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    discountcode = models.ForeignKey('Discount', models.DO_NOTHING, db_column='DiscountCode', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    totaldiscount = models.FloatField(db_column='TotalDiscount')  # Field name made lowercase.
    bookingstatus = models.CharField(db_column='BookingStatus', max_length=10,choices = status)  # Field name made lowercase.
    totalguest = models.IntegerField(db_column='TotalGuest', blank=True, null=True)  # Field name made lowercase.
    totalbreakfast = models.IntegerField(db_column='TotalBreakfast', blank=True, null=True)  # Field name made lowercase.

    def __str__ (self):
        return str(self.bookingid)
    class Meta:
        managed = False
        db_table = 'Booking'




class Discount(models.Model):
    discountcode = models.CharField(db_column='DiscountCode', primary_key=True, max_length=10)  # Field name made lowercase.
    discountpercent = models.FloatField(db_column='DiscountPercent')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    expiredate = models.DateField(db_column='ExpireDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discount'
    def __str__ (self):
        return str(self.discountcode)


class Guestinfo(models.Model):
    guestid = models.AutoField(db_column='GuestID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=32)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=32)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GuestInfo'
    def __str__ (self):
        return '{0} ({1} {2})'.format(str(self.guestid), str(self.firstname),str(self.lastname))


class Memberinfo(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=32)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=32)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32)  # Field name made lowercase.
    password = models.CharField(db_column='PassWord', max_length=32)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=32)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=10)  # Field name made lowercase.
    signupdate = models.DateTimeField(db_column='SignUpDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberInfo'
    def __str__ (self):
        return '{0} ({1} {2})'.format(str(self.userid), str(self.firstname),str(self.lastname))


class Paymentinfo(models.Model):
    status = (('Paid', 'Paid'),('Pending', 'Pending')) 
    method = (('Credit Card', 'Credit Card'),('Cash', 'Cash')) 
    paymentid = models.AutoField(db_column='PaymentID', primary_key=True)  # Field name made lowercase.
    bookingid = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BookingID')  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate')  # Field name made lowercase.
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=15,choices = method)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=10,choices = status)  # Field name made lowercase.
    staffid = models.ForeignKey('Staffinfo', models.DO_NOTHING, db_column='StaffID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentInfo'


class Room(models.Model):
    roomid = models.IntegerField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomtype = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType')  # Field name made lowercase.
    roomfloor = models.IntegerField(db_column='RoomFloor')  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room'
    def __str__ (self):
        return str(self.roomid)
    def __str__ (self):
        return '{0} ({1})'.format(str(self.roomid), str(self.roomtype))


class Roombooking(models.Model):
    roomid = models.OneToOneField(Room, models.DO_NOTHING, db_column='RoomID')  # Field name made lowercase.
    bookingid = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BookingID')  # Field name made lowercase.
    guestamount = models.IntegerField(db_column='GuestAmount', blank=True, null=True)  # Field name made lowercase.
    additionbed = models.IntegerField(db_column='AdditionBed', blank=True, null=True)  # Field name made lowercase.
    breakfast = models.IntegerField(db_column='BreakFast', blank=True, null=True)  # Field name made lowercase.
    guestid = models.ForeignKey(Guestinfo, models.DO_NOTHING, db_column='GuestID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomBooking'
        unique_together = (('roomid', 'bookingid'),)


class Roomtype(models.Model):
    roomtype = models.CharField(db_column='RoomType', primary_key=True, max_length=32)  # Field name made lowercase.
    roomdescription = models.TextField(db_column='RoomDescription')  # Field name made lowercase.
    roomprice = models.IntegerField(db_column='RoomPrice')  # Field name made lowercase.
    maxguest = models.IntegerField(db_column='MaxGuest')  # Field name made lowercase.
    beddetail = models.TextField(db_column='BedDetail')  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=10)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomType'
    def __str__(self):
        return self.roomtype


class Service(models.Model):
    serviceid = models.AutoField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=32)  # Field name made lowercase.
    servicedetails = models.CharField(db_column='ServiceDetails', max_length=255)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    bookingid = models.ForeignKey(Booking, models.DO_NOTHING,db_column='BookingID')  # Field name made lowercase.
    roomid = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Service'


class Staffinfo(models.Model):
    sex = (('Male', 'Male'),('Female', 'Female'))
    staffid = models.AutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=32)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=32)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=32)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=10)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6,choices = sex)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=32)  # Field name made lowercase.
    salary = models.FloatField(db_column='Salary')  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffInfo'
    def __str__ (self):
        return '{0} ({1} {2})'.format(str(self.staffid), str(self.firstname),str(self.lastname))

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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
