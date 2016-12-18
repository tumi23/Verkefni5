# PRLA - Forritunarm�li� Python

# Verkefni 5


### Nemendur: Magn�s Nor�dahl, Tryggvi ��r Tryggvason og Tumi Gu�mundsson


##### Implementation
Vi� notu�um PyGame og TinyDB �r PIP


Til �ess a� geta keyrt leikinn �arf fyrst a� keyra:

**Linux:**

pip3 install pygame

pip3 install tinydb

**Windows:**

py -m pip install pygame

py -m pip install tinydb


##### Leikurinn
Vi� �tf�r�um klass�ska leikinn *Bomberman* �t fr� �tg�funni sem gefin var �t � NES fyrir �tlit og er t�nlistin "Stage Theme" �r Bomberman leikjunum. Vi� notu�um PyGame moduleuna vi� �tf�rsluna. 

Leikurinn innheldur tv� *gamemode*. 
Annarsvegar er h�gt er a� spila *Single-Player* gegn einf�ldu AI upp� *High-Score* sem geymt er � TinyDB. 
Hins vegar er h�gt a� spila *Two-Player* �ar sem h�gt er a� etja kappi vi� vini s�na og sj� hvor er betri � a� sprengja hinn � loft upp.


##### Controls

**Player 1**

Hreyfir sem me� �rvat�kkunum og notar SPACE til a� planta sprengju.

**Player 2**

Hreyfir sem me� WASD og notar Q til a� planta sprengju.

##### Framhald
N�stu verkefni � listanum voru a� gera bomburnar �annig ��r v�ru me� collition eins og veggirnir �annig a� ekki v�ri h�gt a� labba yfir ��r. Einnig var � planinu a� gera *upgrades* eins og til d�mis: Geta sparka� sprengjunum, hefta leikmanninn �annig a� hann geti bara planta� �kve�i� m�rum sprengjum � einu og hafa �� *pick-up* sem myndi auka �a� og hafa *blast-radius* hj� sprengjunum sem v�ri h�gt a� auka me� *power-up*