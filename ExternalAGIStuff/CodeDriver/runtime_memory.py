from exception import AGIException
from copy import deepcopy


class Register:
    def __init__(self, index, child_indices):
        self.index = index
        self.child_indices = child_indices
        self.value = None


class Iterator:
    def __init__(self, iter_id):
        self.id = iter_id
        self.value = 0


class ResourceManager:
    def __init__(self, input_params):
        self.input_params = input_params
        self.registers = []
        self.iterators = []

    def has_reg(self, index, child_indices: tuple):
        for register in self.registers:
            if register.index == index and register.child_indices == child_indices:
                return True
        return False

    def create_reg(self, index, child_indices: tuple):  # the reg_id should be local id
        for register in self.registers:
            if register.index == index and register.child_indices == child_indices:
                raise AGIException('Register already created.')
        self.registers.append(Register(index, child_indices))

    def create_iterator(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                raise AGIException('Try to create an iterator twice.')
        self.iterators.append(Iterator(iter_id))

    def update_iterator(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                iterator.value += 1
                return
        raise AGIException('Can\'t find target iterator.')

    def destroy_iterator(self, iter_id):
        for i, iterator in enumerate(self.iterators):
            if iterator.id == iter_id:
                self.iterators.pop(i)
                return
        raise AGIException('Can\'t find target iterator.')

    def get_iterator_value(self, iter_id):
        for iterator in self.iterators:
            if iterator.id == iter_id:
                return iterator.value
        raise AGIException('Can\'t find target iterator.')

    def set_reg_value(self, index, child_indices: tuple, value):
        for register in self.registers:
            if register.index == index and register.child_indices == child_indices:
                register.value = value
                return
        raise AGIException('Can\'t find target register.')

    def get_reg_value(self, index, child_indices: tuple):
        for register in self.registers:
            if register.index == index and register.child_indices == child_indices:
                return register.value
        raise AGIException('Can\'t find target register.')


"""
    def get_reg(self, index, child_indices) -> Register:
        for register in self.registers:
            if register.index == index and register.child_indices == child_indices:
                return register
        raise AGIException('Can\'t find target register.')
"""
