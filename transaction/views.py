from django.shortcuts import render
from transaction.models import Transaction,Status
from subscription.models import Subscription, Membership

# Create your views here.


def callback_view(request):
    data = request.GET
    print(data['pidx'])
    txn = Transaction.objects.get(pidx=data['pidx'])
    if data['status']=="Completed":
        txn.status =Status.COMPLETED
        txn.txn_id = data['tidx']
        member_ship = Membership.objects.get(member=txn.member)
        sub = member_ship.subscription
        member_ship.days = member_ship.days + sub.days
        member_ship.member.is_active = True
        member_ship.save()
    elif data['status']=="Pending":
        txn.status == Status.PENDING
    else:
        txn.status = Status.USER_CANCELED
    txn.save()
    return render(request,'transaction/index.html', {'txn':txn})