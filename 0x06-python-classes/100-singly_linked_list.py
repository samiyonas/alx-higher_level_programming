#!/usr/bin/python3

""" Node of a singly linked list """


class Node:
    """ singly node of singly linked list

    Attribute:
        self.__data (int) - element of a node
        self.__next_node (pointer) - element of a node
    """
    def __init__(self, data, next_node=None):
        """ init automatically initializes the object

        Attribute:
            data (int) - to be assigned to self.__data
            next_node (pointer) - to be assigned to self.__
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ retrieve the data from linked list

        Return:
            returns self.__data
        """
        return self.__data

    @property
    def next_node(self):
        """ retrieve the next node

        Return:
            returns self.__next_node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ data setter

        Attribute:
            value (int) - value to be assigned to self.__data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ next_node setter

        Attribute:
            value (pointer) - next node to be added
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value


""" create sorted linked list """


class SinglyLinkedList:
    """ Linked list goes here

    Attribute:
        self.__head - head of the linked list
    """
    def __init__(self):
        """ initializes the linked list """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts Nodes in ascending order of their data value

        Attribute:
            value (int) - datas of the linked list
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        ptr = self.__head
        while ptr.next_node is not None and ptr.next_node.data < value:
            ptr = ptr.next_node
        new_node.next_node = ptr.next_node
        ptr.next_node = new_node

    def __str__(self):
        """ make the object printable """
        datas = []
        ptr = self.__head
        while ptr is not None:
            datas.append(str(ptr.data))
            ptr = ptr.next_node
        return "\n".join(datas)
