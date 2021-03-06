import datetime
from itertools import islice
from twitch.helix.api import TwitchHelix
import csv

def user_follows(user_id):
    followers = list()
    client = TwitchHelix(client_id='g39od75kqbxwu2lf988t52ttfqd96p', oauth_token='iuqqudf4nxvh07nqbbzsekutd5erh9')
    user_follows_iterator = client.get_user_follows(to_id=user_id)
    print("Total: {}".format(user_follows_iterator.total))
    for user_follow in islice(user_follows_iterator, 0, user_follows_iterator.total):
        followers.append(user_follow['from_id'])
    return followers, user_follows_iterator.total


def list_to_csv(streamer_channels_common):
    with open('edges_data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(('Source', 'Target', 'Weight'))

        for channel in streamer_channels_common:
            writer.writerow([channel['Source'], channel['Target'], channel['Weight']])


def find_common_followers(streamerA, streamerB):
    a_set = set(streamerA)
    b_set = set(streamerB)
    common = []
    if a_set & b_set:
        print(a_set & b_set)
        common = a_set & b_set
    else:
        print("No common elements")
    print(len(common))
    return len(common)

streamers = [{'id': '41097512062', 'user_id': '56401891', 'user_name': 'Bluddshed', 'game_id': '510150',
              'game_name': 'Diablo Immortal', 'type': 'live', 'title': '😈Maxing DH !DIWIZ !END - !DI !BUILDS !MERCH ',
              'viewer_count': 354, 'started_at': datetime.datetime(2020, 12, 27, 16, 57, 5), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_bluddshed-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097772190', 'user_id': '96726033', 'user_name': 'TwiggleSoft', 'game_id': '499859',
              'game_name': 'Spelunky 2', 'type': 'live',
              'title': 'Cursed runs, if Ghist Shop has Plasma Cannon turns into !NoCO score run! (also daily)',
              'viewer_count': 348, 'started_at': datetime.datetime(2020, 12, 27, 17, 38, 20), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_twigglesoft-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '81df4005-f654-40b2-9fc0-9fd767bc8e3e',
                          '7cefbf30-4c3e-4aa7-99cd-70aabb662f27']},
             {'id': '39990486317', 'user_id': '25828190', 'user_name': 'mantistobagan', 'game_id': '32982',
              'game_name': 'Grand Theft Auto V', 'type': 'live',
              'title': 'Toretti Christmas Special | nopixel | !viewsonic', 'viewer_count': 347,
              'started_at': datetime.datetime(2020, 12, 27, 16, 52, 23), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_mantistobagan-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097131886', 'user_id': '74657307', 'user_name': 'imPROBZZ', 'game_id': '491487',
              'game_name': 'Dead by Daylight', 'type': 'live', 'title': 'cracked plays incoming !youtube !jumpscare',
              'viewer_count': 343, 'started_at': datetime.datetime(2020, 12, 27, 15, 41, 49), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_improbzz-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '1eba3cfe-51cc-460a-8259-bc8bb987f904']},
             {'id': '40506497164', 'user_id': '38646632', 'user_name': 'Chanimaly', 'game_id': '18122',
              'game_name': 'World of Warcraft', 'type': 'live',
              'title': 'C9 Chan | Capping toons + new yt vid up !boost !coaching', 'viewer_count': 339,
              'started_at': datetime.datetime(2020, 12, 27, 17, 48, 29), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_chanimaly-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39988596365', 'user_id': '489298323', 'user_name': 'IndoAngel', 'game_id': '493551',
              'game_name': 'Conan Exiles', 'type': 'live',
              'title': 'Have a lovely weekend everyone. #Indonesian #English in #Australia #chillout',
              'viewer_count': 338, 'started_at': datetime.datetime(2020, 12, 27, 9, 28, 59), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_indoangel-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40499644876', 'user_id': '27446517', 'user_name': 'Monstercat', 'game_id': '26936',
              'game_name': 'Music', 'type': 'live', 'title': 'Non Stop Music - Monstercat Radio 🎶',
              'viewer_count': 332, 'started_at': datetime.datetime(2020, 12, 27, 2, 57, 35), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_monstercat-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39989550845', 'user_id': '105918024', 'user_name': 'RetrogradeTom', 'game_id': '27284',
              'game_name': 'Retro', 'type': 'live', 'title': '🍩 Crusader: No Remorse (1995) 🍩 First Playthrough',
              'viewer_count': 327, 'started_at': datetime.datetime(2020, 12, 27, 14, 2, 20), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_retrogradetom-{width}x{height}.jpg',
              'tag_ids': ['e027fb8b-219e-4959-8240-a4a082be0316', 'cc8d5abb-39c9-4942-a1ee-e1558512119e',
                          'd0976a7e-26a7-4a48-9225-c522808540f2', '8ba227ca-073c-46a7-b3cc-193e52c5ab4d',
                          '6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990610525', 'user_id': '403094949', 'user_name': 'Jaydvn', 'game_id': '518023',
              'game_name': 'NBA 2K21', 'type': 'li ve', 'title': 'LETS TALK...  (UNCAPPED SUBATHON DAY 7) !sub !prime',
              'viewer_count': 323, 'started_at': datetime.datetime(2020, 12, 27, 17, 9, 29), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_jaydvn-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40505105500', 'user_id': '45887494', 'user_name': 'Westham', 'game_id': '459931',
              'game_name': 'Old School RuneScape', 'type': 'live', 'title': '<Method> RSPKL Quarterfinals vs Dizzy',
              'viewer_count': 319, 'started_at': datetime.datetime(2020, 12, 27, 16, 24, 23), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_westham-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503179596', 'user_id': '82292862', 'user_name': 'myztroRAISY', 'game_id': '496253',
              'game_name': 'Quake Champions', 'type': 'live', 'title': 'Pro Estoty Cup series #4 - !bracket',
              'viewer_count': 317, 'started_at': datetime.datetime(2020, 12, 27, 14, 22, 40), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_myztroraisy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503235116', 'user_id': '75451837', 'user_name': 'perplexity', 'game_id': '18122',
              'game_name': 'World of Warcraft', 'type': 'live',
              'title': '#1 ROG. LIGHT OF ELUNE NEXT 48 HRS. LOVE YOU GUYS', 'viewer_count': 313,
              'started_at': datetime.datetime(2020, 12, 27, 14, 26, 35), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_perplexity-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40490985916', 'user_id': '30220059', 'user_name': 'ESL_SC2', 'game_id': '490422',
              'game_name': 'StarCraft II', 'type': 'live',
              'title': 'RERUN: Denver vs. SKillous - DH Masters: Winter 2020 - Playoffs - EU', 'viewer_count': 312,
              'started_at': datetime.datetime(2020, 12, 26, 15, 57, 32), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_esl_sc2-{width}x{height}.jpg',
              'tag_ids': ['36a89a80-4fcd-4b74-b3d2-2c6fd9b30c95', '6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990759645', 'user_id': '45509669', 'user_name': 'WolfDNC', 'game_id': '5126',
              'game_name': 'Resident Evil 3: Nemesis', 'type': 'live',
              'title': '!sub - WORLD PREMIERE - NEW KETU MOD  PART III [srl] ', 'viewer_count': 305,
              'started_at': datetime.datetime(2020, 12, 27, 17, 29, 56), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_wolfdnc-{width}x{height}.jpg',
              'tag_ids': ['c2839af5-f1d2-46c4-8edc-1d0bfbd85070', '6ea6bca4-4712-4ab9-a906-e3336a9d8039',
                          '9458de4e-6d35-422a-84a9-f243a49c212e', 'ba2c968b-867a-49ce-aebc-3d978a204f4a',
                          '7cefbf30-4c3e-4aa7-99cd-70aabb662f27', '860f0dc1-5d6b-4504-a3e2-eca15a1cb816']},
             {'id': '40502163580', 'user_id': '404894135', 'user_name': 'futcrunch', 'game_id': '518204',
              'game_name': 'FIFA 21', 'type': 'live', 'title': '80+ Upgrades!! - #FIFA21HOLIDAYS', 'viewer_count': 303,
              'started_at': datetime.datetime(2020, 12, 27, 12, 55, 11), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_futcrunch-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503504636', 'user_id': '21369084', 'user_name': 'JamesBardolph', 'game_id': '32399',
              'game_name': 'Counter-Strike: Global Offensive', 'type': 'live', 'title': 'Bardolph: Apex / CS',
              'viewer_count': 300, 'started_at': datetime.datetime(2020, 12, 27, 14, 45, 19), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_jamesbardolph-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'f60605b1-1d03-446a-b3a4-74ebe9ae1051']},
             {'id': '40505200924', 'user_id': '122874870', 'user_name': 'RadiantSoul_Tv', 'game_id': '499003',
              'game_name': 'VRChat', 'type': 'live', 'title': 'new video today after stream', 'viewer_count': 298,
              'started_at': datetime.datetime(2020, 12, 27, 16, 30, 24), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_radiantsoul_tv-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '6606e54c-f92d-40f6-8257-74977889ccdd',
                          '325a32c7-7b8e-48f8-b4fa-10875f18bb6d', 'ca470745-c1df-4c11-9474-9ab79dfc1863']},
             {'id': '40504507148', 'user_id': '51925282', 'user_name': 'glermz', 'game_id': '488634',
              'game_name': "Don't Starve Together", 'type': 'live',
              'title': 'Big time Farmer | new !drop | Giant zone continues | !nopc | !discord #SocialClub',
              'viewer_count': 296, 'started_at': datetime.datetime(2020, 12, 27, 15, 48, 28), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_glermz-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990749181', 'user_id': '44132002', 'user_name': 'Arumba07', 'game_id': '138585',
              'game_name': 'Hearthstone', 'type': 'live', 'title': 'Battlegrounds ~10k mmr (+coaching?)',
              'viewer_count': 295, 'started_at': datetime.datetime(2020, 12, 27, 17, 28, 27), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_arumba07-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'b157e8d6-b7ba-49f4-836f-09886c072f1f']},
             {'id': '40505837116', 'user_id': '29273855', 'user_name': 'PureSpam', 'game_id': '459931',
              'game_name': 'Old School RuneScape', 'type': 'live', 'title': '1B+ PvP Stacking <!method>',
              'viewer_count': 291, 'started_at': datetime.datetime(2020, 12, 27, 17, 8, 16), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_purespam-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990497325', 'user_id': '63778637', 'user_name': 'BabaYetu_', 'game_id': '27103',
              'game_name': "Sid Meier's Civilization V", 'type': 'live',
              'title': 'Playing CIV 5 as SPAIN with !civlist !lekmod and !lekmap (!v26.1)', 'viewer_count': 287,
              'started_at': datetime.datetime(2020, 12, 27, 16, 54, 5), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_babayetu_-{width}x{height}.jpg',
              'tag_ids': ['ff56eeeb-99ed-4a60-93fc-0b3f05d8661e', '96b6073f-450d-4248-8ed4-988e28f3f759',
                          '9458de4e-6d35-422a-84a9-f243a49c212e', '1eba3cfe-51cc-460a-8259-bc8bb987f904',
                          'cea7bc0c-75a5-4446-8743-6db031b71550', '6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503033596', 'user_id': '8488048', 'user_name': 'Fuzzyness', 'game_id': '16282',
              'game_name': 'Super Smash Bros. Melee', 'type': 'live',
              'title': 'Melee Classic Very Hard WR Attempts !raid !24hrs', 'viewer_count': 283,
              'started_at': datetime.datetime(2020, 12, 27, 14, 11, 51), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_fuzzyness-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '7cefbf30-4c3e-4aa7-99cd-70aabb662f27',
                          '2b19c8f9-695f-4ea1-a5fe-eba176770dbc']},
             {'id': '40505032188', 'user_id': '513677294', 'user_name': 'KatiePilot', 'game_id': '7193',
              'game_name': 'Microsoft Flight Simulator', 'type': 'live',
              'title': 'New Rig, who dis? RTX3070 | Real World Normal Ops👩\u200d✈️| Prepar3d v5 | EBBR ↔ LSGG | BEL3GV | VATSIM',
              'viewer_count': 281, 'started_at': datetime.datetime(2020, 12, 27, 16, 19, 44), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_katiepilot-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40501701324', 'user_id': '65172786', 'user_name': 'Mela', 'game_id': '19357',
              'game_name': 'Guild Wars 2', 'type': 'live',
              'title': 'First time raiding EVER !part5 !raidguides !charity', 'viewer_count': 276,
              'started_at': datetime.datetime(2020, 12, 27, 12, 3, 30), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_mela-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'bb5e7234-380e-48ad-a59c-03e51274e478']},
             {'id': '41094370526', 'user_id': '615590032', 'user_name': 'Bittersssweet', 'game_id': '509658',
              'game_name': 'Just Chatting', 'type': 'live', 'title': '❤️❤️❤️❤️❤️Adults only❤️❤️❤️❤️❤️',
              'viewer_count': 276, 'started_at': datetime.datetime(2020, 12, 27, 7, 3, 59), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_bittersssweet-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '89e105c9-2c45-42a9-a5f0-fc1ea6e7ba8b',
                          '8bbdb07d-df18-4f82-a928-04a9003e9a7e', 'd11b9289-806a-403b-945a-afb47ad2eea5',
                          '64d9afa6-139a-48d5-ab4e-51d0a92b22de', '77223888-8535-4614-974b-b1b2673456eb']},
             {'id': '40506631084', 'user_id': '36998513', 'user_name': 'Nikez', 'game_id': '32982',
              'game_name': 'Grand Theft Auto V', 'type': 'live',
              'title': '3.0RC2 | Development | @LaidbackNikez on Twitter | discord.gg/nikez', 'viewer_count': 275,
              'started_at': datetime.datetime(2020, 12, 27, 17, 56, 13), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_nikez-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40506558796', 'user_id': '112327448', 'user_name': 'MissBaffy', 'game_id': '21779',
              'game_name': 'League of Legends', 'type': 'live', 'title': "UK︱a bruv's journey to diamond",
              'viewer_count': 274, 'started_at': datetime.datetime(2020, 12, 27, 17, 52, 10), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_missbaffy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '1eba3cfe-51cc-460a-8259-bc8bb987f904',
                          'e85e4ccb-41fa-45b4-9c3a-f37807af3a5a', 'dcf598ca-b5de-47d4-af33-ecabe9eaeee1',
                          'b157e8d6-b7ba-49f4-836f-09886c072f1f', '292972f2-6beb-4e01-aa46-89dcfa4e4ef3',
                          'dfa7dd87-18b5-47db-b7b7-bdb1ef69547c', '51529054-5baf-493e-8961-2a43e4d0c6ac']},
             {'id': '39989984141', 'user_id': '601207139', 'user_name': 'gajugamestreamer', 'game_id': '33214',
              'game_name': 'Fortnite', 'type': 'live', 'title': 'Fortnite Battle Royale - Trio East & West Cash Cup ',
              'viewer_count': 274, 'started_at': datetime.datetime(2020, 12, 27, 15, 30, 26), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_gajugamestreamer-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'dc709206-c072-4340-a706-694578574c7e',
                          'fd8f5e68-42d3-4544-a273-5fc92dabc568', 'ff56eeeb-99ed-4a60-93fc-0b3f05d8661e',
                          'dbe20395-0e44-4156-92de-4a77f6cdccf0', 'f588bd74-e496-4d11-9169-3597f38a5d25']},
             {'id': '39990533901', 'user_id': '41253053', 'user_name': 'Baalorlord', 'game_id': '313031',
              'game_name': 'Invisible, Inc.', 'type': 'live',
              'title': '[Expert] December community game: First look at Invisible, Inc! - Currently 75% off on steam',
              'viewer_count': 269, 'started_at': datetime.datetime(2020, 12, 27, 16, 59, 28), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_baalorlord-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '67259b26-ff83-444e-9d3c-faab390df16f',
                          'cea7bc0c-75a5-4446-8743-6db031b71550']},
             {'id': '41096945182', 'user_id': '43349612', 'user_name': 'NoxiousLive', 'game_id': '517251',
              'game_name': 'Mini Healer', 'type': 'live',
              'title': '🏰 Mini Healer: Early Access Game 🏰 ☠️ Like the stream? Your subscription is most welcome ☠️ !vikings',
              'viewer_count': 267, 'started_at': datetime.datetime(2020, 12, 27, 14, 58, 39), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_noxiouslive-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41096705198', 'user_id': '113442086', 'user_name': 'UnbelivableTV', 'game_id': '491115',
              'game_name': 'Paladins', 'type': 'live', 'title': 'Ranked YEP | !youtube', 'viewer_count': 266,
              'started_at': datetime.datetime(2020, 12, 27, 13, 57, 12), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_unbelivabletv-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097481326', 'user_id': '89077758', 'user_name': 'Heisendong', 'game_id': '21779',
              'game_name': 'League of Legends', 'type': 'live', 'title': 'Preseason shenanigans ~ 5 Pushups per Sub',
              'viewer_count': 263, 'started_at': datetime.datetime(2020, 12, 27, 16, 51, 45), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_heisendong-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40502827628', 'user_id': '167770949', 'user_name': 'ThumblessCudi', 'game_id': '512710',
              'game_name': 'Call of Duty: Warzone', 'type': 'live', 'title': '5.3KD 1.3K Wins 47K Kills\n',
              'viewer_count': 260, 'started_at': datetime.datetime(2020, 12, 27, 13, 57, 6), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_thumblesscudi-{width}x{height}.jpg',
              'tag_ids': ['ff56eeeb-99ed-4a60-93fc-0b3f05d8661e', '6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40505775036', 'user_id': '157637554', 'user_name': 'kronawow', 'game_id': '18122',
              'game_name': 'World of Warcraft', 'type': 'live',
              'title': 'Krona︱Mythic reclear later new yt video out︱Rank 1 rio Balance Druid︱!ui !exitlag !youtube !legendary !covswap',
              'viewer_count': 260, 'started_at': datetime.datetime(2020, 12, 27, 17, 4, 46), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_kronawow-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'b157e8d6-b7ba-49f4-836f-09886c072f1f']},
             {'id': '41095053774', 'user_id': '153859298', 'user_name': 'RelaxBeats', 'game_id': '26936',
              'game_name': 'Music', 'type': 'live', 'title': 'Relax & Chill Beats -!trivia- -!hangman- -!scramble-',
              'viewer_count': 259, 'started_at': datetime.datetime(2020, 12, 27, 8, 33, 53), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_relaxbeats-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39989977725', 'user_id': '555713070', 'user_name': 'yojolu', 'game_id': '509659',
              'game_name': 'ASMR', 'type': 'live', 'title': 'LIVE Tingles & Fun', 'viewer_count': 259,
              'started_at': datetime.datetime(2020, 12, 27, 15, 29, 17), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_yojolu-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '64d9afa6-139a-48d5-ab4e-51d0a92b22de']},
             {'id': '39989899965', 'user_id': '31795012', 'user_name': 'Rarezy', 'game_id': '512710',
              'game_name': 'Call of Duty: Warzone', 'type': 'live', 'title': 'Sunday OOMPHIN | !yt',
              'viewer_count': 257, 'started_at': datetime.datetime(2020, 12, 27, 15, 14, 22), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_rarezy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40504536508', 'user_id': '179065334', 'user_name': 'poopernoodle', 'game_id': '497883',
              'game_name': 'My Time at Portia', 'type': 'live', 'title': 'only 363 days till christmas!',
              'viewer_count': 256, 'started_at': datetime.datetime(2020, 12, 27, 15, 50, 22), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_poopernoodle-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39989717245', 'user_id': '106058400', 'user_name': 'JimDavisMTG', 'game_id': '2748',
              'game_name': 'Magic: The Gathering', 'type': 'live',
              'title': 'Cube4Charity vs JBro and his minions! !cube4charity for info and to donate!',
              'viewer_count': 256, 'started_at': datetime.datetime(2020, 12, 27, 14, 38, 26), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_jimdavismtg-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'b157e8d6-b7ba-49f4-836f-09886c072f1f']},
             {'id': '40503632828', 'user_id': '26412614', 'user_name': 'Nili_AoE', 'game_id': '32399',
              'game_name': 'Counter-Strike: Global Offensive', 'type': 'live',
              'title': 'Charity Stream for Viva Con Agua: LoL, CS:GO, AOE2 & Among Us !charity !event',
              'viewer_count': 256, 'started_at': datetime.datetime(2020, 12, 27, 14, 53, 55), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_nili_aoe-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40498749708', 'user_id': '566626765', 'user_name': 'Roulettem', 'game_id': '498566',
              'game_name': 'Slots', 'type': 'live', 'title': 'Automated Roulette Master Strategy - $180/day',
              'viewer_count': 255, 'started_at': datetime.datetime(2020, 12, 27, 1, 11, 40), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_roulettem-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097251966', 'user_id': '609960077', 'user_name': 'MommyxDaddy', 'game_id': '18122',
              'game_name': 'World of Warcraft', 'type': 'live', 'title': 'BG leveling Uncle Jeff w/ snow cam',
              'viewer_count': 254, 'started_at': datetime.datetime(2020, 12, 27, 16, 7, 7), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_mommyxdaddy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '2e037750-5051-44ea-a51f-7a376bbacb29',
                          'b157e8d6-b7ba-49f4-836f-09886c072f1f']},
             {'id': '41097243102', 'user_id': '65428174', 'user_name': 'Razerninjas', 'game_id': '513181',
              'game_name': 'Genshin Impact', 'type': 'live',
              'title': '[AR55] Chill Sunday Stream | !albedo !youtube !rant !video !tierlist !johnlee !jean',
              'viewer_count': 246, 'started_at': datetime.datetime(2020, 12, 27, 16, 5, 9), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_razerninjas-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990695853', 'user_id': '121135020', 'user_name': 'Moxsy', 'game_id': '491318',
              'game_name': 'Borderlands 3', 'type': 'live',
              'title': '12 HOUR HOLIDAY STREAM! GIVEAWAYS ALL DAY! // !youtube !discord !newvid !socials !goals',
              'viewer_count': 245, 'started_at': datetime.datetime(2020, 12, 27, 17, 21, 18), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_moxsy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'b157e8d6-b7ba-49f4-836f-09886c072f1f',
                          'f9029b6f-a894-482d-a77a-84598859b2a3']},
             {'id': '41097161886', 'user_id': '112375357', 'user_name': 'Lana_Lux', 'game_id': '509670',
              'game_name': 'Science & Technology', 'type': 'live', 'title': 'THIS IS GAME DEV!', 'viewer_count': 245,
              'started_at': datetime.datetime(2020, 12, 27, 15, 48, 44), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_lana_lux-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'f588bd74-e496-4d11-9169-3597f38a5d25',
                          '02ba4017-ed3b-4b82-ab20-011860784f77', 'b97ee881-e15a-455d-9876-657fcba7cfd8']},
             {'id': '40502628012', 'user_id': '28655798', 'user_name': 'Stallion', 'game_id': '512709',
              'game_name': 'Call of Duty: Black Ops Cold War', 'type': 'live',
              'title': '[UK/ENG] 🛑 Camo Grind W/ Viewers • !2K • !GFuel • !Merch • !Giveaway', 'viewer_count': 245,
              'started_at': datetime.datetime(2020, 12, 27, 13, 39, 30), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_stallion-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'ff56eeeb-99ed-4a60-93fc-0b3f05d8661e']},
             {'id': '40505266140', 'user_id': '2400710', 'user_name': 'MembTV', 'game_id': '13389',
              'game_name': 'Age of Empires II', 'type': 'live',
              'title': 'Goal 17xx Merry Christmas - 485 Days Streaming in a row !expansion !pushups',
              'viewer_count': 244, 'started_at': datetime.datetime(2020, 12, 27, 16, 34, 23), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_membtv-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'a005b174-b20e-46b1-8679-4589fef81c8e',
                          '1eba3cfe-51cc-460a-8259-bc8bb987f904']},
             {'id': '40500449244', 'user_id': '34978952', 'user_name': 'ZeldaSpeedRuns', 'game_id': '11557',
              'game_name': 'The Legend of Zelda: Ocarina of Time', 'type': 'live',
              'title': 'ZSR Charity: Go To Hell TreZ OoTR Plando benefitting The Full Plate Project',
              'viewer_count': 242, 'started_at': datetime.datetime(2020, 12, 27, 8, 0, 29), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_zeldaspeedruns-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', '81df4005-f654-40b2-9fc0-9fd767bc8e3e',
                          'bb5e7234-380e-48ad-a59c-03e51274e478', '2fd30cb8-f2e5-415d-9d42-1316cfa61367',
                          'a005b174-b20e-46b1-8679-4589fef81c8e', '7cefbf30-4c3e-4aa7-99cd-70aabb662f27']},
             {'id': '41085006270', 'user_id': '107939114', 'user_name': 'DutchsinseOfficial', 'game_id': '509670',
              'game_name': 'Science & Technology', 'type': 'live',
              'title': 'Live Earthquakes 24/7 -- Most recent activity past 48 hours up to current', 'viewer_count': 242,
              'started_at': datetime.datetime(2020, 12, 26, 14, 55, 18), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_dutchsinseofficial-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'cea7bc0c-75a5-4446-8743-6db031b71550']},
             {'id': '39985330685', 'user_id': '430708432', 'user_name': 'ASMR_Marie', 'game_id': '509659',
              'game_name': 'ASMR', 'type': 'live', 'title': '🔴 Relaxing Mouth Sounds 💤 💤 💤  ', 'viewer_count': 241,
              'started_at': datetime.datetime(2020, 12, 27, 1, 29, 10), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_asmr_marie-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097724638', 'user_id': '140873889', 'user_name': 'absoluteHabibi', 'game_id': '67584',
              'game_name': 'Europa Universalis IV', 'type': 'live',
              'title': '[English] Playing as VENICE in Polish Multiplayer lobby !youtube !discord !plan',
              'viewer_count': 240, 'started_at': datetime.datetime(2020, 12, 27, 17, 31, 1), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_absolutehabibi-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990547453', 'user_id': '411377640', 'user_name': 'Jynxzi', 'game_id': '460630',
              'game_name': "Tom Clancy's Rainbow Six Siege", 'type': 'live', 'title': '[XBOX] RANKED w/ VIEWERS',
              'viewer_count': 240, 'started_at': datetime.datetime(2020, 12, 27, 17, 1, 5), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_jynxzi-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40504732172', 'user_id': '152184473', 'user_name': 'Keily___', 'game_id': '27546',
              'game_name': 'World of Tanks', 'type': 'live', 'title': '[ENG] DROPS! Cozy BLELELE stream! ❤ !dc',
              'viewer_count': 238, 'started_at': datetime.datetime(2020, 12, 27, 16, 1, 41), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_keily___-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '39990900957', 'user_id': '99591839', 'user_name': 'Natarsha', 'game_id': '509658',
              'game_name': 'Just Chatting', 'type': 'live', 'title': 'Morning Stream! 🌸 | !video !sub !prime ',
              'viewer_count': 238, 'started_at': datetime.datetime(2020, 12, 27, 17, 48, 38), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_natarsha-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503692140', 'user_id': '185227953', 'user_name': 'auraofpsych', 'game_id': '509658',
              'game_name': 'Just Chatting', 'type': 'live', 'title': 'Short Sunday Church Service\nInsta: AuraofPsyche',
              'viewer_count': 237, 'started_at': datetime.datetime(2020, 12, 27, 14, 57, 41), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_auraofpsych-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41097638126', 'user_id': '401980665', 'user_name': 'realrayford', 'game_id': '509538',
              'game_name': 'Animal Crossing: New Horizons', 'type': 'live',
              'title': '8 FREE treasure islands on screen! Come get free stuff!', 'viewer_count': 236,
              'started_at': datetime.datetime(2020, 12, 27, 17, 17, 22), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_realrayford-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '41096182862', 'user_id': '30521334', 'user_name': 'TeamJbro', 'game_id': '2748',
              'game_name': 'Magic: The Gathering', 'type': 'live',
              'title': 'FINAL PUSH!!!! #CUBE4CHARITY! !Charity  #BLM', 'viewer_count': 235,
              'started_at': datetime.datetime(2020, 12, 27, 12, 15, 6), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_teamjbro-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40494958348', 'user_id': '268540895', 'user_name': 'HotBeatsTV', 'game_id': '26936',
              'game_name': 'Music', 'type': 'live',
              'title': '[EN - 24/7] Electronica directly from Clubs, Events & Festivals # Daily live session from 7 PM CET # !live !mmoga',
              'viewer_count': 233, 'started_at': datetime.datetime(2020, 12, 26, 20, 8, 15), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_hotbeatstv-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'e525f885-ccc0-42dd-9b6e-0586f76fdb3c',
                          'c553e849-7019-479b-a14d-a78cd3462e9a', 'c5247b10-deec-4d7a-84a5-db6a75cb5908',
                          '338d7a92-8bcc-429e-a30c-9f1c41a2d79a', 'd81d54c8-d705-4df6-aaf0-01d715c1dbcc']},
             {'id': '41097886638', 'user_id': '32679000', 'user_name': 'Mrhappy1227', 'game_id': '513181',
              'game_name': 'Genshin Impact', 'type': 'live',
              'title': '"What Does The 1227 In Your Name Mean?"| !submas | !audible | !vpn | !battle',
              'viewer_count': 230, 'started_at': datetime.datetime(2020, 12, 27, 17, 55, 38), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_mrhappy1227-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40505899548', 'user_id': '183051236', 'user_name': 'cyberonixx', 'game_id': '509658',
              'game_name': 'Just Chatting', 'type': 'live', 'title': 'ONE JOKE GO (WITH VIEWERS) !ds',
              'viewer_count': 229, 'started_at': datetime.datetime(2020, 12, 27, 17, 12), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_cyberonixx-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039']},
             {'id': '40503535388', 'user_id': '104477397', 'user_name': 'snupy', 'game_id': '18122',
              'game_name': 'World of Warcraft', 'type': 'live',
              'title': '<SNUPY> NIGHT FAE FERAL GAMING !guide !youtube', 'viewer_count': 222,
              'started_at': datetime.datetime(2020, 12, 27, 14, 47, 26), 'language': 'en',
              'thumbnail_url': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_snupy-{width}x{height}.jpg',
              'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039', 'b157e8d6-b7ba-49f4-836f-09886c072f1f']}]

streamers_followers = list()

for idx, val in enumerate(streamers):
    follow, total = user_follows(val['user_id'])
    streamers_followers.append(follow)
    streamers[idx]['total_number'] = total

common_followers = list()

for idx, valx in enumerate(streamers_followers):
    for idy, valy in enumerate(streamers_followers):
        if idx < idy:  # ensure that we don't compare the same streamers twice
            common_followers.append({'Source': streamers[idx]['user_id'],
                                     'Target': streamers[idy]['user_id'],
                                     'Weight': find_common_followers(valx, valy)})
list_to_csv(common_followers)

