import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize colorama for colored output in the terminal
init(autoreset=True)

# Load environment variables from a .env file
load_dotenv()

# Retrieve Facebook credentials from environment variables
FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASS = os.getenv('FB_PASS')

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--user-agent=Mozilla/5.0")

# Set the path to the ChromeDriver executable
webdriver_service = Service('./driver/chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)


def delay(seconds):
    """Pause execution for a given number of seconds."""
    time.sleep(seconds)


def scroll_to_element(element):
    """Scroll the page to bring the specified element into view."""
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", element)


try:
    print(Fore.GREEN + 'Logging in...')

    # Open Facebook login page
    driver.get('https://www.facebook.com/')
    WebDriverWait(driver, 20).until(EC.title_contains('Facebook'))
    

    # Perform login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))).send_keys(FB_EMAIL)
    driver.find_element(By.ID, 'pass').send_keys(FB_PASS)
    driver.find_element(By.NAME, 'login').click()
    WebDriverWait(driver, 20).until(EC.url_contains('facebook.com'))
    print(Fore.GREEN + 'Logged in. Navigating to Pokes page...')
    

    # Navigate to the Pokes page
    driver.get('https://www.facebook.com/pokes')
    print(Fore.GREEN + 'Opening Pokes page...')
    WebDriverWait(driver, 20).until(EC.title_contains('Pokes'))

    while True:
        try:
            # Find all "Poke Back" buttons on the page
            poke_back_buttons = WebDriverWait(driver, 1).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//div[@aria-label="Poke Back"]'))
            )

            users_to_poke_back = len(poke_back_buttons)
            print(Fore.YELLOW + f'Found {users_to_poke_back} user{
                  "" if users_to_poke_back == 1 else "s"} to poke back')

            if users_to_poke_back > 0:
                for i, button in enumerate(poke_back_buttons, start=1):
                    try:
                        scroll_to_element(button)
                        WebDriverWait(driver, 1).until(
                            EC.element_to_be_clickable(button))
                        driver.execute_script("arguments[0].click();", button)
                        print(Fore.CYAN + f'[{i}] Poked back!')
                    except Exception as e:
                        print(
                            Fore.RED + f'Error clicking button: {e.__class__.__name__}: {str(e)}')
            else:
                print(Fore.YELLOW + 'No pokes to return.')

            delay(0.5)
            print(Fore.YELLOW + 'Rechecking for users to poke back...')

        except Exception as e:
            print(Fore.RED + 'No User to Poke Back!' )
            delay(0.5)
            continue

except Exception as e:
    print(Fore.RED + 'Error in script: ' + str(e))

finally:
    driver.quit()
