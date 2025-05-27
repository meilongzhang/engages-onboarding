import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suites = []
    for subfolder in ['python', 'ml', 'deep_learning']:
        suite = loader.discover(f'{subfolder}/tests')
        suites.append(suite)

    all_tests = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_tests)
