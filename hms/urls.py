from django.urls import path,include
from . import views

urlpatterns = [
    path('memberSignIn/', views.memberSignIn,name='memberSignIn'),
    path('bookingLanding/',views.bookingLanding,name='bookingLanding'),
    path('memberSignUp/',views.memberSignUp,name='memberSignUp'),
    path('memberLogout/', views.memberLogout, name="memberLogout"),
    path('reserveRoom/<str:rType>/',views.reserveRoom,name = 'reserveRoom'),
    path('checkout/', views.checkout, name="checkout"),
    path('', views.landingPage, name="landingPage"),

    path('management/', views.staffSignIn,name='staffSignIn'),
    path('management/bashboard', views.management,name='management'),
    path('staffLogout/', views.staffLogout, name="staffLogout"),

    path('bookSuccess/', views.bookSuccess, name="bookSuccess"),
    path('management/analysis', views.Analysis, name="Analysis"),


    #staffInfo
    path('management/staff/', views.staffInfo, name="staffInfo"),
    path('management/staff/staffProfile/<str:staffid>/', views.staffProfile, name="staffProfile"),
    path('management/staff/staffForm/', views.staffFormPage, name="staffFormPage"),
    path('management/staff/staffUpdate/<int:staffid>/', views.staffFormPage, name="staffUpdate"),
    path('management/staff/staffDelete/<int:staffid>/', views.staffDelete, name="staffDelete"),

    #memberInfo
    path('management/member/', views.memberInfo, name="memberInfo"),
    path('management/member/memberForm/', views.memberFormPage, name="memberFormPage"),
    path('management/member/memberProfile/<str:userid>/', views.memberProfile, name="memberProfile"),
    path('management/member/memberUpdate/<int:userid>/', views.memberFormPage, name="memberUpdate"),
    path('management/member/memberDelete/<int:userid>/', views.memberDelete, name="memberDelete"),

    #guestInfo
    path('management/guest/', views.guestInfo, name="guestInfo"),
    path('management/guest/guestForm/', views.guestFormPage, name="guestFormPage"),
    path('management/guest/guestProfile/<str:guestid>/', views.guestProfile, name="guestProfile"),
    path('management/guest/guestUpdate/<int:guestid>/', views.guestFormPage, name="guestUpdate"),
    path('management/guest/guestDelete/<int:guestid>/', views.guestDelete, name="guestDelete"),

    #Discount
    path('management/discountcode/', views.discountInfo, name="discountInfo"),
    path('management/discountcode/discountForm/', views.discountFormPage, name="discountFormPage"),
    path('management/discountcode/discountInfo/<str:discountcode>/', views.discountEachInfo, name="discountEachInfo"),
    path('management/discountcode/discountUpdate/<str:discountcode>/', views.discountFormPage, name="discountUpdate"),
    path('management/discountcode/discountDelete/<str:discountcode>/', views.discountDelete, name="discountDelete"),

    #Roomtype
    path('management/roomtype/', views.roomtypeInfo, name="roomtypeInfo"),
    path('management/roomtype/roomtypeForm/', views.roomtypeFormPage, name="roomtypeFormPage"),
    path('management/roomtype/roomtypeInfo/<str:roomtypeID>/', views.roomtypeEachInfo, name="roomtypeEachInfo"),
    path('management/roomtype/roomtypeUpdate/<str:roomtypeID>/', views.roomtypeFormPage, name="roomtypeUpdate"),
    path('management/roomtype/roomtypeDelete/<str:roomtypeID>/', views.roomtypeDelete, name="roomtypeDelete"),

    #Room
    path('management/room/', views.roomInfo, name="roomInfo"),
    path('management/room/roomForm/', views.roomFormPage, name="roomFormPage"),
    path('management/room/roomInfo/<str:roomid>/', views.roomEachInfo, name="roomEachInfo"),
    path('management/room/roomUpdate/<int:roomid>/', views.roomFormPage, name="roomUpdate"),
    path('management/room/roomDelete/<int:roomid>/', views.roomDelete, name="roomDelete"),

    #service
    path('management/service/', views.serviceInfo, name="serviceInfo"),
    path('management/service/serviceForm/', views.serviceFormPage, name="serviceFormPage"),
    path('management/service/serviceInfo/<str:serviceid>/', views.serviceEachInfo, name="serviceEachInfo"),
    path('management/service/serviceUpdate/<str:serviceid>/', views.serviceFormPage, name="serviceUpdate"),
    path('management/service/serviceDelete/<str:serviceid>/', views.serviceDelete, name="serviceDelete"),

    #booking
    path('management/booking/', views.bookingInfo, name="bookingInfo"),
    path('management/booking/bookingForm/', views.bookingFormPage, name="bookingFormPage"),
    path('management/booking/bookingInfo/<str:bookingid>/', views.bookingEachInfo, name="bookingEachInfo"),
    path('management/booking/bookingUpdate/<int:bookingid>/', views.bookingFormPage, name="bookingUpdate"),
    path('management/booking/bookingDelete/<int:bookingid>/', views.bookingDelete, name="bookingDelete"),

    #RoomBooking
    path('management/roombooking/roombookingForm/<int:bookingid>/', views.roombookingFormPage, name="roombookingFormPage"),
    path('management/roombooking/roombookingForm/<int:bookingid>/<int:roomid>/', views.roombookingUpdateFormPage, name="roombookingUpdateFormPage"),
    path('management/roombooking/roombookingDeleteForm/<int:bookingid>/<int:roomid>/', views.roombookingDeleteFormPage, name="roombookingDeleteFormPage"),

    #payment
    path('management/payment/', views.paymentInfo, name="paymentInfo"),
    path('management/payment/paymentForm/', views.paymentFormPage, name="paymentFormPage"),
    path('management/payment/paymentInfo/<str:paymentid>/', views.paymentEachInfo, name="paymentEachInfo"),
    path('management/payment/paymentUpdate/<int:paymentid>/', views.paymentFormPage, name="paymentUpdate"),
    path('management/payment/paymentDelete/<int:paymentid>/', views.paymentDelete, name="paymentDelete"),
]
