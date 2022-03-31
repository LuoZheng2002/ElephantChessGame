from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.FundamentalCode.numeral_code import compare_natural_numbers_code
from ExternalAGIStuff.CodeVisualization.code_editor import generate_code, slice_code
from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.CodeVisualization.StructureVisualization.translate_AGIObject import translate_AGIObject
from exception import AGIException
from ElephantChessInstance.instance import elephant_chess, xq_chessboard
try:
    result = translate_AGIObject(xq_chessboard)
    print(result)
except AGIException as e:
    e.show()
