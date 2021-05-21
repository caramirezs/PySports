from riotwatcher import LolWatcher, ApiError
import pandas as pd
pd.set_option("display.max_rows", 50, "display.max_columns", 50)

api = 'RGAPI-ddd49a03-3571-4bbd-9560-f27789f05e8a'
lol_watcher = LolWatcher(api)
my_region = 'la1'
sumoners_names = {'Rem', 'Santoyft', 'JuliusYT', 'MyLoVoid'}

columns = ['summonerName', 'queueType', 'tier', 'rank', 'leaguePoints',
           'wins', 'losses', 'hotStreak']
columns_rn = ['Name', 'Tier', 'Rank', 'LP', 'W', 'L', 'HS']

df_stats = pd.DataFrame(columns=columns)  # Dataframe vacio
for name in sumoners_names:
    try:
        me = lol_watcher.summoner.by_name(my_region, name)
        my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
        df_stats_temp = pd.DataFrame(my_ranked_stats)
        df_stats_temp = df_stats_temp[columns]  # quita información que no queremos
        temp = df_stats_temp[df_stats_temp['queueType'] == 'RANKED_SOLO_5x5'].iloc[0]
        df_stats = df_stats.append(temp)
    except KeyError:
        print('{}: No está clasificado'.format(name))

df_stats.drop(['queueType'], axis=1, inplace=True)  # Quitar columna tipo
df_stats.columns = columns_rn  # renombrar columna
df_stats.set_index('Name', inplace=True)  # Indexar por nombre
print(df_stats)



