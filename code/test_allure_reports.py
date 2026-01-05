"""
Docstring for code.test_allure_reports

Allure Reports
------------------

step 1: Install Allure Pytest Plugin
        uv add allure-pytest
step 2: Install Allure Command-Line  Tool ( to view and generate reports)
        Windows : https://github.com/allure-framework/allure2/releases 
        Mac: brew install allure
        Linux : sudo apt update
                sudo apt install allure


        
step 3: Configure  Allure in pytest.ini
        [pytest]

        addopts = --alluredir=reports/allure-results
Step 4: Create and Run Your Tests

Step 5: Generate and View the Allure Report

Run time:
	allure serve reports/allure-results

Permanent report:
	allure generate reports/allure-results -o reports/allure-report --clean
	
	

Step 6: Attach Screenshots on Test Failures (conftest.py)


allure generate reports/allure-results -o allure-report --clean

cd allure-report
python3 -m http.server 8080

"""
