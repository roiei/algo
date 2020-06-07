/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    function dfs(l, r, s, opn) {
        if (l > r)
            return opn == 0

        res = [false]

        if (s[l] == '(')
            res.push(dfs(l + 1, r, s, opn + 1))
        else if (s[l] == ')') {
            if (!opn)
                return false

            res.push(dfs(l + 1, r, s, opn - 1))
        } else if (s[l] == '*') {
            s[l] = '('
            res.push(dfs(l, r, s, opn))
            s[l] = ')'
            res.push(dfs(l, r, s, opn))
            res.push(dfs(l + 1, r, s, opn))
        }

        return res.some(true)
    }

    return dfs(0, s.length - 1, s.split(''), 0)
};

console.log(true == checkValidString("(*)"))
