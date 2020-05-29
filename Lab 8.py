#lab 8

"""Problem 1"""
###pre order traversal 
##
##A B D G C E F H
##
###post order traversal
##
##G D B E H F C A
##
###inorder traversal
##
##B G D A E C H F
##
##
###heightoftree
##
##3
##
###depth of tree
##
##2

#Problem 2



class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None
            
    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def add_first(self, data):
        self.add_after(self.header, data)

    def add_last(self, data):
        self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        self.add_after(self.node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        node.disconnect()
        self.size -= 1
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.first_node()
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next

    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) + ']'



def right_circular_shift(lnk_lst):
  #Storing values of last, secondlast, and first node
  last_node=lnk_lst.last_node()
  second_last_node=last_node.prev
  first_node=lnk_lst.first_node()
  #setting the firstpart of the linkedlist
  lnk_lst.header.next=last_node
  last_node.prev=lnk_lst.header
  #moving the second last node up by one
  second_last_node.next=lnk_lst.trailer
  lnk_lst.trailer.prev=second_last_node
  #making changes to the second node
  first_node.prev=lnk_lst.header.next
  lnk_lst.header.next.next=first_node
  return lnk_lst
  

lnk_lst = DoublyLinkedList()
lnk_lst.add_last(4)
lnk_lst.add_last(5)
lnk_lst.add_last(5)
lnk_lst.add_last(4)
lnk_lst.add_last(7)
lnk_lst.add_first(0)
print(lnk_lst)
right_circular_shift(lnk_lst)
print(lnk_lst)
right_circular_shift(lnk_lst)
print(lnk_lst)





#Problem 3



class LinkedBinaryTree:
    class Node:

        def __init__(self, data, left=None, right=None):
            # Set the data, left, and right values
            self.data = data
            self.parent = None
            self.left = left
            self.right = right

            # As described above, if self.left is a node (not None), then its parent is self: we set self.left.parent = self
            if self.left is not None:
                self.left.parent = self
            # We do the same for self.right. If it is a node, set its parent to `self`
            if self.right is not None:
                self.right.parent = self
    # End of Node class (LinkedBinaryTree.Node)

    def __init__(self, root=None):
        # Create a new LinkedBinaryTree with the given Node as the root. Compute and store the size (number of nodes)
        self.root = root
        self.size = self.subtree_count(self.root)

    # Returns number of nodes in the subtree rooted by `subtree_root`
    def subtree_count(self, subtree_root):
        if subtree_root is None:
            return 0

        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)

        return left_count + right_count + 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum(self.root)

    # Returns the sum of all the (data values of the) nodes in the subtree rooted by `subtree_root`
    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)

        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)


    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return 0
        elif subtree_root.left is None:
            # right is not None (but left is)
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            # left is not None (but right is)
            return 1 + self.subtree_height(subtree_root.left)
        else:
            # left and right are both not None
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)

            return 1 + max(left_height, right_height)


    
    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    # postorder traversal
    def postorder(self):
        yield from self.subtree_postorder(self.root)


    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postrder(subtree_root.right)
            yield subtree_root.data


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


    def breadth_first(self):
        if self.is_empty():
            return
        
        node_queue = ArrayQueue.ArrayQueue()
        node_queue.enqueue(self.root)
        while node_queue.is_empty() == False:
            curr_node = node_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                node_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                node_queue.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

def count_val(root,val):
  count=0
  ##need to write traversal code again since you cannot traverse using root as a parameter in the function
  def subtree_inorder(root):
    if root is None:
        return
    else:
        yield from subtree_inorder(root.left)
        yield root.data
        yield from subtree_inorder(root.right)
  generator_to_iterate=subtree_inorder(root)
  for elem in generator_to_iterate:
    if elem==val:
      count+=1
  return count
      




root=LinkedBinaryTree.Node(1)
root.left=LinkedBinaryTree.Node(2)
root.right=LinkedBinaryTree.Node(3)
root.left.left=LinkedBinaryTree.Node(4)
root.left.right=LinkedBinaryTree.Node(4)
root.right.left=LinkedBinaryTree.Node(4)
root.right.right=LinkedBinaryTree.Node(1)
binaryTree=LinkedBinaryTree(root)
print(count_val(root,2))
print(count_val(root,3))
print(count_val(root,4))





  



