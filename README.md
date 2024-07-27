# Python Learning

Below are the key topics to learn in Python:

- **Python Basics**
  - Introduction to Python
  - Installation and Setup
  - Running Python Programs
  - Python Syntax
  - Variables and Data Types
  - Basic Operators
  - Control Flow
    - If Statements
    - Loops (For, While)

- **Functions**
  - Defining Functions
  - Function Arguments
  - Return Statement
  - Lambda Functions
  - Map, Filter, and Reduce Functions
  - Recursion

- **Strings**
  - Formatting Strings

- **Data Structures**
  - Lists
  - Tuples
  - Dictionaries
  - Sets
  
- **Modules and Packages**
  - Importing Modules
  - Standard Library Modules
  - Creating and Using Packages

- **File Handling**
  - Reading and Writing Files
  - Working with CSV and JSON Files

- **Error and Exception Handling**
  - Try, Except Blocks
  - Finally and Else Clauses
  - Custom Exceptions

- **Object-Oriented Programming (OOP)**
  - Classes and Objects
  - Inheritance
  - Polymorphism
  - Encapsulation
  - Method Overriding

### How to Work with the PyTest?

 - pip install pytest
 - File name - test_name.py
 - Test name - test_name_of_test():
 - Assert - Actual Result == Expected Result.

### How to run the PyTest?

 - Open cmd -> Go the folder -> pytest
 - run icon

### PyTest Commands

 - pytest -h
 - To run all the testcases
   - pytest
 - To run specific testcase
   - pytest Ex_22072024/test_Lab172.py
 - To run specific testcase with pattern
   - pytest -k "17"
 - To run a specific marked Testcase
   - Add an annotation @pytest.mark.smoke
   - pytest -m "smoke" Ex_22072024/test_Lab173.py

### How to see the Report of the PyTest Testcases?

  - Download the Node.js
    - node -v
  - Install allure-commandline
    - npm install -g allure-commandline
  - Verify that allure -> options
      - allure
  - Run your Pytest TestCase 
    - pytest Ex_22072024/test_Lab174.py --alluredir=allure_result
    - allure serve allure_result

