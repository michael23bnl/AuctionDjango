from auctions.models import Lot, Auction

def user_lots(request):
    user_id = request.session.get('user_id')

    if user_id:
        auctions = Auction.objects.filter(ownerid=user_id)
        lots = Lot.objects.filter(auctionid__in=auctions)
    else:
        lots = []

    return {
        'user_lots': lots
    }


