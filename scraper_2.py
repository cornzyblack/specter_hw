# Import necesary Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging
from typing import List, Dict
import re
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

tqdm.pandas()


def get_social_media_link(scraped_media_list: List, social_media_names: str) -> Dict:

    """
        This method filters out valid Social media handles from a list

        Parameters:
            scraped_media_list (list): The list of scraped URLs from a site
            social_media_names (str): The social media names to filter out from the list

        Returns:
            Dict: A list containing the Social media handles and the respective links from the page if present
    """
    result = {}
    social_media_pattern = re.compile(f"({social_media_names})")
    social_media_platforms = list(
        filter(
            lambda scraped_url: re.search(social_media_pattern, scraped_url),
            scraped_media_list,
        )
    )

    for social_media_platform in social_media_platforms:
        social_media_match = re.search(social_media_pattern, social_media_platform)
        if re.search(social_media_pattern, social_media_platform):
            result[social_media_match.group(1)] = social_media_platform.lower()

    return result


def a_href_checker(domain: str) -> Dict:

    """
        This method gets all hyperlinks from the <a> tag in a particular page/domain

        Parameters:
            domain (str): The domain name or page to Scrape

        Returns:
            bool: A boolean value that indicates if the Social media links on a Domain or page were successfully scraped
            Dict: A list containing the Social media handles and the respective links from the page if present
    """
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
    }

    temp_result = {}
    response = None
    social_media_names = (
        "facebook|twitter|youtube|instagram|linkedin|medium|weibo|snapchat"
    )
    logging.basicConfig(
        filename="scraping.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    try:
        site_url = "https://" + domain
        response = requests.get(
            site_url, allow_redirects=True, timeout=25, headers=HEADERS
        )

    except requests.exceptions.ConnectionError:
        try:
            time.sleep(2)
            site_url = "http://" + domain
            response = requests.get(
                site_url, allow_redirects=True, timeout=25, headers=HEADERS
            )

        except (requests.exceptions.RequestException, Exception) as e:
            print("Error ", e)
            logging.exception(site_url)

    except (requests.exceptions.RequestException, Exception) as e:
        print("Error ", e)
        logging.exception(site_url)

    logging.shutdown()

    if response is not None and response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        page_title = soup.find("title").text

        ans = [
            link.get("href")
            for link in soup.select("a[href]")
            if re.search(
                f"[https]*:*//[www]*\.*({social_media_names})", link.get("href")
            )
        ]
        temp_result = get_social_media_link(ans, social_media_names)
        print(f"{site_url}, {page_title}, {temp_result}")

    final_result = {
        "facebook": None,
        "twitter": None,
        "youtube": None,
        "instagram": None,
        "linkedin": None,
        "medium": None,
        "weibo": None,
        "snapchat": None,
    }
    is_scrape_successful = False if len(temp_result) == 0 else True
    final_result.update(temp_result)

    return is_scrape_successful, list(final_result.values())


def a_href_checker_selenium(domain: str) -> Dict:
    # Start Selenium using Chromium
    options = Options()
    options.headless = True
    page_title = None
    temp_result = {}

    social_media_names = (
        "facebook|twitter|youtube|instagram|linkedin|medium|weibo|snapchat"
    )
    logging.basicConfig(
        filename="scraping.log",
        filemode="a",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    site_url = "http://" + domain
    temp_result = {}
    try:
        driver = webdriver.Chrome("chromedriver/chromedriver.exe", options=options)
        driver.get(site_url)
        time.sleep(10)

        # Get HTML on using Beautifulsoup
        soup = BeautifulSoup(driver.page_source)
        page_title = driver.title

        social_media_names = (
            "facebook|twitter|youtube|instagram|linkedin|medium|weibo|snapchat"
        )

        ans = [
            link.get("href")
            for link in soup.select("a[href]")
            if re.search(
                f"[https]*:*//[www]*\.*({social_media_names})", link.get("href")
            )
        ]
        driver.quit()
        temp_result = get_social_media_link(ans, social_media_names)

    except Exception as e:
        print("Error ", e)
        logging.exception(site_url)

    logging.shutdown()

    time.sleep(1)
    print(f"{domain}, {page_title}, {temp_result}")

    final_result = {
        "facebook": None,
        "twitter": None,
        "youtube": None,
        "instagram": None,
        "linkedin": None,
        "medium": None,
        "weibo": None,
        "snapchat": None,
    }

    final_result.update(temp_result)

    return list(final_result.values())


def main_scraper(domain: str) -> Dict:
    is_scrape_successful, social_media_handles = a_href_checker(domain)
    result = None
    if is_scrape_successful:
        result = social_media_handles
    else:
        result = a_href_checker_selenium(domain)
    return result


if __name__ == "__main__":
    df = pd.read_csv("sample_domains.csv")
    social_media_df_2 = pd.DataFrame(
        df.new_domain.progress_apply(main_scraper).tolist(),
        columns=[
            "facebook",
            "twitter",
            "youtube",
            "instagram",
            "linkedin",
            "medium",
            "weibo",
            "snapchat",
        ],
    )

    df.join(social_media_df_2).to_csv("scraping_results_2.csv", index=False)
    print(f"The results of the Scraping can be found in scraping_results_2.csv file")
