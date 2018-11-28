from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape for weather in Cost Rica
def scrape_weather():

    # Initialize browser
    browser = init_browser()

    # Visit the Chicago climate site
    url = "https://weather-and-climate.com/average-monthly-Rainfall-Temperature-Sunshine-fahrenheit,Chicago,United-States-of-America"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find today's forecast
    forecast_today = soup.find(
        "div", class_="weather-forecasts todays-weather forecast"
    )
    forecast_today

    # Get the max temp
    max_temp = forecast_today.find("span", class_="temp-max").text

    # Print the min temp
    min_temp = forecast_today.find("span", class_="temp-min").text

    # Get current time stamp
    time_stamp = str(datetime.now())

    # Store in dictionary
    weather = {
        "time": time_stamp,
        "name": "Chicago",
        "min_temp": min_temp,
        "max_temp": max_temp,
    }

    # Return results
    return weather


# Function to scrape surf info
# def scrape_surf():

#     # Initialize browser
#     browser = init_browser()

#     # Visit Costa Rica surf site
#     url = "https://www.surfline.com/surf-reports-forecasts-cams/costa-rica/3624060"
#     browser.visit(url)

    # Scrape page into soup
    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")

    # Find today's surf conditions
    # location = soup.find("h3", class_="sl-spot-details__name").get_text()
    # surf_height = soup.find("span", class_="quiver-surf-height").get_text()

    # Store in dictionary
    # surf = {"location": location, "height": surf_height}

    # Return results
    # return surf
# Function to scrape pollution info
# def scrape_pollution():

    # Initialize browser
    # browser = init_browser()

    # Visit air quality site
    # url = "http://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=60607&date=2018-11-25&distance=25&API_KEY=9B10336A-B013-4385-AC09-987F41EE224D"
    # browser.visit(url)

    #Scrape page into soup
    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")

    #Find today's AQI conditions
    # #location = soup.find("h3", class_="sl-spot-details__name").get_text()
    # #surf_height = soup.find("span", class_="quiver-surf-height").get_text()

    #Store in dictionary
    # #airquality = {"particle_pollution": location, "ozone": surf_height}

    # Return results
    # return airquality
