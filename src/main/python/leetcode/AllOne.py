class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(float('-inf'))  # Dummy head
        self.tail = Node(float('inf'))   # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_count = {}   # key -> count
        self.count_nodes = {} # count -> node
        self.key_node = {}    # key -> node

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_nodes[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            # Key exists
            count = self.key_count[key]
            node = self.count_nodes[count]
            next_count = count + 1

            # Remove key from current node
            node.keys.remove(key)
            if next_count in self.count_nodes:
                next_node = self.count_nodes[next_count]
            else:
                # Create new node
                next_node = Node(next_count)
                self.count_nodes[next_count] = next_node
                self._add_node_after(next_node, node)
            next_node.keys.add(key)

            # Update key mappings
            self.key_count[key] = next_count
            self.key_node[key] = next_node

            # Remove current node if empty
            if len(node.keys) == 0:
                self._remove_node(node)
        else:
            # New key
            self.key_count[key] = 1
            if 1 in self.count_nodes:
                node = self.count_nodes[1]
            else:
                node = Node(1)
                self.count_nodes[1] = node
                self._add_node_after(node, self.head)
            node.keys.add(key)
            self.key_node[key] = node

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        count = self.key_count[key]
        node = self.count_nodes[count]
        node.keys.remove(key)

        if count == 1:
            # Remove key entirely
            del self.key_count[key]
            del self.key_node[key]
        else:
            prev_count = count - 1
            if prev_count in self.count_nodes:
                prev_node = self.count_nodes[prev_count]
            else:
                prev_node = Node(prev_count)
                self.count_nodes[prev_count] = prev_node
                self._add_node_after(prev_node, node.prev)
            prev_node.keys.add(key)
            self.key_count[key] = prev_count
            self.key_node[key] = prev_node

        # Remove current node if empty
        if len(node.keys) == 0:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Return any key from the last node before tail
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        # Return any key from the first node after head
        return next(iter(self.head.next.keys))



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
