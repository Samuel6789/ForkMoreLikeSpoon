# ForkMoreLikeSpoon

We had strange import errors, that were individual from student to student so we settled on a suboptimal solution: from bag import bag (omitting azul.).
This was the only solution that worked for us all. 

folder azul import template:
from {floor, unsedTiles,...} import {Floor, unsedTiles,...}

folder test import template:
from {azul.floor, azul.unsedTiles,...} import {Floor, unsedTiles,...}

