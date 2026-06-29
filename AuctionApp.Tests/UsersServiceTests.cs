
using Moq;
using AuctionApp.UsersModule;
using AuctionApp.UsersModule.Models;
using AuctionApp.UsersModule.Repositories;
using AuctionApp.UsersModule.Services;

namespace AuctionApp.Tests;

public class UsersServiceTests
{
    private readonly Mock<IUsersRepository> _usersRepositoryMock;
    private readonly Mock<IPasswordHasher> _passwordHasherMock;
    private readonly UsersService _usersService;

    public UsersServiceTests()
    {
        _usersRepositoryMock = new Mock<IUsersRepository>();
        _passwordHasherMock = new Mock<IPasswordHasher>();

        _usersService = new UsersService(
            _usersRepositoryMock.Object,
            _passwordHasherMock.Object
        );
    }

    [Fact]
    public async Task RegisterUserAsync_ShouldReturnGuid_WhenUserDoesNotExist()
    {
        var email = "test@mail.com";
        var password = "123456";
        var hashedPassword = "hashed";

        _usersRepositoryMock
            .Setup(r => r.GetByEmailAsync(email))
            .ReturnsAsync((User?)null);

        _passwordHasherMock
            .Setup(h => h.Generate(password))
            .Returns(hashedPassword);

        _usersRepositoryMock
            .Setup(r => r.CreateAsync(It.IsAny<string>(), It.IsAny<string>(), email, hashedPassword))
            .ReturnsAsync(Guid.NewGuid());

        var result = await _usersService.RegisterUserAsync("Test", "User", email, password);

        Assert.NotEqual(Guid.Empty, result);
    }

    [Fact]
    public async Task RegisterUserAsync_ShouldReturnEmptyGuid_WhenUserExists()
    {
        var email = "test@mail.com";

        _usersRepositoryMock
            .Setup(r => r.GetByEmailAsync(email))
            .ReturnsAsync(new User { Email = email });

        var result = await _usersService.RegisterUserAsync("Test", "User", email, "123456");

        Assert.Equal(Guid.Empty, result);
    }

    [Fact]
    public async Task VerifyUserPasswordAsync_ShouldReturnTrue_WhenPasswordCorrect()
    {
        var email = "test@mail.com";
        var password = "123456";

        var user = new User
        {
            Email = email,
            HashedPassword = "hashed"
        };

        _usersRepositoryMock
            .Setup(r => r.GetByEmailAsync(email))
            .ReturnsAsync(user);

        _passwordHasherMock
            .Setup(h => h.Verify(password, user.HashedPassword))
            .Returns(true);

        var (result, returnedUser) = await _usersService.VerifyUserPasswordAsync(email, password);

        Assert.True(result);
        Assert.NotNull(returnedUser);
    }

    [Fact]
    public async Task VerifyUserPasswordAsync_ShouldReturnFalse_WhenUserNotFound()
    {
        _usersRepositoryMock
            .Setup(r => r.GetByEmailAsync(It.IsAny<string>()))
            .ReturnsAsync((User?)null);

        var (result, user) = await _usersService.VerifyUserPasswordAsync("test@mail.com", "123");

        Assert.False(result);
        Assert.Null(user);
    }
}