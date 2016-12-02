from django.conf.urls import include, url

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework_nested import routers

from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [

	url(r'^api/v1/', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
]
