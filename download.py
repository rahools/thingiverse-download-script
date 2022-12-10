# %%
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from tqdm import tqdm

# ---------------- #
# --- settings --- #
# ---------------- #
THING_CODES = [2035221]
DOWNLOAD_LOCALTION = "D:\\code\\thingiverse-download\\downloads"
DOWNLOAD_XPATH = "/html/body/div/div/div/div/div/div/div/div/div/div/div/span/div"

# %%
# ---------------- #
# --- helpers ---- #
# ---------------- #
def get_driver():
    global DOWNLOAD_LOCALTION

    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", DOWNLOAD_LOCALTION)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    # for some reason, using webdriver.Firefox() doesn't work
    # and webdriver.Chrome() does.
    # driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
    driver = webdriver.Chrome(GeckoDriverManager().install(), options=options)
    driver.implicitly_wait(10)

    return driver

def get_thing_urls():
    global THING_CODES

    if isinstance(THING_CODES, int):
        THING_CODES = [THING_CODES]

    return [f"https://www.thingiverse.com/thing:{code}/files" for code in THING_CODES]

def download_things(driver: webdriver.Firefox, url: str):
    global DOWNLOAD_XPATH
    
    driver.get(url)
    time.sleep(1)

    download_buttons = driver.find_elements("xpath", DOWNLOAD_XPATH)
    for download_button in tqdm(download_buttons):
        download_button.click()
        time.sleep(.25)

# %%
def main():
    driver = get_driver()
    thing_urls = get_thing_urls()

    for thing_url in tqdm(thing_urls):
        download_things(driver, thing_url)

    driver.quit()

# %%
if __name__ == "__main__":
    main()