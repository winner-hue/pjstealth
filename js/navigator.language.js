Object.defineProperty(Object.getPrototypeOf(navigator), 'language', {
    get: () => opts.language
});
