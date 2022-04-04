import random


class Chord:
    def __init__(self, id_space):
        self.id_space = id_space
        self.noNodes = 2**id_space
        self.finger_table = dict() 
        self.nodes = list()

    def addNode(self, node_id):
        if node_id > self.noNodes:
            print("Sorry maximum no of nodes reached")
        elif node_id in self.nodes:
            print("The node already exists in the ring. ")
        else:
            self.nodes.append(node_id)
            self.nodes.sort()
            print('Current nodes in the ring: ', self.nodes)
            self.create_finger_table()
    
    def removeNode(self, node_id):
        if node_id not in self.nodes:
            print("This node doesn't exist in the ring.")
        else:
            self.nodes.remove(node_id)
            print('Current nodes in the ring: ', self.nodes)
            self.create_finger_table()

    def getSuccessor(self, node_id):
        for i in self.nodes:
            if i >= node_id:
                return i
        return self.nodes[0]
    
    def create_finger_table(self):
        self.finger_table = dict()
        for node in self.nodes:
            for i in range(1, self.id_space+1):
                if node in self.finger_table.keys():
                    self.finger_table[node].append(self.getSuccessor((node + pow(2,i-1))%self.noNodes))
                else:
                    self.finger_table[node] = [self.getSuccessor((node + pow(2,i-1))%self.noNodes)]

    def display_finger_table(self, node):
        print("Finger Table for node: ", node)
        print(self.finger_table[node])

    def lookup(self, key, node):
        path = [str(node)]
        n = node
        while True:
            if self.finger_table[n][0] > key:
                path.append(str(self.finger_table[n][0]))
                print('The path followed from node', node, 'to reach key', key, 'is','->'.join(path))
                break
            for i in range(len(self.finger_table[n])):
                if max(self.finger_table[n]) < key:
                    n = max(self.finger_table[n])
                    path.append(str(n))
                    break

                if self.finger_table[n][i] > key:
                    n = self.finger_table[n][i-1]
                    path.append(str(n))
                    break
                else:
                    continue


def main():
    c = Chord(6)
    while True:
        print('''
1. Add a node
2. Remove a node
3. Display the finger table for a node
4. Lookup a key
5. Exit         
        ''')

        option = int(input("Enter your choice >> "))
        if option == 1:
            n = int(input("Enter node id: "))
            c.addNode(n)
        elif option == 2:
            n = int(input("Enter node id: "))
            c.removeNode(n)
        elif option == 3:
            n = int(input("Enter node id: "))
            c.display_finger_table(n)
        elif option == 4:
            n = int(input("Enter node id: "))
            k = int(input("Enter key to search: "))
            c.lookup(k,n)
        else:
            break

        print('\n----------------------------------------------------------\n')

if __name__ == "__main__":
    main()
    print('''
        M.SREE CHARAN SAI
        AM.EN.U4CSE19232
        S6 CSE-C
    ''')
