#!/usr/bin/env python3
"""
Final test to simulate the exact CI scenario that was failing
"""
import subprocess
import sys
import os

def simulate_ci_codestyle_check():
    """Simulate the exact command that was failing in CI"""
    print("Simulating CI codestyle check...")
    print("Running: black --check errbot/core_plugins/vcheck.py")
    
    result = subprocess.run([
        sys.executable, "-m", "black", "--check", 
        "errbot/core_plugins/vcheck.py"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    # Check if the specific error from the original issue is gone
    if "would reformat" in result.stderr and "vcheck.py" in result.stderr:
        print("❌ FAILURE: The original error is still present!")
        return False
    elif result.returncode == 0:
        print("✅ SUCCESS: vcheck.py passes black formatting check!")
        return True
    else:
        print("⚠️  UNEXPECTED: Different error occurred")
        return False

if __name__ == "__main__":
    print("=== Final CI Test Simulation ===")
    print("Testing the specific issue mentioned in the error message:")
    print('Original error: "would reformat /home/runner/work/errbot/errbot/errbot/core_plugins/vcheck.py"')
    print()
    
    # Change to the repository directory
    os.chdir("/lca-workspace/repos/errbotio__errbot")
    
    # Run the test
    success = simulate_ci_codestyle_check()
    
    print(f"\n=== Final Result ===")
    if success:
        print("✅ The CI workflow issue has been RESOLVED!")
        print("The specific error mentioned in the issue description is fixed.")
        sys.exit(0)
    else:
        print("❌ The CI workflow issue is NOT resolved.")
        sys.exit(1)