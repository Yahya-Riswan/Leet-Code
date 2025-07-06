/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let cancelRequested = false;
    let cancelFn;

    const promise = new Promise((resolve, reject) => {

        function step(nextFn, arg) {
            let result;
            try {
                result = nextFn.call(generator, arg);
            } catch (err) {
                reject(err);
                return;
            }

            if (result.done) {
                resolve(result.value);
                return;
            }

            result.value
                .then(res => {
                    if (cancelRequested) {
                        try {
                            step(generator.throw, "Cancelled");
                        } catch (e) {
                            reject(e);
                        }
                    } else {
                        step(generator.next, res);
                    }
                })
                .catch(err => {
                    try {
                        step(generator.throw, err);
                    } catch (e) {
                        reject(e);
                    }
                });
        }

        step(generator.next);

        cancelFn = () => {
            cancelRequested = true;
        };
    });

    return [cancelFn, promise];
};
/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */