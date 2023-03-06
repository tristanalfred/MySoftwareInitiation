from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager

from MySoftwareInitiation import settings


chrome_options = Options()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--headless")


# Create your views here.
@api_view(['GET'])
def archetypes_view(request):
    """
    View returning the ordered list of archetype actually on the top deck
    """
    if settings.SELENIUM_URL:
        driver = webdriver.Remote(settings.SELENIUM_URL,
                                  options=chrome_options)  # For Docker deployment
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options)  # For local deployment
    driver.get(settings.URL_MD_TOP)

    # Explicit wait to click on "Accept cookies"
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((
            By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p'))).click()

    elements_archetype = \
        driver.find_elements(By.XPATH,
                             '//*[@id="svelte"]/main/div/div[3]/div[7]/div/div/div/div[*]/div/div[1]/div[2]')

    archetypes = [x.text for x in elements_archetype]
    driver.quit()

    context = {
        "archetypes": archetypes
    }

    if "api" in request.GET:
        return Response(status=status.HTTP_200_OK, data=context)
    else:
        return render(request, "archetypes.html", context)

