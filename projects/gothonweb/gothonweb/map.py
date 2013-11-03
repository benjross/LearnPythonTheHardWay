class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        result = self.paths.get(direction, None)
        if not result:
            return self.paths.get('*', None)
        else:
            return result

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
        """
        The Gothons of Planet Percal #25 have invaded and destoyed your entire
        crew. You are the last surviving member and your last mission is to get
        the neutron destruct bomb from the Weapons Armory, put it in the bridge,
        and bloww the ship up after getting into an escape pod.

        You're running down the central corridor to the Weapons Armory when a
        Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
        costume flowing around his hate filled body. He's blocking the door to
        the Armory and about to pull a weapon to blast you.
        """)

laser_weapon_armory = Room("Laser Weapon Armory",
        """
        Lucky for you they made you learn Gothon insults in the academy.  You
        tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
        nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
        The Gothon stops, tries not to laugh, then busts out laughing and can't
        move. While he's laughing you run up and shoot him square in the head
        putting him down, then jump through the Weapon Armory door.

        You do a dive roll into the Weapons Armory, crouch and scan the room for
        more Gothons that might be hiding. It's dead quiet, too quiet. You stand
        up and run to the far side of the room and find the neutron bomb in its
        container.  There's a keypad lock on the box and you need the code to
        get the bomb out.  If you get the code wrong 10 times then the lock
        closes forever and you can't get the bomb. The code is 3 digits.
        """)

the_bridge = Room("The Bridge",
        """
        The container clicks open and the seal breaks, letting gas out.  You
        grab the neutron bomb and run as fast as you can to the bridge where you
        must place it in the right spot.

        You burst onto the Bridge with the neutron bomb under your arm and
        surprise 5 Gothons who are trying to take control of the ship.  Each of
        them has an even uglier colown costume than the last. They haven't
        pulled their weapons out yet, as they see the active bomb under your arm
        and don't want to set it off.
        """)

escape_pod = Room("Escape Pod",
        """
        You point your blaster at the bomb under your arm and the Gothons put
        their hands up and start to sweat.  You inch backward to the door, open
        it, and the carefully place the bomb on the floor, pointing your
        blaster ast it.  You then jump back through the door, puch the close
        button and blast the lock so the Gothons can't get out.  Now that the
        bomb is placed, you run to the escape pd to get off this tin can.

        You rush through the ship desperately trying to make it to the excape
        pod before the whole ship explodes.  It seems like hardly any Gothons
        are on the ship, so your run is clear of interference.  You get to the
        chamber with the escape pods, and now need to pick one to take.  Some of
        them could be damaged, but you don't have time to look.  There's 5 pods,
        which one do you take?
        """)

the_end_winner = Room("The End",
        """
        You jump into pod 2 and hit the eject button. The pod easily slides out
        int space heading to the planet below.  As it flies to the planet, you
        look back and see your ship implode then explode like a bright star,
        taking out the Gothon ship at the same time.  You won!
        """)

the_end_loser = Room("The End",
        """
        You jump into a random pod and the the eject button.  The pod escapes
        out into the void of space, then implodes as the hull ruptures, crushing
        your body into jam jelly.
        """)

escape_pod.add_paths({'2': the_end_winner, '*': the_end_loser})

the_bridge_death = Room("death", 
        """
        In a panic you throw the bomb at the group of Gothons and make a leap
        for the door. Right as you drop it a Gothon shoots you right in the back
        killing you.  As you die you see another Gothon frantically try to
        disarm the bomb.  You die knowing they will probably blow up when it
        goes off.
        """)

the_bridge.add_paths({"throw the bomb": the_bridge_death,
    "slowly place the bomb": escape_pod, "*": the_bridge})

laser_weapon_armory_death = Room("death", 
        """
        The lock buzzes one last time and then you hear a sickeng melting sound
        as the mechanism is fused together.  You decide to sit there, and
        finally the Gothons blow up the ship from their ship and you die.
        """)

laser_weapon_armory.add_paths({'0132': the_bridge, '*': laser_weapon_armory_death})

central_corridor_shoot_death = Room("death", 
        """
        Quick on the draw you yank out your blaster and fite it as the Gothon.
        His clown costume is flowing and moving around his body, which throws
        off your aim.  Your laser hits his costume, but misses him entirely.
        This completely ruins his brand new costume his mother bought him, which
        makes him fly into an insane rage and blast you repeatedly in the face
        until you are dead.  Then he eats you.
        """)

central_corridor_dodge_death = Room("death", 
        """
        Like a wold class boxer you dodge, weave, slip, and slide right as the
        Gothon's blaster cranks a laser past your head.  In the middle of your
        artful dodge your foot slips and you bang your head on the metal wall
        and pass out.  You wake up shortly after only to die as the Gothon
        stomps on your head and eats you.
        """)

central_corridor.add_paths({"shoot!": central_corridor_shoot_death, "dodge!":
    central_corridor_dodge_death, "tell a joke": laser_weapon_armory, "*":
    central_corridor})

START = central_corridor
