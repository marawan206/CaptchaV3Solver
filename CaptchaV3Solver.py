import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Constants
CHECK_BOX = ".recaptcha-checkbox-border"
AUDIO_BUTTON = "#recaptcha-audio-button"
AUDIO_SOURCE = "#audio-source"
AUDIO_RESPONSE = "#audio-response"
VERIFY_BUTTON = "#recaptcha-verify-button"
RELOAD_BUTTON = "#recaptcha-reload-button"
AUDIO_ERROR_MESSAGE = ".rc-audiochallenge-error-message"
RECAPTCHA_STATUS = "#recaptcha-accessible-status"
DOSCAPTCHA = ".rc-doscaptcha-body"
MAX_ATTEMPTS = 5
SERVERS = ["https://engageub.pythonanywhere.com", "https://engageub1.pythonanywhere.com"]

# Set up the Selenium driver
driver = webdriver.Chrome()  # Adjust for your browser (e.g., Firefox or Edge)

def is_hidden(element):
    return element.get_attribute("style") == "display: none;"

def get_text_from_audio(url, lang="en-US"):
    for server in SERVERS:
        response = requests.post(server, data={"input": url, "lang": lang})
        if response.ok:
            return response.text
    return None

# Main function to solve recaptcha
def solve_recaptcha():
    attempts = 0
    solved = False
    waiting_for_audio_response = False
    audio_url = None

    while attempts < MAX_ATTEMPTS and not solved:
        try:
            check_box = driver.find_element(By.CSS_SELECTOR, CHECK_BOX)
            check_box.click()
            time.sleep(2)
            
            recaptcha_status = driver.find_element(By.CSS_SELECTOR, RECAPTCHA_STATUS)
            initial_status = recaptcha_status.text if recaptcha_status else ""

            # Click the audio button if available
            audio_button = driver.find_element(By.CSS_SELECTOR, AUDIO_BUTTON)
            if audio_button and not is_hidden(audio_button):
                audio_button.click()

            # Handle the audio challenge
            audio_source = driver.find_element(By.CSS_SELECTOR, AUDIO_SOURCE)
            if audio_source:
                if audio_url != audio_source.get_attribute("src"):
                    audio_url = audio_source.get_attribute("src")
                    response_text = get_text_from_audio(audio_url)

                    if response_text and len(response_text) > 2:
                        audio_response = driver.find_element(By.CSS_SELECTOR, AUDIO_RESPONSE)
                        audio_response.send_keys(response_text)
                        verify_button = driver.find_element(By.CSS_SELECTOR, VERIFY_BUTTON)
                        verify_button.click()
                        solved = True
                    else:
                        reload_button = driver.find_element(By.CSS_SELECTOR, RELOAD_BUTTON)
                        if reload_button:
                            reload_button.click()
                waiting_for_audio_response = False
            else:
                reload_button = driver.find_element(By.CSS_SELECTOR, RELOAD_BUTTON)
                if reload_button:
                    reload_button.click()

            # Check if the captcha is solved
            current_status = recaptcha_status.text if recaptcha_status else ""
            if current_status != initial_status:
                solved = True

        except Exception as e:
            print(f"Error: {e}")
            attempts += 1
            time.sleep(5)
    
    if solved:
        print("Captcha solved successfully!")
    else:
        print("Max attempts reached, failed to solve the captcha.")

# Start solving
solve_recaptcha()
