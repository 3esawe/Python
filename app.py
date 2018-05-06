def user ():
    UI = input ("enter m to add movie , t to add type , d to add day , s to stop: ")
    while UI !=  's' :
        if UI == 'm':
            addmovie()
        elif UI == 't':
            printList()
        elif UI == 'd':
            print(get())
        else:
            print("you typed wrong later")
            break

        UI = input("enter m to add movie , t to add type , d to add day , s to stop: ")




movieDict = dict()
movieList = list()
def addmovie():

    input_movie_name = input("add your movie name\n")
    movieDict["name"]= input_movie_name
    input_movie_type = input("add your movie type\n")
    movieDict["type"]= input_movie_type
    input_movie_date = input("add your movie date\n")
    movieDict["date"]= input_movie_date
    movieList.append(dict(movieDict))
    return movieList

def printList() :
    for i in movieList:
        print(i)
def get():
    key = input("Enter name or type or date")
    value = input("What you are looking for: ")
    foud= []
    for movie in movieDict :
        if movieDict[key] == value:
            foud.append(movie)
    return foud
user()
print("just to commit")
