# Selenium Testing Project

This project is designed for automated testing using Selenium with a structured approach utilizing the Page Object Model (POM). It connects to a Selenium Grid for executing tests across different browsers.

## Project Structure

```
selenium-testing-project
├── tests
│   └── test_main.py
├── utilities
│   └── driver_factory.py
├── pageobjects
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── base_page.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd selenium-testing-project
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Start Selenium Grid**:
   Make sure you have Selenium Grid running at `http://127.0.0.1:4444/wd/hub`. You can start it using Docker:
   ```
   docker run -d -p 4444:4444 --name selenium-grid selenium/standalone-chrome
   ```

## Usage

To run the tests, execute the main test file:
```
pytest
```

To run the tests with output JUnit XML files
```
pytest --junitxml=fileName.xml
```

## Selenium Grid & noVNC

[Selenium Grid](https://www.selenium.dev/documentation/grid/) allows you to run tests on multiple machines and browsers in parallel. The [chrome-selenium standalone Docker image](https://hub.docker.com/r/selenium/standalone-chrome) provides an all-in-one solution with Chrome and a built-in VNC server. [noVNC](https://novnc.com/info.html) lets you view the browser UI in your web browser for debugging.

## Docker Setup (Windows & Linux)

1. **Pull the Docker image:**
   ```sh
   docker pull selenium/standalone-chrome
   ```

2. **Start the container (ports 4444 for WebDriver, 7900 for noVNC):**
   ```sh
   docker run -d -p 4444:4444 -p 7900:7900 --name selenium-chrome selenium/standalone-chrome
   ```
   - Access Selenium Grid at: http://localhost:4444
   - Access noVNC (browser UI): http://localhost:7900 (password: `secret`)

3. **Stop the container:**
   ```sh
   docker stop selenium-chrome
   docker rm selenium-chrome
   ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.