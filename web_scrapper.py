from bs4 import BeautifulSoup
import requests

class Parser:

    def __init__(self, url):
        self.save_results = False
        response = requests.get(url)
        htmlToText = response.text 
        self.html = response.content
        self.parsed_html = BeautifulSoup(self.html, 'html.parser')
        self.parsed_txt = BeautifulSoup(htmlToText)
    def options(self):
        options = input("Do you wish to print your search results? (y/n)").lower()
        if options == "y":
            self.save_results = True
        else:
            self.save_results = False

    def showHtml(self):
        print(self.parsed_html)
        if self.save_results == True:
            try:
                with open("html.txt", "w") as file:
                    file.write(str(self.parsed_txt))
            except Exception as e:
                print(e)                  
        print("What do you wish to do?\nRead the html(1)\nLook for something in the document(2)\nOptions(3)\nExit(4)")

    def manipulation(self):
        manipulation_bool = True
        while manipulation_bool == True:
            print("findalldiv          print all the semantic elements in the document")
            print("findallclass       print all the classes in the document")
            print("findallid      print all the ids in the document")
            print("press x to finish")
            command = input().lower()
            if command == "x":
                print("What do you wish to do?\nRead the html(1)\nLook for something in the document(2)\nOptions(3)\nExit(4)")
                manipulation_bool = False
            elif command == "findalldiv":
                self.find_all_divs()
            elif command == "findallclass":
                self.find_all_classes()
            elif command == "findallid":
                self.find_all_id()

    def find_all_divs(self):
        tags= set()
        program = True
        while program == True:
            for counter, tag in enumerate(self.parsed_html.find_all()):
                if tag.name == "body":
                    for tag in self.parsed_html.find_all()[counter + 1:]:
                        tags.add(tag.name)
                    if self.save_results == True:
                        with open("divisions.txt", "w") as file:
                            file.write(str(tags))
                    print(tags)
                    program = False

    def find_all_id(self):
        id_list = set() 
        tags = {tag.name for tag in self.parsed_html.find_all()}
        for tag in tags:
            for i in self.parsed_html.find_all( tag ):
                if i.has_attr( "id" ):
                    if len( i['id'] ) != 0:
                        id_list.add("".join( i['id']))
        if self.save_results == True:
            with open("ids.txt", "w") as file:
                file.write(str(id_list))
        print(id_list) 

    def find_all_classes(self):
        tags = {tag.name for tag in self.parsed_html.find_all()}
        class_list = set()
        for tag in tags:  
            for i in self.parsed_html.find_all( tag ):  
                if i.has_attr( "class" ): 
                    if len( i['class'] ) != 0:
                        class_list.add("".join( i['class']))
        if self.save_results == True:
            with open("ids.txt", "w") as file:
                file.write(str(class_list))
        print(class_list)       
                    



    
        