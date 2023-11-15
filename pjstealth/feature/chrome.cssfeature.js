var obj_get_computed_style = getComputedStyle;
getComputedStyle = function (data) {
    for (const key in opts.cssfeature) {
        if (data.style.backgroundColor === key) {
            data.style.backgroundColor = opts.cssfeature[key];
            break;
        }
    }
    return obj_get_computed_style(data);
};