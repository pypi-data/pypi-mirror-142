# importing libraries
from bs4 import BeautifulSoup
import requests
 
class WebScraper():
    def __init__(self,URL):
        HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
 
        # Making the HTTP Request
        self.webpage = requests.get(URL, headers=HEADERS)
 
        # Creating the Soup Object containing all data
        self.soup = BeautifulSoup(self.webpage.content, "lxml")
 
        # retrieving product title
    def title(self):
        try:
        # Outer Tag Object
            title = self.soup.find("span",attrs={"id": 'productTitle'})
 
        # Inner NavigableString Object
            title_value = title.string
 
        # Title as a string value
            title_string = title_value.strip().replace(',', '')
 
        except AttributeError:
            title_string = "NA"
        return title_string
 
    def price(self):
        try:
            price = self.soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace('$', '')
        except AttributeError:
            price = "NA"
        return price
 
    # saving

 
    def rating(self):
        try:
            rating = self.soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
 
        except AttributeError:
 
            try:
                rating = self.soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
            except:
                rating = "NA"
        return rating
 
    def total_reviews(self):
 
        try:
            review_count = self.soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
 
        except AttributeError:
            review_count = "NA"
        return review_count

    def availability(self):
    # print availablility status
        try:
            available = self.soup.find("div", attrs={'id': 'availability'})
            available = available.find("span").string.strip().replace(',', '')
 
        except AttributeError:
            available = "NA"
        return available
 

 

page=WebScraper("https://www.amazon.com/AmazonBasics-6-Outlet-Protector-2-Pack-2-Foot/dp/B014EKQ5AA/ref=sr_1_1?brr=1&pd_rd_r=31315fc7-f601-4807-b4a2-4b1bc5d4e9b1&pd_rd_w=B5bo5&pd_rd_wg=TfV4X&pf_rd_p=e728773e-6bba-409c-b2ea-ef5cac1c0edf&pf_rd_r=WASH7ZBXN8KXRD0D27H4&qid=1647205057&rd=1&s=electronics&sr=1-1&th=1")

print(page.title())