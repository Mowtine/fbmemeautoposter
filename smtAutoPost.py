import facebook
from PIL import Image
import requests
from io import BytesIO
import datetime
from goodMeme import findMeme


accessToken = '<FB access token>'


def PostNewMeme(imgURL):
    fb = facebook.GraphAPI(access_token=accessToken)
    # Get the current date
    curDate = datetime.date.today().strftime("%B %d, %Y")

    # Post the photo
    imgResponce = requests.get(imgURL)
    imageFile = Image.open(BytesIO(imgResponce.content))
    fb.put_photo(image=imgResponce.content,message=curDate + ' Meme of the day. <Add call to action>')




if __name__ == '__main__':

    # Ask for a subreddit to check
    sbrdt = input("From what subreddit? (Press Enter for default): ")

    # run the find meme
    imgURL = findMeme(sbrdt, 10)

    # Post the selected meme
    PostNewMeme(imgURL)
