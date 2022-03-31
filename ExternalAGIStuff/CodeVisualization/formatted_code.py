from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException

formatted_code1 = [
    [r['return'], [r['call'], cid_of['func::logic_not'],
                   [
                       [r['call'], cid_of['func::compare_concepts'],
                        [
                            [obj(1)],
                            [r['concept_instance'], cid_of['True']]
                        ]
                        ]
                   ]]]
]
