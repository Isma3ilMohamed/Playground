package binary_tree

import java.util.*


class BinaryTree {
    var root: Node? = null


    //Insertion
    private fun addRecursive(current: Node?, value: Int): Node {
        if (current == null) {
            return Node(value)
        }

        when {
            value < current.value -> {
                current.left = addRecursive(current.left, value)
            }
            value > current.value -> {
                current.right = addRecursive(current.right, value)
            }
            else -> {
                // value already exists
                return current
            }
        }

        return current
    }

    fun add(value:Int){
        root=addRecursive(root,value)
    }

    //Finding Element
    private fun containsNodeRecursive(current: Node?, value: Int):Boolean{
        if (current==null){
            return false
        }

        if (value==current.value){
            return true;
        }
        return if (value<current.value){
            containsNodeRecursive(current.left,value)
        }else{
            containsNodeRecursive(current.right,value)
        }
    }

    fun containsNode(value:Int):Boolean{
        return containsNodeRecursive(root,value)
    }

    //Deleting Element
    private fun deleteNodeRecursive(current: Node?,value: Int):Node?{
        if (current==null){
            return null
        }
        if (value==current.value){
            //we delete node here
            /**
                there are 3 main different cases:
                a node has no children – this is the simplest case; we just need to replace this node with null in its parent node
                a node has exactly one child – in the parent node, we replace this node with its only child.
                a node has two children – this is the most complex case because it requires a tree reorganization
             * */

            //first case
            if (current.left==null && current.right==null){
                return null
            }
            //Second case
            else if (current.right==null){
                return current.left
            }else if (current.left==null){
                return current.right
            }
            //Third case
            else{
                val smallestValue=findSmallestValue(current.right)
                current.value=smallestValue
                current.right=deleteNodeRecursive(current.right,smallestValue)
                return current
            }


        }
        if (value<current.value){
            current.left=deleteNodeRecursive(current.left,value)
        }
        current.right=deleteNodeRecursive(current.right,value)
        return current
    }

    private fun findSmallestValue(node: Node?):Int{
        return if (node?.left==null){
            return node?.value?:0
        }else{
            findSmallestValue(node.left)
        }
    }


    fun delete(value: Int){
        root=deleteNodeRecursive(root,value)
    }

    //Traversing

    //Depth First search

    // in-order traversal consists of first visiting the left sub-tree, then the root node, and finally the right sub-tree
    fun traverseInOrder(node: Node?){
        if (node!=null){
            traverseInOrder(node.left)
            println(" ${node.value}")
            traverseInOrder(node.right)
        }
    }

    //Pre-order traversal visits first the root node, then the left sub-tree, and finally the right sub-tree:
    fun traversePreOrder(node: Node?){
        if (node!=null){
            println(" ${node.value}")
            traversePreOrder(node.left)
            traversePreOrder(node.right)
        }
    }

    //Post-order traversal visits the left sub-tree, the right subt-ree, and the root node at the end:
    fun traversePostOrder(node: Node?){
        if (node!=null){
            traversePostOrder(node.left)
            traversePostOrder(node.right)
            println(" ${node.value}")
        }
    }


    //Breadth First search -> This is another common type of traversal that visits all the nodes of a level before going to the next level.

    fun traverseLevelOrder() {
        if (root == null) {
            return
        }

        val nodes: Queue<Node?> = LinkedList<Node?>()
        nodes.add(root)

        while (!nodes.isEmpty()) {
            val node = nodes.remove()

            println(" ${node?.value}")

            if (node?.left != null) {
                nodes.add(node.left)
            }

            if (node?.right != null) {
                nodes.add(node.right)
            }
        }
    }

}


fun main() {
    val bt=BinaryTree()
    bt.add(6)
    bt.add(4)
    bt.add(8)
    bt.add(3)
    bt.add(5)
    bt.add(7)
    bt.add(9)

    println(bt.traverseLevelOrder())
}