# Generated by Django 3.2 on 2021-04-16 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingid', models.AutoField(db_column='BookingID', primary_key=True, serialize=False)),
                ('checkindate', models.DateTimeField(db_column='CheckInDate')),
                ('checkoutdate', models.DateTimeField(db_column='CheckOutDate')),
                ('totalprice', models.FloatField(db_column='TotalPrice')),
                ('totaldiscount', models.FloatField(db_column='TotalDiscount')),
                ('bookingstatus', models.CharField(db_column='BookingStatus', max_length=10)),
            ],
            options={
                'db_table': 'Booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discountcode', models.CharField(db_column='DiscountCode', max_length=10, primary_key=True, serialize=False)),
                ('discountpercent', models.FloatField(db_column='DiscountPercent')),
                ('startdate', models.DateTimeField(db_column='StartDate')),
                ('expiredate', models.DateTimeField(db_column='ExpireDate')),
            ],
            options={
                'db_table': 'Discount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guestinfo',
            fields=[
                ('guestid', models.AutoField(db_column='GuestID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=32)),
                ('lastname', models.CharField(db_column='LastName', max_length=32)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=10)),
                ('email', models.CharField(db_column='Email', max_length=32)),
            ],
            options={
                'db_table': 'GuestInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Memberinfo',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=32)),
                ('lastname', models.CharField(db_column='LastName', max_length=32)),
                ('username', models.CharField(db_column='UserName', max_length=32)),
                ('password', models.CharField(db_column='PassWord', max_length=32)),
                ('email', models.CharField(db_column='Email', max_length=32)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=10)),
                ('signupdate', models.DateTimeField(db_column='SignUpDate')),
            ],
            options={
                'db_table': 'MemberInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paymentinfo',
            fields=[
                ('paymentid', models.AutoField(db_column='PaymentID', primary_key=True, serialize=False)),
                ('paymentdate', models.DateTimeField(db_column='PaymentDate')),
                ('paymentmethod', models.CharField(db_column='PaymentMethod', max_length=15)),
                ('paymentstatus', models.CharField(db_column='PaymentStatus', max_length=10)),
            ],
            options={
                'db_table': 'PaymentInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomid', models.AutoField(db_column='RoomID', primary_key=True, serialize=False)),
                ('roomfloor', models.IntegerField(db_column='RoomFloor')),
                ('building', models.CharField(db_column='Building', max_length=20)),
            ],
            options={
                'db_table': 'Room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('roomtype', models.CharField(db_column='RoomType', max_length=10, primary_key=True, serialize=False)),
                ('roomdescription', models.TextField(db_column='RoomDescription')),
                ('roomprice', models.FloatField(db_column='RoomPrice')),
                ('maxguest', models.IntegerField(db_column='MaxGuest')),
                ('beddetail', models.TextField(db_column='BedDetail')),
                ('area', models.CharField(db_column='Area', max_length=10)),
                ('picture', models.TextField(db_column='Picture')),
            ],
            options={
                'db_table': 'RoomType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seasonratesetup',
            fields=[
                ('seasonid', models.AutoField(db_column='SeasonID', primary_key=True, serialize=False)),
                ('seasonstart', models.DateTimeField(db_column='SeasonStart')),
                ('seasonend', models.DateTimeField(db_column='SeasonEnd')),
                ('seasonpricerate', models.FloatField(db_column='SeasonPriceRate')),
            ],
            options={
                'db_table': 'SeasonRateSetup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service', models.CharField(db_column='Service', max_length=32, primary_key=True, serialize=False)),
                ('servicedetails', models.CharField(db_column='ServiceDetails', max_length=255)),
                ('price', models.FloatField(db_column='Price')),
            ],
            options={
                'db_table': 'Service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staffinfo',
            fields=[
                ('staffid', models.AutoField(db_column='StaffID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=32)),
                ('lastname', models.CharField(db_column='LastName', max_length=32)),
                ('username', models.CharField(db_column='UserName', max_length=32)),
                ('password', models.CharField(db_column='Password', max_length=32)),
                ('email', models.CharField(db_column='Email', max_length=32)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=10)),
                ('gender', models.CharField(db_column='Gender', max_length=6)),
                ('dob', models.DateTimeField(db_column='DOB')),
                ('address', models.TextField(db_column='Address')),
                ('position', models.CharField(db_column='Position', max_length=32)),
                ('salary', models.FloatField(db_column='Salary')),
                ('bankaccount', models.CharField(db_column='BankAccount', max_length=10)),
            ],
            options={
                'db_table': 'StaffInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roombooking',
            fields=[
                ('roomid', models.OneToOneField(db_column='RoomID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='hms.room')),
                ('guestamount', models.IntegerField(db_column='GuestAmount')),
                ('additionbed', models.IntegerField(db_column='AdditionBed')),
            ],
            options={
                'db_table': 'RoomBooking',
                'managed': False,
            },
        ),
    ]
