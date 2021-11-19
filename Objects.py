class Game:
    def __init__(self, title, image, system, date, genre, complete):
        self.__title__ = title
        self.__image__ = image
        self.__system__ = system
        self.__date__ = date
        self.__genre__ = genre
        self.__complete__ = complete

    def getTitle(self):
        return self.__title__

    def getImage(self):
        return self.__image__

    def getSystem(self):
        return self.__system__

    def getDate(self):
        return self.__date__

    def getGenre(self):
        return self.__genre__

    def getComplete(self):
        return self.__complete__
