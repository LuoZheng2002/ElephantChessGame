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
from ExternalAGIStuff.FundamentalCode.Visualized.remove_one_element import remove_one_element
from ExternalAGIStuff.FundamentalCode.Visualized.increment import increment
from exception import AGIException
from visualized_code import visualized_code
try:
    generate_code_file(visualized_code,
                       '../../generate_code.py',
                       'test')
    print('Succeeded!')
except AGIException as e:
    e.show()
