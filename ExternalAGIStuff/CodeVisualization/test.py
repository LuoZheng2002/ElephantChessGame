from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.FundamentalCode.numeral_code import compare_natural_numbers_code
from ExternalAGIStuff.CodeVisualization.code_editor import generate_code
from ExternalAGIStuff.TestCode.test_code1 import *
from exception import AGIException
from test_code import code
try:
    result = generate_code(code)
    print(result)
except AGIException as e:
    e.show()
