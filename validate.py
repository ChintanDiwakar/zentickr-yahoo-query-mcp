#!/usr/bin/env python3
"""
Validation script to test Zentickr setup and functionality
"""

import sys
import importlib.util
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are available"""
    dependencies = [
        'yahooquery',
        'pandas', 
        'mcp',
        'pydantic',
        'json',
        'asyncio'
    ]
    
    missing = []
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - NOT FOUND")
            missing.append(dep)
    
    return missing

def check_server_module():
    """Check if the server module can be imported"""
    try:
        from src.stock_mcp.server import main
        print("✅ Server module imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Server module import failed: {e}")
        return False

def test_basic_functionality():
    """Test basic server functionality"""
    try:
        from yahooquery import Ticker
        # Test with a simple ticker
        ticker = Ticker("AAPL")
        data = ticker.price
        if data:
            print("✅ Yahoo Finance API connection successful")
            return True
        else:
            print("⚠️ Yahoo Finance API returned empty data")
            return False
    except Exception as e:
        print(f"❌ Yahoo Finance API test failed: {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 Validating Zentickr setup...\n")
    
    print("📦 Checking dependencies:")
    missing = check_dependencies()
    
    print("\n🔧 Checking server module:")
    server_ok = check_server_module()
    
    print("\n🌐 Testing Yahoo Finance API:")
    api_ok = test_basic_functionality()
    
    print("\n" + "="*50)
    if not missing and server_ok and api_ok:
        print("🎉 All checks passed! Zentickr is ready to run.")
        print("\nYou can start the server using:")
        print("  - Windows: .\\run_server.bat")
        print("  - Unix/Linux/macOS: ./run_server.sh")
        print("  - Manual: python run_server.py")
    else:
        print("⚠️ Some issues were found:")
        if missing:
            print(f"   - Missing dependencies: {', '.join(missing)}")
        if not server_ok:
            print("   - Server module cannot be imported")
        if not api_ok:
            print("   - Yahoo Finance API test failed")
        print("\nPlease run: python setup_dev.py")

if __name__ == "__main__":
    main()
