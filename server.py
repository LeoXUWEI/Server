from flask import Flask, render_template, request
from logic import Game

app = Flask(__name__)
game = Game()
game_mode = None
board = None
winner = None
player = 'X'
round = 0
player1 = None
player2 = None

none2empty = lambda x: '' if x is None else x

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    global game_mode, player1, player2, board
    board = game.make_empty_board()
    game_mode = 'PvP' if request.args.get('numPlayers') == '2' else 'PvE'
    player1 = request.args.get('player1')
    player2 = request.args.get('player2')
    return render_template("play.html")

@app.route("/playing")
def playing():
    global game, board, winner, round, player, game_mode
    position = int(request.args.get('board').replace('board', '')) - 1
    row, col = position // 3 + 1, position % 3 + 1
    success = game.board_update(board, row, col, player)
    if success:
        round += 1
        winner = game.get_winner(board)
        if winner is not None or round > 9:
            return render_template("stats.html", player=player1 if winner == 'X' else player2)
        player = game.other_player(player)
    if game_mode == 'PvE':
        row, col = game.get_random_position(board)
        success = game.board_update(board, row, col, player)
        if success:
            round += 1
            winner = game.get_winner(board)
            if winner is not None or round > 9:
                return render_template("stats.html", player=player1 if winner == 'X' else player2)
            player = game.other_player(player)
    return render_template("play.html", board1=none2empty(board[0][0]), board2=none2empty(board[0][1]), board3=none2empty(board[0][2]), board4=none2empty(board[1][0]), board5=none2empty(board[1][1]), board6=none2empty(board[1][2]), board7=none2empty(board[2][0]), board8=none2empty(board[2][1]), board9=none2empty(board[2][2]))

@app.route("/stats")
def stats():
    return render_template("stats.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=4000)