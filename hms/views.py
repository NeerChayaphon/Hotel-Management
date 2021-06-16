from django.shortcuts import render,redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
import string
from .models import *
import datetime
from django.db import connection
from datetime import date
from datetime import datetime as dt
dt.fromtimestamp
from django.urls import reverse


from .forms import *

from .filters import * 

# Create your views here.
def memberSignIn(request):
    form = request.POST
    signInEmail = request.POST.get('email')
    signInPass = request.POST.get('password')

    if len(request.POST) != 0:
        for i in Memberinfo.objects.all():
            if(i.email == signInEmail and i.password == signInPass) or (i.username == signInEmail and i.password == signInPass):
                request.session['member_id'] = i.userid
                return redirect('bookingLanding')
                break
        
        messages.add_message(request, messages.INFO, 'Incorrect Username or password')

    return render(request, 'hms/login2.html')

def bookingLanding(request):
    #### User Auth ####
    member_id = request.session["member_id"]
    member = Memberinfo.objects.get(userid = member_id)
    context = {'member' : member}

    #### Room Data #####
    typeRoom = Roomtype.objects.all()
    roomData = {}
    for i in typeRoom:
        rType = i.roomtype
        roomData[rType.replace(" ", "")] = i
    
    context2 = {'RoomType': typeRoom}
    context.update(context2)
    context.update(roomData)
    
### session (direct login)

    form = request.POST
    
    if len(request.POST) != 0:
        #time = datetime.time(12,0,0)
        CheckInDate = request.POST.get('Check In')
        
        CheckOutDate = request.POST.get('Check Out')
        #CheckOutDate =  CheckOutDate.strftime("%Y-%m-%d")
        NumRoom = int(request.POST.get('Room')) 
        NumGuest = int(request.POST.get('Guest'))

        BookingInfo = {'CheckInDate': CheckInDate,'CheckOutDate' : CheckOutDate,'NumRoom' : NumRoom,'NumGuest' : NumGuest}
        context.update(BookingInfo)

        if ((CheckInDate < CheckOutDate) and (CheckInDate >= date.today().strftime('%Y-%m-%d')) and (CheckOutDate != CheckInDate)):
            list1 = []
            MaxType = ['one','two','three']
            dict1 = {}
            count = 0
            for i in Roomtype.objects.all():
                cursor = connection.cursor() 
                cursor.execute('SELECT COUNT(*) AS %s FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s  AND RoomType = %s;',[i.roomtype,CheckOutDate,CheckInDate,i.roomtype])
                #print(dictfetchall(cursor))

                cursor = connection.cursor() 
                cursor.execute('SELECT ABS(COUNT(*) - (SELECT COUNT(*) FROM Room WHERE roomtype = %s)) AS %s FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s  AND RoomType = %s;',[i.roomtype,MaxType[count],CheckOutDate,CheckInDate,i.roomtype])
                list2 = dictfetchall(cursor)
                print(list2[0])
                dict1.update(list2[0])
                count = count + 1

            check = {'oneC' : dict1['one'] - NumRoom, 'twoC' : dict1['two'] - NumRoom, 'threeC' : dict1['three'] - NumRoom}
            dict1.update(context)
            print(type(dict1['one']))
            print(type(dict1['NumRoom']))
            dict1.update(check)
            print(dict1)   

            # session
            request.session['CheckInDate'] = CheckInDate
            request.session['CheckOutDate'] = CheckOutDate
            request.session['Room'] = NumRoom
            request.session['Guest'] = NumGuest
            return render(request,'hms/booking2.html',dict1)
                
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Date Range')
    return render(request, 'hms/booking.html',context)



def reserveRoom(request,rType):
    # member
    member_id = request.session["member_id"]
    member = Memberinfo.objects.get(userid = member_id)
    context = {'member' : member}

    typeRoom = Roomtype.objects.get(roomtype = rType)
    content = {'RoomType' : typeRoom}

    content.update(context)

    value = ['CheckInDate','CheckOutDate','Room','Guest']

    for x in value:
        print(request.session[x])
        content[x] = request.session[x]


    RbInfo = {}

    if len(request.POST) != 0:
        if request.method == 'POST':
            RbInfo['CheckInDate'] = request.POST.get('Check In')
            RbInfo['CheckOutDate'] = request.POST.get('Check Out')
            RbInfo['Room'] = int(request.POST.get('Room'))
            RbInfo['Guest'] = int(request.POST.get('Guest'))
            RbInfo['EB'] = request.POST.get('EB')
            RbInfo['NEB'] = int(request.POST.get('NEB'))
            RbInfo['BF'] = request.POST.get('BF')
            RbInfo['NBF'] = int(request.POST.get('NBF'))

            print(type(RbInfo['CheckOutDate']))
            # messages.add_message(request, messages.INFO, 'Sign up success')
            print(RbInfo)
            content.update(RbInfo)

            request.session['TypeRoom'] = typeRoom.roomtype
            request.session['RoomPrice'] = typeRoom.roomprice
            request.session['CheckInDate'] = RbInfo['CheckInDate']
            request.session['CheckOutDate'] = RbInfo['CheckOutDate'] 
            request.session['Room'] = RbInfo['Room']
            request.session['Guest'] = RbInfo['Guest']

            #### total #####
            if RbInfo['EB'] == "on":
                Bprice = RbInfo['NEB'] * 500
            else:
                Bprice = 0
            if RbInfo['BF'] == "on":
                BFprice = RbInfo['NBF'] * 100
            else:
                BFprice = 0
            request.session['Total'] = (typeRoom.roomprice * RbInfo['Room']) + Bprice + BFprice

            if RbInfo['EB'] != None:
                request.session['EB']  = RbInfo['EB'] 
                request.session['NEB'] = RbInfo['NEB'] 
            else :
                request.session['EB']  = "off"
                request.session['NEB'] = 0 
            if RbInfo['BF'] != None:
                request.session['BF'] = RbInfo['BF']
                request.session['NBF'] = RbInfo['NBF']
            else :
                request.session['BF']  = "off"
                request.session['NBF'] = 0

            # promoCode
            request.session['promoID'] = None
            request.session['promoP'] = 0

            print(content)
            return redirect('checkout')
            
    print(content)
    return render(request, 'hms/reserveRoom.html',content)

