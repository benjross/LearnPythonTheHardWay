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

* Attack
    - punch
    - kick
    - special_move
* Player
    - attack
    * Bob
    * Jill
    * Sue
    * Dave
* Engine
    - play
    - select_player
    - generate_ai
* Map
    - draw    
