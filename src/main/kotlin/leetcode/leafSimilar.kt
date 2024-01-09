package leetcode

import leetcode.helper.TreeNode

fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
    val leaves1= mutableListOf<Int>()
    val leaves2= mutableListOf<Int>()
        fun dfs(node: TreeNode?,leaves:MutableList<Int>){
            if (node!=null){
                if (node.left==null && node.right==null){
                    leaves.add(node.`val`)
                }
                dfs(node.left,leaves)
                dfs(node.right,leaves)
            }
        }

    dfs(root1,leaves1)
    dfs(root2,leaves2)

    return leaves1.equals(leaves2)
}