#Problem 4


class ArrayQueue:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        # Use a list to store queue elements
        # self.data is the list used to store elements
        # len(self.data) is our capacity (how many elements we can store before resizing
        # self.num_of_elems is the number of elements in the queue
        # self.front_ind will be the index of the "front" of the queue (the first element to have been inserted)
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None

    # O(1) time
    def __len__(self):
        # len(self) is the number of elements in the queue == self.num_of_elems
        return self.num_of_elems

    # O(1) time
    def is_empty(self):
        # Queue is empty if it has no elements (len is 0)
        return len(self) == 0

    # Amortized worst case running time is O(1)
    # But an individual enqueue can take worst case O(n) if resize is done
    # This time complexity is just like the append operation in dynamic arrays
    def enqueue(self, elem):
        # If number of elements == capacity (we've filled the list completely), resize
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
            
        # If list was empty before trying to enqueue `elem`,
        # Put it at index 0 at set the front_ind to 0 (since this is the first elem in the queue)
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        # Otherwise, if the queue already had elements
        else:
            # back_ind is the index of the "back" of the queue
            # The back is where we will add new elements
            # Using mod (as in % len(self.data)) makes the back "wrap around"
            #       to index 0 if it exceeds len(self.data)
            # Example: [None, None, None, 1];
            #       front_ind == 3, num_of_elems == 1, len(self.data) == 4
            #       Then: back_ind = (3 + 1) % 4 = 0
            # Another Example: [3, None, 1, 2];
            #       front_ind == 2, num_of_elems == 3, len(self.data) == 4
            #       Then: back_ind = (2 + 3) % 4 = 1
            #       1 is at the front of the queue
            #       3 is "last" in the queue, and the new element will be after 3
            #       If the new element is 4, after inserting, the array will be: [3, 4, 1, 2] and 4 is now "last"
            # This is often referred to as a "circular array" because of how we cycle back around to the beginning of the queue
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1

    # Amortized worst case running time of O(1)
    # But, an individual dequeue might cause a resize with running time O(n)
    # The time complexity is just like pop in dynamic arrays
    def dequeue(self):
        # Raise an exception if the queue is empty (we can't remove from an empty queue!)
        if self.is_empty():
            raise Exception("Queue is empty")
        # Get the elem at the front of the queue
        # Then set the front to None so that it is "reset"
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        # Once we've removed an element from the front, the next element is now the front
        # Once again, the front should cycle back to index 0 ("wrap around"), so we use mod (% len(self.data))
        # Example: [None, None, 1, 2];
        #       front_ind == 2, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get: [None, None, None, 2]; front_ind == 3; and num_of_elems == 1
        # Another Example: [2, None, None, 1];
        #       front_ind == 3, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get [2, None, None, None], front_ind = (3 + 1) % 4 = 0; num_of_elems == 1
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        # After removing the front, check if queue is empty. There is no "front" in an empty queue
        if self.is_empty():
            self.front_ind = None
        # As with dynamic arrays, we shrink the underlying array (by half) if we are using less than 1/4 of the capacity
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem

    # O(1) running time
    def first(self):
        # The first element in the queue is at the "front" index
        # But we raise an error if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    # Resizing takes time O(n) where n is the number of elements in the queue
    def resize(self, new_capacity):
        # Create new array of size new_capacity, and copy elements to new array
        old_data = self.data
        self.data = [None] * new_capacity
        # The "front" of the old array is at front_ind. We will start copying from the front.
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            # We copy from the old array starting at the front, to index 0 in the new array
            # In the new array, the "front" will be at index 0
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        # Update the front -- it is now at index 0
        self.front_ind = 0





