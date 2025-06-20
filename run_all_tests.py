import os
import sys
import unittest

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Ensure project root is in sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suites = []

    for subfolder in ['python', 'ml', 'dl']:
        test_dir = os.path.join(project_root, subfolder, 'tests')
        if os.path.isdir(test_dir):
            suite = loader.discover(start_dir=test_dir, top_level_dir=project_root)
            suites.append(suite)

    all_tests = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(all_tests)

    # Count results
    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    failed = failures + errors
    passed = total - failed

    # Print summary
    print(f"\n{BOLD}Test Summary:{RESET}")
    print(f"{GREEN}Passed: {passed}/{total}{RESET}")
    print(f"{RED}Failed: {failed}/{total} ({failures} failures, {errors} errors){RESET}")
