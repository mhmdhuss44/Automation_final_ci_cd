# Automated Testing Project README

## Introduction
This project focuses on automation testing using CI/CD methodologies for the Global Forest Watch website. Global Forest Watch is an online platform providing real-time data and tools for monitoring forests worldwide. The testing framework encompasses API tests, UI tests, and integrated tests combining both UI and API interactions.

## Website Overview
Global Forest Watch offers a comprehensive suite of tools and data for monitoring and managing forests globally. The platform includes features such as interactive maps, satellite imagery, and data analysis tools aimed at facilitating forest conservation efforts and decision-making processes.

## API Tests Performed
- **User Authentication**: Testing user login functionality.
- **Data Retrieval**: Verifying data retrieval from various endpoints.
- **Data Manipulation**: Adding new areas or modifying and area .

## UI Tests Performed
- **Navigation**: Ensuring smooth navigation across different sections of the website.
- **Form Validation**: Verifying form inputs and error messages.
- **Map Interactions**: Testing functionalities related to map interactions.


## Tools and Technologies Used
- **Selenium**: Used for automating web browser interactions.
- **Selenium Grid**: Employed to execute tests in parallel across different browsers.
- **GitActions**: CI/CD tool utilized for automating the testing process.

### Selenium and Selenium Grid
Selenium is a powerful automation tool for web browser testing. It allows us to simulate user interactions on web pages. Selenium Grid extends this functionality by enabling the parallel execution of tests across multiple browsers and platforms, thus optimizing testing efficiency and coverage.

## CI/CD Setup
GitActions has been employed for setting up the CI/CD pipeline. A YAML file is configured to trigger test execution upon code changes. The test runner script is invoked, initiating the test suite. Once the tests conclude, an HTML report is generated and stored in the artifacts for easy access and analysis.


## Getting Started
To get started with running the tests locally:

1. Clone this repository to your local machine.
2. Install the necessary dependencies listed in `requirements.txt`.
3. Ensure Selenium Grid is set up with desired browser configurations.
4. Run the test suite using the provided test runner script.
5. View the generated HTML report in the artifacts directory for test results.

## Contributors
- moahmmed hussien


    

