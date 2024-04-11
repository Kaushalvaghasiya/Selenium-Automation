from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

def visit_link(link_url):
    driver = webdriver.Chrome()
    driver.get(link_url)
    time.sleep(5)
    driver.quit()

url = 'https://www.logiclitz.com'

driver = webdriver.Chrome()

# Navigate to the webpage
driver.get(url)

pagination_element = driver.find_element(By.CLASS_NAME, 'pagination')
page_number_elements = pagination_element.find_elements(By.CLASS_NAME, 'page-numbers')
max_page_num = max([int(page_number.text) for page_number in page_number_elements if page_number.text.isdigit()])

thread_count = 0
max_thread_count = 5
base_url = 'https://www.logiclitz.com/page/'

threads = []

for page_num in range(1, max_page_num + 1):  # Update range to include max_page_num
    page_url = f"{base_url}{page_num}/"
    driver.get(page_url)
    
    # Find all the links on the webpage
    links = driver.find_elements(By.TAG_NAME, 'a')
    
    # Iterate through each link and visit it if it contains an image
    for link in links:
        # Get the URL of the link
        link_url = link.get_attribute('href')
        
        # Check if the link contains an image
        if link.find_elements(By.TAG_NAME, 'img'):
            # Create a thread to visit the link
            thread = threading.Thread(target=visit_link, args=(link_url,))
            threads.append(thread)
            thread.start()
            thread_count += 1
            
            # Check if the maximum thread count is reached
            if thread_count >= max_thread_count:
                # Wait for the threads to finish before starting new ones
                for thread in threads:
                    thread.join()
                threads = []
                thread_count = 0

# Join the remaining threads
for thread in threads:
    thread.join()

# Close the WebDriver instance
driver.quit()
