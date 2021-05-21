from riotwatcher import LolWatcher, ApiError
import pandas as pd
pd.set_option("display.max_rows", 50, "display.max_columns", 50)

api = 'RGAPI-ddd49a03-3571-4bbd-9560-f27789f05e8a'
lol_watcher = LolWatcher(api)
my_region = 'la1'
sumoners_names = {'Rem'}

for name in sumoners_names:
    me = lol_watcher.summoner.by_name(my_region, name)
    #print(me['id'])
    #print(me['accountId'])
    my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
    my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
    last_match = my_matches['matches'][0]
    chp = last_match['champion']
    match_detail = lol_watcher.match.by_id(my_region, last_match['gameId'])
    # print(match_detail['participants'])

    df_temp = pd.DataFrame(match_detail['participants'])
    print(df_temp[df_temp['championId'] == chp])

    # participants = []
    # for row in match_detail['participants']:
    #     participants_row = {}
    #     participants_row['champion'] = row['championId']
    #     participants_row['spell1'] = row['spell1Id']
    #     participants_row['spell2'] = row['spell2Id']
    #     participants_row['win'] = row['stats']['win']
    #     participants_row['kills'] = row['stats']['kills']
    #     participants_row['deaths'] = row['stats']['deaths']
    #     participants_row['assists'] = row['stats']['assists']
    #     participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    #     participants_row['goldEarned'] = row['stats']['goldEarned']
    #     participants_row['champLevel'] = row['stats']['champLevel']
    #     participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    #     participants_row['item0'] = row['stats']['item0']
    #     participants_row['item1'] = row['stats']['item1']
    #     participants.append(participants_row)
    # df = pd.DataFrame(participants)
    # pd.set_option("display.max_rows", 50, "display.max_columns", 50)
    # print(df)