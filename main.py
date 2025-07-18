from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Weather Service")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a city
    Args:
        city: The city to get the weather for
    Returns:
        The current weather for the city
    """
    return f"The weather in {city}: Sunny, 20°C"

@mcp.resource("weather://{location}")
def get_weather_forecast(location: str) -> str:
    """
    Provide wather data as a resource.
    Args:
        location: The location to get the weather forecast for
    Returns:
        The weather forecast for the location
    """
    return f"The weather forecast for {location}: Sunny, 20°C"

@mcp.prompt()
def weather_report(location: str) -> str:
    """
    Create a weather report for a location.
    Args:
        location: The location to create a weather report for
    Returns:
        The weather report for the location
    """
    return f"""You are a weather reporter.
    You are given a weather forecast for a location.
    You need to create a weather report for {location}."""

if __name__ == "__main__":
    mcp.run()
