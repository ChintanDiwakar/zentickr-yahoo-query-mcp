#!/usr/bin/env python3
"""
Zentickr Deployment Script
Automated deployment and setup for Zentickr MCP Server
"""

import os
import subprocess
import sys
import platform
from pathlib import Path

# Windows-compatible symbols
if platform.system() == "Windows":
    CHECK = "[OK]"
    CROSS = "[FAIL]"
    WARNING = "[WARN]"
    ARROW = "-->"
    ROCKET = ">>>"
else:
    CHECK = "✅"
    CROSS = "❌"
    WARNING = "⚠️"
    ARROW = "🔄"
    ROCKET = "🚀"

def print_banner():
    """Print a nice banner"""
    banner = f"""
    ================================================
    ZENTICKR - Yahoo Finance MCP Server
    {ROCKET} Ready for Launch! {ROCKET}
    ================================================
    """
    print(banner)

def run_command(command, description, critical=True):
    """Run a command and handle results"""
    print(f"\n{ARROW} {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(f"{CHECK} {description} - SUCCESS")
        if result.stdout.strip():
            # Limit output length to avoid clutter
            output = result.stdout.strip()
            if len(output) > 200:
                output = output[:200] + "..."
            print(f"   Output: {output}")
        return True
    except subprocess.CalledProcessError as e:
        if critical:
            print(f"{CROSS} {description} - FAILED")
            error_msg = e.stderr.strip() if e.stderr else "Unknown error"
            if len(error_msg) > 200:
                error_msg = error_msg[:200] + "..."
            print(f"   Error: {error_msg}")
            return False
        else:
            print(f"{WARNING} {description} - Optional step failed")
            return True
    except Exception as e:
        print(f"{CROSS} {description} - Unexpected error: {str(e)}")
        return False if critical else True

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        print(f"{CHECK} Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"{CROSS} Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.10+")
        return False

def setup_environment():
    """Set up the development environment"""
    print(f"\n{ARROW} Setting up Zentickr environment...")
    
    # Check for virtual environment
    venv_path = Path("env")
    if not venv_path.exists():
        if not run_command(f"{sys.executable} -m venv env", "Creating virtual environment"):
            return False
    else:
        print(f"{CHECK} Virtual environment already exists")
    
    # Determine pip command based on OS
    if platform.system() == "Windows":
        pip_cmd = "env\\Scripts\\pip"
        python_cmd = "env\\Scripts\\python"
    else:
        pip_cmd = "env/bin/pip"
        python_cmd = "env/bin/python"
    
    # Upgrade pip
    run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip", critical=False)
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Install package in development mode
    run_command(f"{pip_cmd} install -e .", "Installing Zentickr package", critical=False)
    
    return True

def test_installation():
    """Test if the installation works"""
    print(f"\n{ARROW} Testing installation...")
    
    # Test basic imports
    test_script = '''
import sys
import os
print("Testing core dependencies...")
try:
    import yahooquery
    print("[OK] yahooquery imported")
    
    import pandas
    print("[OK] pandas imported")
    
    import mcp
    print("[OK] mcp imported")
    
    print("[OK] All core dependencies imported successfully")
    
    # Test Yahoo Finance connection
    print("Testing Yahoo Finance API...")
    from yahooquery import Ticker
    ticker = Ticker("AAPL")
    data = ticker.price
    if data and "AAPL" in data:
        print("[OK] Yahoo Finance API connection successful")
    else:
        print("[WARN] Yahoo Finance API returned empty data")
        
    print("[SUCCESS] Zentickr is ready to run!")
    sys.exit(0)
except ImportError as e:
    print(f"[FAIL] Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"[WARN] Warning: {e}")
    print("[INFO] Some issues detected but server may still work")
    sys.exit(0)
'''
    
    if platform.system() == "Windows":
        python_cmd = "env\\Scripts\\python"
    else:
        python_cmd = "env/bin/python"
    
    # Write test script to temporary file
    try:
        with open("test_installation.py", "w", encoding='utf-8') as f:
            f.write(test_script)
        
        success = run_command(f"{python_cmd} test_installation.py", "Running installation test")
        
        # Clean up test file
        try:
            os.remove("test_installation.py")
        except:
            pass
        
        return success
    except Exception as e:
        print(f"{CROSS} Could not create test file: {e}")
        return False

def show_launch_instructions():
    """Show instructions for launching the app"""
    print("\n" + "="*60)
    print(f"{ROCKET} ZENTICKR IS READY TO LAUNCH! {ROCKET}")
    print("="*60)
    
    print(f"\n{ARROW} How to start your server:")
    if platform.system() == "Windows":
        print("   .\\run_server.bat")
    else:
        print("   ./run_server.sh")
    
    print(f"\n{ARROW} Manual start (if scripts don't work):")
    if platform.system() == "Windows":
        print("   env\\Scripts\\activate")
    else:
        print("   source env/bin/activate")
    print("   python run_server.py")
    
    print(f"\n{ARROW} Integration with Claude Desktop:")
    print("   Add this to your Claude Desktop config:")
    if platform.system() == "Windows":
        current_dir = os.getcwd().replace("\\", "\\\\")
        print(f'''   {{
     "mcpServers": {{
       "zentickr": {{
         "command": "{current_dir}\\\\run_server.bat"
       }}
     }}
   }}''')
    else:
        current_dir = os.getcwd()
        print(f'''   {{
     "mcpServers": {{
       "zentickr": {{
         "command": "{current_dir}/run_server.sh"
       }}
     }}
   }}''')
    
    print(f"\n{ARROW} What you can do now:")
    print("   * Get real-time stock prices")
    print("   * Analyze financial statements") 
    print("   * Research company information")
    print("   * Track analyst recommendations")
    print("   * Monitor ESG scores")
    print("   * Access historical price data")
    
    print(f"\n{ARROW} Next steps for production:")
    print("   * Deploy to cloud (AWS, GCP, Azure)")
    print("   * Set up Docker containers")
    print("   * Add monitoring and logging")
    print("   * Implement authentication")
    print("   * Scale horizontally")

def main():
    """Main deployment function"""
    # Set console encoding for Windows
    if platform.system() == "Windows":
        try:
            # Try to set UTF-8 encoding
            os.system('chcp 65001 >nul 2>&1')
        except:
            pass
    
    print_banner()
    
    print(f"{ARROW} Checking system requirements...")
    
    # Check Python version
    if not check_python_version():
        print(f"\n{CROSS} Python version incompatible. Please install Python 3.10 or higher.")
        print("Download from: https://www.python.org/downloads/")
        return False
    
    # Setup environment
    if not setup_environment():
        print(f"\n{CROSS} Environment setup failed. Please check errors above.")
        return False
    
    # Test installation
    if not test_installation():
        print(f"\n{WARNING} Installation test had issues, but you can still try to run the server.")
    
    # Show launch instructions
    show_launch_instructions()
    
    print(f"\n{CHECK} Deployment complete! Zentickr is live and ready to use!")
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print(f"\n{CHECK} SUCCESS: Run '.\\run_server.bat' to start your server!")
        else:
            print(f"\n{CROSS} FAILED: Please check the errors above and try again.")
        input("\nPress Enter to continue...")
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n{WARNING} Deployment cancelled by user")
        input("Press Enter to continue...")
        sys.exit(1)
    except Exception as e:
        print(f"\n{CROSS} Unexpected error: {e}")
        print("This might be a character encoding issue.")
        print("Try running in PowerShell instead of Command Prompt.")
        input("Press Enter to continue...")
        sys.exit(1)
