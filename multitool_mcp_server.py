from typing import List
from mcp.server.fastmcp import FastMCP
import requests
import json
import os
from typing import List, Dict
from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Get port from environment variable (Render sets this, defaults to 8001 for local dev)
PORT = int(os.environ.get("PORT", 8001))

# Initialize FastMCP server with host and port in constructor
mcp = FastMCP("Multitool", host="0.0.0.0", port=PORT)

@mcp.tool()
async def health_check() -> str:
    """Check server health"""
    return "ok"
    
@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"
  
@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
async def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
async def subtract(a: int, b: int) -> int:
    """Subtract b from a"""
    return a - b

@mcp.tool()
async def divide(a: int, b: int) -> float:
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    

@mcp.tool()
async def today_date() -> str:
    """Use when asked what day it is today."""
    today = datetime.today()
    return today.strftime("%Y-%m-%d")  # รูปแบบ: ปี-เดือน-วัน (เช่น 2025-09-01)

# ตัวอย่างการใช้งาน
print("วันนี้วันที่:", today_date())    
if __name__ == "__main__":
    print(f"Starting Weather MCP server on 0.0.0.0:{PORT}")
    mcp.run(transport="streamable-http")
