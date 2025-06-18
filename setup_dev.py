#!/usr/bin/env python3
"""
Setup script for Zentickr development environment
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def main():
    """Main setup function"""
    print("🚀 Setting up Zentickr development environment...\n")
    
    # Check if virtual environment exists
    venv_path = Path("env")
    if not venv_path.exists():
        print("📦 Creating virtual environment...")
        run_command(f"{sys.executable} -m venv env", "Virtual environment creation")
    else:
        print("✅ Virtual environment already exists")
    
    # Determine activation script based on OS
    if os.name == 'nt':  # Windows
        activate_script = "env\\Scripts\\activate"
        pip_command = "env\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        activate_script = "source env/bin/activate"
        pip_command = "env/bin/pip"
    
    # Install dependencies
    print("\n📋 Installing dependencies...")
    run_command(f"{pip_command} install -r requirements.txt", "Dependencies installation")
    
    # Install package in development mode
    print("\n🔧 Installing package in development mode...")
    run_command(f"{pip_command} install -e .", "Development installation")
    
    print("\n✨ Setup complete! You can now run the server using:")
    print("   - Windows: .\\run_server.bat")
    print("   - Unix/Linux/macOS: ./run_server.sh")
    print("   - Manual: python run_server.py")

if __name__ == "__main__":
    main()