def checkout(request):
    content = {}
    member_id = request.session["member_id"]
    member = Memberinfo.objects.get(userid = member_id)
    content['member'] = member

    discount = Discount.objects.all()
    value = ['TypeRoom','RoomPrice','CheckInDate','CheckOutDate','Room','Guest','EB','NEB','BF','NBF']

    
    for x in value:
        print(request.session[x])
        content[x] = request.session[x]

    # Find day
    cin = content['CheckInDate']
    cin2 = dt.strptime(str(cin),'%Y-%m-%d')
    print(cin2)
    cout = content['CheckOutDate']
    cout2 = dt.strptime(str(cout),'%Y-%m-%d')
    print(cout2)
    dayC = (cout2 - cin2).days
    print(type(dayC))
    
    content['RoomPrice'] = content['RoomPrice'] * content['Room'] * dayC    

    if content['EB'] == "on":
        content['Bprice'] = content['NEB'] * 500
    else:
        content['Bprice'] = 0
    if content['BF'] == "on":
        content['BFprice'] = content['NBF'] * 100
    else:
        content['BFprice'] = 0

    content['Total'] = content['RoomPrice'] + content['Bprice'] + content['BFprice']

    content['promo'] = 0
    content['promoP'] = 0
    
    dcode = None
    if request.POST.get('promo'):
        for d in discount:
            if (d.discountcode == request.POST.get('promo')) and (date.today() <= d.expiredate):
                content['promo'] = 1
                content['promoD'] = d
                content['promoP'] = int((d.discountpercent / 100) * content['Total'])
                request.session['promoID'] = d.discountcode
                dcode = d.discountcode
                request.session['promoP'] = int((d.discountpercent / 100) * content['Total'])
                break
            else:
                content['promo'] = 2
                
        content['Total'] = int(content['Total'] - content['promoP'])
        content['Total']
        request.session['Total'] = content['Total']

    elif request.method == 'POST':

        cursor = connection.cursor() 
        cursor.execute('SELECT R.RoomID FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s  AND RoomType = %s;',[content['CheckOutDate'],content['CheckInDate'],content['TypeRoom']])
        dataDict = dictfetchall(cursor)
        bookRoom = []
        for i in dataDict:
            bookRoom.append(i['RoomID'])

        allRoom = Room.objects.filter(roomtype = content['TypeRoom'])

        aviRoom = []
        for j in allRoom:
            if (j.roomid not in bookRoom):
                aviRoom.append(int(j.roomid))
        
         ## Booking ##
        booking = Booking()
        # booking.bookingid = bCount + 1
        booking.checkindate = content['CheckInDate']
        booking.checkoutdate = content['CheckOutDate']
        booking.userid = member
        # discount object
        if request.session['promoID'] != None :
            codeD = request.session['promoID']
            discountObj = Discount.objects.get(discountcode = codeD)
            booking.discountcode = discountObj
        booking.totalprice = request.session['Total']
        booking.totaldiscount = request.session['promoP']
        booking.bookingstatus = "Booked"
        booking.totalguest = content['Guest']
        booking.totalbreakfast = content['NBF']
        booking.save()

        
        
        lastBook = Booking.objects.last()
        bCount = lastBook.bookingid

        print(bCount)

        ## RoomBooking
        newbookingObj = Booking.objects.get(bookingid = bCount)
        for i in range(0,int(content['Room'])):
            #room object
            roomObj = Room.objects.get(roomid = aviRoom[i])
            # input
            roombooking = Roombooking()
            roombooking.bookingid = newbookingObj
            roombooking.roomid = roomObj
            roombooking.guestamount = 0
            roombooking.additionbed = 0
            roombooking.breakfast = 0
            roombooking.save()
        print(list(aviRoom))

        ## Paymentinfo
        paymentinfo = Paymentinfo()
        paymentinfo.bookingid = newbookingObj
        paymentinfo.paymentdate = datetime.datetime.now()
        paymentinfo.paymentmethod = 'Credit'
        paymentinfo.paymentstatus = 'Paid'
        paymentinfo.save()

        return redirect('bookSuccess')

        

        
    #for x in value:
    #   try:
     #       del request.session[x]
     #  except KeyError:
    #       pass

    return render(request, 'hms/checkout.html',content)
         

