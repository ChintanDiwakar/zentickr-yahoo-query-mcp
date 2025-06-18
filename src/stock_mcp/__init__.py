"""
Zentickr - Yahoo Finance MCP Server

A powerful Model Context Protocol (MCP) server that provides comprehensive access to 
Yahoo Finance data through the yahooquery library.
"""

__version__ = "0.1.0"
__author__ = "Chintan Diwakar"
__email__ = "chintan.diwakar012@gmail.com"

from .server import main

__all__ = ["main"]
