from classes.result import Result
from classes.player import Player
from classes.game import Game

game = Game("Skribbl.io")
player = Player('Saaammmm')
player_2 = Player('ActuallyTopher')
Result(player, game, 2000)
Result(player, game, 19)
Result(player, game, 1900)
Result(player_2, game, 9)


print(Result.all)

# Player.highest_scored(game)