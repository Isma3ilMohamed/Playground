package binary_tree

import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Test
import kotlin.test.assertTrue

class BinaryTreeKtTest{
    private fun createBinaryTree(): BinaryTree {
        val bt = BinaryTree()

        bt.add(6)
        bt.add(4)
        bt.add(8)
        bt.add(3)
        bt.add(5)
        bt.add(7)
        bt.add(9)

        return bt
    }
    @Test
    fun `given a binary tree when adding elements then tree contains those elements`(){
        val bt=createBinaryTree()
        assertTrue(bt.containsNode(6))
        assertTrue(bt.containsNode(4))
        assertFalse(bt.containsNode(1))
    }

    @Test
    fun `given a binary tree when deleting elements then tree does not contain those elements`(){
        val bt=createBinaryTree()
        assertTrue(bt.containsNode(9))
        bt.delete(9)
        assertFalse(bt.containsNode(9))
    }

}