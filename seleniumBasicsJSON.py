import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
url = 'https://data.vsin.com/linetracker/?sportid=cbb'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Locate the table body using XPath
tbody_xpath = '/html/body/div[6]/div[2]/div/div[2]/div/div/div/div[4]/div/table/tbody[1]'
tbody = driver.find_element(By.XPATH, tbody_xpath)

# Initialize an empty list to hold all rows of data
data = []

# Extract data from each row
rows = tbody.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    cell_data = [cell.text for cell in cells]
    # Here we assume each row has the same number of cells and there are no headers provided.
    # If there are headers, they should be extracted similarly and used as keys for the dictionaries.
    row_data = {'Column{}'.format(index+1): value for index, value in enumerate(cell_data)}
    data.append(row_data)

# Close the WebDriver
driver.quit()

# Write the data to a JSON file
with open('output_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
