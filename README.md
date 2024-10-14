# reCAPTCHA Solver (Python)

### Overview
This Python script automates the solving of Google reCAPTCHA audio challenges using Selenium for browser interaction and external services for audio transcription. It is designed for **educational purposes** only as part of a **personal project**. Use it responsibly and **do not abuse any website**.

### Features
- Automates reCAPTCHA checkbox selection and audio challenge solving.
- Transcribes the audio challenge via external servers.
- Handles retries and reloads on failed attempts.

### Requirements
- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [Requests](https://docs.python-requests.org/)
- A web driver (e.g., ChromeDriver or GeckoDriver)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/marawan206/CaptchaV3Solver
   ```

2. Install the dependencies:
   ```bash
   pip install selenium requests
   ```

3. Download and install the appropriate web driver:
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome.
   - [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

### Usage

1. Update the script to set up your preferred browser (Chrome, Firefox, etc.).
2. Run the script:
   ```bash
   python CaptchaV3Solver.py
   ```

### Disclaimer
This project is solely for **educational purposes**. **Do not use it to abuse websites** or violate any terms of service. Misuse of this tool may result in website blocks or legal consequences.

### License
This project is licensed under the MIT License.
