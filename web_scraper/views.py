from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from MySoftwareInitiation import settings


delay = 1  # seconds
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# chrome_options.add_argument("--headless")


# Create your views here.
def archetypes_view(request):
    if settings.SELENIUM_URL:
        driver = webdriver.Remote(settings.SELENIUM_URL,
                                  options=chrome_options)  # For Docker deployment
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options)  # For local deployment

    driver.get(settings.URL_MD_TOP)

    # elements_archetype = WebDriverWait(driver, delay). \
    #     until(EC.presence_of_all_elements_located(
    #     (By.XPATH, '//*[@id="svelte"]/main/div/div[3]/div[7]/div/div/div/div[*]/div/div[1]/div[2]')))

    elements_archetype = \
        driver.find_elements(By.XPATH,
                             '//*[@id="svelte"]/main/div/div[3]/div[7]/div/div/div/div[*]/div/div[1]/div[2]')

    archetypes = [x.text for x in elements_archetype]
    driver.quit()



    context = {
        "archetypes_list": archetypes
    }
    return render(request, "archetypes.html", context)