class LinkedBinaryTree:
    class Node:
        # Binary Tree nodes store a single data element, and a reference to their left child and right child
        # It is also helpful to keep track of the parent of a Node
        # The parent of a node v is the node u for which v is either the left child or right child
        # That is, if u.left is v or u.right is v, then v.parent is u (and vice-versa)
        def __init__(self, data, left=None, right=None):
            # Set the data, left, and right values
            self.data = data
            self.parent = None
            self.left = left
            self.right = right

            # As described above, if self.left is a node (not None), then its parent is self: we set self.left.parent = self
            if self.left is not None:
                self.left.parent = self
            # We do the same for self.right. If it is a node, set its parent to `self`
            if self.right is not None:
                self.right.parent = self
    # End of Node class (LinkedBinaryTree.Node)

    def __init__(self, root=None):
        # Create a new LinkedBinaryTree with the given Node as the root. Compute and store the size (number of nodes)
        self.root = root
        self.size = self.subtree_count(self.root)

    # Returns number of nodes in the subtree rooted by `subtree_root`
    def subtree_count(self, subtree_root):
        if subtree_root is None:
            return 0

        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)

        return left_count + right_count + 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum(self.root)

    # Returns the sum of all the (data values of the) nodes in the subtree rooted by `subtree_root`
    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)

        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)

    # Returns the height of the subtree rooted by `subtree_root`
    # Recall the height is the max length of any path (= number of EDGES on the path)
    #   from the root (i.e., `subtree_root`) to a leaf node.
    # Important to note: The length of the path from `subtree_root` to either of its children is 1
    #   (a child is connected directly to its parent by a single edge)
    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return 0
        elif subtree_root.left is None:
            # right is not None (but left is)
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            # left is not None (but right is)
            return 1 + self.subtree_height(subtree_root.left)
        else:
            # left and right are both not None
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)

            return 1 + max(left_height, right_height)


    ### The following are several different ways to traverse the nodes of a tree
    ### preorder, inorder, postorder work by traversing the subtrees rooted by the current node's children recursively
    ###   We also yield the current node.
    ### preorder yields the current node before recursing on the left, then right subtrees (the subtrees rooted by the left and right child, respectively)
    ### inorder recurses on the right subtree, then yields the current node, then recurses on the right subtree
    ### postorder recurses on the left, then right subtrees, and yields the current node after recursing.
    ### Remember it this way: when do we yield the current node? pre = BEFORE recursing. in = IN-between recursive calls. post = AFTER recursing.

    # preorder traversal
    def preorder(self):
        yield from self.subtree_preorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in preorder
    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    # postorder traversal
    def postorder(self):
        yield from self.subtree_postorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in postorder
    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postrder(subtree_root.right)
            yield subtree_root.data

    # inorder traversal
    def inorder(self):
        yield from self.subtree_inorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in inorder
    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


    ## The last way to "traverse" the tree is rather different.
    ## Sometimes called "level order", it yields all the nodes in level 0, then all the nodes in level 1, then level 2, ... (and so on)
    ## It is sometimes also referred to by the name of the method used to accomplish this "level order" traversal: "breadth-first" search
    ## It uses a queue!
    def breadth_first(self):
        if self.is_empty():
            return
        
        node_queue = ArrayQueue()
        node_queue.enqueue(self.root)
        while node_queue.is_empty() == False:
            curr_node = node_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                node_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                node_queue.enqueue(curr_node.right)

    # We will define our iterator to use the breadth-first ("in-order") method of traversing the tree
    def __iter__(self):
        for node in self.breadth_first():
            yield node.data


def invertedbinarytree(linkedbinarytree):
  listnodes=[]
  generator= linkedbinarytree.breadth_first()
  for node in generator:
    listnodes.append(node)
  for node in listnodes:
    if node.right is not None or node.left is not None:
      node.right,node.left=node.left,node.right
    elif node.right is not None and node.left is None:
      node.left=node.right
      node.right=None
    elif node.right is None and node.left is not None:
      node.right=node.left
      node.left=None
      
  newtree=LinkedBinaryTree(listnodes[0])
  return newtree
  
  
    
      
    
    
root_node = LinkedBinaryTree.Node(4)
root_node.left=LinkedBinaryTree.Node(7)
root_node.right=LinkedBinaryTree.Node(2)
root_node.left.left=LinkedBinaryTree.Node(9)
root_node.left.right=LinkedBinaryTree.Node(6)
root_node.right.left= LinkedBinaryTree.Node(3)
root_node.right.right=LinkedBinaryTree.Node(1)
tree=LinkedBinaryTree(root_node)
for elem in tree.breadth_first():
  print(elem.data)
