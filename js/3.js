const start = new Date

let n = 60085147514309
let c = 2
let list_simple = []

while (n > 1){
    if (n % c != 0){
        if (c > 2){
            c += 2
        }
        else{
            c = 3
        }
        }
    else{
        n = n / c
        if (!list_simple.includes(c)) {
            list_simple.push(c)
        }
    }
}

console.log(list_simple)
let t = new Date - start
console.log(t)