from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, status, pagination, generics, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.db.models import Q
from pricing.models import OfficeBooking, WorkplaceBooking, MeetingRoomsBooking, Places, Comments
from django_filters.rest_framework import DjangoFilterBackend





class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

def trigger_error(request):
    division_by_zero = 1 / 0


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password' , 'is_staff']
        write_only_fields = ('password',)

    def validate_email(self, email):
        if not '@' in email:
            raise ValidationError('@ is not included')
        return email


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['url', 'id', 'name', 'place_type', 'desc', 'free']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['place', 'user_id', 'text', 'date']

      

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = ()

    @action(methods=['GET'], detail=True)
    def comments(self, request, **kwargs):
      place = self.get_object()
      comments = Comments.objects.filter(place=place).values()
      return Response(comments)

    @action(detail=True, methods=['POST'])
    def create_comment(self, request, pk=None):
      serializer = CommentsSerializer(data=request.data)
      if (serializer.is_valid()):
        serializer.save()
        place = self.get_object()
        comments = Comments.objects.filter(place=place).values()
        return Response(comments)
      else:
        return Response(serializer.errors,
          status=status.HTTP_400_BAD_REQUEST)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = ()

    def delete(self, request, pk, format=None):
      comment = self.get_object(pk)
      return Response(1)
    
    def update(self, request, *args, **kwargs):
      instance = self.get_object()
      instance.text = request.data.get("text")
      instance.save()

      place = request.data.get("place")

      serializer = CommentsSerializer(instance, data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_update(serializer)
      comments = Comments.objects.filter(place=place).values()
      return Response(comments)


class BookingsSerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.CharField(source='place.name')
    class Meta:
        model = OfficeBooking
        fields = ['date', 'paid', 'place_name']




class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
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

    filter_backends = [filters.SearchFilter]
    search_fields = ['place__name']



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

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']



router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/places', PlaceViewSet)
router.register(r'api/comments', CommentViewSet)


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('pricing/', include('pricing.urls')),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/bookings', UserBookingsList.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)