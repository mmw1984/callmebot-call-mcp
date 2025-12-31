"""
Local Run Script

Run MCP server using stdio transport for local development and debugging.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.server import mcp

if __name__ == "__main__":
    print("Starting CallMeBot MCP Server (local mode)...")
    mcp.run(transport="stdio")
