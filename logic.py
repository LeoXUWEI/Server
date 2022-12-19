import csv
class Game:
    def __init__(self) -> None:
        pass
    
    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self, board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        # Gain all the possible cases
        pos = []
        # Get each row
        pos.extend(board)
        # Get each colomn
        for col in range(3):
            pos.append([row[col] for row in board])
        # Get each diagonal
        pos.append([board[0][0],board[1][1],board[2][2]])
        pos.append([board[0][2],board[1][1],board[2][0]])
        # Test each case
        for case in pos:
            if (case[0] != None) and case[0]==case[1] and case[0]==case[2]:
                return case[0]
        return None

    def board_update(self, board, row, col, player):
        # Check input legality
        if row < 1 or row > 3 or col < 1 or col > 3:
            print('Go beyond the boundaries. Try again!')
            return False
        # Check if the cell is occupied
        if board[row-1][col-1] != None:
            print('Elements already present. Try again!')
            return False
        # Assign the val and return
        board[row-1][col-1] = player
        return True

    def other_player(self, player):
        """Given the character for a player, returns the other player."""
        if player == 'X':
            return 'O'
        else:
            return 'X'
        
    # Function to provide random position
    def get_random_position(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == None:
                    return i+1, j+1
    
    # Function to list all the players in record
    def read_csv(self):
        # Open the csv file
        with open('player.csv', 'r') as f_read:
            data = list(csv.reader(f_read,delimiter=','))
        f_read.close()
        return data
 
    # Function to insert new players into csv
    def insert_new_player(self, name):
        # Init the data
        row = [name, 0, 0, 0] # Name, Win, Loss, Draw
        # Open the csv file
        with open('player.csv','a',newline='') as f_append:
            writer = csv.writer(f_append)
            writer.writerow(row)
        f_append.close()

    # Function to create a new player
    def init_player(self, player):
        player_list = [row[0] for row in self.read_csv()]
        # Make sure all the players are in the list
        for p in player:
            if p not in player_list:
                self.insert_new_player(p)
    
    # Update the game result and return the stat of the players
    # score: win in 1, draw in 0, loss in -1
    def update_csv(self, player, score):
        list = self.read_csv()
        player_list = [row[0] for row in self.read_csv()]
        player_stat = []
        # Locate each player
        for p,s in zip(player,score):
            row_idx = player_list.index(p)
            # Change the score
            if s == 1:
                list[row_idx][1] = int(list[row_idx][1]) + 1
            elif s == -1:
                list[row_idx][2] = int(list[row_idx][2]) + 1
            else:
                list[row_idx][3] = int(list[row_idx][3]) + 1
            player_stat.append(list[row_idx])
        # Write back to the file
        with open('player.csv','w',newline='') as f_write:
            writer = csv.writer(f_write)
            for row in list:
                writer.writerow(row)
        f_write.close()
        # Get the rank for players
        win_list = [int(row[1]) for row in list]
        win_list.sort(reverse=True)
        for stat in player_stat:
            stat.append(win_list.index(int(stat[1]))+1)
        return player_stat