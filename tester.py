# Get instance
import instaloader
import string
import emoji
import csv
import os
import pandas as pd
L = instaloader.Instaloader()

translator = str.maketrans('', '', string.punctuation)
def give_emoji_free_text(text):
    allchars = [str for str in text.encode('ascii', 'ignore').decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.encode('ascii', 'ignore').decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text
def getFileSize(fileName):
    return os.stat(fileName).st_size



# Login or load session
L.login("vikarjufri", "ahmad123")        # (login)

sizeOfFile = 0
captionlist = []
hashtaglist = []
likeslist = []
commentlist = []
usernamelist = []
# Obtain profile metadata

while sizeOfFile < 1024*1024*100:

    profile_target = instaloader.Profile.from_username(L.context, "vikarjufri")

    hitung = 0
    # Print list of followers
    for follower in profile_target.get_followers():
        followers_target = follower.username
        followers_followers = follower.followers
        profile = instaloader.Profile.from_username(L.context, followers_target)
        #print(type(profile))
    
        for posts in profile.get_posts():
            post = posts.caption
            hashtag = posts.caption_hashtags
            likes = posts.likes
            #comment = posts.comments
            comments = []
            for comment in posts.get_comments():
                comments.append(comment.text.encode('ascii', 'ignore'))
            commentlist.append(comments)
            
            
            if post is not None:
                comments = []
                post = give_emoji_free_text(post)
                post = post.translate(translator).lower().replace('  ','')
                
                if hitung == 0:
                    with open('dataset.csv','a',newline = '') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['username','post','tag','likes','comment'])
                        writer.writerow([followers_target, post, hashtag, likes, commentlist])
                    hitung += 1
                else:
                    with open('dataset.csv','a',newline = '') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([followers_target, post, hashtag, likes, commentlist])
                print("caption: ", post)
                print("hashtag: ", hashtag)
                print("like: ", likes)
                print("comment: ", commentlist)
                print("\n")
    sizeOfFile = getFileSize('dataset.csv')

data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
print(data)
