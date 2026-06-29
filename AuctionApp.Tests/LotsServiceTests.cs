
using Moq;
using AuctionApp.AuctionModule.Models;
using AuctionApp.AuctionModule.Repositories;
using AuctionApp.AuctionModule.Services;

namespace AuctionApp.Tests;

public class LotsServiceTests
{
    private readonly Mock<ILotsRepository> _repoMock;
    private readonly LotsService _service;

    public LotsServiceTests()
    {
        _repoMock = new Mock<ILotsRepository>();
        _service = new LotsService(_repoMock.Object);
    }

    [Fact]
    public async Task GetLotAsync_ShouldReturnLot()
    {
        var lot = new Lot { Id = Guid.NewGuid(), Name = "Test Lot" };

        _repoMock
            .Setup(r => r.GetAsync(lot.Id))
            .ReturnsAsync(lot);

        var result = await _service.GetLotAsync(lot.Id);

        Assert.NotNull(result);
        Assert.Equal("Test Lot", result.Name);
    }
}