from django.shortcuts import render, redirect, get_object_or_404
from auctions.models import Lot, Auction
from django.utils import timezone
import uuid

from users.models import User
from .tasks import send_lot_created_email

def my_lots(request):
    user_id = request.session.get('user_id')

    auctions = Auction.objects.filter(ownerid=user_id)
    lots = Lot.objects.filter(auctionid__in=auctions)

    return render(request, 'user_lots/my_lots.html', {
        'lots': lots
    })


def create_lot(request):
    user_id = request.session.get('user_id')
    auctions = Auction.objects.filter(ownerid=user_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        auction_id = request.POST.get('auction_id')
        startprice = request.POST.get('startprice')
        reserveprice = request.POST.get('reserveprice')

        lot = Lot.objects.create(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            auctionid_id=auction_id,
            startprice=startprice,
            reserveprice=reserveprice,
            currentprice=startprice,
            exhibitiondate=timezone.now(),
        )

        user = User.objects.get(id=user_id)
        send_lot_created_email.delay(user.email, lot.name)

        return redirect('my_lots')

    return render(request, 'user_lots/create_lot.html', {
        'auctions': auctions
    })


def edit_lot(request, lot_id):
    lot = get_object_or_404(Lot, id=lot_id)

    if request.method == 'POST':
        lot.name = request.POST.get('name')
        lot.description = request.POST.get('description')
        lot.startprice = request.POST.get('startprice')
        lot.reserveprice = request.POST.get('reserveprice')
        lot.save()

        return redirect('my_lots')

    return render(request, 'user_lots/edit_lot.html', {
        'lot': lot
    })