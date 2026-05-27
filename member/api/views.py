from member.api.serializer import MemberSerializer
from member.models import Member
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Get member list
@api_view(['GET'])
def memberlist(request):
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

# Create member
@api_view(['POST'])
def membercreate(request):
    post_data = request.data
    serializer = MemberSerializer(data=post_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member successfully created !!"
        },status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)
    
# Update member
@api_view(['PUT'])
def memberupdate(request, id):
    member = Member.objects.get(id=id)
    serializer = MemberSerializer(member, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member successfully updated!!"
        },status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)
    
