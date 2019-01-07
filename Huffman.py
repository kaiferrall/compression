# Compressing Text


class HeapNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


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
            return heap.append(node)
        else:
            heap.append(node)
            new_heap = self.heapify(heap)
            return new_heap

    def heapify(self, array):
        j = 0
        for i in range(1, len(array)):
            if array[i].freq < array[self.parent(i)].freq:
                array[i].freq, array[self.parent(
                    i)].freq = array[self.parent(i)].freq, array[i].freq
                j += 1
            if j != 0:
                self.heapify(array)
        return array

    def pop_2(self, heap):
        if len(heap) == 1:
            return ((heap[0], None), None)
        elif len(heap) == 2:
            return ((heap[0], heap[1]), None)
        min_1 = heap[0]
        min_2 = heap[1] if heap[1].freq < heap[2].freq else heap[2]

        heap = self.heapify(heap[1:])
        return ((min_1, min_2), heap)

    def set_child(self, parent, child):
        if parent.l_child is None:
            parent.l_child = child
        else:
            parent.r_child = child


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
            node = HeapNode(key, dict[key])
            freq_array.append(node)
        return freq_array

    def pop_min_vals(self, heap):
        min_heap = Heap_Utils()
        pop = min_heap.pop_2(heap)
        sum = pop[0][0].freq + pop[0][1].freq
        new_node = HeapNode(None, sum)
        final_heap = min_heap.insert_node(pop[1], new_node)
        return (pop[0], final_heap)


def create_tree(text):
    Coder = HuffmanCoding()
    Heap = Heap_Utils()

    freq_dict = Coder.frequency_dict(text)
    freq_array = Coder.frequency_array(freq_dict)
    min_heap = Heap.heapify(freq_array)
    min_vals = Coder.pop_min_vals(min_heap)


'''
comp = HuffmanCoding()
heap = Heap_Utils()

binary = comp.string_to_binary("this is somne random string here snad")
dict = comp.frequency_dict("this is somne random string here snad")

ar = comp.frequency_array(dict)
print(dict)
heap_ar = heap.heapify(ar)
'''
text = "th"
head = create_tree(text)
print(head)
