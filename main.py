from ExternalAGIStuff.CodeDriver.code_driver import run_code
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.to_object import obj, to_integer, to_str
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
from exception import AGIException
try:
    result = run_code(cid_of['func::test_code'], [obj(123456)])
    print(to_str(result))
except AGIException as e:
    e.show()
