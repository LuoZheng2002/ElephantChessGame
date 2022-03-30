from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException

formatted_code1 = [
    [r['request'],
     [obj(0), obj(1), obj(2)],
     [r['call'], cid_of['func::logic_and'],
      [
          [r['call'], cid_of['func::math_equal'],
           [
               [r['call'], cid_of['func::sum'],
                [
                    [r['reg'], obj(0), []],
                    [r['reg'], obj(1), []]
                ]
                ],
               [obj(5)]
           ]
           ],
          [r['call'], cid_of['func::math_equal'],
           [
               [r['call'], cid_of['func::sum'],
                [
                    [r['reg'], obj(1), []],
                    [r['reg'], obj(2), []]
                ]
                ],
               [obj(6)]
           ]
           ]
      ]
      ],
     [
         [r['assert'], [r['concept_instance'], cid_of['True']]]
     ]
     ],
    [r['return'], [r['call'], cid_of['func::sum'],
                   [
                       [r['call'], cid_of['func::sum'],
                        [
                            [r['reg'], obj(0), []],
                            [r['reg'], obj(1), []]
                        ]
                        ],
                       [r['reg'], obj(2), []]
                   ]
                   ]]
]
