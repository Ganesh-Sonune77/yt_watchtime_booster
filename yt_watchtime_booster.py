
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Example: open YouTube video
driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
time.sleep(60)  # Simulate watch time

driver.quit()
