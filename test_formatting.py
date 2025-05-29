#!/usr/bin/env python3
"""
Script to reproduce and verify the black formatting issue.
"""

import subprocess
import sys
from pathlib import Path

def run_black_check():
    """Run black --check on errbot/ tests/ tools/ and return the result."""
    try:
        result = subprocess.run(
            ["black", "--check", "errbot/", "tests/", "tools/"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        print("Error: black is not installed")
        return 1, "", "black not found"

def run_black_check_non_tests():
    """Run black --check on non-test files only."""
    try:
        result = subprocess.run(
            ["black", "--check", "errbot/", "tools/"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        print("Error: black is not installed")
        return 1, "", "black not found"

def main():
    print("=== Testing Black Formatting ===")
    
    print("\n1. Checking all files (errbot/, tests/, tools/):")
    returncode, stdout, stderr = run_black_check()
    print(f"Return code: {returncode}")
    if stdout:
        print("STDOUT:")
        print(stdout)
    if stderr:
        print("STDERR:")
        print(stderr)
    
    print("\n2. Checking non-test files only (errbot/, tools/):")
    returncode_non_tests, stdout_non_tests, stderr_non_tests = run_black_check_non_tests()
    print(f"Return code: {returncode_non_tests}")
    if stdout_non_tests:
        print("STDOUT:")
        print(stdout_non_tests)
    if stderr_non_tests:
        print("STDERR:")
        print(stderr_non_tests)
    
    print("\n=== Summary ===")
    if returncode == 0:
        print("✅ All files pass black formatting check")
    else:
        print("❌ Some files fail black formatting check")
        
    if returncode_non_tests == 0:
        print("✅ Non-test files pass black formatting check")
    else:
        print("❌ Non-test files fail black formatting check")
    
    return returncode

if __name__ == "__main__":
    sys.exit(main())