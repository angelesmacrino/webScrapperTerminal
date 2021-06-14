import sys, os
from web_scrapper import Parser
import requests, sys
from bs4 import BeautifulSoup

#if len(sys.argv) != 2:
#    print("You should rund the script with the complete url of the webpage")
#    sys.exit()

def main():
    web_to_scrape = Parser("http://books.toscrape.com/index.html")
    program=True
    print("What do you wish to do?\nRead the html(1)\nLook for something in the document(2)\nOptions(3)\nExit(4)")
    while program == True:
        option = input()
        if option == "4":
            program = False
        elif option == "3":
            web_to_scrape.options()
            print(web_to_scrape.save_results)
        elif option == "1":
            web_to_scrape.showHtml()
        elif option == "2":
            web_to_scrape.manipulation()
        
        


    







if __name__ == "__main__":
    main()
    