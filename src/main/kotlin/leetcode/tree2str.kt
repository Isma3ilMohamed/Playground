package leetcode

import leetcode.helper.TreeNode


val result=StringBuilder()


fun tree2str(root: TreeNode?): String {
    preOrderTraversal(root)
    return result.toString()
}

fun preOrderTraversal(root: TreeNode?) {
    if (root==null){
        return
    }
    result.append(root.`val`)
    if (root.left!=null || root.right!=null){
        result.append("(")
        preOrderTraversal(root.left)
        result.append(")")
    }
    if(root.right!=null){
        result.append("(")
        preOrderTraversal(root.right)
        result.append(")")
    }
}
