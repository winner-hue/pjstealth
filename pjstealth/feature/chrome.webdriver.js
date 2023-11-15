Object.defineProperty(Object.getPrototypeOf(navigator), 'webdriver', {
    get: () => false
});
