let add = [[1, '', 3], [1, '', 3]]
map = add.flat(1)
let tar = [0, 0]
map.findIndex((item, index) => {
    tar[0] = Math.floor(index / 3)
    tar[1] = index % 3
    return item == ''
})

console.log(tar)