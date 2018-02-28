
class RBTree:
    """
    红黑树数据结构
    """

    class Node:
        """
        红黑树-节点对象
        """
        RED = 1
        BLACK = 0

        def __init__(self, data, left, right, parent):
            """
            红黑树-节点对象构造器
            Parameter:
            data: 节点数据
            left: 节点的左子树
            right: 节点的右子树
            parent: 节点的父节点
            color: 节点的颜色
            """
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent
            self.color = RBTree.Node.RED

        def getdata(self):
            return self.data

        def getparent(self):
            return self.parent

    def __init__(self):
        self.size = 0
        self.root = None
        self.tail = None

    def rrotate(self, node):
        """
        红黑树-右旋
        """
        l = node.left
        node.left = l.right
        if l.right is not None:
            l.right.parent = node
        l.parent = node.parent
        if node.parent is None:
            self.root = l
        elif node == node.parent.left:
            node.parent.left = l
        else:
            node.parent.right = l
        l.right = node
        node.parent = l

    def lrotate(self, node):
        """
        红黑树-左旋
        """
        r = node.right
        node.right = r.left
        if r.left is not None:
            r.left.parent = node
        r.parent = node.parent
        if node.parent is None:
            self.root = r
        elif node == node.parent.left:
            node.parent.left = r
        else:
            node.parent.right = r
        r.left = node
        node.parent = r

    def insert(self, data):
        """
        红黑树-插入
        """
        node = self.Node(data, None, None, None)
        self.tail = node
        if self.root is None:
            node.color = RBTree.Node.BLACK
            self.root = node
        else:
            node_tmp = self.root
            node_tmp_p = None
            while node_tmp is not None:
                node_tmp_p = node_tmp
                if data >= node_tmp.data:
                    node_tmp = node_tmp.right
                else:
                    node_tmp = node_tmp.left

            node.parent = node_tmp_p
            # 空树
            if node_tmp_p is None:
                self.root = node
            elif data >= node_tmp_p.data:
                node_tmp_p.right = node
            else:
                node_tmp_p.left = node
            # 检测红黑树性质
            self.check(node)

        self.size += 1

    def size(self):
        """
        红黑树-元素大小
        """
        return self.size

    def empty(self):
        """
        红黑树-是否为空
        """
        return self.size == 0

    def check(self, x):
        """
        红黑树-检测红黑树性质:
        case 1:

        case 2:

        case 3:
        """

        while True:
            if x.parent is None:
                self.root.color = RBTree.Node.BLACK
                break
            if x.parent.color == RBTree.Node.BLACK or x.parent.parent is None:
                break
            xp = x.parent
            xpp = xp.parent
            xppl = xpp.left
            # 节点的父节点是左孩子
            if xp == xppl:
                # 节点的父节点的兄弟节点(父父节点右孩子)
                xppr = xpp.right
                if xppr is not None and xppr.color == RBTree.Node.RED:
                    xp.color = RBTree.Node.BLACK
                    xppr.color = RBTree.Node.BLACK
                    xpp.color = RBTree.Node.RED
                    x = xpp
                else:
                    if x == xp.right:
                        x = xp
                        self.lrotate(xp)
                        xp = x.parent
                        if xp is not None:
                            xpp = xp.parent
                        else:
                            xpp = None
                    if xp is not None:
                        xp.color = RBTree.Node.BLACK
                        if xpp is not None:
                            xpp.color = RBTree.Node.RED
                            self.rrotate(xpp)
            else:
                # 节点的父节点的兄弟节点(父父节点右孩子)
                if xppl is not None and xppl.color == RBTree.Node.RED:
                    xp.color = RBTree.Node.BLACK
                    xppl.color = RBTree.Node.BLACK
                    xpp.color = RBTree.Node.RED
                    x = xpp
                else:
                    if x == xp.left:
                        x = xp
                        self.rtrotate(x)
                        xp = x.parent
                        if xp is not None:
                            xpp = xp.parent
                        else:
                            xpp = None

                    if xp is not None:
                        xp.color = RBTree.Node.BLACK
                        if xpp is not None:
                            xpp.color = RBTree.Node.RED
                            self.lrotate(xpp)

