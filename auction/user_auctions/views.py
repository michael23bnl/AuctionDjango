from django.shortcuts import render, redirect, get_object_or_404
from auctions.models import Auction
import uuid


def my_auctions(request):
    user_id = request.session.get('user_id')

    auctions = Auction.objects.filter(ownerid=user_id)

    return render(request, 'user_auctions/my_auctions.html', {
        'auctions': auctions
    })


def create_auction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        startdate = request.POST.get('startdate')
        finishdate = request.POST.get('finishdate')

        Auction.objects.create(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            startdate=startdate,
            finishdate=finishdate,
            status=0,
            ownerid=request.session.get('user_id')
        )

        return redirect('my_auctions')

    return render(request, 'user_auctions/create_auction.html')


def edit_auction(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)

    if request.method == 'POST':
        auction.name = request.POST.get('name')
        auction.description = request.POST.get('description')
        auction.startdate = request.POST.get('startdate')
        auction.finishdate = request.POST.get('finishdate')
        auction.save()

        return redirect('my_auctions')

    return render(request, 'user_auctions/edit_auction.html', {
        'auction': auction
    })

