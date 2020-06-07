/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stk = []
    this.s_stk = []
    this.n = 0
    
    this.bisect_left = function(stk, val) {
        var l = 0
        var r = stk.length - 1
        
        while (l <= r) {
            var m = parseInt((l + r)/2)
            if (stk[m] == val)
                return m
            if (stk[m] > val)
                r = m - 1
            else
                l = m + 1
        }
        
        return l
    }
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.stk.push(x)
    let idx = this.bisect_left(this.s_stk, x)
    this.s_stk.splice(idx, 0, x)
    this.n += 1
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (this.n) {
        let val = this.stk.pop()  
        let idx = this.bisect_left(this.s_stk, val)
        this.s_stk.splice(idx, 1)
        this.n -= 1
    }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    var res = -1
    if (this.n) {
        return this.stk[this.n - 1]
    }
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    if (this.n) {
        return this.s_stk[0]
    }
    
    return -1
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
 
