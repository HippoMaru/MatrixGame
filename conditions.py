# import random
#
#
# class Player:
#
#
#     def __init__(self, name, probability=0.5, win_conditions=[]):
#         self.name = name
#         self.probability = probability
#         self.win_conditions = win_conditions
#
#
#     def set_probability(self, probability):
#         if 0 <= probability <= 1:
#             self.probability = probability
#
#     def get_probability(self):
#         return self.probability
#
#     def set_win_conditions(self, conditions):
#         self.win_conditions = conditions
#
#     def add_win_conditions(self, conditions):
#         for condition in conditions:
#             if condition not in self.win_conditions:
#                 self.win_conditions.append(condition)
#
#     def remove_win_conditions(self, conditions):
#         for condition in conditions:
#             if condition in self.win_conditions:
#                 self.win_conditions.remove(condition)
#
#     def get_win_conditions(self):
#         return self.win_conditions
#
#
#
# class MatrixGame:
#
#
#     def __init__(self, amount_of_players, players, matrix):
#         self.amount_of_players = amount_of_players
#         self.players = players
#         self.matrix = matrix
#
#
#     def get_result(self):
#         choices = []
#         for player in self.players:
#             choices.append(random.choices([0, 1], weights=[player.get_probability(), 1 - player.get_probability()]))
#         result = self.matrix.copy()
#         for i in range(self.amount_of_players):
#             choice = choices[i]
#             result = result[choice]
#         return result
#
#
#     def play(self):
#         result = self.get_result()
#         for player in self.players:
#             win_conditions = player.get_win_conditions()
#             for condition in result:
#
