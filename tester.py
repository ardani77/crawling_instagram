# Get instance
import instaloader, string, emoji, os, csv, pandas as pd
from prompt_toolkit import prompt
L = instaloader.Instaloader()

translator = str.maketrans('', '', string.punctuation)
def give_emoji_free_text(text):
    allchars = [str for str in text.encode('ascii', 'ignore').decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.encode('ascii', 'ignore').decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text
def getFileSize(fileName):
    return os.stat(fileName).st_size

def tabel2(namafile, username, caption):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        print('masuk try')
        dataset = pd.read_csv(namafile)
        output = {}
        pairing = []
        print(caption)
        for i in range(len(caption)):
            if len(caption[i]) == 1:
                caption[i].append('')
            post = caption[i]
            #print(post)
            #print("TIPE: " + str(type(caption)))
            split = post.split() #Untuk membuat string bisa diakses lewat index --> contoh: 'saya mau makan' akan menjadi ['saya', 'mau', 'makan']. Dipisah berdasarkan ada space atau tidak
            #print(split)
            for length in range(len(split)-1):
                real_pairing = []
                merge = split[length] + ' ' + split[length+1]
                real_pairing.append(username)
                real_pairing.append(split[length])
                real_pairing.append(split[length+1])
                if real_pairing not in pairing:
                    pairing.append(bantu)
                if merge in done.keys():
                    done[merge] += 1
                else:
                    done[merge] = 1
        with open(namafile,'a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            for n in range(len(pairing)):
                writer.writerow([pairing[n][0],pairing[n][1],pairing[n][2], output[pairing[n][1] + ' ' + pairing[n][2]]])
            
    except: #Karena file belum ada lalu dibuat filenya
        print('masuk except')
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow(['id_user','word1','word2','totals'])


# Login or load session
#username = input("Masukkan username : ")
#password = prompt("Masukkan password : ", is_password = True)
#L.login(username, password)
#L.login("roxxstarrr99", "lupabanget1234")        # (login)
tabel2('level___2.csv', 'p','n')
L.login("vikarjufri", "ahmad123")

sizeOfFile = 0
profiles = []
# Obtain profile metadata

while sizeOfFile < 1024*1024*100:

#    profile = ["ari.ardani", "roxxstarrr99", "lazuardyk"]
    if len(profiles) != 0:
        for i in profiles:
            profile_target = instaloader.Profile.from_username(L.context, i)
    else:
        profile_target = instaloader.Profile.from_username(L.context, "roxxstarrr99")

    hitung = 0
    # Print list of followers
    for follower in profile_target.get_followers():
        captionlist = []
        hashtaglist = []
        likeslist = []
        usernamelist = []
        caption4tabel2 = []
        followers_target = follower.username
        profiles.append(str(followers_target))
        followers_followers = follower.followers
        profile = instaloader.Profile.from_username(L.context, followers_target)
        #print(type(profile))
    
        for posts in profile.get_posts():
            commentlist = []
            post = posts.caption
            hashtag = posts.caption_hashtags
            likes = posts.likes
            comments = ''
            #comment = posts.comments
            for comment in posts.get_comments():
                comments = str(comment.text.encode('ascii', 'ignore'))
                comments = give_emoji_free_text(comments)
                comments = comments.translate(translator).lower().replace('  ','')
            commentlist.append(comments)
            #print(commentlist)
            if len(commentlist) == 1:
                commentlist[0] = commentlist[0][1:]
            #print(commentlist)
            
            
            if post is not None:
                comments = []
                post = give_emoji_free_text(post)
                post = post.translate(translator).lower().replace('  ','')
                caption4tabel2.append(post)
                print('\n\nini caption untuk tabel 2   ' + str(caption4tabel2))
                
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
                if len(hashtag) == 0:
                    hashtag = ''
                print("hashtag: ", hashtag)
                print("like: ", likes)
                if len(commentlist) == 0:
                    commentlist = ''
                print("comment: ", commentlist)
                print("\n")
        tabel2('level___2.csv', str(followers_target), caption4tabel2)
    sizeOfFile = getFileSize('dataset.csv')

#data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
#print(data)
