from tkinter import *
from PIL import ImageTk, Image
from os import *
from TestCase import TestCase
from service.MovieService import MovieService


movieService = MovieService()

window = Tk()
width, height = 800, 700
frame1, frame2, frame3, frame4 = Frame(window), Frame(window), Frame(window), Frame(window)

def before():
    TestCase.createMovies()
    TestCase.createCinemas()
    TestCase.createSchedules()
    TestCase.createSeats()
    TestCase.createTickets()
    
    window.geometry(str(width) + 'x' + str(height))
    window.title('영화예매')
    window.resizable(False, False)

def main():
    
    frame1.pack()

    posterDicts = []
    posterDict = {}

    column, row = 0, 0
    canvasWidth = width / 3
    cnavasHeight = height / 2 - 50

    basePath = path.dirname(path.realpath(__file__))
    movies = movieService.retriveMovieWithPaging(0, 6)
    
    for movie in movies:
        posterPath = movie.posterPath
        moiveName = movie.name

        poster = ImageTk.PhotoImage(Image.open(basePath + posterPath))
        canvas = Canvas(frame1, width=canvasWidth, height=cnavasHeight, background='gray')
        canvas.grid(column = column, row = row)
        canvas.create_image(canvasWidth/2, 125, image=poster)
        canvas.create_text(130, 280, text = moiveName)

        posterDict = {'poster' : poster, 'canvas' : canvas}
        posterDicts.append(posterDict)
        column += 1
        if column >= 3: column = 0; row += 1;

    
    Button(frame1, text='예매하기', height = 4, width = 20).grid(column = 0, row = 2)
    Button(frame1, text='예약확인', height = 4, width = 20).grid(column = 1, row = 2)
    Button(frame1, text='예약취소', height = 4, width = 20).grid(column = 2, row = 2)

    window.mainloop()

    
def after():
    pass

if __name__ == "__main__":
    before()
    main()
    after()