def memberSignUp(request):
    form = request.POST
    if len(request.POST) != 0:
        if (request.POST.get('inputPassword') != request.POST.get('ConfirmPassword')) :
            messages.add_message(request, messages.INFO, 'Password does not match')
        else :
            if request.method == 'POST':
                memberinfo = Memberinfo()
                memberinfo.username = request.POST.get('userName')
                memberinfo.password = request.POST.get('inputPassword')
                memberinfo.email = request.POST.get('inputEmail')
                memberinfo.firstname = request.POST.get('firstName')
                memberinfo.lastname = request.POST.get('lastName')
                memberinfo.phonenumber = request.POST.get('phone')
                memberinfo.signupdate = datetime.datetime.now()
                memberinfo.save()
                # messages.add_message(request, messages.INFO, 'Sign up success')
                return redirect('memberSignIn')

    return render(request, 'hms/signUp2.html')


def memberLogout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('landingPage')

def landingPage(request):
    form = request.POST
    
    if len(request.POST) != 0:
        #time = datetime.time(12,0,0)
        CheckInDate = request.POST.get('Check In')
        print(CheckInDate)
        x = dt.strptime(str(CheckInDate),'%Y-%m-%d')
        print(x)
        #CheckInDate = CheckInDate.strftime("%Y-%m-%d")
        CheckOutDate = request.POST.get('Check Out')
        #CheckOutDate =  CheckOutDate.strftime("%Y-%m-%d")
        NumRoom = request.POST.get('Room')
        NumGuest = request.POST.get('Guest')
        
        
        if ((CheckInDate < CheckOutDate) and (CheckInDate >= date.today().strftime('%Y-%m-%d')) and (CheckOutDate != CheckInDate)):
            list1 = []
            MaxType = ['one','two','three']
            dict1 = {}
            count = 0
            for i in Roomtype.objects.all():
                cursor = connection.cursor() 
                cursor.execute('SELECT COUNT(*) AS %s FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s  AND RoomType = %s;',[i.roomtype,CheckOutDate,CheckInDate,i.roomtype])
                #print(dictfetchall(cursor))

                cursor = connection.cursor() 
                cursor.execute('SELECT ABS(COUNT(*) - (SELECT COUNT(*) FROM Room WHERE roomtype = %s)) AS %s FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s  AND RoomType = %s;',[i.roomtype,MaxType[count],CheckOutDate,CheckInDate,i.roomtype])
                list2 = dictfetchall(cursor)
                print(list2[0])
                dict1.update(list2[0])
                count = count + 1

            print(dict1)   

            # session
            request.session['CheckInDate'] = CheckInDate
            request.session['CheckOutDate'] = CheckOutDate
            request.session['Room'] = NumRoom
            request.session['Guest'] = NumGuest
            return render(request,'hms/index2.html',dict1)
                
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Date Range')
    return render(request, 'hms/index.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def bookSuccess(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request,'hms/endpage.html')


######### Hotel Management Part ##########

#### Staff  ####
def staffInfo(request):
    i = Staffinfo.objects.all()
    myFilter = staffinfoFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'staffInfo': i,'myFilter' : myFilter}
    return render(request,'hms/Staff/staffInfo.html',content)

def staffFormPage(request,staffid = 0):
    if staffid == 0: # create
        form = staffForm()
    elif staffid != 0: # update
        staff = Staffinfo.objects.get(staffid=staffid)
        form = staffForm(instance = staff)

    content = {'form' : form}
    if request.method == "POST":
        if staffid == 0: # create
            form = staffForm(request.POST)
        elif staffid != 0: # update
            staff = Staffinfo.objects.get(staffid = staffid)
            form = staffForm(request.POST,instance = staff)

        if form.is_valid():
            form.save()
            return redirect('staffInfo')
    return render(request,'hms/Staff/staffForm.html',content)

def staffProfile(request,staffid):
    staff = Staffinfo.objects.get(staffid=staffid)
    return render(request,'hms/Staff/staffProfile.html',{'staff':staff})

def staffDelete(request,staffid):
    staff = Staffinfo.objects.get(staffid=staffid)
    staff.delete() 
    return redirect('staffInfo')


#### member  ####
def memberInfo(request):
    i = Memberinfo.objects.all()
    myFilter = memberinfoFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'memberInfo': i,'myFilter' : myFilter}
    return render(request,'hms/Member/memberInfo.html',content)

def memberFormPage(request,userid = 0):
    if userid == 0: # create
        form = memberForm()
    elif userid != 0: # update
        member = Memberinfo.objects.get(userid=userid)
        form = memberForm(instance = member)
    
    content = {'form' : form}
    if request.method == "POST":
        if userid == 0: # create
            form = memberForm(request.POST)
        elif userid != 0: # update
            member = Memberinfo.objects.get(userid = userid)
            form = memberForm(request.POST,instance = member)

        if form.is_valid():
            form.save()
            return redirect('memberInfo')
    return render(request,'hms/Member/memberForm.html',content)

def memberProfile(request,userid):
    member = Memberinfo.objects.get(userid=userid)
    return render(request,'hms/member/memberProfile.html',{'member':member})

