
**Main Features of Python 3 pytest with Examples:**

Let's create a simple calculator class and organize it in a way that follows good practices for testing.

1. **Directory Structure:**
   - `calculator_app/`
     - `calculator.py`
     - `tests/`
       - `test_calculator.py`

2. **calculator.py:**
   ```python
   # calculator.py

   class Calculator:
       def add(self, x, y):
           return x + y

       def subtract(self, x, y):
           return x - y

       def multiply(self, x, y):
           return x * y

       def divide(self, x, y):
           if y != 0:
               return x / y
           else:
               raise ValueError("Cannot divide by zero.")
   ```
   This is the main code for the calculator application.

3. **test_calculator.py:**
   ```python
   # tests/test_calculator.py
   from ..calculator import Calculator
   import pytest

   @pytest.fixture
   def calculator():
       return Calculator()

   def test_add(calculator):
       assert calculator.add(2, 3) == 5

   def test_subtract(calculator):
       assert calculator.subtract(5, 3) == 2

   def test_multiply(calculator):
       assert calculator.multiply(2, 3) == 6

   def test_divide(calculator):
       assert calculator.divide(6, 3) == 2
       with pytest.raises(ValueError):
           calculator.divide(1, 0)
   ```
   The `test_calculator.py` file contains test functions using the `pytest` framework. Each test function starts with "test_" and uses the `calculator` fixture to create an instance of the Calculator class.

4. **Running Tests:**
   - Open a terminal and navigate to the `calculator_app/` directory.
   - Run the tests using the following command:
     ```
     pytest
     ```
   This will discover and run all the tests in the `tests/` directory.

5. **Key Features and Explanations:**
   - **Fixture (`@pytest.fixture`):** Fixtures are used to set up preconditions for your tests. In this case, the `calculator` fixture provides an instance of the Calculator class for each test function.

   - **Assertions:** The `assert` statements are used to verify that the actual results match the expected results. If an assertion fails, pytest will raise an exception, indicating a test failure.

   - **Parametrized Tests (not shown in this example):** Pytest allows you to write parametrized tests to run the same test logic with different inputs.

   - **Test Discovery:** Pytest automatically discovers and runs test functions based on naming conventions. Test functions must start with "test_" to be considered by pytest.

   - **Test Organization:** Structuring tests in a separate `tests/` directory makes it easy to differentiate between production code and test code.

   - **Selective Test Execution:** You can run specific tests by providing the test file or test name as a command-line argument to pytest.

   - **Exception Handling:** The `pytest.raises` context manager is used to check whether a specific exception is raised during the execution of a test.

These are some of the key features of using pytest for testing Python code. The example demonstrates a simple test suite for a calculator class, and you can expand on this foundation for more complex projects.