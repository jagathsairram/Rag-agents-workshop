from fastmcp import Client
import asyncio

async def main():
    async with Client("weather_server.py") as mcp_client:
        # Get list of available tools
        tools = await mcp_client.list_tools()
        print("Available Tools:")
        for tool in tools:
            print(tool)

if __name__ == "__main__":
    asyncio.run(main())
