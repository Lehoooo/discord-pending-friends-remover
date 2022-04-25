import time
import discum
import json


# put your token here
bot = discum.Client(token="YOUR TOKEN HERE",
                    log=False)

a = bot.getRelationships()
json = json.loads(a.text)
print(json)
length = int(len(json))
for x in range(len(json)):
    friend = json[x]
    if friend['type'] == 3: # 1 = friend, 2 = blocked, 3 = incoming, 4 = outgoing - keep at 3 to remove pending incoming reqs
        print("incoming " + friend['id'])
        c = bot.removeRelationship(str(friend['id']), location="friends")
        if c.status_code == 204:
            length -= 1
            print("remove OK :) Remaining: " + str(length))

        else:
            print("failed to remove :(")
        time.sleep(1)
    else:
        print("outgoing or added already")

bot.gateway.run(auto_reconnect=True)
