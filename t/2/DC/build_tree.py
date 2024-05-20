class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int = 0):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用

def dfs(
    preorder: list[int],
    inorder_map: dict[int, int],
    i: int,
    l: int,
    r: int,
) -> TreeNode | None:
    """构建二叉树：分治"""
    # 子树区间为空时终止
    if l>r:
        return -1
    root=TreeNode(preorder[i])
    m=inorder_map[preorder[i]]
    root.left=dfs(preorder,inorder_map,i+1,l,m-1)
    root.right=dfs(preorder,inorder_map,i+1+m-l,m+1,r)
    return root

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引的映射
    inorder_map = {val: i for i, val in enumerate(inorder)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root

if __name__ == "__main__":
        preorder = [3, 9, 2, 1, 7]
        inorder = [9, 3, 1, 2, 7]
        print(f"前序遍历 = {preorder}")
        print(f"中序遍历 = {inorder}")
        root = build_tree(preorder, inorder)
