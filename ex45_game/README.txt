This is the spec for the game I am developing.  It will be an extension of the
combat system I made for ex43.py.  It will be like Mortal Kombat I hope.  It
will feature a list of characters that the user can choose from, each with its
own set of moves.  I want to encorporate some ASCII animations too.  The REPL
will print out the scene and the characters health and attacks.  It will be a
text based combat system.

Character will have to have:
    - health
    - attack
        - punch
        - kick
        - special moves
    - defense stats
        - a player's defense affects the likelihood of a succesful hit

Scenes:
    - A scene will show the state of the game
    - 	0 		0
    -----------------


Should a player just be a dictionary of attacks?
List of player is also a dictionary
Display moves is just keys from attacks


* Attack
    - punch
    - kick
    - special_move
* Engine
    - play
    - select_player
    - generate_ai
* Map
    - draw    
    * drawer
