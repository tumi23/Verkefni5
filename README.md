# PRLA - Forritunarmálið Python

# Verkefni 5


### Nemendur: Magnús Norðdahl, Tryggvi Þór Tryggvason og Tumi Guðmundsson


##### Implementation
Við notuðum PyGame og TinyDB úr PIP


Til þess að geta keyrt leikinn þarf fyrst að keyra:

**Linux:**

pip3 install pygame

pip3 install tinydb

**Windows:**

py -m pip install pygame

py -m pip install tinydb


##### Leikurinn
Við útfærðum klassíska leikinn *Bomberman* út frá útgáfunni sem gefin var út á NES fyrir útlit og er tónlistin "Stage Theme" úr Bomberman leikjunum. Við notuðum PyGame moduleuna við útfærsluna. 

Leikurinn innheldur tvö *gamemode*. 
Annarsvegar er hægt er að spila *Single-Player* gegn einföldu AI uppá *High-Score* sem geymt er í TinyDB. 
Hins vegar er hægt að spila *Two-Player* þar sem hægt er að etja kappi við vini sína og sjá hvor er betri í að sprengja hinn í loft upp.


##### Controls

**Player 1**

Hreyfir sem með örvatökkunum og notar SPACE til að planta sprengju.

**Player 2**

Hreyfir sem með WASD og notar Q til að planta sprengju.

##### Framhald
Næstu verkefni á listanum voru að gera bomburnar þannig þær væru með collition eins og veggirnir þannig að ekki væri hægt að labba yfir þær. Einnig var á planinu að gera *upgrades* eins og til dæmis: Geta sparkað sprengjunum, hefta leikmanninn þannig að hann geti bara plantað ákveðið mörum sprengjum í einu og hafa þá *pick-up* sem myndi auka það og hafa *blast-radius* hjá sprengjunum sem væri hægt að auka með *power-up*