from players import nim
from players import tictactoe
from players import sentiment

def isNumeric(str):
    try:
        i = float(str)
        return True
    except (ValueError, TypeError):
        return  False

class Player(object):
    """docstring for Player"""
    def __init__(self, className,max_depth=4):
        super(Player, self).__init__()
        try:
            inst = eval(className)
            self.player = inst()
            self.player.setMaxDepth(max_depth)
        except NameError:
            self.player = None

    def play(self,state):
        if self.player != None:
            node = self.player.generate(state)
            return self.player.move(node,"=")
        else:
            return '{"error":true,"message":"Unknown game player, drop me an E-mail me@anujkch.com"}'

tictactoe = Player("tictactoe",5)
nim = Player("nim",5)
sentiment = Player("sentiment")

states = {}
states["nim"] = {"player":1,"sticks":7}
states["tictactoe"] = {"player":"1","locations":["5","4","3"]}
states["sentiment"] = {"message":"I am not angry but i am sad"}

state = {}
active = "n"
if active == "t":
    if "tictactoe" in states:
        state = states["tictactoe"]
    state = tictactoe.play(state)

if active == "n":
    if "nim" in states:
        state = states["nim"]
        # while state["sticks"] > 0:
        #     print state["sticks"]
        #     print ("Max" if state["player"] == 1 else "Min")+" turn "
        #     choose = input("\npick 1 or 2 ")
        #     try:
        #         if choose == 1 or choose == 2:
        #             state["sticks"] = state["sticks"]-choose;
        #             state["player"] = state["player"]*-1
        #         else:
        #             print "You can pick only 1 or 2 sticks"
        #     except Exception as e:
        #         print "Invalid key"
        # if state["player"]*-1 == 1:
        #     print "Winner Max"
        # else:
        #     print "Winner Min"

        state = {"player":1,"sticks":7}
        state = nim.play(state)
        print state

if active == "s":
    if "sentiment" in states:
        state = states["sentiment"]
    state = sentiment.play(state)
