/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0;
let b = 1;
while (true) {
    yield a; 
    let temp = b;
    b = b + a;
    a = temp;
}
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */