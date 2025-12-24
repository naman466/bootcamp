class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.balance_factor = 0  

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
        else:
            self._insert(self.root, val)
        self._update_balance_factors(self.root)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = BSTNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = BSTNode(val)
            else:
                self._insert(node.right, val)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append((node.val, node.balance_factor)) 
        self._inorder(node.right, result)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _update_balance_factors(self, node):
        if node is None:
            return
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        node.balance_factor = left_height - right_height
        self._update_balance_factors(node.left)
        self._update_balance_factors(node.right)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return None
        if val == node.val:
            return node
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)


tree = BST()
arr = [4, 1, 3, 5, 6, 7]

for i in arr:
    tree.insert(i)

print(tree.inorder())  
