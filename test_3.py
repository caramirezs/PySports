import config
import random
import cassiopeia as cass

# This overrides the value set in your configuration/settings.

cass.set_riot_api_key(config.API_KEY_JULIAN)
cass.set_default_region("LAN")

summoner = cass.get_summoner(name="JuliusYT")

print(summoner.level)