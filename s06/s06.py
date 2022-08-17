import requests
import json

# response = requests.get('https://digikala.com')
# print(response.status_code)
# print(response.text)

# f = open('data.html', 'w', encoding='utf8')
# f.write(response.text)
# f.close()

# f = open("data.json", 'w')
# a = [
#     {"name": "mohammad"},
#     {"grades": [20, 10, 12]}
# ]

# a = {"data": "salam"}

# json.dump(a, f)
# f.close()

# f = open("data.json", "r")
# b = json.load(f)
# f.close()
# print(b)


r = requests.get('https://api.github.com/users/mohammadnpak')
if r.status_code == 200:
    a = r.json()
    b = requests.get(a["followers_url"])
    if b.status_code == 200:
        followers = []
        for follower in b.json():
            followers.append(follower)
        followers.sort()
        print(followers)
