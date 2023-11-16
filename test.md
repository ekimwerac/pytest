

```markdown
# Python unittest: Example of a Calculator class

## Calculator Class (`calculator/calculator.py`):

```python
# calculator/calculator.py

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
```

## Test Cases (`tests/test_calculator.py`):

```python
# tests/test_calculator.py
import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Optional: Set up resources before each test
        pass

    def tearDown(self):
        # Optional: Clean up resources after each test
        pass

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 7)
        self.assertEqual(result, 14)

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(8, 2)
        self.assertEqual(result, 4)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

## Test Runner (`run_tests.py`):

```python
# run_tests.py
import unittest

# Discover and run the tests
if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
```

### Execution:

To run the tests, execute the `run_tests.py` script. This script will discover and run all test files in the `tests` directory, including `test_calculator.py`. The directory structure allows for a clear separation between the source code and the test code, making it easy to manage and organize the project.
```