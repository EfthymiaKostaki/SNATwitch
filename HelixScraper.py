import numpy as np
from twitch.helix.api import TwitchHelix

random_ids = np.random.randint(1000, 1500, 200)
client = TwitchHelix(client_id='g39od75kqbxwu2lf988t52ttfqd96p', oauth_token='iuqqudf4nxvh07nqbbzsekutd5erh9')

streams = client.get_streams() ### returns according to viewer count let's say I keed the first 100
streams_with_most_live_viewers = list()

# Users with many live viewers will be disregarded since they require enormous computational power
sum=0

for i in streams:
    if sum in random_ids:
        if i['language'] == 'en' and i['game_id'] != '':
            print(i)
            streams_with_most_live_viewers.append(i)
    sum += 1
    if sum > 1500:
        break
