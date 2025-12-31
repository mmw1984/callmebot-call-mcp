"""
Vercel Serverless Function Entry Point

This file is the entry point for Vercel, running FastMCP server as an ASGI application.
"""

from src.server import mcp

# Create ASGI application - Vercel natively supports ASGI
# Use stateless_http=True to adapt to serverless environment
app = mcp.http_app(stateless_http=True)
