from copy import deepcopy


class AGIObject:
    def __init__(self, concept_id: int, attributes: dict):
        self.concept_id = concept_id
        self.attributes = attributes


class AGIList:
    def __init__(self, value: list = None):
        if value is None:
            self.forward = []
            self.reverse = []
            self.value = []
        else:
            self.forward = deepcopy(value)
            self.reverse = []
            self.value = deepcopy(value)
