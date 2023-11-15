const patchNavigator3 = (name, value) =>
    utils.replaceProperty(Object.getPrototypeOf(navigator), name, {
        get() {
            return value
        }
    })

patchNavigator3('hardwareConcurrency', opts.navigator_hardware_concurrency || 4);