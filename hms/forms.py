from django import forms
from .models import *

class staffForm(forms.ModelForm):
    class Meta:
        model = Staffinfo
        fields = ('staffid','firstname','lastname','position','salary','email','username','password','phonenumber','gender','dob','bankaccount','address')
        labels = {'firstname' : 'First Name',
        'lastname' : 'Last Name',
        'phonenumber' : 'Phone number',
        'bankaccount' : 'Bank account',
        'dob' : 'Date of birth (YYYY-MM-DD)'
        }


class memberForm(forms.ModelForm):
    class Meta:
        model = Memberinfo
        fields = ('userid','firstname','lastname','username','password','email','phonenumber')
        labels = {'firstname' : 'First Name',
        'lastname' : 'Last Name',
        'phonenumber' : 'Phone number'
        }

class guestForm(forms.ModelForm):
    class Meta:
        model = Guestinfo
        fields = ('guestid','firstname','lastname','phonenumber')
        labels = {'firstname' : 'First Name',
        'lastname' : 'Last Name',
        'phonenumber' : 'Phone number'
        }

class discountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('discountcode','discountpercent','startdate','expiredate')
        labels = {'discountcode' : 'Discount code',
        'discountpercent' : 'Discount percent',
        'startdate' : 'Start date (YYYY-MM-DD)',
        'expiredate' : 'Expire date (YYYY-MM-DD)'
        }

class discountFormUpdate(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('discountpercent','startdate','expiredate')
        labels = {'discountpercent' : 'Discount percent',
        'startdate' : 'Start date (YYYY-MM-DD)',
        'expiredate' : 'Expire date (YYYY-MM-DD)'
        }
        
class roomtypeForm(forms.ModelForm):
    class Meta:
        model = Roomtype
        fields = ('roomtype','roomdescription','roomprice','maxguest','beddetail','area')
        labels = {'roomtype' : 'Room type','roomdescription' : 'Room description' ,
        'roomprice' : 'Room price','maxguest' : 'Max guest','beddetail' : 'Bed detail'
        }
class roomtypeFormUpdate(forms.ModelForm):
    class Meta:
        model = Roomtype
        fields = ('roomdescription','roomprice','maxguest','beddetail','area')
        labels = {'roomdescription' : 'Room description' ,
        'roomprice' : 'Room price','maxguest' : 'Max guest','beddetail' : 'Bed detail'
        }

class roomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('roomid','roomtype','roomfloor','building')
        labels = {'roomtype' : 'Room type' ,
        'roomfloor' : 'Room floor'}

class serviceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('serviceid','service','servicedetails','price','bookingid','roomid')
        labels = {'servicedetails' : 'service details'}



class bookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('bookingid','checkindate','checkoutdate','userid','discountcode','totalprice',
        'totaldiscount','bookingstatus','totalguest','totalbreakfast')
        labels = {'bookingid' : 'Booking ID','checkindate' : 'Checkin date' ,'checkoutdate' : 'Checkout date',
        'userid' : 'User ID','discountcode':'Discount code','totalprice':'Total price','totaldiscount':'Total discount',
        'bookingstatus':'Booking status'}

        
class bookingForm2(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('bookingid','checkindate','checkoutdate','userid')
        labels = {'bookingid' : 'Booking ID','checkindate' : 'Checkin date' ,'checkoutdate' : 'Checkout date',
        'userid' : 'User ID'}

        

class roombookingForm(forms.Form):
    roomid = forms.ModelChoiceField(queryset=Room.objects.all())
    guestamount = forms.IntegerField(required = False,label='Guest amount')
    additionbed = forms.IntegerField(required = False,label='Addition bed')
    guestid = forms.ModelChoiceField(required = False,queryset=Guestinfo.objects.all())
    breakfast = forms.IntegerField(required = False)

class paymentForm(forms.ModelForm):
    class Meta:
        model = Paymentinfo
        fields = ('bookingid','paymentdate','paymentmethod','paymentstatus','staffid')
        labels = {'bookingid':'BookingID','paymentdate': 'Payment Date','paymentmethod' : 'Payment method',
        'paymentstatus' : 'Payment status','staffid' : 'StaffID' }

m = (('01', '01'),('02', '02'),('03', '03'),('04', '04'),('05', '05'),('06', '06'),
('07', '07'),('08', '08'),('09', '09'),('10', '10'),('11', '11'),('12', '12'))

class anaform(forms.Form):
    Year = forms.CharField(required = False,label='')
    Month = forms.ChoiceField(choices=m,required = False,label='')
