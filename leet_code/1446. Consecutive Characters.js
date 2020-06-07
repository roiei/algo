

var maxPower = (s) => {
    if (s.length == 0)
        return 0

    let seq = s.split('')
    let cur = s[0]
    let mx = 1
    let cnt = 1

    seq.shift()

    for (var i in seq) {
        if (cur == seq[i]) {
            cnt += 1
            mx = Math.max(...[cnt, mx])
            continue
        }

        cnt = 1
        cur = seq[i]
    }

    console.log(mx)
    return mx
}

console.log(2 == maxPower("leetcode"))