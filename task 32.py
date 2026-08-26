#Write the constructor and the getBookInfo() method for the Book class.
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def getBookInfo(self):
         return f"Title: [{self.title}], Author: [{self.author}], Year: [{self.year}]"
obj=Book("Rich Dad Poor Dad","Robert Kiyosaki, Sharon Lechter",1997)
print(obj.getBookInfo())
