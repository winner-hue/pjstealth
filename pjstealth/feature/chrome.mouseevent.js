// const originalDispatchEvent = EventTarget.prototype.dispatchEvent;
//
// // 重定义 dispatchEvent 方法
// Object.defineProperty(EventTarget.prototype, 'dispatchEvent', {
//     value: function (event) {
//         console.log("--------");
//         // 在这里检查是否是 mousedown 事件
//         if (event.type === 'mousedown' || event.type === 'mouseup') {
//             // 在这里修改 detail 值
//             event.detail = opts.mouse_event.detail;  // 设置自定义的 detail 值
//         }
//
//         // 调用原始的 dispatchEvent 方法
//         return originalDispatchEvent.apply(this, arguments);
//     },
//     configurable: true,
//     writable: true
// });

// Object.defineProperty(MouseEvent.prototype, "detail", {
//     get() {
//         if (this.type === 'mousedown') {
//             return opts.mouse_event.detail;
//         } else {
//             console.log(this.type);
//             return this.detail;
//         }
//     }
// });

// Object.defineProperty(MouseEvent.prototype, "button", {
//     get() {
//         return opts.mouse_event.button;
//     }
// });
//
// Object.defineProperty(MouseEvent.prototype, "buttons", {
//     get() {
//         return opts.mouse_event.buttons;
//     }
// });

