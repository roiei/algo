

var maxLevelSum = function(root) {
    let q = [[1, root]]
    levels = {}

    while (q.length > 0) {
        let nq = []

        while (q.length > 0) {
            item = q.shift()
            let lev = item[0]
            let node = item[1]

            if (!(lev in levels))
                levels[lev] = 0

            levels[lev] += node.val

            if (node.left)
                nq.push([lev + 1, node.left])

            if (node.right)
                nq.push([lev + 1, node.right])
        }

        q = nq
    }
    
    var kvs = []
    for (var key in levels)
        kvs.push([key, levels[key]])

    kvs.sort(function compare(l, r) {
        return l[1] - r[1]
    });

    return kvs[kvs.length - 1][0]
}


