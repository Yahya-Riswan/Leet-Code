class EventEmitter {
    constructor() {
        this.events = {}; // stores eventName -> list of callbacks
    }

    /**
     * Subscribes a callback to an event
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object} An object with an unsubscribe() method
     */
    subscribe(eventName, callback) {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }

        const callbacks = this.events[eventName];
        callbacks.push(callback);

        const index = callbacks.length - 1;

        return {
            unsubscribe: () => {
                // Remove the callback from the array
                callbacks.splice(index, 1);
            }
        };
    }

    /**
     * Emits an event with optional arguments
     * @param {string} eventName
     * @param {Array} args
     * @return {Array} Results of the callback invocations
     */
    emit(eventName, args = []) {
        const callbacks = this.events[eventName];
        if (!callbacks) return [];

        return callbacks.map(fn => fn(...args));
    }
}


/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */