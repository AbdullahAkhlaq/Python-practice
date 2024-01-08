user = {}

name = input('what is your name :')
age = input ('What is your age :')
fav_movies=input("What is your fav movies : ").split()
fav_songs=input("What is your fav song : ").split()

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

for key,value in user.items():
    print(f"{key}:{value}")
