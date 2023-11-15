var getImageData2 = HTMLCanvasElement.prototype.toDataURL;

HTMLCanvasElement.prototype.toDataURL = function () {
    // console.log("当前data");
    // console.log(this.width);
    // console.log(this.height);
    this.width = this.width + opts.canvasfeature.width;
    this.height = this.height + opts.canvasfeature.height;
    return getImageData2.apply(this);
};

