"""
Правила игры «Камень, ножницы, бумага» таковы:

Камень побеждает ножницы, Ножницы побеждают бумагу,
Бумага побеждает камень, При выборе одинаковых фигур объявляется ничья.
Давайте сыграем! Вам будут предложены ходы двух игроков;
нужно определить победителя и вывести сообщение:
«Player 1 won!» (если победил первый игрок) или
«Player 2 won!» (если победил второй игрок).
В случае ничьей следует вывести «Draw!».

    if player_1 == player_2:
        return "Draw!"

"""


def rps(player_1: str, player_2:str) -> str:
    moves = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if player_1 == player_2:
        return "Draw!"

    if moves[player_1] == player_2:
        return "Player 1 won!"

    else:
        return "Player 2 won!"

if __name__ == "__main__":
    print(rps("rock", "scissors"))