nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]]

class FlatIterator(list):
    def __init__(self, _list):
        self._list = _list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        flat_list = sum(self._list,[])
        self.cursor += 1
        if self.cursor == len (flat_list):
            raise StopIteration
        return flat_list[self.cursor]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
print('__________________________________________')

def flat_generator(list_1):
    lt = []
    yield sum([item for item in list_1], lt)

for item in  flat_generator(nested_list):
	print(item)

