import time
import pygame
import datetime
import bs4 as bs
from urllib.request import urlopen
from pip._vendor.distlib.compat import raw_input

def play_sound():
    pygame.init()
    pygame.mixer.pre_init()
    pygame.mixer.music.load("beep.mp3")
    while 1 == 1:
        pygame.mixer.music.play()
        time.sleep(10)

def main():
    city = raw_input("Enter your city name :: ")
    movie_keyword = raw_input("Enter movie keyword :: ")
    movie_keyword = str(movie_keyword).lower()
    url = "http://in.bookmyshow.com/" + str(city).lower() + "/movies"
    while 1 == 1:
        response = urlopen(url)
        data = response.read()
        soup = bs.BeautifulSoup(data, 'html.parser')
        movie_list = soup.find_all('div', attrs={'class':'card-container wow fadeIn movie-card-container'})

        for movie in movie_list:
            if str(movie).lower().__contains__(movie_keyword):
                play_sound()
                break
        print("Movie keyword " + movie_keyword + " not found at " + str(datetime.datetime.now()))
        time.sleep(5 * 60)
if __name__ == '__main__': main()




