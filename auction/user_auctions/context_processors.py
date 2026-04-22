from auctions.models import Auction

def user_auctions(request):
    user_id = request.session.get('user_id')

    if user_id:
        auctions = Auction.objects.filter(ownerid=user_id)
    else:
        auctions = []

    return {
        'user_auctions': auctions
    }







