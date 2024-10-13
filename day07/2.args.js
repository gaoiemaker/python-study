// 箭头函数没有自己的arguments对象

const fun = (...args)=>{
    console.log(args)
}


fun('123','456')