import requests
import csv


class player:
    def __init__(self):
        self.id = []
        self.first_name = {}
        self.last_Name = {}
        self.age = {}
        self.weight = {}
        self.height = {}


    def add_player(self, id, first_Name, last_Name, age, weight, height):
        self.id.append(id)
        self.first_name[id] = first_Name
        self.last_Name[id] = last_Name
        self.age[id] = age
        self.weight[id] = weight
        self.height[id] = height

        return True

    def change_age(self, id, new_age):
        self.age[id] = new_age

        return id

    def remove_player(self, id):s
        self.id.remove(id)
        del self.first_name[id]
        del self.last_Name[id]
        del self.age[id]
        del self.weight[id]
        del self.height[id]


try:
    url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5"
    response = requests.get(url)
    dictionary = response.json()
except:
    print("it's not woring")

playerObject = player()
for innerDict in dictionary["items"]:
    # print(innerDict["$ref"])
    url = innerDict["$ref"]
    response = requests.get(url)
    val = response.json()
    # print(val["id"], val["firstName"], val["lastName"], val["age"], val["weight"], val["height"])
    playerObject.add_player(val["id"], val["firstName"], val["lastName"], val["age"], val["weight"], val["height"])

playerObject.change_age("3728305", 99)
playerObject.remove_player("4384595")


# print(playerObject.id)
# print(playerObject.age)


# for i in range(len(playerObject.id)):
#     temp = playerObject.id[i]
#     print(temp, playerObject.first_name[temp], playerObject.last_Name[temp], playerObject.age[temp], playerObject.weight[temp],playerObject.height[temp])

with open('playercsv.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(len(playerObject.id)):
        temp = playerObject.id[i]
        print(temp, playerObject.first_name[temp], playerObject.last_Name[temp], playerObject.age[temp], playerObject.weight[temp],playerObject.height[temp])
        spamwriter.writerow([temp, playerObject.first_name[temp], playerObject.last_Name[temp], playerObject.age[temp], playerObject.weight[temp],playerObject.height[temp]])


def f():
    return 3

def test_dummy():
    assert f() == 3