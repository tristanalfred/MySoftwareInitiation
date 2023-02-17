from rest_framework.response import Response
from rest_framework import viewsets, status

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from MySoftwareInitiation import settings

delay = 3  # seconds
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")


class CheckApi(viewsets.ViewSet):
    """
    View returning 200 to check if an API works correctly
    """

    def list(self, _request):
        return Response(status=status.HTTP_200_OK)


class WebScrapingArchetypes(viewsets.ViewSet):
    """
    View returning the ordered list of archetype actually on the top deck
    """

    def list(self, _request):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options)
        driver.get(settings.URL_MD_TOP)

        elements_archetype = WebDriverWait(driver, delay). \
            until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@id="svelte"]/main/div/div[3]/div[7]/div/div/div/div[*]/div/div[1]/div[2]')))

        archetypes = [x.text for x in elements_archetype]

        return Response(status=status.HTTP_200_OK, data={'archetypes': archetypes})
