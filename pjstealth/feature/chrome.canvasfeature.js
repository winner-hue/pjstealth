const getImageData = CanvasRenderingContext2D.prototype.getImageData;
//
var noisify = function (canvas, context) {
    if (context) {
        const shift = {
            'r': Math.floor(Math.random() * 10) - 5,
            'g': Math.floor(Math.random() * 10) - 5,
            'b': Math.floor(Math.random() * 10) - 5,
            'a': Math.floor(Math.random() * 10) - 5
        };
        //
        const width = canvas.width;
        const height = canvas.height;
        if (width && height) {
            const imageData = getImageData.apply(context, [0, 0, width, height]);
            for (let i = 0; i < height; i++) {
                for (let j = 0; j < width; j++) {
                    const n = ((i * (width * 4)) + (j * 4));
                    imageData.data[n + 0] = imageData.data[n + 0] + opts.canvasfeature.r;
                    imageData.data[n + 1] = imageData.data[n + 1] + opts.canvasfeature.g;
                    imageData.data[n + 2] = imageData.data[n + 2] + opts.canvasfeature.b;
                    imageData.data[n + 3] = imageData.data[n + 3] + opts.canvasfeature.a;
                }
            }
            //
            context.putImageData(imageData, 0, 0);
        }
    }
};
Object.defineProperty(CanvasRenderingContext2D.prototype, "getImageData", {
    "value": function () {
        noisify(this.canvas, this);
        return getImageData.apply(this, arguments);
    }
});