newtree=invertedbinarytree(tree)
print(newtree)
for elem in newtree.breadth_first():
  print(elem.data)
newtree=invertedbinarytree(tree)









      




#Problem 5


class ArrayQueue:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        # Use a list to store queue elements
        # self.data is the list used to store elements
        # len(self.data) is our capacity (how many elements we can store before resizing
        # self.num_of_elems is the number of elements in the queue
        # self.front_ind will be the index of the "front" of the queue (the first element to have been inserted)
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None

    # O(1) time
    def __len__(self):
        # len(self) is the number of elements in the queue == self.num_of_elems
        return self.num_of_elems

    # O(1) time
    def is_empty(self):
        # Queue is empty if it has no elements (len is 0)
        return len(self) == 0

    # Amortized worst case running time is O(1)
    # But an individual enqueue can take worst case O(n) if resize is done
    # This time complexity is just like the append operation in dynamic arrays
    def enqueue(self, elem):
        # If number of elements == capacity (we've filled the list completely), resize
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
            
        # If list was empty before trying to enqueue `elem`,
        # Put it at index 0 at set the front_ind to 0 (since this is the first elem in the queue)
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        # Otherwise, if the queue already had elements
        else:
            # back_ind is the index of the "back" of the queue
            # The back is where we will add new elements
            # Using mod (as in % len(self.data)) makes the back "wrap around"
            #       to index 0 if it exceeds len(self.data)
            # Example: [None, None, None, 1];
            #       front_ind == 3, num_of_elems == 1, len(self.data) == 4
            #       Then: back_ind = (3 + 1) % 4 = 0
            # Another Example: [3, None, 1, 2];
            #       front_ind == 2, num_of_elems == 3, len(self.data) == 4
            #       Then: back_ind = (2 + 3) % 4 = 1
            #       1 is at the front of the queue
            #       3 is "last" in the queue, and the new element will be after 3
            #       If the new element is 4, after inserting, the array will be: [3, 4, 1, 2] and 4 is now "last"
            # This is often referred to as a "circular array" because of how we cycle back around to the beginning of the queue
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1

    # Amortized worst case running time of O(1)
    # But, an individual dequeue might cause a resize with running time O(n)
    # The time complexity is just like pop in dynamic arrays
    def dequeue(self):
        # Raise an exception if the queue is empty (we can't remove from an empty queue!)
        if self.is_empty():
            raise Exception("Queue is empty")
        # Get the elem at the front of the queue
        # Then set the front to None so that it is "reset"
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        # Once we've removed an element from the front, the next element is now the front
        # Once again, the front should cycle back to index 0 ("wrap around"), so we use mod (% len(self.data))
        # Example: [None, None, 1, 2];
        #       front_ind == 2, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get: [None, None, None, 2]; front_ind == 3; and num_of_elems == 1
        # Another Example: [2, None, None, 1];
        #       front_ind == 3, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get [2, None, None, None], front_ind = (3 + 1) % 4 = 0; num_of_elems == 1
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        # After removing the front, check if queue is empty. There is no "front" in an empty queue
        if self.is_empty():
            self.front_ind = None
        # As with dynamic arrays, we shrink the underlying array (by half) if we are using less than 1/4 of the capacity
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem

    # O(1) running time
    def first(self):
        # The first element in the queue is at the "front" index
        # But we raise an error if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    # Resizing takes time O(n) where n is the number of elements in the queue
    def resize(self, new_capacity):
        # Create new array of size new_capacity, and copy elements to new array
        old_data = self.data
        self.data = [None] * new_capacity
        # The "front" of the old array is at front_ind. We will start copying from the front.
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            # We copy from the old array starting at the front, to index 0 in the new array
            # In the new array, the "front" will be at index 0
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        # Update the front -- it is now at index 0
        self.front_ind = 0



