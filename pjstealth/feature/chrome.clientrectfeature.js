var rand = {
    "noise": function () {
        var SIGN = Math.random() < Math.random() ? -1 : 1;
        return Math.floor(Math.random() + SIGN * Math.random());
    },
    "sign": function () {
        const tmp = [-1, -1, -1, -1, -1, -1, +1, -1, -1, -1];
        const index = Math.floor(Math.random() * tmp.length);
        return tmp[index];
    },
    'get': function (e, fun, name, index) {
        let d
        try {
            if (typeof index == "undefined") {
                d = Math.floor(e[fun]()[name]);
            } else {
                d = Math.floor(e[fun]()[index][name]);
            }

        } catch (e) {
            console.log(e)
        }
        const valid = d && rand.sign() === 1;
        const result = valid ? d + rand.noise() : d;
        return result;
    },
    'value': function (d) {

        const valid = d && rand.sign() === 1;
        const result = valid ? d + rand.noise() : d;
        return result;
    }
};
Object.defineProperty(HTMLElement.prototype, "getBoundingClientRect", {
    value() {
        let rects = this.getClientRects()[0];
        console.log(rects);
        let _rects = JSON.parse(JSON.stringify(rects));
        let _json = {};
        for (let k in _rects) {
            let d = rand.value(_rects[k]);
            // console.log(k,d)
            _json[k] = d;
            Object.defineProperty(rects.__proto__, k, {
                get() {
                    return d
                }
            })
        }
        Object.defineProperty(rects.__proto__, "toJSON", {
            value() {
                return _json
            }
        });
        return rects;
    },
});
