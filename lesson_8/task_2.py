"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, deque


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    # Считаем путь до нужного символа
    def show_path(self, _char):

        def _show_path(node, _char):
            path = ''
            if node is None:
                return False, path
            if node.value == _char:
                return True, path
            is_find_l, _path_l = _show_path(node.left, _char)
            if is_find_l:
                path += '0' + _path_l
                return True, path
            is_find_r, _path_r = _show_path(node.right, _char)
            if is_find_r:
                path += '1' + _path_r
                return True, path
            return False, 'Char doesn\'t exist'

        _, path = _show_path(self, _char)
        return path


def encode_huffman(s):
    arr = Counter(s)
    # Скопируем словар символов, в дальнейшем понадобится
    symbols_list = arr.keys()
    arr = arr.most_common()
    # Сортируем получаемую очередь по возрастанию относительно частнотности
    # и по убыванию относительно ASCII-таблицы (to-do: разобраться зачем второе всё-таки)
    arr = sorted(arr, key=lambda tup: (-tup[1], tup[0]), reverse=True)
    arr = deque(arr)
    # Составляем дерево (и словарь кодов)
    while True:
        if len(arr) < 2:
            break
        freq = arr[0][1] + arr[1][1]
        _left, _right = arr[0][0], arr[1][0]
        if not isinstance(_left, Node):
            _left = Node(arr[0][0])
        if not isinstance(_right, Node):
            _right = Node(arr[1][0])
        _node = Node(left=_left, right=_right)
        # Удаляем элементы, которые соединили через узел (т.е. первые 2 элемента массива)
        arr.popleft()
        arr.popleft()
        # Если частотность больше максимальной или после удаления элементов из массива, элементов там не осталось, то
        # просто добавляем полученный элемент в массив (дерево)
        if len(arr) < 1 or freq > arr[len(arr) - 1][1]:
            arr.append((_node, freq))
        elif freq <= arr[0][1]:
            arr.appendleft((_node, freq))
        else:
            for i in range(len(arr)):
                if arr[i][1] < freq <= arr[i + 1][1]:
                    arr.insert(i + 1, (_node, freq))
                    break

    huffman_dict = {}
    for key in symbols_list:
        huffman_dict[key] = arr[0][0].show_path(key)

    # Непосредственно кодирование
    _res = ''
    res_list = list(s)
    for i in res_list:
        _res += huffman_dict[i]
    return _res


def test_encode(func):
    assert '0011111010110001001010101100111110001001' == func('beep boop beer!')
    print('TEST IS OK')


test_encode(encode_huffman)

s = input('Введите строку, которую хотите закодировать: ')
res = encode_huffman(s)
# Красиво распечатываем - добавление разделительных пробелов можно добавить и в саму функцию
for i in range(len(res)):
    print(res[i], end='')
    if (i + 1) % 4 == 0:
        print(' ', end='')
