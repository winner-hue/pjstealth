const getChannelData = AudioBuffer.prototype.getChannelData;
Object.defineProperty(AudioBuffer.prototype, "getChannelData", {
    "value": function () {
        const results_1 = getChannelData.apply(this, arguments);
        window.top.postMessage("audiocontext-fingerprint-defender-alert", '*');
        for (var i = opts.videofeature.start_index; i < results_1.length; i += 100) {
            results_1[i] = results_1[i] + opts.videofeature.random_value;
        }
        return results_1;
    }
});
