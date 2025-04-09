#!/usr/bin/env python3
import subprocess
import sys

def check_black_formatting():
    """Check if the vcheck.py file passes Black formatting."""
    try:
        result = subprocess.run(
            ["black", "--check", "errbot/core_plugins/vcheck.py"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Black formatting check passed!")
            return True
        else:
            print("❌ Black formatting check failed!")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error running Black: {e}")
        return False

if __name__ == "__main__":
    success = check_black_formatting()
    sys.exit(0 if success else 1)