class LinkedBinaryTree:
    class Node:
        # Binary Tree nodes store a single data element, and a reference to their left child and right child
        # It is also helpful to keep track of the parent of a Node
        # The parent of a node v is the node u for which v is either the left child or right child
        # That is, if u.left is v or u.right is v, then v.parent is u (and vice-versa)
        def __init__(self, data, left=None, right=None):
            # Set the data, left, and right values
            self.data = data
            self.parent = None
            self.left = left
            self.right = right

            # As described above, if self.left is a node (not None), then its parent is self: we set self.left.parent = self
            if self.left is not None:
                self.left.parent = self
            # We do the same for self.right. If it is a node, set its parent to `self`
            if self.right is not None:
                self.right.parent = self
    # End of Node class (LinkedBinaryTree.Node)

    def __init__(self, root=None):
        # Create a new LinkedBinaryTree with the given Node as the root. Compute and store the size (number of nodes)
        self.root = root
        self.size = self.subtree_count(self.root)

    # Returns number of nodes in the subtree rooted by `subtree_root`
    def subtree_count(self, subtree_root):
        if subtree_root is None:
            return 0

        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)

        return left_count + right_count + 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum(self.root)

    # Returns the sum of all the (data values of the) nodes in the subtree rooted by `subtree_root`
    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)

        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)

    # Returns the height of the subtree rooted by `subtree_root`
    # Recall the height is the max length of any path (= number of EDGES on the path)
    #   from the root (i.e., `subtree_root`) to a leaf node.
    # Important to note: The length of the path from `subtree_root` to either of its children is 1
    #   (a child is connected directly to its parent by a single edge)
    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return 0
        elif subtree_root.left is None:
            # right is not None (but left is)
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            # left is not None (but right is)
            return 1 + self.subtree_height(subtree_root.left)
        else:
            # left and right are both not None
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)

            return 1 + max(left_height, right_height)


    ### The following are several different ways to traverse the nodes of a tree
    ### preorder, inorder, postorder work by traversing the subtrees rooted by the current node's children recursively
    ###   We also yield the current node.
    ### preorder yields the current node before recursing on the left, then right subtrees (the subtrees rooted by the left and right child, respectively)
    ### inorder recurses on the right subtree, then yields the current node, then recurses on the right subtree
    ### postorder recurses on the left, then right subtrees, and yields the current node after recursing.
    ### Remember it this way: when do we yield the current node? pre = BEFORE recursing. in = IN-between recursive calls. post = AFTER recursing.

    # preorder traversal
    def preorder(self):
        yield from self.subtree_preorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in preorder
    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    # postorder traversal
    def postorder(self):
        yield from self.subtree_postorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in postorder
    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postrder(subtree_root.right)
            yield subtree_root.data

    # inorder traversal
    def inorder(self):
        yield from self.subtree_inorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in inorder
    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


    ## The last way to "traverse" the tree is rather different.
    ## Sometimes called "level order", it yields all the nodes in level 0, then all the nodes in level 1, then level 2, ... (and so on)
    ## It is sometimes also referred to by the name of the method used to accomplish this "level order" traversal: "breadth-first" search
    ## It uses a queue!
    def breadth_first(self):
        if self.is_empty():
            return
        
        node_queue = ArrayQueue()
        node_queue.enqueue(self.root)
        while node_queue.is_empty() == False:
            curr_node = node_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                node_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                node_queue.enqueue(curr_node.right)

    # We will define our iterator to use the breadth-first ("in-order") method of traversing the tree
    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

            
    def subtree_children_distance(self,subtree_root):
      main_list=[]
      result_list=[0,0,0]
      def subtree_preorder(subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from subtree_preorder(subtree_root.left)
            yield from subtree_preorder(subtree_root.right)
            
      generator=subtree_preorder(subtree_root)
      for elem in generator:
        main_list.append(elem)
      print(main_list)
      for elem in main_list:
        if elem.right is None and elem.left is None:
          result_list[0]+=1
        elif elem.right is None and elem.left is not None:
          result_list[1]+=1
        elif elem.right is not None and elem.left is None:
          result_list[1]+=1
        else:
          result_list[2]+=1
      return result_list

root_node = LinkedBinaryTree.Node(4)
root_node.left=LinkedBinaryTree.Node(7)
root_node.right=LinkedBinaryTree.Node(2)
root_node.left.left=LinkedBinaryTree.Node(9)
root_node.right.left= LinkedBinaryTree.Node(3)
root_node.right.right=LinkedBinaryTree.Node(1)
tree=LinkedBinaryTree(root_node)
print(tree.subtree_children_distance(root_node))
          
      
      
      



