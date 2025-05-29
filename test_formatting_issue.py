#!/usr/bin/env python3
"""
Script to reproduce the black formatting issue in vcheck.py
"""
import subprocess
import sys
import os

def run_black_check():
    """Run black --check on the specific file that's failing"""
    print("Running black --check on errbot/core_plugins/vcheck.py...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--check", 
        "errbot/core_plugins/vcheck.py"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def run_black_diff():
    """Show what black would change"""
    print("\nRunning black --diff to see what would change...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--diff", 
        "errbot/core_plugins/vcheck.py"
    ], capture_output=True, text=True)
    
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")

def run_full_codestyle_check():
    """Run the full codestyle check as done in CI"""
    print("\nRunning full codestyle check (black --check errbot/ tests/ tools/)...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--check", 
        "errbot/", "tests/", "tools/"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

if __name__ == "__main__":
    print("=== Black Formatting Issue Reproduction Script ===")
    
    # Change to the repository directory
    os.chdir("/lca-workspace/repos/errbotio__errbot")
    
    # Test the specific file
    vcheck_passes = run_black_check()
    
    # Show the diff
    run_black_diff()
    
    # Test the full suite
    full_passes = run_full_codestyle_check()
    
    print(f"\n=== Results ===")
    print(f"vcheck.py passes black check: {vcheck_passes}")
    print(f"Full codestyle check passes: {full_passes}")
    
    if not vcheck_passes:
        print("\n❌ The vcheck.py file needs formatting fixes")
        sys.exit(1)
    elif not full_passes:
        print("\n⚠️  The vcheck.py file passes but other files need formatting")
        sys.exit(1)
    else:
        print("\n✅ All formatting checks pass!")
        sys.exit(0)