from collections import namedtuple


Node = namedtuple("Node", "meta children")
Node.__doc__ = "Container for nodes and its metadata"


def parser(nrs):
    """Parses an iterable of numbers into a tree of Node objects"""
    itr = iter(nrs)
    return _parser(itr)


def _parser(nrs):
    """Recursive parser of numbers into a tree of Node objects
    """
    n_children = next(nrs)
    n_meta = next(nrs)
    # If the Node has children, first parse the children
    children = [_parser(nrs) for i in range(n_children)]
    # Parsing the children has consumed the iterator up to
    # the start of the meta-data
    meta = [next(nrs) for i in range(n_meta)]
    return Node(children=children, meta=meta)


def metasum(node):
    """Recursivly add all the meta data for Part 1"""
    return sum(node.meta) + sum(map(metasum, node.children))


def refsum(node):
    """Recusively add meta data in the way specified in Part 2"""
    
    # The value of a node depends on whether it has child nodes.
    if not node.children:
        # (then) its value is the sum of its metadata entries
        return sum(node.meta)

    # (else) its value is the sum of its metadata entries
    # skip over metadata which are 0 and those out of bounds
    references = (idx-1 for idx in node.meta if 0 < idx <= len(node.children))
    return sum(refsum(node.children[idx]) for idx in references)
    

if __name__ == "__main__":
    list_of_numbers = map(int, open("day8.txt").read().split())
    tree = parser(list_of_numbers)
    print("Part1:", metasum(tree))
    print("Part2:", refsum(tree))