def memberDelete(request,userid):
    member = Memberinfo.objects.get(userid=userid)
    member.delete() 
    return redirect('memberInfo')


#### guest  ####
def guestInfo(request):
    i = Guestinfo.objects.all()
    myFilter = guestinfoFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'guestInfo': i,'myFilter' : myFilter}
    return render(request,'hms/Guest/guestInfo.html',content)

def guestFormPage(request,guestid = 0):
    if guestid == 0: # create
        form = guestForm()
    elif guestid != 0: # update
        guest = Guestinfo.objects.get(guestid=guestid)
        form = guestForm(instance = guest)
    
    content = {'form' : form}
    if request.method == "POST":
        if guestid == 0: # create
            form = guestForm(request.POST)
        elif guestid != 0: # update
            guest = Guestinfo.objects.get(guestid = guestid)
            form = guestForm(request.POST,instance = guest)

        if form.is_valid():
            form.save()
            return redirect('guestInfo')
    return render(request,'hms/Guest/guestForm.html',content)

def guestProfile(request,guestid):
    guest = Guestinfo.objects.get(guestid=guestid)
    return render(request,'hms/Guest/guestProfile.html',{'guest':guest})

def guestDelete(request,guestid):
    guest = Guestinfo.objects.get(guestid=guestid)
    guest.delete() 
    return redirect('guestInfo')   

#### discount  ####
def discountInfo(request):
    i = Discount.objects.all()
    myFilter = discountFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'discount': i,'myFilter':myFilter}
    return render(request,'hms/Discount/discountInfo.html',content)

def discountFormPage(request,discountcode = 'None'):
    if discountcode == 'None': # create
        form = discountForm()
    elif discountcode != 'None': # update
        discount = Discount.objects.get(discountcode=discountcode)
        form = discountFormUpdate(instance = discount)
    
    content = {'form' : form}
    if request.method == "POST":
        if discountcode == 'None': # create
            form = discountForm(request.POST)
        elif discountcode != 'None': # update
            discount = Discount.objects.get(discountcode = discountcode)
            form = discountFormUpdate(request.POST,instance = discount)

        if form.is_valid():
            form.save()
            return redirect('discountInfo')
    if discountcode == 'None':
        return render(request,'hms/Discount/discountForm.html',content)
    elif discountcode != 'None':
        content = {'form' : form,'d': discountcode}
        return render(request,'hms/Discount/discountFormUpdate.html',content)


def discountEachInfo(request,discountcode):
    discount = Discount.objects.get(discountcode=discountcode)
    return render(request,'hms/Discount/discountProfile.html',{'discount':discount})

def discountDelete(request,discountcode):
    discount = Discount.objects.get(discountcode=discountcode)
    discount.delete() 
    return redirect('discountInfo')   


#### roomtype  ####
def roomtypeInfo(request):
    i = Roomtype.objects.all()
    myFilter = roomtypeFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'roomtype': i,'myFilter':myFilter}
    return render(request,'hms/Roomtype/roomtypeInfo.html',content)

def roomtypeFormPage(request,roomtypeID = 'None'):
    if roomtypeID == 'None': # create
        form = roomtypeForm()
    elif roomtypeID != 'None': # update
        roomtype = Roomtype.objects.get(roomtype=roomtypeID)
        form = roomtypeFormUpdate(instance = roomtype)
    
    content = {'form' : form}
    if request.method == "POST":
        if roomtypeID == 'None': # create
            form = roomtypeForm(request.POST)
        elif roomtypeID != 'None': # update
            roomtype = Roomtype.objects.get(roomtype = roomtypeID)
            form = roomtypeFormUpdate(request.POST,instance = roomtype)

        if form.is_valid():
            form.save()
            return redirect('roomtypeInfo')
    if roomtypeID == 'None':
        return render(request,'hms/Roomtype/roomtypeForm.html',content)
    elif roomtypeID != 'None':
        content = {'form' : form,'rt': roomtype}
        return render(request,'hms/Roomtype/roomtypeFormUpdate.html',content)


def roomtypeEachInfo(request,roomtypeID):
    roomtype = Roomtype.objects.get(roomtype=roomtypeID)
    return render(request,'hms/Roomtype/roomtypeProfile.html',{'roomtype':roomtype})

def roomtypeDelete(request,roomtypeID):
    roomtype = Roomtype.objects.get(roomtype=roomtypeID)
    roomtype.delete() 
    return redirect('roomtypeInfo')  


#### Room  ####
def roomInfo(request):
    i = Room.objects.all()
    j = Roomtype.objects.all()
    myFilter = roomFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'room': i,'type' : j,'myFilter':myFilter}
    return render(request,'hms/Room/roomInfo.html',content)

def roomFormPage(request,roomid = 0):
    if roomid == 0: # create
        form = roomForm()
    elif roomid != 0: # update
        room = Room.objects.get(roomid=roomid)
        form = roomForm(instance = room)
    
    content = {'form' : form}
    if request.method == "POST":
        if roomid == 0: # create
            form = roomForm(request.POST)
        elif roomid != 0: # update
            room = Room.objects.get(roomid = roomid)
            form = roomForm(request.POST,instance = room)

        if form.is_valid():
            form.save()
            return redirect('roomInfo')
    return render(request,'hms/Room/roomForm.html',content)

