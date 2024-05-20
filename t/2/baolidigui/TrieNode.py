class TrieNode:
    def __init__(self):
        self.path=0
        self.end=0
        self.next=[None]*26

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def Insert(self,word):
        if word is None:
            return

        chs=list(word)
        node=self.root
        node.path+=1
        for ch in chs:
            index=ord(ch)-ord("a")
            if node.next[index]==None:#没有路径就新建路径
                node.next[index]=TrieNode()
            # node变为路径上的下一个节点
            node=node.next[index]
            node.path+=1
        node.end+=1

    def Delete(self,word):
        # 如果加入过这个词，才做删除
        if self.Search(word)!=0:
            chs=list(word)
            node=self.root
            for ch in chs:
                index=ord(ch)-ord("a")
                node.next[index].path-=1
                if (node.next[index].path==0):#如果在删除路径的过程中，遇到path为0了，后续路径 可以直接丢弃
                    node.next[index]=None
                    return
                node=node.next[index]
            node.end-=1

    def Search(self,word):
        if word is None:
            return

        chs=list(word)
        node=self.root
        for ch in chs:
            index=ord(ch)-ord("a")
            if node.next[index]==None:# 到节点末端都没找到，就是加入了0次
                return 0
            node=node.next[index]
        return node.end

    def prefixNumber(self,pre):
        if pre is None:
            return 0

        chs=list(pre)
        node=self.root
        for ch in chs:
            index=ord(ch)-ord("a")
            if node.next[index]==None:
                return 0
            node = node.next[index]
        return node.path


# 创建一个Trie对象
trie = Trie()

# 插入单词
trie.Insert("apple")
trie.Insert("app")
trie.Insert("apricot")
trie.Insert("banana")

# 搜索单词
print(trie.Search("apple"))  # 输出: 1
print(trie.Search("app"))    # 输出: 1
print(trie.Search("apricot")) # 输出: 1
print(trie.Search("banana"))  # 输出: 1
print(trie.Search("orange"))  # 输出: 0

# 统计以给定前缀为前缀的单词数量
print(trie.prefixNumber("ap"))  # 输出: 3 (apple, app, apricot)
print(trie.prefixNumber("ban")) # 输出: 1 (banana)

# 删除单词
trie.Delete("apple")
print(trie.Search("apple"))  # 输出: 0
print(trie.prefixNumber("ap"))  # 输出: 2 (app, apricot)