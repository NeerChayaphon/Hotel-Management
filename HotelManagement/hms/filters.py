import django_filters
from django_filters import DateFilter,CharFilter,NumberFilter,ChoiceFilter,DateTimeFilter
from .models import *


class bookingFilters(django_filters.FilterSet):
    checkindate = DateTimeFilter(field_name='checkindate',label='Checkin (YYYY-MM-DD)')
    checkoutdate = DateTimeFilter(field_name='checkoutdate',label='Checkout (YYYY-MM-DD)')
    class Meta:
        model = Booking
        fields = ('bookingid','userid','bookingstatus')

class paymentFilters(django_filters.FilterSet):
    paymentdate = DateTimeFilter(field_name='paymentdate',lookup_expr='gte',label='payment date (YYYY-MM-DD)')
    class Meta:
        model = Paymentinfo
        fields = ('paymentstatus','bookingid')

class staffinfoFilters(django_filters.FilterSet):
    firstname = CharFilter(field_name='firstname',lookup_expr='icontains',label='Firstname')
    lastname = CharFilter(field_name='lastname',lookup_expr='icontains',label='Lastname')
    class Meta:
        model = Staffinfo
        fields = ('position','email','phonenumber')

class memberinfoFilters(django_filters.FilterSet):
    firstname = CharFilter(field_name='firstname',lookup_expr='icontains',label='Firstname')
    lastname = CharFilter(field_name='lastname',lookup_expr='icontains',label='Lastname')
    class Meta:
        model = Memberinfo
        fields = ('email','phonenumber')

class guestinfoFilters(django_filters.FilterSet):
    firstname = CharFilter(field_name='firstname',lookup_expr='icontains',label='Firstname')
    lastname = CharFilter(field_name='lastname',lookup_expr='icontains',label='Lastname')
    phonenumber = NumberFilter(field_name='phonenumber',label='Phone number')

class discountFilters(django_filters.FilterSet):
    startdate = DateTimeFilter(field_name='startdate',lookup_expr='gte',label='Start date (YYYY-MM-DD)')
    expiredate = DateTimeFilter(field_name='expiredate',lookup_expr='lte',label='expiredate (YYYY-MM-DD)')
    discountcode = CharFilter(field_name='discountcode',lookup_expr='icontains',label='discountcode')

class roomFilters(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = ('roomid','roomtype')

class roomtypeFilters(django_filters.FilterSet):
    roomprice = NumberFilter(field_name='roomprice',label='Room price (less than or equal)',lookup_expr='lte')

class serviceFilters(django_filters.FilterSet):
    service = CharFilter(field_name='service',lookup_expr='icontains',label='Service')
    class Meta:
        model = Service
        fields = ('service','bookingid','roomid','price')

    

    