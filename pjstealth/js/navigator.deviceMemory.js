const patchNavigator2 = (name, value) =>
    utils.replaceProperty(Object.getPrototypeOf(navigator), name, {
        get() {
            return value
        }
    });

patchNavigator2('deviceMemory', opts.device_memory || 4);