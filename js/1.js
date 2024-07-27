const start = new Date

let sum_num = 0

for (let i = 0; i < 1000000000; i++){
    if (((i % 3) == 0) || ((i % 5) == 0)){
        sum_num += i
    }
}
console.log(sum_num)
let t = new Date - start
console.log(t)