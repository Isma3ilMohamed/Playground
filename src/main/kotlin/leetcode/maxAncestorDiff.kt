package leetcode

import leetcode.helper.TreeNode

fun maxAncestorDiff(root: TreeNode?): Int {
    var diff = 0
    if (root == null) return 0
    val min = root.`val`
    val max = root.`val`
    fun diff(root: TreeNode?, min: Int, max: Int) {
        var min = min
        var max = max
        if (root == null) return
        diff = Math.max(diff, Math.max(Math.abs(min - root.`val`), Math.abs(max - root.`val`)))
        min = Math.min(min, root.`val`)
        max = Math.max(max, root.`val`)
        diff(root.left, min, max)
        diff(root.right, min, max)
    }
    diff(root, min, max)
    return diff
}



