#!/usr/bin/env python3
import subprocess
import sys

def main():
    """Run black in check mode on the commands_test.py file."""
    result = subprocess.run(
        ["black", "--check", "tests/commands_test.py"],
        capture_output=True,
        text=True,
    )
    
    print("Exit code:", result.returncode)
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())