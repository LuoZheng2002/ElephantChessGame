from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.FundamentalCode.numeral_code import compare_natural_numbers_code
from ExternalAGIStuff.CodeVisualization.code_editor import generate_code_file
from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.TestCode.test_code1 import *
from ElephantChessInstance.VisualizedCode.operation_func import operation_func
from ElephantChessInstance.VisualizedCode.who_is_next_func import who_is_next_func
from ElephantChessInstance.VisualizedCode.end_game_func import end_game_func
from ElephantChessInstance.VisualizedCode.end_game_benefit import end_game_benefit
from ExternalAGIStuff.FundamentalCode.batch_code import *
from ExternalAGIStuff.FundamentalCode.Visualized.run_dynamic_code_object import *
from exception import AGIException
try:
    generate_code_file(solve_expression,
                       '../../ExternalAGIStuff/FundamentalCode/Formatted/solve_expression_f.py',
                       'solve_expression_f')
    print('Succeeded!')
except AGIException as e:
    e.show()
