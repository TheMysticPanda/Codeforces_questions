#Problem 6a

def prefix_expression(expr_tree):
  
  def preorder_traverse_helper(lst, subtree_root):
    if subtree_root is None:
      return
    else:
      lst.append(subtree_root.data)
      preorder_traverse_helper(lst, subtree_root.left)
      preorder_traverse_helper(lst, subtree_root.right)
      return lst

  lst_val=preorder_traverse_helper([], expr_tree.root)
  return " ".join(lst_val)


#Problem 6b

def postfix_expression(expr_tree):
  
  def postorder_traverse_helper(lst, subtree_root):
    if subtree_root is None:
      return
    else:
      postorder_traverse_helper(lst, subtree_root.left)
      postorder_traverse_helper(lst, subtree_root.right)
      lst.append(subtree_root.data)
      return lst

  lst_val=postorder_traverse_helper([], expr_tree.root)
  return " ".join(lst_val)
