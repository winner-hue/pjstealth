if (opts.user_agent_data) {
    Object.defineProperty(Object.getPrototypeOf(navigator), 'userAgentData', {
        get: () => opts.user_agent_data,
    })
}