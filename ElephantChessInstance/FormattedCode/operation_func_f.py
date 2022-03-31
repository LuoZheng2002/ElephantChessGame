from ExternalAGIStuff.IDs.reserved_keywords import r
from ExternalAGIStuff.IDs.to_object import to_integer, to_str, obj
from ExternalAGIStuff.IDs.concept_ids import cid_of, cid_reverse
from ExternalAGIStuff.CodeDriver.concept_instance_struct import AGIObject
from ExternalAGIStuff.CodeVisualization.code_browser import letter_to_number
from exception import AGIException

operation_func_f = [
    [r['assert'], [r['call'], cid_of['func::compare_concepts'],
                   [
                       [r['input'], obj(1)],
                       [r['get_member'], [r['input'], obj(0)], cid_of['xq::whose_turn']]
                   ]
                   ]],
    [r['assign'], [r['reg'], obj(0), []], [r['input'], obj(0)]],
    [r['assign_as_reference'], [r['reg'], obj(1), []], [r['get_member'], [r['reg'], obj(0), []], cid_of['xq::pieces']]],
    [r['request'],
     [obj(2), obj(3)],
     [r['call'], cid_of['func::batch_logic_and'],
      [
          [r['reg'], obj(4), []]
      ]
      ],
     [
         [r['assign'], [r['reg'], obj(4), []], [r['concept_instance'], cid_of['list']]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::compare_concepts'],
                                                [
                                                    [r['reg'], obj(2), []],
                                                    [r['concept_instance'], cid_of['natural_number']]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::compare_concepts'],
                                                [
                                                    [r['reg'], obj(3), []],
                                                    [r['concept_instance'], cid_of['natural_number']]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::greater_than_or_equal_to'],
                                                [
                                                    [r['reg'], obj(2), []],
                                                    [obj(0)]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::less_than_or_equal_to'],
                                                [
                                                    [r['reg'], obj(2), []],
                                                    [obj(9)]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::greater_than_or_equal_to'],
                                                [
                                                    [r['reg'], obj(3), []],
                                                    [obj(0)]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::less_than_or_equal_to'],
                                                [
                                                    [r['reg'], obj(3), []],
                                                    [obj(10)]
                                                ]
                                                ]],
         [r['append'], [r['reg'], obj(4), []],
          [r['exist'], [r['reg'], obj(1), []], [r['call'], cid_of['func::logic_and'],
                                                [
                                                    [r['call'], cid_of['func::math_equal'],
                                                     [
                                                         [r['at'],
                                                          [r['get_member'], [r['target']], cid_of['xq::position']],
                                                          [obj(0)]],
                                                         [r['reg'], obj(2), []]
                                                     ]
                                                     ],
                                                    [r['call'], cid_of['func::math_equal'],
                                                     [
                                                         [r['at'],
                                                          [r['get_member'], [r['target']], cid_of['xq::position']],
                                                          [obj(1)]],
                                                         [r['reg'], obj(3), []]
                                                     ]
                                                     ]
                                                ]
                                                ]]],
         [r['append'], [r['reg'], obj(4), []], [r['call'], cid_of['func::compare_concepts'],
                                                [
                                                    [r['get_member'], [r['find'], [r['reg'], obj(1), []],
                                                                       [r['call'], cid_of['func::logic_and'],
                                                                        [
                                                                            [r['call'], cid_of['func::math_equal'],
                                                                             [
                                                                                 [r['at'],
                                                                                  [r['get_member'], [r['target']],
                                                                                   cid_of['xq::position']], [obj(0)]],
                                                                                 [r['reg'], obj(2), []]
                                                                             ]
                                                                             ],
                                                                            [r['call'], cid_of['func::math_equal'],
                                                                             [
                                                                                 [r['at'],
                                                                                  [r['get_member'], [r['target']],
                                                                                   cid_of['xq::position']], [obj(1)]],
                                                                                 [r['reg'], obj(3), []]
                                                                             ]
                                                                             ]
                                                                        ]
                                                                        ]], cid_of['xq::piece_owner']],
                                                    [r['input'], obj(1)]
                                                ]
                                                ]]
     ]
     ],
    [r['assign_as_reference'], [r['reg'], obj(5), []],
     [r['find'], [r['reg'], obj(1), []], [r['call'], cid_of['func::logic_and'],
                                          [
                                              [r['call'], cid_of['func::math_equal'],
                                               [
                                                   [r['at'], [r['get_member'], [r['target']], cid_of['xq::position']],
                                                    [obj(0)]],
                                                   [r['reg'], obj(2), []]
                                               ]
                                               ],
                                              [r['call'], cid_of['func::math_equal'],
                                               [
                                                   [r['at'], [r['get_member'], [r['target']], cid_of['xq::position']],
                                                    [obj(1)]],
                                                   [r['reg'], obj(3), []]
                                               ]
                                               ]
                                          ]
                                          ]]],
    [r['if'], [r['call'], cid_of['func::compare_concepts'],
               [
                   [r['get_member'], [r['reg'], obj(5), []], cid_of['xq::piece_name']],
                   [r['concept_instance'], cid_of['xq::Che']]
               ]
               ],
     [
         [r['request'],
          [obj(6), obj(7)],
          [r['call'], cid_of['func::batch_logic_and'],
           [
               [r['reg'], obj(8), []]
           ]
           ],
          [
              [r['assign'], [r['reg'], obj(8), []], [r['concept_instance'], cid_of['list']]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::compare_concepts'],
                                                     [
                                                         [r['reg'], obj(6), []],
                                                         [r['concept_instance'], cid_of['natural_number']]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::compare_concepts'],
                                                     [
                                                         [r['reg'], obj(7), []],
                                                         [r['concept_instance'], cid_of['natural_number']]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::greater_than_or_equal_to'],
                                                     [
                                                         [r['reg'], obj(6), []],
                                                         [obj(0)]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::less_than_or_equal_to'],
                                                     [
                                                         [r['reg'], obj(7), []],
                                                         [obj(9)]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::greater_than_or_equal_to'],
                                                     [
                                                         [r['reg'], obj(6), []],
                                                         [obj(0)]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::less_than_or_equal_to'],
                                                     [
                                                         [r['reg'], obj(7), []],
                                                         [obj(10)]
                                                     ]
                                                     ]],
              [r['assign'], [r['reg'], obj(9), []], [r['concept_instance'], cid_of['list']]],
              [r['append'], [r['reg'], obj(9), []], [r['call'], cid_of['func::math_equal'],
                                                     [
                                                         [r['reg'], obj(6), []],
                                                         [r['reg'], obj(2), []]
                                                     ]
                                                     ]],
              [r['append'], [r['reg'], obj(9), []], [r['call'], cid_of['func::logic_not'],
                                                     [
                                                         [r['call'], cid_of['func::math_equal'],
                                                          [
                                                              [r['reg'], obj(7), []],
                                                              [r['reg'], obj(3), []]
                                                          ]
                                                          ]
                                                     ]]],
              [r['append'], [r['reg'], obj(9), []], [r['call'], cid_of['func::logic_not'],
                                                     [
                                                         [r['exist'], [r['reg'], obj(1), []],
                                                          [r['call'], cid_of['func::logic_and'],
                                                           [
                                                               [r['call'], cid_of['func::logic_and'],
                                                                [
                                                                    [r['call'], cid_of['func::math_equal'],
                                                                     [
                                                                         [r['at'], [r['get_member'], [r['target']],
                                                                                    cid_of['xq::position']], [obj(0)]],
                                                                         [r['reg'], obj(2), []]
                                                                     ]
                                                                     ],
                                                                    [r['call'], cid_of['func::greater_than'],
                                                                     [
                                                                         [r['at'], [r['get_member'], [r['target']],
                                                                                    cid_of['xq::position']], [obj(1)]],
                                                                         [r['call'], cid_of['func::min'],
                                                                          [
                                                                              [r['reg'], obj(7), []],
                                                                              [r['reg'], obj(3), []]
                                                                          ]
                                                                          ]
                                                                     ]
                                                                     ]
                                                                ]
                                                                ],
                                                               [r['call'], cid_of['func::less_than'],
                                                                [
                                                                    [r['at'], [r['get_member'], [r['target']],
                                                                               cid_of['xq::position']], [obj(1)]],
                                                                    [r['call'], cid_of['func::max'],
                                                                     [
                                                                         [r['reg'], obj(7), []],
                                                                         [r['reg'], obj(3), []]
                                                                     ]
                                                                     ]
                                                                ]
                                                                ]
                                                           ]
                                                           ]]
                                                     ]
                                                     ]],
              [r['assign'], [r['reg'], obj(10), []], [r['call'], cid_of['func::batch_logic_and'],
                                                      [
                                                          [r['reg'], obj(9), []]
                                                      ]
                                                      ]],
              [r['assign'], [r['reg'], obj(11), []], [r['concept_instance'], cid_of['list']]],
              [r['append'], [r['reg'], obj(11), []], [r['call'], cid_of['func::math_equal'],
                                                      [
                                                          [r['reg'], obj(7), []],
                                                          [r['reg'], obj(3), []]
                                                      ]
                                                      ]],
              [r['append'], [r['reg'], obj(11), []], [r['call'], cid_of['func::logic_not'],
                                                      [
                                                          [r['call'], cid_of['func::math_equal'],
                                                           [
                                                               [r['reg'], obj(6), []],
                                                               [r['reg'], obj(2), []]
                                                           ]
                                                           ]
                                                      ]]],
              [r['append'], [r['reg'], obj(11), []], [r['call'], cid_of['func::logic_not'],
                                                      [
                                                          [r['exist'], [r['reg'], obj(1), []],
                                                           [r['call'], cid_of['func::logic_and'],
                                                            [
                                                                [r['call'], cid_of['func::logic_and'],
                                                                 [
                                                                     [r['call'], cid_of['func::math_equal'],
                                                                      [
                                                                          [r['at'], [r['get_member'], [r['target']],
                                                                                     cid_of['xq::position']], [obj(0)]],
                                                                          [r['reg'], obj(3), []]
                                                                      ]
                                                                      ],
                                                                     [r['call'], cid_of['func::greater_than'],
                                                                      [
                                                                          [r['at'], [r['get_member'], [r['target']],
                                                                                     cid_of['xq::position']], [obj(1)]],
                                                                          [r['call'], cid_of['func::min'],
                                                                           [
                                                                               [r['reg'], obj(6), []],
                                                                               [r['reg'], obj(2), []]
                                                                           ]
                                                                           ]
                                                                      ]
                                                                      ]
                                                                 ]
                                                                 ],
                                                                [r['call'], cid_of['func::less_than'],
                                                                 [
                                                                     [r['at'], [r['get_member'], [r['target']],
                                                                                cid_of['xq::position']], [obj(1)]],
                                                                     [r['call'], cid_of['func::max'],
                                                                      [
                                                                          [r['reg'], obj(6), []],
                                                                          [r['reg'], obj(2), []]
                                                                      ]
                                                                      ]
                                                                 ]
                                                                 ]
                                                            ]
                                                            ]]
                                                      ]
                                                      ]],
              [r['assign'], [r['reg'], obj(12), []], [r['call'], cid_of['func::batch_logic_and'],
                                                      [
                                                          [r['reg'], obj(11), []]
                                                      ]
                                                      ]],
              [r['assign'], [r['reg'], obj(13), []], [r['call'], cid_of['func::logic_or'],
                                                      [
                                                          [r['reg'], obj(10), []],
                                                          [r['reg'], obj(11), []]
                                                      ]
                                                      ]],
              [r['append'], [r['reg'], obj(8), []], [r['reg'], obj(13), []]],
              [r['append'], [r['reg'], obj(8), []], [r['call'], cid_of['func::logic_not'],
                                                     [
                                                         [r['exist'], [r['reg'], obj(1), []],
                                                          [r['call'], cid_of['func::logic_and'],
                                                           [
                                                               [r['call'], cid_of['func::compare_concepts'],
                                                                [
                                                                    [r['get_member'], [r['target']],
                                                                     cid_of['xq::piece_owner']],
                                                                    [r['input'], obj(1)]
                                                                ]
                                                                ],
                                                               [r['call'], cid_of['func::logic_and'],
                                                                [
                                                                    [r['call'], cid_of['func::math_equal'],
                                                                     [
                                                                         [r['at'], [r['get_member'], [r['target']],
                                                                                    cid_of['xq::position']], [obj(0)]],
                                                                         [r['reg'], obj(6), []]
                                                                     ]
                                                                     ],
                                                                    [r['call'], cid_of['func::math_equal'],
                                                                     [
                                                                         [r['at'], [r['get_member'], [r['target']],
                                                                                    cid_of['xq::position']], [obj(1)]],
                                                                         [r['reg'], obj(7), []]
                                                                     ]
                                                                     ]
                                                                ]
                                                                ]
                                                           ]
                                                           ]]
                                                     ]
                                                     ]]
          ]
          ]
     ],
     [],
     []
     ],
    [r['if'], [r['exist'], [r['reg'], obj(1), []], [r['call'], cid_of['func::logic_and'],
                                                    [
                                                        [r['call'], cid_of['func::logic_not'],
                                                         [
                                                             [r['call'], cid_of['func::compare_concepts'],
                                                              [
                                                                  [r['get_member'], [r['target']],
                                                                   cid_of['xq::piece_owner']],
                                                                  [r['input'], obj(1)]
                                                              ]
                                                              ]
                                                         ]],
                                                        [r['call'], cid_of['func::logic_and'],
                                                         [
                                                             [r['call'], cid_of['func::math_equal'],
                                                              [
                                                                  [r['at'], [r['get_member'], [r['target']],
                                                                             cid_of['xq::position']], [obj(0)]],
                                                                  [r['reg'], obj(6), []]
                                                              ]
                                                              ],
                                                             [r['call'], cid_of['func::math_equal'],
                                                              [
                                                                  [r['at'], [r['get_member'], [r['target']],
                                                                             cid_of['xq::position']], [obj(1)]],
                                                                  [r['reg'], obj(7), []]
                                                              ]
                                                              ]
                                                         ]
                                                         ]
                                                    ]
                                                    ]],
     [
         [r['remove'], [r['reg'], obj(1), []], [r['call'], cid_of['func::logic_and'],
                                                [
                                                    [r['call'], cid_of['func::logic_not'],
                                                     [
                                                         [r['call'], cid_of['func::compare_concepts'],
                                                          [
                                                              [r['get_member'], [r['target']],
                                                               cid_of['xq::piece_owner']],
                                                              [r['input'], obj(1)]
                                                          ]
                                                          ]
                                                     ]],
                                                    [r['call'], cid_of['func::logic_and'],
                                                     [
                                                         [r['call'], cid_of['func::math_equal'],
                                                          [
                                                              [r['at'],
                                                               [r['get_member'], [r['target']], cid_of['xq::position']],
                                                               [obj(0)]],
                                                              [r['reg'], obj(6), []]
                                                          ]
                                                          ],
                                                         [r['call'], cid_of['func::math_equal'],
                                                          [
                                                              [r['at'],
                                                               [r['get_member'], [r['target']], cid_of['xq::position']],
                                                               [obj(1)]],
                                                              [r['reg'], obj(7), []]
                                                          ]
                                                          ]
                                                     ]
                                                     ]
                                                ]
                                                ]]
     ],
     [],
     []
     ],
    [r['assign'], [r['at'], [r['get_member'], [r['reg'], obj(4), []], cid_of['xq::position']], [obj(0)]],
     [r['reg'], obj(6), []]],
    [r['assign'], [r['at'], [r['get_member'], [r['reg'], obj(4), []], cid_of['xq::position']], [obj(1)]],
     [r['reg'], obj(7), []]],
    [r['if'], [r['call'], cid_of['func::compare_concepts'],
               [
                   [r['input'], obj(1)],
                   [r['concept_instance'], cid_of['xq::red_team']]
               ]
               ],
     [
         [r['assign'], [r['get_member'], [r['find'], [r['input'], obj(0)], [r['call'], cid_of['func::compare_concepts'],
                                                                            [
                                                                                [r['target']],
                                                                                [r['concept_instance'],
                                                                                 cid_of['xq::whose_turn']]
                                                                            ]
                                                                            ]], cid_of['content']],
          [r['concept_instance'], cid_of['xq::black_team']]]
     ],
     [],
     [
         [r['assign'], [r['get_member'], [r['find'], [r['input'], obj(0)], [r['call'], cid_of['func::compare_concepts'],
                                                                            [
                                                                                [r['target']],
                                                                                [r['concept_instance'],
                                                                                 cid_of['xq::whose_turn']]
                                                                            ]
                                                                            ]], cid_of['content']],
          [r['concept_instance'], cid_of['xq::red_team']]]
     ]
     ],
    [r['return'], [r['reg'], obj(0), []]]
]
