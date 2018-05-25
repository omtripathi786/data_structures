def question1(s, t):
    if not s or not t:
        return False
    len_s = len(s)
    len_t = len(t)
    sort_t = list(t)
    sort_t.sort()
    for i in range(len_s - len_t + 1):
        comp_str = list(s[i: i + len_t])
        comp_str.sort()
        if comp_str == sort_t:
            return True
    return False


def question2(a):
    if not a:
        return ''
    len_a = len(a)
    for item in range(len_a, 0, -1):
        sub_str = a[0:item]
        if sub_str == sub_str[::-1]:
            return sub_str
    return ''


def question3(G):
    if type(G) != dict:
        return "Error: G is not dictionary!"
    if len(G) < 2:
        return "Error: G has not enough vertices to form edges!"
    vertices = G.keys()
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))
    edges = sorted(list(edges))
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)
        if len(vertices) == 1:
            break
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph


def question4(T, r, n1, n2):
    if not T:
        return 'Error: Tree is empty'
    n1_ps = []
    while n1 != r:
        n1 = parent(T, n1)
        n1_ps.append(n1)
    if len(n1_ps) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in n1_ps:
            return n2
    return -1


def parent(T, n):
    # return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_length(ll):
    if ll.next == None:
        return 1
    length_ll = 0
    current_node = ll
    current_node2 = ll.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_ll += 1

    if current_node == None:
        return length_ll
    else:
        return -1


def question5(ll, m):
    current_node = ll
    length_ll = get_length(ll)
    if m > length_ll:
        return None
    for i in range(length_ll - m):
        current_node = current_node.next
    return current_node.data

if __name__ == '__main__':
    print '----------Test Case For Question 1------------'
    # function should print False
    print question1(None, None)
    # function should print True
    print question1('udacity', 'yit')
    # function should print False
    print question1('udacity', 'uy')
    print '----------Test Case For Question 1 End---------'
    print ''

    print '----------Test Case For Question 2------------'
    # function should return an empty string
    print question2(None)
    # function should return omo
    print question2('omomm')
    # function should return mom
    print question2('mom')
    print '----------Test Case For Question 2 End--------'
    print ''

    print '----------Test Case For Question 3------------'
    # function should return Error: G is not dictionary!
    print question3(None)
    # function should return Error: G has not enough vertices to form edges!
    print question3({})
    G = {'A': [('B', 2), ('D', 1)],
         'B': [('A', 2), ('c', 2), ('D', 5)],
         'C': [('D', 7), ('B', 2)],
         'D': [('A', 1), ('C', 7)]}
    # function should return {'A': [('D', 1), ('B', 2)], 'C': [('B', 2)], 'B': [('A', 2), ('C', 2)], 'D': [('A', 1)]}
    print question3(G)
    print '----------Test Case For Question 3 End--------'
    print ''

    print '----------Test Case For Question 4------------'
    # function should return 3
    print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
    # function should return Error: Tree is empty
    print question4(None,
              3,
              1,
              4)
    # function should return Error: Tree is empty
    print question4([],
                    3,
                    1,
                    4)
    print '----------Test Case For Question 4 End--------'
    print ''

    print '----------Test Case For Question 5------------'
    ll = Node(10)
    ll.next = Node(11)
    ll.next.next = Node(12)
    ll.next.next.next = Node(13)
    ll.next.next.next.next = Node(14)
    ll.next.next.next.next.next = Node(15)
    # function should return 15 here
    print question5(ll, 1)
    # function should return 14 here
    print question5(ll, 2)
    # function should return None here
    print question5(ll, 9)
    print '----------Test Case For Question 5 End--------'
