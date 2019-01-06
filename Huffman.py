# Compressing Text


class TreeNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


class Heap():
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

    def frequency_array(self, dic):
        freq_array = []
        for key in dict:
            node = TreeNode(key, dict[key])
            freq_array.append(node)
        return freq_array


comp = HuffmanCoding()
heap = Heap()

binary = comp.string_to_binary("this is somne random string here snad")
dict = comp.frequency_dict("this is somne random string here snad")
ar = comp.frequency_array(dict)
print(ar)
heap_ar = heap.heapify(ar)
for i in range(len(heap_ar)):
    print(heap_ar[i].freq)
