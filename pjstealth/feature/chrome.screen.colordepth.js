const screen_color_depth = window.screen.colorDepth;
Object.defineProperty(Object.getPrototypeOf(screen), 'colorDepth', {
    get: function () {
        return opts.screen_color_depth || screen_color_depth;
    }
});

Object.defineProperty(Object.getPrototypeOf(screen), 'pixelDepth', {
    get: () => opts.screen_color_depth || screen_color_depth
});
