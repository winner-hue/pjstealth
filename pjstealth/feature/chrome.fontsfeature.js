var rand = {
    "noise": function () {
        var SIGN = Math.random() < Math.random() ? -1 : 1;
        return Math.floor(Math.random() + SIGN * Math.random());
    },
    "sign": function () {
        const tmp = [-1, -1, -1, -1, -1, -1, +1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1];
        const index = Math.floor(Math.random() * tmp.length);
        return tmp[index];
    }
};
var hookFonts = function (originFamily) {
    if (originFamily.includes("monospace")) {
        let tmpFontFamily = originFamily.replace("monospace", "").replace(",", "").trim();
        if (opts.fontsfeature.hasOwnProperty(tmpFontFamily)) {
            originFamily = opts.fontsfeature[tmpFontFamily] + ", " + "monospace";
        }
    }

    if (originFamily.includes("sans-serif")) {
        let tmpFontFamily = originFamily.replace("sans-serif", "").replace(",", "").trim();
        if (opts.fontsfeature.hasOwnProperty(tmpFontFamily)) {
            originFamily = opts.fontsfeature[tmpFontFamily] + ", " + "sans-serif";
        }
    }

    if (originFamily.includes("serif")) {
        let tmpFontFamily = originFamily.replace("serif", "").replace(",", "").trim();
        if (opts.fontsfeature.hasOwnProperty(tmpFontFamily)) {
            originFamily = opts.fontsfeature[tmpFontFamily] + ", " + "serif";
        }
    }
    return originFamily;
}

Object.defineProperty(HTMLElement.prototype, "offsetHeight", {
    get() {

        this.style.fontFamily = hookFonts(this.style.fontFamily);
        let height = 500;
        try {
            height = Math.floor(this.getBoundingClientRect().height);
        } catch (e) {
            height = Math.floor(this.clientHeight)
        }
        return height;
    }
});

Object.defineProperty(HTMLElement.prototype, "offsetWidth", {
    get() {
        // opts.fonts_start = opts.fonts_start + 1;
        // if (opts.fonts_start < opts.fontsfeature.change_index.length && opts.fontsfeature.change_index[opts.fonts_start] !== 0) {
        //     this.style.fontFamily = opts.fontsfeature.width[opts.fonts_start];
        // }
        this.style.fontFamily = hookFonts(this.style.fontFamily);

        let width = 500;
        try {
            width = Math.floor(this.getBoundingClientRect().width);
        } catch (e) {
            width = Math.floor(this.clientWidth)
        }
        return width;
    }
});
// Object.defineProperty(HTMLElement.prototype, "offsetHeight", {
//     get() {
//         let height = 500;
//         try {
//             height = Math.floor(this.getBoundingClientRect().height);
//         } catch (e) {
//             height = Math.floor(this.clientHeight)
//         }
//         const valid = height && rand.sign() === 1;
//         const result = valid ? height + rand.noise() : height;
//         return result;
//     }
// });
//
// Object.defineProperty(HTMLElement.prototype, "offsetWidth", {
//     get() {
//         let width = 500;
//         try {
//             width = Math.floor(this.getBoundingClientRect().width);
//         } catch (e) {
//             width =  Math.floor(this.clientWidth)
//         }
//         const valid = width && rand.sign() === 1;
//         const result = valid ? width + rand.noise() : width;
//         return result;
//     }
// });