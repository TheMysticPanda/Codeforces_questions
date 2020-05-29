class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    # END OF Item class

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
    # END OF Node class

    # Constructor for BinarySearchTreeMap
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    # Allows for syntax: m[k] (returns the value associated with key k)
    # Raises Exception if the key is not found
    def __getitem__(self, key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) + " is not in the map")
        else:
            return node.item.value

    # Returns None if the key is not found
    def find(self, key):
        curr_node = self.root
        while curr_node is not None:
            if key == curr_node.item.key:
                return curr_node
            elif key < curr_node.item.key:
                curr_node = curr_node.left
            else: # key > curr_node.item.key
                curr_node = curr_node.right
        return None

    # Allows for syntax: m[key] = val (associates key `key` with value `val`)
    def __setitem__(self, key, value):
        node = self.find(key)
        if node is None:
            self.insert(key, value)
        else:
            node.item.value = value

    # Assumes key is not in the map
    # Insert (key, value) into subtree rooted by curr_node
    def insert(self, key, value):
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)

        if self.is_empty():
            self.root = new_node
            self.size = 1
        else:
            next_node = self.root
            while next_node is not None:
                curr_node = next_node
                if key < curr_node.item.key:
                    next_node = curr_node.left
                else: # key > curr_node.item.key
                    next_node = curr_node.right
            # insert the node
            if key < curr_node.item.key:
                curr_node.left = new_node
            else: # key > curr_node.item.key
                curr_node.right = new_node
            new_node.parent = curr_node
            self.size += 1

    # Allows for the syntax 'del map[key]'
    def __delitem__(self, key):
        node = self.find(key)
        if node is None:
            raise Exception(str(key) + " is not in the map")
        else:
            self.delete_node(node)

    # Assumes key to delete is in the tree
    def delete_node(self, node_to_delete):
        item_to_delete = node_to_delete.item
        num_children = node_to_delete.num_children()

        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 1:
                if self.root.left is not None:  #Don't we have to disconnect the node here as well
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                    self.root.parent = None
                    node_to_delete.disconnect()
                self.size -= 1
            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)
        else: #node_to_delete is not the root
            if num_children == 0:
                # node_to_delete is a leaf node
                parent = node_to_delete.parent
                if node_to_delete is parent.left:
                    # node_to_delete is the left child
                    parent.left = None
                else:
                    # node_to_delete is the right child
                    parent.right = None
                node_to_delete.disconnect()
            elif num_children == 1:
                parent = node_to_delete.parent
                child = None
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                if node_to_delete is parent.left:
                    # node_to_delete is left child
                    parent.left = child
                else:
                    # node_to_delete is right child
                    parent.right = child

                child.parent = parent
                node_to_delete.disconnect()
                self.size -= 1
            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                # delete max_of_left
                self.delete_node(max_of_left)

    def subtree_max(subtree_root):
        #if subtree_root.right is None:
            #return subtree_root
        #else:
            #return subtree_max(subtree_root.right)
        curr_node = subtree_root
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node

    def inorder(self):
        #for node in self.subtree_inorder(self, self.root):
        #    yield node
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key



twenty=BinarySearchTreeMap.Item(20)
node20=BinarySearchTreeMap.Node(twenty)
node201=BinarySearchTreeMap.Node(twenty)

ten=BinarySearchTreeMap.Item(10)
node10=BinarySearchTreeMap.Node(ten)
node101=BinarySearchTreeMap.Node(ten)

eight=BinarySearchTreeMap.Item(8)
node8=BinarySearchTreeMap.Node(eight)
node81=BinarySearchTreeMap.Node(eight)

fifteen=BinarySearchTreeMap.Item(15)
node15=BinarySearchTreeMap.Node(fifteen)
node151=BinarySearchTreeMap.Node(fifteen)

twentyeight=BinarySearchTreeMap.Item(28)
node28=BinarySearchTreeMap.Node(twentyeight)
node281=BinarySearchTreeMap.Node(twentyeight)

twentytwo=BinarySearchTreeMap.Item(22)
node22=BinarySearchTreeMap.Node(twentytwo)
node221=BinarySearchTreeMap.Node(twentytwo)

fifty=BinarySearchTreeMap.Item(50)
node50=BinarySearchTreeMap.Node(fifty)
node501=BinarySearchTreeMap.Node(fifty)

twentyfive=BinarySearchTreeMap.Item(25)
node25=BinarySearchTreeMap.Node(twentyfive)
node251=BinarySearchTreeMap.Node(twentyfive)

fifteen=BinarySearchTreeMap.Item(15)
node15=BinarySearchTreeMap.Node(fifteen)
node151=BinarySearchTreeMap.Node(fifteen)



node20.left=node10
node10.left=node8
node10.right=node15
node20.right=node28
node28.left=node22
node22.right=node25
node28.right=node50
a=BinarySearchTreeMap()
a.root=node20


node201.left=node81
node81.right=node151
node151.left=node101
node201.right=node221
node221.right=node251
node251.right=node501
node501.left=node281
b=BinarySearchTreeMap()
b.root=node201



#Coding problem 2

def are_bst_keys_same(bst1,bst2):
  array_keys_bst1=[]
  array_keys_bst2=[]
  for key in bst1:
    array_keys_bst1.append(key)
  for key in bst2:
    array_keys_bst2.append(key)
  if array_keys_bst1==array_keys_bst2:
    return True
  else:
    return False 





#Coding problem 3
def is_bst(binary_tree):
  return is_bst_helper(binary_tree.root)[0]

def is_bst_helper(subtree_root):
  #base case is when number of children is 0
  if subtree_root.num_children() is 0:
    return (True, subtree_root.item.key)
  else:
    #If number of children is 1
    if subtree_root.num_children() is 1:
      
      # if left child is none
      if subtree_root.left is None:
        bool_val,key_val=is_bst_helper(subtree_root.right)
        if subtree_root.item.key<key_val:
          return (True and bool_val,subtree_root.item.key)
        else:
          return (False,subtree_root.item.key)
      else:
           bool_val,key_val=is_bst_helper(subtree_root.left)
           if subtree_root.item.key>key_val:
              return (True and bool_val,subtree_root.item.key)
           else:
              return (False,subtree_root.item.key)
        
    #if number of children is 2    
    else:
      bool_val_left,key_val_left=is_bst_helper(subtree_root.left)
      bool_val_right,key_val_right=is_bst_helper(subtree_root.right)
      if key_val_left<subtree_root.item.key<key_val_right:
          if bool_val_left and bool_val_right:
              return (True,subtree_root.item.key)
          else:
              return (False,subtree_root.item.key)
              
      else:
        return (False,subtree_root.item.key)
      




#Coding problem 4

def lca_bst(bst, node1, node2):
  curr_node=bst.root
  while curr_node is not None:
    if (node1.item.key<=curr_node.item.key<=node2.item.key):
      return curr_node.item.key
    elif (node1.item.key<curr_node.item.key) and (node2.item.key<curr_node.item.key):
      curr_node=curr_node.left
    else:
      curr_node=curr_node.right
































