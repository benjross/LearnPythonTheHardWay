from nose.tools import *
from gothonweb.map import *

def test_room():
    gold = Room("GoldRoom",
            """This room has gold in it you can grab. There's a door to the
            north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test toom in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are tree here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_map():
    assert_equal(START.go('shoot!'), central_corridor_shoot_death)
    assert_equal(START.go('dodge!'), central_corridor_dodge_death)
    assert_equal(START.go('made up input'), central_corridor)

    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    
    assert_equal(room.go('made up input'), laser_weapon_armory_death)

    room = room.go('0132')
    assert_equal(room, the_bridge)

    assert_equal(room.go("throw the bomb"), the_bridge_death)
    assert_equal(room.go("made up input"), the_bridge)

    room = room.go("slowly place the bomb")
    assert_equal(room, escape_pod)

    assert_equal(room.go('wrong answer'), the_end_loser)
    assert_equal(room.go('2'), the_end_winner)
