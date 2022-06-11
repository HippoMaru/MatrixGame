import random
import collections


class Player:

    def __init__(self, name, probability=0.5, points=0):
        self.name = name
        self.probability = probability
        self.points = points

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def set_probability(self, probability):
        if 0 <= probability <= 1:
            self.probability = probability

    def add_points(self, val):
        self.points += val

    def get_points(self):
        return self.points

    def get_probability(self):
        return self.probability


class MatrixGame:

    def __init__(self, amount_of_players, players, main_matrix, award_matrix):
        self.amount_of_players = amount_of_players
        self.players = players
        self.main_matrix = main_matrix
        self.award_matrix = award_matrix
        self.last_game_choices = []

    def __str__(self):
        return f'Main matrix: {self.main_matrix}\nAward matrix: {self.award_matrix}\nPlayers: {self.players}'

    def __repr__(self):
        return f'Main matrix: {self.main_matrix}\nAward matrix: {self.award_matrix}\nPlayers: {self.players}'

    def get_result(self):
        self.last_game_choices = []
        for player in self.players:
            self.last_game_choices.append(random.choices([0, 1], weights=[player.get_probability(), 1 - player.get_probability()]))
        result = self.main_matrix.copy()
        for i in range(self.amount_of_players):
            choice = self.last_game_choices[i][0]
            result = result[choice]
        return result[0]

    def get_winner(self, result):
        result_code = result % self.amount_of_players
        return self.players[result_code]

    def get_points(self):
        result = self.award_matrix.copy()
        for i in range(self.amount_of_players):
            choice = self.last_game_choices[i][0]
            result = result[choice]
        return result[0]

    def play(self, amount_of_games=1):
        if amount_of_games == 1:
            result = self.get_result()
            winner = self.get_winner(result)
            winner.add_points(self.get_points())
            print(f'The winner is {winner}')
            return winner
        else:
            winners = []
            for i in range(amount_of_games):
                result = self.get_result()
                winner = self.get_winner(result)
                winner.add_points(self.get_points())
                winners.append(winner)
            print(f'Statistics: {collections.Counter(winners)}')
            return winners


'''Hard code example'''

player1 = Player('Ivan')
player1.set_probability(0.33)
player2 = Player('Kyrill')
player2.set_probability(0.47)
player3 = Player('Naruto')
player3.set_probability(0.82)

players = [player1, player2, player3]

mg1 = MatrixGame(3, players, [[[[0], [1]], [[2], [3]]],
                              [[[4], [5]], [[6], [7]]]], [[[[0], [0]], [[0], [0]]],
                                                         [[[0], [0]], [[0], [0]]]])

print(mg1)
mg1.play()
mg1.play(1000)
for player in players:
    print(f'Player: {player}\t\tPoints: {player.get_points()}')
print(players)

'''CLI example'''


def generate_matrix_automatically(matrix, n):
    if len(matrix) == 2:
        matrix[0] = generate_matrix_automatically(matrix[0].copy(), n)
        matrix[1] = generate_matrix_automatically(matrix[1].copy(), n)
        return matrix
    else:
        return [random.randint(0, n-1)]


def generate_matrix_manually(matrix, n):
    if len(matrix) == 2:
        matrix[0] = generate_matrix_manually(matrix[0].copy(), n)
        matrix[1] = generate_matrix_manually(matrix[1].copy(), n)
        return matrix
    else:
        val = int(input('Enter the cell: '))
        return [val]


n = int(input('Enter the amount of players: '))
template_matrix = [[], []]
for i in range(1, n):
    temp = template_matrix.copy()
    template_matrix = [temp, temp]
print("Main matrix will be generated automatically\n")
matrix = generate_matrix_automatically(template_matrix.copy(), n)
print("Enter award matrix: ")
award_matrix = generate_matrix_manually(template_matrix.copy(), n)
players = []
for i in range(n):
    name = input(f'Enter the name of player number {i + 1}: ')
    probability = float(input(f'Enter the probability of choosing first of two rows for player {name}: '))
    players.append(Player(name, probability))
mg = MatrixGame(n, players, matrix, award_matrix)
print(mg)
k = int(input('Enter the amount of games: '))
mg.play(k)
for player in players:
    print(f'Player: {player}\t\tPoints: {player.get_points()}')
print(players)
