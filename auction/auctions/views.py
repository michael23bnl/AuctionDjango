from django.shortcuts import render
from .models import Auction, Lot, Bid


def auction_list(request):
    auctions = Auction.objects.all()
    return render(request, 'auctions/auction_list.html', {'auctions': auctions})


def lot_list(request):
    lots = Lot.objects.all()
    return render(request, 'auctions/lot_list.html', {'lots': lots})


def bid_list(request):
    bids = Bid.objects.all()
    return render(request, 'auctions/bid_list.html', {'bids': bids})


def search_lots(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Lot.objects.filter(name__icontains=query)

    return render(request, 'auctions/search.html', {
        'results': results,
        'query': query
    })


def home(request):
    return render(request, 'home.html')
