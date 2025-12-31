"""
CallMeBot Telegram Voice Call MCP Server

This MCP server provides functionality to make voice calls to Telegram users via CallMeBot API.
"""

import os
from typing import Dict, Any

import httpx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("CallMeBot Telegram Voice Call")

# CallMeBot API base URL
CALLMEBOT_API_URL = "http://api.callmebot.com/start.php"


@mcp.tool(description="Make a voice call to a Telegram user with TTS (Text-to-Speech)")
async def call_telegram_user(
    username: str,
    text: str,
    lang: str = "en-US-Standard-B",
    repeat: int = 2,
    carbon_copy: str = "yes",
    timeout: int = 30
) -> Dict[str, Any]:
    """
    Make a voice call to a Telegram user.

    Args:
        username: Telegram username (e.g. @myuser) or phone number (e.g. +331234567890)
        text: Text message to be spoken (max 256 characters)
        lang: Voice language, default en-US-Standard-B. Check Google Cloud TTS for available voices
        repeat: Number of times to repeat the message (default 2)
        carbon_copy: Text copy option (yes/no/missed/only), default yes
        timeout: Call timeout in seconds (default 30, only available on dedicated bots)

    Returns:
        Dictionary containing API call result
    """
    # Validate required parameters
    if not username:
        return {
            "success": False,
            "error": "Missing username",
            "message": "Please provide a Telegram username or phone number"
        }

    if not text:
        return {
            "success": False,
            "error": "Missing text message",
            "message": "Please provide a text message to be spoken"
        }

    # Truncate text if too long
    if len(text) > 256:
        text = text[:256]

    # Validate carbon_copy parameter
    valid_cc_options = ["yes", "no", "missed", "only"]
    if carbon_copy not in valid_cc_options:
        carbon_copy = "yes"

    # Ensure repeat is within reasonable range
    if repeat < 1:
        repeat = 1
    elif repeat > 10:
        repeat = 10

    # Ensure timeout is within reasonable range
    if timeout < 5:
        timeout = 5
    elif timeout > 120:
        timeout = 120

    # Build API request parameters
    params = {
        "user": username,
        "text": text,
        "lang": lang,
        "rpt": str(repeat),
        "cc": carbon_copy,
        "timeout": str(timeout)
    }

    try:
        # Send GET request to CallMeBot API
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(CALLMEBOT_API_URL, params=params)
            response_text = response.text

            if response.status_code == 200:
                return {
                    "success": True,
                    "message": f"Successfully initiated voice call to {username}",
                    "details": {
                        "username": username,
                        "text": text,
                        "language": lang,
                        "repeat": repeat,
                        "carbon_copy": carbon_copy,
                        "timeout": timeout
                    },
                    "api_response": response_text
                }
            else:
                return {
                    "success": False,
                    "error": f"API request failed with status code: {response.status_code}",
                    "api_response": response_text
                }

    except httpx.TimeoutException:
        return {
            "success": False,
            "error": "Request timeout",
            "message": "CallMeBot API did not respond within the specified time"
        }
    except httpx.RequestError as e:
        return {
            "success": False,
            "error": "Request error",
            "message": str(e)
        }
    except Exception as e:
        return {
            "success": False,
            "error": "Unknown error",
            "message": str(e)
        }
