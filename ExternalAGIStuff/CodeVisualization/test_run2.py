from ExternalAGIStuff.CodeDriver.code_driver import run_code
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
from ExternalAGIStuff.CodeVisualization.formatted_code import *
from ElephantChessInstance.instance import xq_chessboard
from ExternalAGIStuff.FundamentalCode.batch_code import *
from ElephantChessInstance.FormattedCode.operation_func_f import operation_func_f
from ExternalAGIStuff.FundamentalCode.Formatted.increment_f import increment_f
from ExternalAGIStuff.code_to_object import code_to_object
from ExternalAGIStuff.CodeDriver.code_getter import get_code
from exception import AGIException
try:
    result = run_code(cid_of['func::test'], [])
    print('result is: ' + to_str(result))
except AGIException as e:
    e.show()
