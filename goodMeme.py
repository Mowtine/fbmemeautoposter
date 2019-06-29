import praw
import webbrowser
from PIL import Image
import requests
from io import BytesIO

# Finds a meme from the subreddit sbrdt. A reddit account with a secret and
# client ID needs to be added manually.
# Inputs: subreddit name, quantity of memes displayed to select from.
# Returns URL of the image file to the selected meme
def findMeme(sbrdt, quant):
    secret = '<user secret>'
    clientId = '<client ID>'
    reddit = praw.Reddit(user_agent='Super',
                     client_id=clientId, client_secret=secret,
                     username='<username>',password='<passrod>')

    # Selects defualt subreddit if not inputed.
    if sbrdt == '':
        sbrdt = 'dankmemes'


    subreddit = reddit.subreddit(sbrdt)
    hot_memes = subreddit.hot(limit=(quant+5))

    # Get memes
    imgs = []
    urls = []
    for submission in hot_memes:
        if not submission.stickied and len(urls)<quant:
            response = requests.get(submission.url)
            urls.append(submission.url)
            imgs.append(Image.open(BytesIO(response.content)))


    # Create big image
    lrgImg = Image.new('RGBA',(min(len(imgs),5)*400, (1+len(imgs)//6)*400))
    # join the images and show them
    for indx in range(len(imgs)):
        imgs[indx] = imgs[indx].resize((400,400))
        lrgImg.paste(imgs[indx],(indx%5*400,(indx//5)*400))

    lrgImg.show()

    # select the image we want.
    urlreturn = input('Which image to return (select index): ')
    urlreturn = int(urlreturn) - 1
    return urls[urlreturn]





if __name__ == '__main__':
    # run the post meme
    findMeme('',10)
