const start = new Date

let n = 1000, max_pal = 0;
let s = 0;

for (let a = n * 0.9; n; a ++){
    for (let b = n * 0.9; n; b ++){
        s = a * b 
        if (String(s) == String(s).split('').reverse().join('')){
            max_pal = s
        }
    }
}

console.log(max_pal)
let t = new Date - start
console.log(t)
