const getChannelData = AudioBuffer.prototype.getChannelData;
Object.defineProperty(AudioBuffer.prototype, "getChannelData", {
    "value": function () {
        const results_1 = getChannelData.apply(this, arguments);
        // if (context.BUFFER !== results_1) {
        //     context.BUFFER = results_1;
            window.top.postMessage("audiocontext-fingerprint-defender-alert", '*');
            for (var i = 0; i < results_1.length; i += 100) {
                let index = Math.floor(Math.random() * i);
                results_1[index] = results_1[index] + Math.random() * 0.0000001;
            // }
        }
        //
        return results_1;
    }
});
