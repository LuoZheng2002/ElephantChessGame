from ExternalAGIStuff.CodeVisualization.code_browser import visualize_code
from ExternalAGIStuff.FundamentalCode.numeral_code import compare_natural_numbers_code
from ExternalAGIStuff.TestCode.test_code1 import *
result = visualize_code(compare_natural_numbers_code)
for line in result:
    print(line)
