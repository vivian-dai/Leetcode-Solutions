class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        alice_turn = True
        alice_win = False
        while x >= 1 and y >= 4:
            if alice_turn:
                alice_win = True
            else:
                alice_win = False
            x -= 1
            y -= 4
            alice_turn = not alice_turn
        return "Alice" if alice_win else "Bob"
