from rest_framework import (
    views, response, generics,  validators, status, viewsets,
    permissions, authentication
)
from .serializers import CustomerSerializer
from .models import Customer


# class CustomerViewSet(viewsets.ModelViewSet):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
class CustomerUpdateView(views.APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise validators.ValidationError({'message': f'{pk} id user not found'})

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = CustomerSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class CustomerCreateView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        context = {'user': request.user}
        serializer = CustomerSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

"""
# get list qaytsin clientlani
# post create customer
put update customer name or date of birth
"""
