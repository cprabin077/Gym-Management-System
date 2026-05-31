from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from subscription.api.serializer import MembershipSerializer, SubscriptionSerializer
from subscription.models import Membership, Subscription

class SubscriptionView(GenericAPIView):
    queryset = Subscription.objects.all() 
    serializer_class = SubscriptionSerializer

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many = True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        data = request.data
        serializer = SubscriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subscription Successfully created"}, 201)
        else:
            return Response(serializer.errors, 422)
        
        
class SubscriptionUpdateAndDelete(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def put(self,request,pk):
        subscription= Subscription.objects.get(id=pk)
        data = request.data
        serializer = SubscriptionSerializer(subscription, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Subscription successfully updated!!"
            })
        else:
            return Response(serializer.errors,422)
        
    def delete(self, request,pk):
        subscription = Subscription.objects.filter(id=pk)
        subscription.delete()
        return Response({
            "message":"Subscription successfully deleted!!"
        },204)
    

@extend_schema(
    request=MembershipSerializer,
    responses=MembershipSerializer,
    tags=["Membership"]
)
class MembershipView(GenericAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def get(self, request):
        data = Membership.objects.all()
        serializer = MembershipSerializer(data, many = True)
        return Response(serializer.data, 200)
        

        


