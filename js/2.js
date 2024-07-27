const start = new Date

let fib = function (a, b, sum_fib, list_fib) {
    let req
    let c = a
    a = b
    b = a + c
    if (b < 4_000_000) {
        list_fib.push(b)
        if (b % 2 == 0) {
            sum_fib += b
        }
        req = fib (a, b, sum_fib, list_fib)
    }
    else {
        return [list_fib, sum_fib]
    }
    return req
}

let req = fib (1, 2, 2, [1, 2])

console.log(req[0])
console.log(req[1])
let t = new Date - start
console.log(t)

