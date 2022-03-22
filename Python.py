import random

import cassiopeia as cass
from cassiopeia import Rank


cass.set_riot_api_key("RGAPI-0d31bb8c-a5a9-4249-9770-5992e27bc38b")  # This overrides the value set in your configuration/settings.

summoner = cass.get_summoner(name="KC Rekkles", region="EUW")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name, level=summoner.level, region=summoner.region))

champions = cass.get_champions(region="EUW")
random_champion = random.choice(champions)
#print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

print("You should play {name}.".format(name=random_champion.name))

topMasteries = cass.get_champion_masteries(summoner=summoner, region="EUW")
mostPlayedChamp = topMasteries[0]
secPlayedChamp = topMasteries[1]
thirdPlayedChamp = topMasteries[2]

print("This players most played champion is:")

print(f"1.{mostPlayedChamp.champion.name}")
print(f"2.{secPlayedChamp.champion.name}")
print(f"3.{thirdPlayedChamp.champion.name}")




