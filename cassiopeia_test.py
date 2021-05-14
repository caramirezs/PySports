import config
import random
import cassiopeia as cass

# This overrides the value set in your configuration/settings.

cass.set_riot_api_key(config.API_KEY_CAMILO)
cass.set_default_region("LAN")

summoner = cass.get_summoner(name="Santoyft")

champions = cass.get_champions()

good_with = summoner.champion_masteries.filter(lambda cm: cm.level == 7)
for i in good_with:
    print(i)

historial = summoner.match_history()
for data in historial[:5]:
    print(data)