# Sauce Demo Selenium Python Framework

This repository contains an automated testing framework for the Sauce Demo website using Selenium with Python. The framework is built using the Page Object Model (POM) design pattern, which makes the test code more maintainable, reusable, and readable.

## Project Structure

```
├── pages/
│   ├── actions/
│   │   └── login_page.py         # Page actions/methods for login functionality
│   └── locators/
│       └── login_locators.py     # Element locators for login page
├── tests/
│   └── test_login.py            # Test cases for login functionality
├── utils/
│   └── test_data.py            # Test data management
├── conftest.py                  # PyTest configurations and fixtures
└── requirements.txt            # Project dependencies
```

## Technologies Used

- **Python**: Programming language used for test automation
- **Selenium**: Web automation framework
- **PyTest**: Testing framework for writing and running tests
- **Webdriver Manager**: Automated driver management for Selenium

## Prerequisites

- Python 3.x
- Chrome browser
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/taqirazaj/saucedemo-selenium-python.git
   cd saucedemo-selenium-python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Verify that all required packages are installed:
   ```bash
   pip install selenium==4.19.0
   pip install pytest
   pip install webdriver-manager
   ```
   
   These packages are already listed in `requirements.txt`, but you can install them individually if needed.

3. Configure VS Code Python Interpreter:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type and select `Python: Select Interpreter`
   - Choose the Python interpreter that points to your virtual environment (it should include `.venv` or `venv` in the path)
   - This ensures VS Code uses the correct Python environment with all installed dependencies

4. Enable PyTest in VS Code (Optional):
   - Press `Ctrl+Shift+P` to open the command palette
   - Type and select `Python: Configure Tests`
   - Choose `pytest` as the test framework
   - Select the `tests` folder when prompted
   - VS Code will create `.vscode/settings.json` with PyTest configuration
   - This enables the VS Code Test Explorer UI for easy test execution and debugging

## Framework Architecture

### Page Object Model (POM)

This framework implements the Page Object Model design pattern, which provides the following benefits:

1. **Separation of Concerns**: 
   - Test code is separated from page-specific code
   - Each page has its own class with related actions and locators

2. **Code Reusability**:
   - Page objects can be reused across multiple test cases
   - Reduces code duplication

3. **Easy Maintenance**:
   - Locators are stored in separate files
   - Changes to the UI only require updates in one place

### Framework Components

1. **Pages Package**:
   - `actions/`: Contains page classes with methods representing actions that can be performed on each page
   - `locators/`: Contains classes with element locators for each page

2. **Tests Package**:
   - Contains test files organized by functionality
   - Each test file focuses on specific features or scenarios

3. **Utils Package**:
   - Contains utility functions and test data management
   - Helps in maintaining test data separately from test logic

4. **conftest.py**:
   - Contains PyTest fixtures and configurations
   - Manages WebDriver setup and teardown
   - Handles browser configurations

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test file:
```bash
pytest tests/test_login.py
```

To run tests with detailed output:
```bash
pytest -v
```

## Best Practices Implemented

1. **Driver Management**:
   - Using WebDriver Manager for automated driver updates
   - Centralized driver configuration in conftest.py

2. **Code Organization**:
   - Clear separation of test code, page objects, and configurations
   - Modular and maintainable structure

3. **Locator Strategy**:
   - Locators are maintained separately for better maintenance
   - Using appropriate locator methods (ID, CSS, XPath, etc.)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details