def roomEachInfo(request,roomid):
    room = Room.objects.get(roomid=roomid)
    return render(request,'hms/Room/roomProfile.html',{'room':room})

def roomDelete(request,roomid):
    room = Room.objects.get(roomid=roomid)
    room.delete() 
    return redirect('roomInfo')    


#### service  ####
def serviceInfo(request):
    i = Service.objects.all()
    myFilter = serviceFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'service': i,'myFilter' : myFilter}
    return render(request,'hms/ServiceP/serviceInfo.html',content)

def serviceFormPage(request,serviceid = 'None'):
    if serviceid == 'None': # create
        form = serviceForm()
    elif serviceid != 'None': # update
        service = Service.objects.get(serviceid=serviceid)
        form = serviceForm(instance = service)
    
    content = {'form' : form}
    if request.method == "POST":
        if serviceid == 'None': # create
            form = serviceForm(request.POST)
        elif serviceid != 'None': # update
            service = Service.objects.get(serviceid = serviceid)
            form = serviceForm(request.POST,instance = service)

        if form.is_valid():
            form.save()
            return redirect('serviceInfo')
    return render(request,'hms/ServiceP/serviceForm.html',content)

def serviceEachInfo(request,serviceid):
    service = Service.objects.get(serviceid=serviceid)
    return render(request,'hms/ServiceP/serviceProfile.html',{'service':service})

def serviceDelete(request,serviceid):
    service = Service.objects.get(serviceid=serviceid)
    service.delete() 
    return redirect('serviceInfo')    
 

## booking
def bookingInfo(request):
    i = Booking.objects.all().order_by('-bookingid')
    myFilter = bookingFilters(request.GET,queryset=i)
    i = myFilter.qs
    
    content = {'booking': i,'myFilter':myFilter}
    return render(request,'hms/Booking/bookingInfo.html',content)

def bookingFormPage(request,bookingid = 0):
    if bookingid == 0: # create
        form = bookingForm2()
    elif bookingid != 0: # update
        booking = Booking.objects.get(bookingid=bookingid)
        form = bookingForm(instance = booking)
    
    content = {'form' : form}
    if request.method == "POST":
        if bookingid == 0: # create
            form = bookingForm2(request.POST)
            if form.is_valid():
                extra = form.save(commit=False)
                extra.totalprice = 0
                extra.totaldiscount = 0
                extra.bookingstatus = 'Booked'
                extra.save()
                return redirect('bookingInfo')
        elif bookingid != 0: # update
            booking = Booking.objects.get(bookingid = bookingid)
            form = bookingForm(request.POST,instance = booking)
            if form.is_valid():
                form.save()
                return redirect('bookingInfo')

    if bookingid == 0: # create
        return render(request,'hms/Booking/bookingForm2.html',content)
    elif bookingid != 0: # update
        return render(request,'hms/Booking/bookingForm.html',content)
    

def bookingEachInfo(request,bookingid):
    booking = Booking.objects.get(bookingid=bookingid)
    request.session["bookingid"] = bookingid

    
    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s',[bookingid])
    roombooking = dictfetchall(cursor)
    print(roombooking)

    if booking.discountcode != None and booking.totaldiscount == 0:
        print(booking.discountcode.discountpercent)
        oldprice = booking.totalprice
        totaldis = oldprice * (booking.discountcode.discountpercent / 100)
        booking.totalprice = oldprice - totaldis
        booking.totaldiscount = totaldis

    return render(request,'hms/Booking/bookingProfile.html',{'booking':booking ,'roombooking': roombooking})

def bookingDelete(request,bookingid):
    booking = Booking.objects.get(bookingid=bookingid)
    booking.delete() 
    return redirect('bookingInfo')    



