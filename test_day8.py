from day8 import parser, refsum, metasum, Node

example = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
example_tree = Node(meta=[1, 1, 2], children=[
                   Node(meta=[10, 11, 12], children=[]), 
                   Node(meta=[2], children=[
                       Node(meta=[99], children=[])])])

def test_parse():
    # No children
    assert parser([0, 1, 99]) == Node(children=[], meta=[99])
    # With children
    assert parser(example) == example_tree

def test_part1():
    assert metasum(example_tree) == 138

def test_part2():
    # test no children
    assert refsum(Node(children=[], meta=[1, 2, 3])) == 6
    # test children
    assert refsum(Node(meta=[3,2], children=[
        Node(children=[], meta=[1,]),
        Node(children=[], meta=[2]),
        Node(children=[], meta=[3])])) == 5
    # test example
    assert refsum(example_tree) == 66

