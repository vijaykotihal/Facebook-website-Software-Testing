Project Description: Facebook Automation Testing
About the Project:
This project is designed to automate functional testing for the Facebook login page using Selenium WebDriver. The purpose is to ensure that essential web elements and functionalities of the Facebook login page are operating correctly. The tests cover key aspects such as page load verification, the presence of the login button, visibility of the "Create New Account" button, and basic scrolling functionality.

Test Cases Included:
Home Page Load Verification (test_home_page_load):

Objective: Verify that the Facebook home page loads correctly by checking if the page title contains "Facebook."
Method: Navigates to the Facebook login page and validates the page title after a brief wait.
Login Button Presence Check (test_login_button_presence):

Objective: Ensure the login button is present and visible on the Facebook login page.
Method: Locates the login button using its name attribute and verifies its presence and visibility.
Create New Account Button Presence (test_create_account_button_presence):

Objective: Validate the presence and visibility of the "Create New Account" button.
Method: Identifies the "Create New Account" button using its XPath and checks that it is displayed.
Scrolling Down Functionality (test_scrolling_down):

Objective: Test the functionality of scrolling down the page.
Method: Uses JavaScript to scroll to the bottom of the page and confirms the scroll action.
Scrolling Up Functionality (test_scrolling_up):

Objective: Test the functionality of scrolling up the page.
Method: Scrolls to the bottom of the page, waits for a short period, and then scrolls back to the top using JavaScript.
Tools and Technologies:
Selenium WebDriver: Automation tool for browser interactions.
Python: Programming language used to write the test scripts.
ChromeDriver: WebDriver for Chrome browser automation.
webdriver_manager: A utility for managing and installing the appropriate version of ChromeDriver.
How to Run the Project:
Install Required Libraries:
Ensure you have Python installed on your system. Then, install the required Python libraries using pip. Open a terminal or command prompt and run the following commands:

bash
Copy code
pip install selenium webdriver-manager
Download and Set Up ChromeDriver:
The webdriver_manager library will automatically download and set up the correct version of ChromeDriver for you, so no additional steps are needed to manually download ChromeDriver.

Prepare the Test Script:
Save the provided Python script in a file named, for example, facebook_test.py.

Run the Tests:
Execute the test script using Python. Open a terminal or command prompt, navigate to the directory where the facebook_test.py file is saved, and run the following command:

bash
Copy code
python facebook_test.py
Review Test Results:
The script will output the results of each test case to the terminal or command prompt. Review the output to determine if all tests have passed or if any failures occurred.

Conclusion:
This project automates key functional tests for the Facebook login page, providing a way to verify the proper operation of important UI elements and interactions. By following the steps above, you can run the tests and ensure that the Facebook login page meets the expected functionality and user experience standards.

