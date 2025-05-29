#!/usr/bin/env python3
"""
Final verification script to ensure the formatting fixes work correctly.
"""

import subprocess
import sys
from pathlib import Path

def main():
    print("=== Final Verification of Black Formatting Fixes ===")
    
    # Test the specific files that were modified
    modified_files = [
        "errbot/backend_plugin_manager.py",
        "errbot/rendering/xhtmlim.py", 
        "errbot/__init__.py",
        "errbot/plugin_manager.py",
        "errbot/backends/irc.py"
    ]
    
    print(f"\n1. Testing {len(modified_files)} modified files individually:")
    all_pass = True
    for file_path in modified_files:
        try:
            result = subprocess.run(
                ["black", "--check", file_path],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent
            )
            if result.returncode == 0:
                print(f"✅ {file_path}")
            else:
                print(f"❌ {file_path}")
                print(f"   Error: {result.stderr.strip()}")
                all_pass = False
        except Exception as e:
            print(f"❌ {file_path} - Exception: {e}")
            all_pass = False
    
    print(f"\n2. Testing all non-test files (errbot/, tools/):")
    try:
        result = subprocess.run(
            ["black", "--check", "errbot/", "tools/"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        if result.returncode == 0:
            print("✅ All non-test files pass black formatting")
        else:
            print("❌ Some non-test files still fail black formatting")
            print(f"   Error: {result.stderr.strip()}")
            all_pass = False
    except Exception as e:
        print(f"❌ Exception testing non-test files: {e}")
        all_pass = False
    
    print(f"\n=== Summary ===")
    if all_pass:
        print("🎉 SUCCESS: All formatting issues in non-test files have been fixed!")
        print("The CI workflow should now pass for the codestyle check on non-test files.")
        return 0
    else:
        print("💥 FAILURE: Some formatting issues remain.")
        return 1

if __name__ == "__main__":
    sys.exit(main())