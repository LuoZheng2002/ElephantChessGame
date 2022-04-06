from ExternalAGIStuff.CodeDriver.code_driver import run_code
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
from ExternalAGIStuff.CodeVisualization.formatted_code import *
from ElephantChessInstance.instance import xq_chessboard
from ExternalAGIStuff.FundamentalCode.batch_code import *
from ElephantChessInstance.FormattedCode.operation_func_f import operation_func_f
from ElephantChessInstance.FormattedCode.who_is_next_func_f import who_is_next_func_f
from ElephantChessInstance.FormattedCode.end_game_func_f import end_game_func_f
from ElephantChessInstance.FormattedCode.end_game_benefit_f import end_game_benefit_f
from ElephantChessInstance.chessboard_browser import print_chessboard
from ExternalAGIStuff.CodeDriver.code_getter import get_code
from ExternalAGIStuff.code_to_object import code_to_object
from copy import deepcopy
from exception import AGIException
try:
    current_chessboard = deepcopy(xq_chessboard)
    while True:
        print('Now chessboard is:')
        print_chessboard(current_chessboard)
        whose_turn = run_code(None, [current_chessboard], who_is_next_func_f)
        if whose_turn.concept_id == cid_of['xq::red_team']:
            print('Now it\'s red team\'s turn to go!')
        elif whose_turn.concept_id == cid_of['xq::black_team']:
            print('Now it\'s black team\'s turn to go!')
        current_chessboard = run_code(cid_of['func::run_dynamic_code_object'], [code_to_object(operation_func_f), AGIList([current_chessboard, whose_turn])])
        end_game = run_code(None, [current_chessboard], end_game_func_f)
        if end_game.concept_id == cid_of['True']:
            print_chessboard(current_chessboard)
            print('Game ended!')
            red_benefit = run_code(None, [current_chessboard, obj('xq::red_team')], end_game_benefit_f)
            black_benefit = run_code(None, [current_chessboard, obj('xq::black_team')], end_game_benefit_f)
            print('Red team\'s benefit is: ' + to_str(red_benefit))
            print('Black team\'s benefit is: ' + to_str(black_benefit))
            break

except AGIException as e:
    e.show()
