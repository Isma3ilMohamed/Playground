package leetcode

fun imageSmoother(img: Array<IntArray>): Array<IntArray> {
    // Save the dimensions of the image.
    val m=img.size
    val n= img.first().size

    // Create a new image of the same dimension as the input image.
    val smoothImg = Array(m) { IntArray(n) }

    //iterate over all the cells of the image
    for (i in 0 ..< m){
        for (j in 0..< n){
            var sum=0
            var count=0

            // Iterate over all plausible nine indices.
            for (x in i-1 .. i+1){
                for (y in j-1 .. j+1){
                    if (x in 0..<m && y in 0 ..< n){
                        sum += img[x][y]
                        count += 1
                    }
                }
            }
            smoothImg[i][j] = sum/count

        }
    }

    return smoothImg
}