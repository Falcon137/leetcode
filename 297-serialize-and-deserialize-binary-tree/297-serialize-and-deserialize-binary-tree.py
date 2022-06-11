# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        data = ['']
        self.ser_helper(root,data)
        return data[0]
        
    def ser_helper(self,node,data):
        if node is None:
            data[0] += 'n,'
        else:
            data[0] += str(node.val)+','
            self.ser_helper(node.left,data)
            self.ser_helper(node.right,data)

    def deserialize(self, data):
        pos = [0]
        #print(data)
        return self.d_helper(data,pos)
    
    def d_helper(self,data,pos):
        start = stop = pos[0]
        while data[stop] != ',':
            stop += 1
        
        pos[0] = stop+1
        if data[start:stop] == 'n':
            return None
            
        parent = TreeNode(int(data[start:stop]))
        parent.left = self.d_helper(data,pos)
        parent.right = self.d_helper(data,pos)
        return parent
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))