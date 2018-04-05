from players import nim
from players import tictactoe
from players import sentiment

class Player(object):
    """docstring for Player"""
    def __init__(self, className):
        super(Player, self).__init__()
        try:
            inst = eval(className)
            self.player = inst()
        except NameError:
            self.player = None

    def play(self,state):
        if self.player != None:
            return self.player.play(state)
        else:
            return '{"error":true,"message":"Unknown game player, drop me an E-mail me@anujkch.com"}'

tictactoe = Player("tictactoe")
nim = Player("nim")
sentiment = Player("sentiment")

ticstate = {"player":"1","locations":["5","4","3"]}
nimstate = {"player":"-1","sticks":4}
sentistate = {"message":"I am not angry but i am sad"}
# print sentiment.play(sentistate)
# print nim.play(nimstate)
# print tictactoe.play(ticstate)
# print sentiment.play(sentistate)

state = {"player":1,"sticks":10}
# state = nim.play(state)
# print state

# print state
# while state["sticks"] > 0:
#     print state
#     state = nim.play(state)
    # state["sticks"] = state["sticks"]-1

states = {}
states["nim"] = {"player":1,"sticks":5}
states["tictactoe"] = {"player":"1","locations":["5","4","3"]}
states["sentiment"] = {"message":"I am not angry but i am sad"}

state = {}

if "nim" in states:
    state = states["nim"]
print "\n"
state = nim.play(state)
print "\n"
# print state
