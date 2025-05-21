from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 

def save_source(url, output_file="page_source.html", wait_time=5):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    # Load time for the page
    print(f"Waiting {wait_time} seconds for the page to fully load...")
    time.sleep(wait_time)

    # Get the page source
    print("Getting page source...")
    page_source = driver.page_source

    # Save the page source to a file
    print(f"Saving page source to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(page_source)

    # Take a screenshot as well to help identify where images are
    screenshot_file = "page_screenshot.png"
    # print(f"Taking a screenshot and saving as {screenshot_file}...")
    driver.save_screenshot(screenshot_file)
    
    # Close the browser
    print("Closing browser...")
    driver.quit()

if __name__ == "__main__":
    website_url = input("Enter the website URL to explore: ")
    wait_seconds = int(input("How many seconds to wait for the page to load? (default: 5): ") or "5")
    output_filename = input("Enter output filename (default: page_source.html): ") or "page_source.html"

    save_source(website_url, output_filename, wait_seconds)