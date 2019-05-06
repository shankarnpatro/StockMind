from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.restapi.views import schema_view
from apps.restapi.views.History import EquityBuyHistoryListAPIView, OptionBuyCEHistoryListAPIView, \
    OptionBuyPEHistoryListAPIView
from apps.restapi.views.equity import BuyListAPIView, BuyCreateAPIView, BuyUpdateAPIView, BuyDeleteAPIView, \
    SellListAPIView, SellCreateAPIView, SellUpdateAPIView, SellDeleteAPIView
from apps.restapi.views.gallery import ImageListAPIView, ImageUploadAPIView, ImageUpdateAPIView, \
    ImageDeleteAPIView, VideoListAPIView, VideoUploadAPIView, VideoUpdateAPIView
from apps.restapi.views.option import OptionAPIView, OptionCreateAPIView, OptionUpdateAPIView, OptionDeleteAPIView
from apps.restapi.views.users import UserCreateAPIView, UserLoginAPIView, UpdateUserView, UserProfileImageView, \
    ChangePasswordView, EmailActivationView

urlpatterns = [
    # Django REST Framework JWT Authentication
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    # Swagger API Documentation
    url(r'^docs/$', schema_view.schema_view, name="schema_view"),

    # User Management:
    # """Register             : api/users/register/""",
    # """Method: POST, BODY: {KEY: first_name, last_name, phone, email, password}""",
    url(r'^users/register/$', UserCreateAPIView.as_view(), name='user-register'),
    # """Email Activation     : api/users/activate/:id/:token/""",
    url(r'^users/activate/(?P<pk>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z\-]+)/$',
        EmailActivationView.as_view(), name='activate'),
    # """Login             : api/users/login/""",
    # """Method: POST, BODY: {KEY: phone, password}""",
    url(r'^users/login/$', UserLoginAPIView.as_view(), name="user-login"),
    # """Update User          : api/users/:id/update""",
    # """" Header KEY: Authorization, VALUE: JWT TOKEN""",
    # """Method: PUT, BODY: {KEY: first_name, last_name}""",
    url(r'^users/(?P<pk>[0-9]+)/update/$', UpdateUserView.as_view(), name='user-update'),
    # """User Profile Image   : api/users/:id/profile_image""",
    # """" Header KEY: Authorization, VALUE: JWT TOKEN""",
    # """Method: PUT, BODY: {KEY: profile_image}""",
    url(r'^users/(?P<pk>[0-9]+)/profile_image/$', UserProfileImageView.as_view(),
        name='user-profile-image-update'),
    # """User Change Password       : api/users/:id/change_password""",
    # """" Header: {KEY:
    # , VALUE: JWT TOKEN}""",
    # """Method: PUT, BODY: {KEY: old_password, password, confirm_password}""",
    url(r'^users/(?P<pk>[0-9]+)/change_password/$', ChangePasswordView.as_view(),
        name='user-change-password'),

    # Gallery Images:
    # """List Images            : api/images/""",
    # """Method: GET """,
    url(r'^images/$', ImageListAPIView.as_view(), name='image-list'),
    # """Upload Images            : api/images/upload/""",
    # """Method: POST, BODY: {KEY: image, desc, tags}""",
    url(r'^images/upload/$', ImageUploadAPIView.as_view(), name='image-upload'),
    # """Update Images          : api/images/:id/update""",
    # """" Header KEY: Authorization, VALUE: JWT TOKEN""",
    url(r'^images/(?P<pk>[0-9]+)/update/$', ImageUpdateAPIView.as_view(), name='image-update'),
    # """delete Images          : api/images/:id/delete""",
    # """Method: delete """,
    url(r'^images/(?P<pk>[0-9]+)/delete/$', ImageDeleteAPIView.as_view(), name='image-delete'),

    # Gallery Videos:
    # """List Videos            : api/videos/""",
    # """Method: GET """,
    url(r'^videos/$', VideoListAPIView.as_view(), name='video-list'),
    # """Upload Videos            : api/videos/upload/""",
    # """Method: POST, BODY: {KEY: image, desc, tags}""",
    url(r'^videos/upload/$', VideoUploadAPIView.as_view(), name='video-upload'),
    # """Update Videos          : api/videos/:id/update""",
    # """Method: PUT, BODY: {KEY: video, desc, tags}""",
    url(r'^videos/(?P<pk>[0-9]+)/update/$', VideoUpdateAPIView.as_view(), name='video-update'),
    # """delete Videos          : api/videos/:id/delete""",
    url(r'^videos/(?P<pk>[0-9]+)/delete/$', ImageDeleteAPIView.as_view(), name='video-delete'),

    # Equity Buy:
    # """List Buy            : api/equity_buys/""",
    # """Method: GET """,
    url(r'^equity_buys/$', BuyListAPIView.as_view(), name='buy-list'),
    # """Create Buy            : api/equity_buys/create/""",
    # """Method: POST, BODY: {KEY: symbol_name, date_time, buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^equity_buys/create/$', BuyCreateAPIView.as_view(), name='buy-create'),
    # """Update Buys          : api/equity_buys/:id/update""",
    # """Method: PUT, BODY: {KEY: symbol_name, date_time, buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^equity_buys/(?P<pk>[0-9]+)/update/$', BuyUpdateAPIView.as_view(), name='buy-update'),
    # """delete Buy          : api/equity_buys/:id/delete""",
    url(r'^equity_buys/(?P<pk>[0-9]+)/delete/$', BuyDeleteAPIView.as_view(), name='buy-delete'),

    # Equity Sell:
    # """List Sells            : api/equity_sells/""",
    # """Method: GET """,
    url(r'^equity_sells/$', SellListAPIView.as_view(), name='sell-list'),
    # """Create Sell            : api/equity_sells/create/""",
    # """Method: POST, BODY: {KEY: symbol_name, date_time, buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^equity_sells/create/$', SellCreateAPIView.as_view(), name='sell-create'),
    # """Update Sells          : api/equity_sells/:id/update""",
    # """Method: PUT, BODY: {KEY: symbol_name, date_time, buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^equity_sells/(?P<pk>[0-9]+)/update/$', SellUpdateAPIView.as_view(), name='buy-update'),
    # """delete Sells          : api/equity_sells/:id/delete""",
    url(r'^equity_sells/(?P<pk>[0-9]+)/delete/$', SellDeleteAPIView.as_view(), name='buy-delete'),

    # Option:
    # """List Sells            : api/sell/""",
    # """Accepted query parmas                  : api/options/?option_type=:option_type"""
    # """option_type = BuyCE/BuyPE"""
    # """Method: GET """,
    url(r'^options/$', OptionAPIView.as_view(), name='option-list'),
    # """Create Sell            : api/options/create/""",
    # """Method: POST, BODY: {KEY: symbol_name, option_type : {BuyCE or BuyPE},date_time,
    # buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^options/create/$', OptionCreateAPIView.as_view(), name='options-create'),
    # """Update Options          : api/options/:id/update""",
    # """Method: PUT, BODY: {KEY: symbol_name, option_type : {BuyCE or BuyPE},
    # date_time, buy_price = eg:200, target_price = eg:400, achievement}""",
    url(r'^options/(?P<pk>[0-9]+)/update/$', OptionUpdateAPIView.as_view(), name='option-update'),
    # """delete Options          : api/options/:id/delete""",
    url(r'^options/(?P<pk>[0-9]+)/delete/$', OptionDeleteAPIView.as_view(), name='option-delete'),

    # History:
    # """Allowed query parameter : api/equity_buys/history/?offset=:offset&limit=:limit"""
    # """offset & limit = int value"""
    url(r'^equity_buys/history/$', EquityBuyHistoryListAPIView.as_view(), name='equity-buy-history'),
    # """Allowed query parameter : api/equity_sells/history/?offset=:offset&limit=:limit"""
    # """offset & limit = int value"""
    url(r'^equity_sells/history/$', EquityBuyHistoryListAPIView.as_view(), name='equity-buy-history'),
    # """Allowed query parameter : api/option_buyces/history/?offset=:offset&limit=:limit"""
    # """offset & limit = int value"""
    url(r'^option_buyces/history/$', OptionBuyCEHistoryListAPIView.as_view(), name='option-buyces-history'),
    # """Allowed query parameter : api/option_buyces/history/?offset=:offset&limit=:limit"""
    # """offset & limit = int value"""
    url(r'^option_buypes/history/$', OptionBuyPEHistoryListAPIView.as_view(), name='option-buypes-history'),

]
