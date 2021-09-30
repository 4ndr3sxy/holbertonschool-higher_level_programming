#!/usr/bin/python3
"""Class Node"""


class Node:
    """Constructor"""
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    """Get node"""
    def get_next_node(self):
        return self.__next_node

    """Set node"""
    def set_next_node(self, value):
        self.__next_node = value

    """Get data"""
    def get_data(self):
        return self.__data

    """set data"""
    def set_data(self, value):
        self.__data = value

    next_node = property(get_next_node, set_next_node)
    data = property(get_data, set_data)

"""Class Node"""


class SinglyLinkedList:
    """Constructor"""
    def __init__(self):
        self.__head = None

    """Sorted linked list"""
    def sorted_insert(self, data):
        newNode = Node(data)
        if(self.__head):
            current = self.__head
            if data < current.data:
                newNode.next_node = current
                self.__head = newNode
            else:
                while(current.next_node and current.next_node.data < data):
                    current = current.next_node
                newNode.next_node = current.next_node
                current.next_node = newNode
        else:
            self.__head = newNode

    """Str built-in"""
    def __str__(self):
        print_str = ""
        copy_linked = self.__head
        while(copy_linked):
            print_str += str(copy_linked.data)
            print_str += "\n"
            copy_linked = copy_linked.next_node
        print_str = print_str[:-1]
        return print_str