# Test Room booking
def roombookingFormPage(request,bookingid):
    # find booking
    booking = Booking.objects.get(bookingid=bookingid)
    cursor = connection.cursor() 
    cursor.execute('SELECT R.RoomID FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s;',[booking.checkoutdate,booking.checkindate])
    dataDict = dictfetchall(cursor)
    bookRoom = []
    for i in dataDict:
        bookRoom.append(i['RoomID'])

    print(bookRoom)


     # create
    form = roombookingForm() 
    #elif bookingid != 0: # update
    #    room = Room.objects.get(bookingid=bookingid)
    #    form = roombookingForm(instance = room)
    
    content = {'form' : form,'bookRoom' : bookRoom,'booking' : booking,'br1' : len(bookRoom)}
    if request.method == "POST":
         # create
        form = roombookingForm(request.POST)
        #elif bookingid != 0: # update
        #    room = Room.objects.get(bookingid = bookingid)
        #    form = roomForm(request.POST,instance = room)

        if form.is_valid():
            room = form.cleaned_data['roomid']
            guestamount = form.cleaned_data['guestamount']
            additionbed = form.cleaned_data['additionbed']
            breakfast = form.cleaned_data['breakfast']
            guestid = form.cleaned_data['guestid']

            # For adding price
            cin = booking.checkindate
            cin2 = dt.strptime(str(cin),'%Y-%m-%d')
            cout = booking.checkoutdate
            cout2 = dt.strptime(str(cout),'%Y-%m-%d')
            day = (cout2 - cin2).days

            roomtype = room.roomtype
            roomprice = 0
            if roomtype.roomtype == 'Standard Double Room':
                roomprice = 1500
            elif roomtype.roomtype == 'Standard Twin Room':
                roomprice = 1800
            elif roomtype.roomtype == 'Super Deluxe Room':   
                roomprice = 2300

            totalprice = (roomprice * day) + (500 * additionbed) + (100 * breakfast)
            oldprice = booking.totalprice
            
            if room.roomid not in bookRoom:
                print(room)
                print(booking)
                print(guestamount)
                print(additionbed)
                print(guestid)

                roombookingDB = Roombooking()
                roombookingDB.bookingid = booking
                roombookingDB.roomid = room
                roombookingDB.guestamount = guestamount
                roombookingDB.additionbed = additionbed
                roombookingDB.guestid = guestid
                roombookingDB.breakfast = breakfast
                roombookingDB.save()

                booking.totalprice = oldprice + totalprice
                booking.save()                

                #count delay fix
                cursor = connection.cursor()
                cursor.execute('SELECT SUM(rb.GuestAmount) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum = dictfetchall(cursor)
                booking.totalguest = Newsum[0]['newS']

                cursor = connection.cursor() 
                cursor.execute('SELECT SUM(rb.BreakFast) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum2 = dictfetchall(cursor)
                booking.totalbreakfast = Newsum2[0]['newS']
                booking.save()

                cursor = connection.cursor() 
                cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s',[booking.bookingid])
                roombooking = dictfetchall(cursor)
                return render(request,'hms/Booking/bookingProfile.html',{'booking':booking ,'roombooking': roombooking})
            
    return render(request,'hms/Roombooking/roombookingForm.html',content)


def roombookingUpdateFormPage(request,bookingid,roomid):
    # find booking
    booking = Booking.objects.get(bookingid=bookingid)
    cursor = connection.cursor() 
    cursor.execute('SELECT R.RoomID FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate < %s  AND CheckOutDate > %s;',[booking.checkoutdate,booking.checkindate])
    dataDict = dictfetchall(cursor)
    bookRoom = []
    for i in dataDict:
        bookRoom.append(i['RoomID'])

    print(bookRoom)

    # Prefill
    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s AND RoomID = %s',[bookingid,roomid])
    rb2 = dictfetchall(cursor)
    print(rb2)

    if rb2[0]['GuestID'] != None:
        guestOb = Guestinfo.objects.get(guestid=rb2[0]['GuestID'])
    else:
        guestOb = None

    roomOb = Room.objects.get(roomid=roomid)
    
    form = roombookingForm(initial={'roomid': roomOb,'guestamount':rb2[0]['GuestAmount'],'guestid':guestOb,'additionbed':rb2[0]['AdditionBed'],'breakfast':rb2[0]['BreakFast']}) 
    roomtypeO = roomOb.roomtype
    roomprice2 = 0
    if roomtypeO.roomtype == 'Standard Double Room':
        roomprice2 = 1500
    elif roomtypeO.roomtype == 'Standard Twin Room':
        roomprice2 = 1800
    elif roomtypeO.roomtype == 'Super Deluxe Room':   
        roomprice2 = 2300
                
    
    #elif bookingid != 0: # update
    #    room = Room.objects.get(bookingid=bookingid)
    #    form = roombookingForm(instance = room)
    
    content = {'form' : form,'bookRoom' : bookRoom,'booking' : booking}
    if request.method == "POST":
         # create
        form = roombookingForm(request.POST)
        #elif bookingid != 0: # update
        #    room = Room.objects.get(bookingid = bookingid)
        #    form = roomForm(request.POST,instance = room)

        if form.is_valid():
            room = form.cleaned_data['roomid']
            guestamount = form.cleaned_data['guestamount']
            additionbed = form.cleaned_data['additionbed']
            breakfast = form.cleaned_data['breakfast']
            guestid = form.cleaned_data['guestid']

            # For adding price
            cin = booking.checkindate
            cin2 = dt.strptime(str(cin),'%Y-%m-%d')
            cout = booking.checkoutdate
            cout2 = dt.strptime(str(cout),'%Y-%m-%d')
            day = (cout2 - cin2).days

            roomtype = room.roomtype
            roomprice = 0
            if roomtype.roomtype == 'Standard Double Room':
                roomprice = 1500
            elif roomtype.roomtype == 'Standard Twin Room':
                roomprice = 1800
            elif roomtype.roomtype == 'Super Deluxe Room':   
                roomprice = 2300

            totalprice = (roomprice * day) + (500 * additionbed) + (100 * breakfast)
            totalprice2 = (roomprice2 * day) + (500 * rb2[0]['AdditionBed']) + (100 * rb2[0]['BreakFast'])
            oldprice = booking.totalprice
            
            
            if room.roomid not in bookRoom:
                print(room)
                print(booking)
                print(guestamount)
                print(additionbed)
                print(guestid)

                roombookingDB = Roombooking()
                roombookingDB.bookingid = booking
                roombookingDB.roomid = room
                roombookingDB.guestamount = guestamount
                roombookingDB.additionbed = additionbed
                roombookingDB.guestid = guestid
                roombookingDB.breakfast = breakfast
                roombookingDB.save()

                booking.totalprice = oldprice + totalprice
                booking.save()

                #count delay fix
                cursor = connection.cursor()
                cursor.execute('SELECT SUM(rb.GuestAmount) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum = dictfetchall(cursor)
                booking.totalguest = Newsum[0]['newS']

                cursor = connection.cursor() 
                cursor.execute('SELECT SUM(rb.BreakFast) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum2 = dictfetchall(cursor)
                booking.totalbreakfast = Newsum2[0]['newS']

                cursor = connection.cursor() 
                cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s',[booking.bookingid])
                roombooking = dictfetchall(cursor)
                return render(request,'hms/Booking/bookingProfile.html',{'booking':booking ,'roombooking': roombooking})

            elif room.roomid in bookRoom:
                cursor = connection.cursor() 
                cursor.execute('DELETE FROM RoomBooking WHERE BookingID = %s AND RoomID = %s',[bookingid,roomid])

                roombookingDB = Roombooking()
                roombookingDB.bookingid = booking
                roombookingDB.roomid = room
                roombookingDB.guestamount = guestamount
                roombookingDB.additionbed = additionbed
                roombookingDB.guestid = guestid
                roombookingDB.breakfast = breakfast
                roombookingDB.save()

                booking.totalprice = oldprice - totalprice2 + totalprice
                booking.save()
    
                cursor = connection.cursor() 
                cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s',[booking.bookingid])
                roombooking = dictfetchall(cursor)

                #count delay fix
                cursor = connection.cursor()
                cursor.execute('SELECT SUM(rb.GuestAmount) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum = dictfetchall(cursor)
                booking.totalguest = Newsum[0]['newS']

                cursor = connection.cursor() 
                cursor.execute('SELECT SUM(rb.BreakFast) AS newS FROM Booking b JOIN RoomBooking rb ON b.BookingID = rb.BookingID WHERE b.BookingID = %s',[bookingid])
                Newsum2 = dictfetchall(cursor)
                booking.totalbreakfast = Newsum2[0]['newS']

                booking.save()

                return render(request,'hms/Booking/bookingProfile.html',{'booking':booking ,'roombooking': roombooking})
            
    return render(request,'hms/Roombooking/roombookingForm.html',content)
    
def roombookingDeleteFormPage(request,bookingid,roomid):
    booking = Booking.objects.get(bookingid=bookingid)
    room = Room.objects.get(roomid=roomid)
    cursor = connection.cursor() 
    cursor.execute('SELECT * FROM RoomBooking WHERE BookingID = %s',[booking.bookingid])
    roombooking = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT AdditionBed FROM RoomBooking WHERE BookingID = %s AND RoomID = %s',[booking.bookingid,roomid])
    AdditionBed = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('DELETE FROM RoomBooking WHERE BookingID = %s AND RoomID = %s',[bookingid,roomid])

    # calculate old price
    cin = booking.checkindate
    cin2 = dt.strptime(str(cin),'%Y-%m-%d')
    cout = booking.checkoutdate
    cout2 = dt.strptime(str(cout),'%Y-%m-%d')
    day = (cout2 - cin2).days

    roomtype = room.roomtype
    roomprice = 0
    if roomtype.roomtype == 'Standard Double Room':
        roomprice = 1500
    elif roomtype.roomtype == 'Standard Twin Room':
        roomprice = 1800
    elif roomtype.roomtype == 'Super Deluxe Room':   
        roomprice = 2300

    totalprice = (roomprice * day) + (500 * AdditionBed[0]['AdditionBed'])
    oldprice = booking.totalprice

    booking.totalprice = oldprice - totalprice
    booking.save()

    return render(request,'hms/Booking/bookingProfile.html',{'booking':booking ,'roombooking': roombooking})


#### Payment  ####
def paymentInfo(request):
    i = Paymentinfo.objects.all().order_by('-paymentid')
    myFilter = paymentFilters(request.GET,queryset=i)
    i = myFilter.qs
    content = {'payment': i,'myFilter':myFilter}
    return render(request,'hms/Payment/paymentInfo.html',content)

def paymentFormPage(request,paymentid = 0):
    if paymentid == 0: # create
        form = paymentForm(initial={'paymentdate' : dt.today().strftime('%Y-%m-%d %H:%M:%S')})
    elif paymentid != 0: # update
        payment = Paymentinfo.objects.get(paymentid=paymentid)
        form = paymentForm(instance = payment)
    
    content = {'form' : form}
    if request.method == "POST":
        if paymentid == 0: # create
            form = paymentForm(request.POST)
        elif paymentid != 0: # update
            payment = Paymentinfo.objects.get(paymentid = paymentid)
            form = paymentForm(request.POST,instance = payment)

        if form.is_valid():
            form.save()
            return redirect('paymentInfo')
    return render(request,'hms/Payment/paymentForm.html',content)

def paymentEachInfo(request,paymentid):
    payment = Paymentinfo.objects.get(paymentid=paymentid)
    return render(request,'hms/Payment/paymentProfile.html',{'payment':payment})

def paymentDelete(request,paymentid):
    payment = Paymentinfo.objects.get(paymentid=paymentid)
    payment.delete() 
    return redirect('paymentInfo')    


# Staff login
def staffSignIn(request):
    form = request.POST
    signInEmail = request.POST.get('email')
    signInPass = request.POST.get('password')

    if len(request.POST) != 0:
        for i in Staffinfo.objects.all():
            if(i.email == signInEmail and i.password == signInPass) or (i.username == signInEmail and i.password == signInPass):
                request.session['staff_id'] = i.staffid
                return redirect('management')
                break
        
        messages.add_message(request, messages.INFO, 'Incorrect Username or password')

    return render(request, 'hms/signInS.html')

def management(request):
    dateinput = date.today().strftime('%Y-%m-%d')
    cursor = connection.cursor() 
    cursor.execute('SELECT b.BookingID,b.CheckInDate,b.CheckOutDate,m.FirstName,m.LastName FROM Booking b,MemberInfo m WHERE b.userid = m.userid AND b.CheckInDate = %s;',[dateinput])
    cin = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT b.BookingID,b.CheckInDate,b.CheckOutDate,m.FirstName,m.LastName FROM Booking b,MemberInfo m WHERE b.userid = m.userid AND b.CheckOutDate = %s;',[dateinput])
    cout = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT b.BookingID,rb.RoomID,b.CheckInDate,b.CheckOutDate,r.RoomType FROM RoomBooking rb, Booking b,Room r WHERE rb.BookingID = b.BookingID AND rb.RoomID = r.RoomID AND b.BookingStatus != "Check Out" AND b.CheckInDate <= %s AND b.CheckOutDate >= %s',[dateinput,dateinput])
    roomCheck = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT Firstname, Lastname, COUNT(s.UserID) AS NumberofBooking FROM MemberInfo s, Booking p  WHERE s.UserID = p.UserID GROUP BY s.UserID ORDER BY NumberofBooking DESC ;')
    first = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT RoomType, COUNT(RoomType) AS Rcount FROM room r, roombooking rb, booking b WHERE r.RoomID = rb.RoomID AND b.BookingID = rb.BookingID AND CheckInDate LIKE "2021%" GROUP BY RoomType;')
    second = dictfetchall(cursor)


    cursor = connection.cursor() 
    cursor.execute('SELECT Position, SUM(Gender = "Male") AS Male, SUM(Gender = "Female") AS Female FROM StaffInfo GROUP BY Position')
    third = dictfetchall(cursor)
    
    content = {'cin' : cin,'cout' : cout,'roomCheck' : roomCheck,'first' : first,'second':second,'third':third}

    print(cin)

    return render(request, 'hms/management.html',content)


def staffLogout(request):
    try:
        del request.session['staff_id']
    except KeyError:
        pass
    return redirect('staffSignIn')

def Analysis(request):
    cursor = connection.cursor() 
    cursor.execute('SELECT Firstname, Lastname, COUNT(s.UserID) AS NumberofBooking FROM MemberInfo s, Booking p  WHERE s.UserID = p.UserID GROUP BY s.UserID ORDER BY s.UserID;')
    first = dictfetchall(cursor)

    cursor = connection.cursor() 
    cursor.execute('SELECT RoomType, COUNT(RoomType) AS Rcount FROM room r, roombooking rb, booking b WHERE r.RoomID = rb.RoomID AND b.BookingID = rb.BookingID AND CheckInDate LIKE "2021%" GROUP BY RoomType;')
    second = dictfetchall(cursor)


    cursor = connection.cursor() 
    cursor.execute('SELECT Position, SUM(Gender = "Male") AS Male, SUM(Gender = "Female") AS Female FROM StaffInfo GROUP BY Position')
    third = dictfetchall(cursor)
    
    content = {'first' : first,'second':second,'third':third}
    return render(request, 'hms/Analysis.html',content)






    





#def memberSignIn(request):
#    form = request.POST
#    signInEmail = request.POST.get('email')
#    signInPass = request.POST.get('password')

#    if len(request.POST) != 0:
#        for i in Memberinfo.objects.all():
#            if(i.email == signInEmail and i.password == signInPass) or (i.username == signInEmail and i.password == signInPass):
#                
#                return redirect('bookingLanding',i.userid)
#               break
        
#        messages.add_message(request, messages.INFO, 'Incorrect Username or password')

#    return render(request, 'hms/signIn.html')



 #   cursor = connection.cursor()
 #   cursor.execute("SELECT COUNT(*) AS Booked FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate >= '2021-4-18 05:00:00'  AND CheckOutDate <= '2021-4-20 12:00:00'  AND RoomType = 'Standard Double Room';")
 #   print(dictfetchall(cursor))

 #   cursor2 = connection.cursor()
 #   cursor2.execute("SELECT COUNT(*) AS Booked FROM RoomBooking as RB JOIN Booking as B ON RB.BookingID = B.BookingID JOIN Room as R ON RB.RoomID = R.RoomID WHERE CheckInDate >= '2021-4-20 05:00:00'  AND CheckOutDate <= '2021-4-22 12:00:00'  AND RoomType = 'Standard Twin Room';")
 #   print(dictfetchall(cursor2))