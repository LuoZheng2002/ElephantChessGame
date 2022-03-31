from ExternalAGIStuff.CodeDriver.code_driver import run_code
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
from ExternalAGIStuff.CodeVisualization.formatted_code import *
from ElephantChessInstance.instance import xq_chessboard
from ExternalAGIStuff.FundamentalCode.batch_code import *
from ElephantChessInstance.FormattedCode.operation_func_f import operation_func_f
from ElephantChessInstance.chessboard_browser import print_chessboard
from exception import AGIException
try:
    current_chessboard = xq_chessboard
    while True:
        print('Now chessboard is:')
        print_chessboard(current_chessboard)
        whose_turn = current_chessboard.attributes[cid_of['xq::whose_turn']]
        if whose_turn.concept_id == cid_of['xq::red_team']:
            print('Now it\'s red team\'s turn to go!')
        elif whose_turn.concept_id == cid_of['xq::black_team']:
            print('Now it\'s black team\'s turn to go!')
        current_chessboard = run_code(None, [current_chessboard, whose_turn], operation_func_f)
except AGIException as e:
    e.show()
