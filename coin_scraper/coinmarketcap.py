from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class CoinMarketCap:
    @staticmethod
    def scrape_coin_data(coin):
        # Initialize Edge WebDriver service with the specified path
        service = EdgeService(EdgeChromiumDriverManager().install())

        # Initialize Edge WebDriver with the service
        driver = webdriver.Edge(service=service)

        # Form the URL
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        driver.get(url)
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Scrape data using XPath
        try:
            price_xpath = '//*[@id="section-coin-overview"]/div[2]/span'
            price_change_xpath = '//*[@id="section-coin-overview"]/div[2]/div/div/p'
            market_cap_xpath = '//*[@id="section-coin-stats"]/div/dl/div[1]/div[1]/dd'
            market_cap_rank_xpath = '//*[@id="section-coin-stats"]/div/dl/div[1]/div[2]/div/span'
            volume_24h_xpath = '//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd'
            volume_rank_xpath = '//*[@id="section-coin-stats"]/div/dl/div[2]/div[2]/div/span'
            volume_change_xpath = '//*[@id="section-coin-stats"]/div/dl/div[2]/div[1]/dd/div/p'
            circulating_supply_xpath = '//*[@id="section-coin-stats"]/div/dl/div[4]/div/dd'
            total_supply_xpath = '//*[@id="section-coin-stats"]/div/dl/div[5]/div/dd'
            diluted_market_cap_xpath = '//*[@id="section-coin-stats"]/div/dl/div[7]/div/dd'
            contracts_name_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div/a/span[1]'
            contracts_address_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div/a'
            official_links_name_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div/div/a'
            official_links_link_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div/div/a'
            twitter_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[1]/a'
            telegram_xpath = '//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[2]/a'

            price = driver.find_element(By.XPATH, price_xpath).text.strip()
            price_change = driver.find_element(By.XPATH, price_change_xpath).text.strip()
            market_cap = driver.find_element(By.XPATH, market_cap_xpath).text.strip()
            market_cap_rank = driver.find_element(By.XPATH, market_cap_rank_xpath).text.strip()
            volume_24h = driver.find_element(By.XPATH, volume_24h_xpath).text.strip()
            volume_rank = driver.find_element(By.XPATH, volume_rank_xpath).text.strip()
            volume_change = driver.find_element(By.XPATH, volume_change_xpath).text.strip()
            circulating_supply = driver.find_element(By.XPATH, circulating_supply_xpath).text.strip()
            total_supply = driver.find_element(By.XPATH, total_supply_xpath).text.strip()
            diluted_market_cap = driver.find_element(By.XPATH, diluted_market_cap_xpath).text.strip()
            contracts_name = driver.find_element(By.XPATH, contracts_name_xpath).text.strip()
            contracts_address = driver.find_element(By.XPATH, contracts_address_xpath).text.strip()
            official_links_name = driver.find_element(By.XPATH, official_links_name_xpath).text.strip()
            official_links_link = driver.find_element(By.XPATH, official_links_link_xpath).get_attribute('href')
            twitter = driver.find_element(By.XPATH, twitter_xpath).get_attribute('href')
            telegram = driver.find_element(By.XPATH, telegram_xpath).get_attribute('href')

            scraped_data = {
                "name": coin,
                "price": price,
                "price_change": price_change,
                "market_cap": market_cap,
                "market_cap_rank": market_cap_rank,
                "volume_24h": volume_24h,
                "volume_rank": volume_rank,
                "volume_change": volume_change,
                "circulating_supply": circulating_supply,
                "total_supply": total_supply,
                "diluted_market_cap": diluted_market_cap,
                "contracts": {"name": contracts_name, "address": contracts_address},
                "official_links": {"name": official_links_name, "link": official_links_link},
                "twitter": twitter,
                "telegram": telegram
            }
        except Exception as e:
            scraped_data = {"error": str(e)}

        # Close WebDriver
        driver.quit()

        return scraped_data
