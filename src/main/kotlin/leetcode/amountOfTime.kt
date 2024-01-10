package leetcode

import leetcode.helper.TreeNode


var maxDistance=0
fun amountOfTime(root: TreeNode?, start: Int): Int {
    traverse(root, start)
    return maxDistance
}

fun traverse(root: TreeNode?, start: Int):Int{
    var depth=0
    if (root==null){
        return depth
    }
    val leftDepth= traverse(root.left,start)
    val rightDepth= traverse(root.right,start)

    if (root.`val`==start){
        maxDistance=Math.max(leftDepth,rightDepth)
        depth=-1
    }else if (leftDepth>= 0 && rightDepth >= 0){
        depth=Math.max(leftDepth,rightDepth)+1
    }else{
        val distance=Math.abs(leftDepth) + Math.abs(rightDepth)
        maxDistance=Math.max(distance, maxDistance)
        depth=Math.min(leftDepth,rightDepth)-1
    }

    return depth
}
