import random
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")


@mcp.tool()
def greeting(name: str) -> str:
    """
    Send a personalized greeting to someone.

    Args:
        name: The name of the person to greet

    Returns:
        A friendly greeting message
    """
    return f"Hi {name}!"


@mcp.tool()
def roll_dice(sides: int = 6, count: int = 1) -> str:
    """
    Roll one or more dice with specified number of sides.

    Args:
        sides: Number of sides on each die (default: 6)
        count: Number of dice to roll (default: 1)

    Returns:
        String describing the dice roll results
    """
    if sides < 2 or count < 1:
        return "Invalid parameters: sides must be >= 2 and count must be >= 1"

    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)

    if count == 1:
        return f"🎲 Rolled a {rolls[0]} on a {sides}-sided die"
    else:
        return f"🎲 Rolled {count} {sides}-sided dice: {rolls} (Total: {total})"


@mcp.tool()
def generate_password(length: int = 12, include_symbols: bool = True) -> str:
    """
    Generate a random secure password.

    Args:
        length: Length of the password (default: 12)
        include_symbols: Whether to include special characters (default: True)

    Returns:
        A randomly generated password
    """
    import string

    if length < 4:
        return "Password length must be at least 4 characters"

    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += "!@#$%^&*"

    password = ''.join(random.choice(chars) for _ in range(length))
    return f"🔐 Generated password: {password}"


@mcp.tool()
def magic_8_ball(question: str) -> str:
    """
    Ask the magic 8-ball a yes/no question and get a mystical answer.

    Args:
        question: The question to ask the magic 8-ball

    Returns:
        A mystical answer from the magic 8-ball
    """
    responses = [
        "It is certain",
        "Reply hazy, try again",
        "Don't count on it",
        "It is decidedly so",
        "My sources say no",
        "Without a doubt",
        "Outlook not so good",
        "Yes definitely",
        "Very doubtful",
        "You may rely on it",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook good",
        "Cannot predict now",
        "Most likely",
        "As I see it, yes",
        "Better not tell you now",
        "Signs point to yes"
    ]

    answer = random.choice(responses)
    return f"🎱 Question: {question}\n🔮 Magic 8-Ball says: {answer}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
