#!/usr/bin/env python3
"""
Run the OpenAlex MCP server using the installed package.
"""
import sys
from src.stock_mcp.server import main

if __name__ == "__main__":
    sys.exit(main())