import requests
import configparser
import os

class Client:
    def __init__(self):
        path_current_directory = os.path.dirname(__file__)
        config_path = os.path.join(path_current_directory, 'config', 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_path)
        self.config = config

    def getPortfolio(self,userId):
        url = "{}/getPortfolioStocks".format(self.config['common']['api'])
        data = {"userId":"{}".format(userId)}
        res = requests.post(url,data=data)
        portfolio = res.json()
        return portfolio['data']['ticker_ids']
        

    def getWatchlist(self, userId):
        url = "{}/getWatchListStocks".format(self.config['common']['api'])
        data = {"userId":"{}".format(userId)}
        res = requests.post(url,data=data)
        portfolio = res.json()
        return portfolio['data']['ticker_ids']

    def getAlertlist(self,userId):
        url = "{}/getAlertListStocks".format(self.config['common']['api'])
        data = {"userId":"{}".format(userId)}
        res = requests.post(url,data=data)
        portfolio = res.json()
        return portfolio['data']['ticker_ids']

userId = "ECe46JzLI1639136594141"
cs = Client()
print(cs.getPortfolio(userId))
print(cs.getWatchlist(userId))
print(cs.getWatchlist(userId))