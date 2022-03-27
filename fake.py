# 这是博弈问题数据结构的伪代码，最终需要写成AGIObject嵌套的形式以被AGI解读
# 最终的结构以structures.py中的内容为准
class Team:
    def __init__(self, team_id, players, end_game_benefit_id):
        self.team_id = team_id
        self.players = players
        self.end_game_benefit_id = end_game_benefit_id


class Player:
    def __init__(self, player_id, occupation_id,):
        self.player_id = player_id
        self.occupation_id = occupation_id


class Choice:
    def __init__(self, content):
        self.content = content


class Occupation:
    def __init__(self, occupation_id, operation_func):
        self.occupation_id = occupation_id
        self.operation_func = operation_func


# 一定是在数组中
class DynamicElement:
    def __init__(self, content_type, content):
        self.content_type = content_type
        self.content = content


class StaticElement:
    def __init__(self, element_id, content_type, content):
        self.element_id = element_id  # 相当于元素的名称，用于规则中指代
        self.content_type = content_type
        self.content = content


class Chessboard:
    def __init__(self, elements: dict):
        self.elements = elements


class Rule:
    def __init__(self, teams, occupations, who_is_next_func, my_team_id):
        self.teams = teams
        self.occupations = occupations
        self.who_is_next_func = who_is_next_func
        self.my_team_id = my_team_id


class EndGameBenefit:
    def __init__(self, benefit_id, benefit_func):
        self.benefit_id = benefit_id
        self.benefit_func = benefit_func


class WinningCriteria:
    def __init__(self, end_game_func, end_game_benefits):
        self.end_game_func = end_game_func
        self.end_game_benefits = end_game_benefits


# this game class is used as a temporary game model, not the memorized one
class Game:
    def __init__(self, chessboard: Chessboard, rule: Rule, winning_criteria: WinningCriteria):
        self.chessboard = chessboard
        self.rule = rule
        self.winning_criteria = winning_criteria
