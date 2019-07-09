// A trivial counter used to demonstrate iterative calls to a JS module from jsbridge.

class Counter {

    constructor() {
        this.count = 0;
    }

    set_counter(new_value) {
        if (isNaN(new_value)){
            return NaN;
        }
        this.count=parseInt(new_value, 10);
        return this.count;
    }

    increment_counter(){
        this.count += 1;
        return this.count;
    }

    get_count(){
        return this.count;   
    }
}

module.exports = Counter;