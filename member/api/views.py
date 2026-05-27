from member.api.serializer import MemberSerializer
from member.models import Member
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def memberlist(request):
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def membercreate(request):
    post_data = request.data
    serializer = MemberSerializer(data=post_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member Successfully created"
        },status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)