const getRandomIntInclusive = function (min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min);
};

var getImageData2 = HTMLCanvasElement.prototype.toDataURL;
//

HTMLCanvasElement.prototype.toDataURL = function () {
    // console.log("当前data");
    // console.log(this.width);
    // console.log(this.height);
    this.width = this.width + getRandomIntInclusive(-5, 5);
    this.height = this.height + getRandomIntInclusive(-5, 5);
    return getImageData2.apply(this);
};

