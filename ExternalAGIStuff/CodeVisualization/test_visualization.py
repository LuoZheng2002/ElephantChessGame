from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.FundamentalCode.numeral_code import compare_natural_numbers_code
from ExternalAGIStuff.CodeVisualization.code_editor import generate_code, slice_code
from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.TestCode.test_code1 import *
from exception import AGIException
from ExternalAGIStuff.CodeVisualization.formatted_code import *
try:
    code_result = visualize_code(formatted_code1)
    for i in code_result:
        print(i)
except AGIException as e:
    e.show()
