from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
import select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
chrome_options = Options()
chrome_options.add_argument("--headless")
# Set the desired download folder path
download_folder = r""  # Update this path to your desired location

# Basic validation to check if the path exists
if not os.path.exists(download_folder):
    print(f"Error: The folder '{download_folder}' does not exist. Please enter a valid path.")
else:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Create the webdriver object with the desired download path
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # URL
        driver.get("https://www.trademap.org/Bilateral_TS.aspx?nvpm=1%7c020%7c%7c100%7c%7cTOTAL%7c%7c%7c2%7c1%7c1%7c1%7c2%7c1%7c1%7c1%7c1%7c1")
        # Checking if the driver is working
        print(driver.title)

        # Ürün dropdown'unun gelmesini bekle ve seçim yap
        product_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_NavigationControl_DropDownList_Product"))
        )
        select_product = Select(product_select)

        # count countries
        countries_count = len(Select(driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_Country")).options)

        # count partners
        partners_count = len(Select(driver.find_element(By.ID, "ctl00_NavigationControl_DropDownList_Partner")).options)

        # Tüm ürünleri dene
        for product_index in range(1, len(select_product.options)):  # Start from 1 to skip the default option
            product_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ctl00_NavigationControl_DropDownList_Product"))
            )
            select_product.select_by_index(product_index)

            # for loop for each country step by step
            for country_index in range(1, countries_count):  # Start from 1 to skip the default option
                select_country = Select(WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ctl00_NavigationControl_DropDownList_Country"))
                ))

                select_country.select_by_index(country_index)

                # each partner
                for partner_index in range(1, partners_count):  # Start from 1 to skip the default option
                    partner_select = Select(WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "ctl00_NavigationControl_DropDownList_Partner"))
                    ))
                    partner_select.select_by_index(partner_index)

                    trade_type_select = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "ctl00_NavigationControl_DropDownList_TradeType"))
                    )

                    trade_type_dropdown = Select(trade_type_select)
                    trade_type_dropdown.select_by_index(1)  # Click on the first option

                    # click on export button
                    export_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "ctl00_PageContent_GridViewPanelControl_ImageButton_Text"))
                    )
                    export_button.click()

                    # time sleep to download (avoid being banned by the site)
                    time.sleep(5)

    finally:
        # quit a driver
        driver.quit()
        