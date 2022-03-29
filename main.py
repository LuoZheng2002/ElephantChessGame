from ExternalAGIStuff.CodeDriver.code_driver import run_code
from ExternalAGIStuff.IDs.concept_ids import cid_of
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject, AGIList
from ExternalAGIStuff.IDs.to_object import obj, to_integer
from ExternalAGIStuff.IDs.concept_ids import cid_reverse
from exception import AGIException
try:
    result = run_code(cid_of['func::compare_natural_numbers'], [obj(1000000001), obj(1000000000)])
    print(cid_reverse[result.concept_id])
except AGIException as e:
    e.show()
