
using Moq;
using AuctionApp.AuctionModule.Models;
using AuctionApp.AuctionModule.Repositories;
using AuctionApp.AuctionModule.Services;

namespace AuctionApp.Tests;

public class AuctionsServiceTests
{
    private readonly Mock<IAuctionsRepository> _repoMock;
    private readonly AuctionsService _service;

    public AuctionsServiceTests()
    {
        _repoMock = new Mock<IAuctionsRepository>();
        _service = new AuctionsService(_repoMock.Object);
    }

    [Fact]
    public async Task GetAuctionAsync_ShouldReturnAuction()
    {
        var auction = new Auction { Id = Guid.NewGuid(), Name = "Test" };

        _repoMock
            .Setup(r => r.GetAsync(auction.Id))
            .ReturnsAsync(auction);

        var result = await _service.GetAuctionAsync(auction.Id);

        Assert.NotNull(result);
        Assert.Equal("Test", result.Name);
    }

    [Fact]
    public async Task GetAllActiveAuctionsAsync_ShouldReturnList()
    {
        var auctions = new List<Auction> { new Auction(), new Auction() };

        _repoMock
            .Setup(r => r.GetAllActiveAsync())
            .ReturnsAsync(auctions);

        var result = await _service.GetAllActiveAuctionsAsync();

        Assert.Equal(2, result.Count);
    }

    [Fact]
    public async Task StartAuctionAsync_ShouldThrowException_WhenAuctionNotFound()
    {
        var id = Guid.NewGuid();
    
        _repoMock
            .Setup(r => r.StartAsync(id))
            .ThrowsAsync(new InvalidOperationException("Аукцион не найден"));

        var exception = await Assert.ThrowsAsync<InvalidOperationException>(() => 
            _service.StartAuctionAsync(id));
    
        Assert.Equal("Аукцион не найден", exception.Message);
    }
}