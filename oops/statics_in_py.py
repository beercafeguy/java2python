class player:
    count = 0  # This is static by default

    def __init__(self, name):
        self.name = name
        player.count += 1

    @staticmethod
    def get_count():
        return player.count


player1 = player('messi')
player2 = player('ronaldo')
print(player.count)
print(player1.count)
print(player1.get_count())
print(player.get_count())