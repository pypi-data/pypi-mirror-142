#!/usr/bin/env python3

"""
2D grid used for teaching CS 110 at BYU

Code developed for Stanford CS106A by Nick Parlante
"""
# Apr 2021: more informative exception for bad x,y in get() and set()
# Jan 2021: add copy()


class Grid:
    """
    2D grid with x,y int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        """
        Create grid width by height.
        Initially all locations hold None.
        """
        # Pretty agro use of comprehensions!
        self.array = [[None for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height

    @staticmethod
    def build(lst):
        """
        Utility.
        Construct Grid using a nested-lst literal
        e.g. this makes a 3 by 2 grid:
        Grid.build([[1, 2, 3], [4, 5 6]])
        >>> Grid.build([[1, 2, 3], [4, 5, 6]])
        [[1, 2, 3], [4, 5, 6]]
        """
        check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        grid = Grid(width, height)
        grid.array = lst  # slight waste, but keeps ctor params simple
        return grid

    def get(self, x, y):
        """
        Gets the value stored value at x,y.
        x,y should be in bounds.
        """
        error = None
        try:
            return self.array[y][x]
        except IndexError as e:
            error = e

        if error:
            # Bad x,y is a common student error, so provide a more spelled-out exception
            # instead of the natural low-level list index error the implementation hits.
            # If we do this in the except block, Doctest reports *both* errors
            # which is confusing, so we do it down here.
            raise RuntimeError('out of bounds get({}, {}) on grid width {}, height {}'
                            .format(x, y, self.width, self.height))

    def set(self, x, y, val):
        """
        Sets a new value into the grid at x,y.
        x,y should be in bounds.
        """
        error = None
        try:
            self.array[y][x] = val
        except IndexError as e:
            error = e

        if error:
            raise Exception('out of bounds get({}, {}) on grid width {}, height {}'
                            .format(x, y, self.width, self.height))

    def in_bounds(self, x, y):
        """Returns True if the x,y is in bounds of the grid. False otherwise."""
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def copy(self):
        """Return a new grid, a duplicate of the original."""
        # Cute: leverage the build() facility
        return Grid.build(self.array)

    def __str__(self):
        return repr(self.array)

    # In particular Doctest seems to use this, so crucial to make
    # Grid work in Doctests.
    def __repr__(self):
        return repr(self.array)

    def __eq__(self, other):
        for x in range(self.width):
            for y in range(self.height):
                if not other.in_bounds(x, y):
                    return False
                if self.get(x, y) != other.get(x, y):
                    return False
        return True


def check_list_malformed(lst):
    """
    Given a list that represents a 2-d nesting, checks that it has the
    right type and the sublists are all the same len.
    Raises exception for malformations.
    Since these lists are tricky to type in by hand, we
    help people out by flagging these structural errors.
    """
    if not lst or type(lst) != list:
        raise Exception('Expecting list but got:' + str(lst))

    if len(lst) >= 2:
        size = len(lst[0])
        for sub in lst:
            if len(sub) != size:
                raise Exception("Sub-lists are not all the same length:" + str(lst))

