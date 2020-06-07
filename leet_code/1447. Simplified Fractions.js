

var simplifiedFractions = (n) => {
    let done = []
    let res = []

    for (var i = 2; i <= n; ++i) {
        for (var j = 1; j < i; ++j) {
            var fraction = j/i
            if (done.includes(fraction)) {
                continue
            }

            done.push(fraction)
            res.push(j.toString() + '/' + i.toString())
        }
    }

    return res
};


console.log(["1/2","1/3","1/4","2/3","3/4"] == simplifiedFractions(4))