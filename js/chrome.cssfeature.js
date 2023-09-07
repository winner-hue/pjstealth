var obj_get_computed_style = getComputedStyle;
getComputedStyle = function(data){
        if (data.style.backgroundColor == "activeborder"){
            var tmp = ["rgb(118, 118, 118)", "rgb(0, 0, 0)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "activetext"){
            var tmp = ["rgb(255, 0, 0)", "rgb(0, 102, 204)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "graytext"){
            var tmp = ["rgb(128, 128, 128)", "rgb(109, 109, 109)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "graytext"){
            var tmp = ["rgb(128, 128, 128)", "rgb(109, 109, 109)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "highlight"){
            var tmp = ["rgb(181, 213, 255)", "rgb(51, 153, 255)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "highlighttext"){
            var tmp = ["rgb(0, 0, 0)", "rgb(255, 255, 255)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "linktext"){
            var tmp = ["rgb(0, 0, 238)", "rgb(0, 102, 204)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "threeddarkshadow"){
            var tmp = ["rgb(118, 118, 118)", "rgb(0, 0, 0)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "threedface"){
            var tmp = ["rgb(239, 239, 239)", "rgb(240, 240, 240)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "threedhighlight"){
            var tmp = ["rgb(0, 0, 0)", "rgb(118, 118, 118)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "threedlightshadow"){
            var tmp = ["rgb(118, 118, 118)", "rgb(0, 0, 0)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "threedshadow"){
            var tmp = ["rgb(118, 118, 118)", "rgb(0, 0, 0)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "visitedtext"){
            var tmp = ["rgb(85, 26, 139)", "rgb(0, 102, 204)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }
        if (data.style.backgroundColor == "windowframe"){
            var tmp = ["rgb(118, 118, 118)", "rgb(0, 0, 0)"]
            data.style.backgroundColor = tmp[Math.floor(Math.random() * tmp.length)];
        }

        var test_n = obj_get_computed_style(data)
        return test_n
}