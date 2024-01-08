package leetcode

import leetcode.helper.TreeNode

fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
   return when {
       root==null -> {
           return 0
       }
       root.`val`>high -> {
           return rangeSumBST(root.left,low, high)
       }
       root.`val`<low -> {
           rangeSumBST(root.right,low,high)
       }
       else -> {
           return root.`val` + rangeSumBST(root.left,low,high) + rangeSumBST(root.right,low,high)
       }
   }
}