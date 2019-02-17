class TreeNode():
    def __init__(self, char, freq, l_child, r_child):
        self.char = char
        self.freq = freq
        self.l_child = l_child
        self.r_child = r_child


class Heap_Utils():
    def parent(self, loc):
        x = loc + 1
        y = x//2
        return y - 1

    def insert_node(self, heap, node):
        if len(heap) == 0:
            new_heap = [node]
            return new_heap
        else:
            heap.append(node)
            new_heap = self.heapify(heap)
            return new_heap

    def heapify(self, array):
        j = 0
        for i in range(1, len(array)):
            if array[i].freq < array[self.parent(i)].freq:
                array[i], array[self.parent(
                    i)] = array[self.parent(i)], array[i]
                j += 1
            if j != 0:
                self.heapify(array)
        return array

    def pop_2(self, heap):
        length = len(heap)
        min_1, min_2 = None, None
        if length >= 3:
            min_1 = heap[0]
            min_2 = heap[1] if heap[1].freq <= heap[2].freq else heap[2]
            heap = self.heapify(heap[2:])
            return (min_1, min_2, heap)
        elif length == 2:
            min_1, min_2 = heap[0], heap[1]
            return (min_1, min_2, [])
        elif length == 1:
            min_1 = heap[0]
            return (min_1, None, [])


class HuffmanCoding():
    def string_to_binary(self, str):
        bit_str = ""
        for char in str:
            byte = ord(char)
            bits = bin(byte)[2:].rjust(8, "0")
            bit_str += bits
        return bit_str

    def frequency_dict(self, str):
        frequency = {}
        for char in str:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def frequency_array(self, dict):
        freq_array = []
        for key in dict:
            node = TreeNode(key, dict[key], None, None)
            freq_array.append(node)
        return freq_array

    def pop_min_vals(self, heap):
        min_heap = Heap_Utils()
        pop = min_heap.pop_2(heap)
        sum = pop[0].freq + pop[1].freq if pop[1] is not None else pop[0].freq
        new_node = TreeNode(None, sum, pop[0], pop[1])
        new_heap = min_heap.insert_node(pop[2], new_node)
        return new_heap


coder = HuffmanCoding()
utils = Heap_Utils()


def create_tree():
    dict = coder.frequency_dict("this is some random text")
    array = coder.frequency_array(dict)
    heap = utils.heapify(array)
    for i in heap:
        print((i.char, i.freq))
    while len(heap) > 1:
        heap = coder.pop_min_vals(heap)
    print("-----------")
    return heap
def traverse_left(tree):
    current_node = tree[0]
    while current_node is not None:
        print((current_node.char, current_node.freq))
        current_node = current_node.l_child


tree = create_tree()
traverse_left(tree)
