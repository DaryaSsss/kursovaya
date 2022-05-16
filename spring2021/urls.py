from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, status, pagination, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.db.models import Q
from pricing.models import OfficeBooking, WorkplaceBooking, MeetingRoomsBooking



class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

def trigger_error(request):
    division_by_zero = 1 / 0


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

    def validate_email(self, email):
        if not '@' in email:
            raise ValidationError('@ is not included')
        return email


class BookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OfficeBooking
        fields = ['date', 'paid']


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User;
        fields = ['email']

    def validate_email(self, email):
        if not '@mail.ru' in email:
            raise ValidationError('@mail.ru is not included')
        return email

class UserBookingsList(generics.ListAPIView):
    serializer_class = BookingsSerializer
    def get_queryset(self):
        user = self.request.user
        return OfficeBooking.objects.filter(user = user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    action_serializers = {
        'set_email': EmailSerializer
    }
    pagination_class = StandardResultsSetPagination

    @action(methods=['GET'], detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-last_login')
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    @action(methods=['DELETE'], detail=False)
    def delete_olegs(self, request, **kwargs):
        olegs = User.objects.filter(Q(username__startswith = 'Oleg'))
        return Response(olegs.delete())


    @action(methods=['POST'], detail=True)
    def set_email(self, request, pk = None):
        user = self.get_object()
        serializer = EmailSerializer(data = request.data)
        if (serializer.is_valid()):
            email = serializer.validated_data['email']
            user.email = email
            user.save()
            return Response({
                'status': 'email changed'
            })
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(MyModelViewSet, self).get_serializer_class()


router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('pricing/', include('pricing.urls')),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/bookings', UserBookingsList.as_view())
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)