# ForkMoreLikeSpoon

## About Project
A school project for PTS1. It tries to implement a known board game Azul. 
Currently there is no GUI, however the game logic should work.

## Known Issues

We had strange import errors, that were individual from student to student so we settled on a suboptimal solution: from bag import bag (omitting azul.).
This was the only solution that worked for us all. 

    folder azul import template:
    from {floor, unsedTiles,...} import {Floor, unsedTiles,...}
    
    folder test import template:
    from {azul.floor, azul.unsedTiles,...} import {Floor, unsedTiles,...}



Some comments are written in Slovak language (Google translate may be needed).


No GUI

## References

[rules of the game](https://www.wikihow.com/Play-Azul)
[online game inspiration](https://azee.mattle.online/lobby/rooms)
