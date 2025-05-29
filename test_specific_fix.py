#!/usr/bin/env python3
"""
Test script to verify that the specific issue mentioned in the error message has been fixed.
The original error was: "would reformat /home/runner/work/errbot/errbot/errbot/core_plugins/vcheck.py"
"""
import subprocess
import sys
import os

def test_vcheck_formatting():
    """Test that vcheck.py passes black formatting check"""
    print("Testing vcheck.py formatting...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--check", 
        "errbot/core_plugins/vcheck.py"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT: {result.stdout}")
    print(f"STDERR: {result.stderr}")
    
    return result.returncode == 0

def test_files_from_same_commit():
    """Test files that were changed in the same commit as vcheck.py"""
    print("\nTesting botplugin.py (also changed in commit a14be35)...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--check", 
        "errbot/botplugin.py"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT: {result.stdout}")
    print(f"STDERR: {result.stderr}")
    
    return result.returncode == 0

if __name__ == "__main__":
    print("=== Testing Specific Fix for vcheck.py Issue ===")
    
    # Change to the repository directory
    os.chdir("/lca-workspace/repos/errbotio__errbot")
    
    # Test the specific file mentioned in the error
    vcheck_passes = test_vcheck_formatting()
    
    # Test the other file from the same commit
    botplugin_passes = test_files_from_same_commit()
    
    print(f"\n=== Results ===")
    print(f"vcheck.py passes black check: {vcheck_passes}")
    print(f"botplugin.py passes black check: {botplugin_passes}")
    
    if vcheck_passes and botplugin_passes:
        print("\n✅ All files from commit a14be35 pass black formatting checks!")
        print("The specific issue mentioned in the error message has been resolved.")
        sys.exit(0)
    else:
        print("\n❌ Some files still have formatting issues")
        sys.exit(1)