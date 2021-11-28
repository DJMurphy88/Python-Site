class Game:
    def __init__(self, gameid, title, image, system, date, genre, complete):
        self.__gameid = gameid
        self.__title = title
        self.__image = image
        self.__system = system
        self.__date = date
        self.__genre = genre
        self.__complete = complete

    def getGameID(self):
        return self.__gameid

    def getTitle(self):
        return self.__title

    def getImage(self):
        return self.__image

    def getSystem(self):
        return self.__system

    def getDate(self):
        return self.__date

    def getGenre(self):
        return self.__genre

    def getComplete(self):
        return self.__complete

class User:
    def __init__(self, userid, username, password):
        self.__userid = userid
        self.__username = username
        self.__password = password

    def getUserID(self):
        return self.__userid

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
