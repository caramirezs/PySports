from riotwatcher import LolWatcher, ApiError

import config

lol_watcher = LolWatcher(config.API_KEY_CAMILO)
my_region = 'la1'
sumoners_names = {'Santoyft', 'SmurfFighter', 'Rem', 'MyLoVoid', 'JuliusYT'}

for name in sumoners_names:
    me = lol_watcher.summoner.by_name(my_region, name)
    print('El nivel de {} es: {}'.format(name, me['summonerLevel']))
    my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
    for elemento in my_ranked_stats:
        tipo = elemento['queueType']
        tier = elemento['tier']
        rank = elemento['rank']
        puntos = elemento['leaguePoints']
        wins = elemento['wins']
        loses = elemento['losses']
        tasa = wins / (wins + loses)
        print('Tipo de clasificación: {}\n'
              'tier: {}, rank: {}\n'
              'puntos: {}, wins: {}, loses {}, tasa: {:.1%}\n'
              .format(tipo, tier, rank, puntos, wins, loses, tasa))
    print('-----')
