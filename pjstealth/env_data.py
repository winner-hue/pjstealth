import random

css_info = {
    "activeborder": random.choice(["rgb(118, 118, 118)", "rgb(0, 0, 0)"]),
    "activetext": random.choice(["rgb(255, 0, 0)", "rgb(0, 102, 204)"]),
    "graytext": random.choice(["rgb(128, 128, 128)", "rgb(109, 109, 109)"]),
    "highlight": random.choice(["rgb(181, 213, 255)", "rgb(51, 153, 255)"]),
    "highlighttext": random.choice(["rgb(0, 0, 0)", "rgb(255, 255, 255)"]),
    "linktext": random.choice(["rgb(0, 0, 238)", "rgb(0, 102, 204)"]),
    "threeddarkshadow": random.choice(["rgb(118, 118, 118)", "rgb(0, 0, 0)"]),
    "threedface": random.choice(["rgb(239, 239, 239)", "rgb(240, 240, 240)"]),
    "threedhighlight": random.choice(["rgb(0, 0, 0)", "rgb(118, 118, 118)"]),
    "threedlightshadow": random.choice(["rgb(118, 118, 118)", "rgb(0, 0, 0)"]),
    "threedshadow": random.choice(["rgb(118, 118, 118)", "rgb(0, 0, 0)"]),
    "visitedtext": random.choice(["rgb(85, 26, 139)", "rgb(0, 102, 204)"]),
    "windowframe": random.choice(["rgb(118, 118, 118)", "rgb(0, 0, 0)"])
}
font_names = [
    "Andale Mono",
    "Arial",
    "Arial Black",
    "Arial Hebrew",
    "Arial MT",
    "Arial Narrow",
    "Arial Rounded MT Bold",
    "Arial Unicode MS",
    "Bitstream Vera Sans Mono",
    "Book Antiqua",
    "Bookman Old Style",
    "Calibri",
    "Cambria",
    "Cambria Math",
    "Century",
    "Century Gothic",
    "Century Schoolbook",
    "Comic Sans",
    "Comic Sans MS",
    "Consolas",
    "Courier",
    "Courier New",
    "Geneva",
    "Georgia",
    "Helvetica",
    "Helvetica Neue",
    "Impact",
    "Lucida Bright",
    "Lucida Calligraphy",
    "Lucida Console",
    "Lucida Fax",
    "LUCIDA GRANDE",
    "Lucida Handwriting",
    "Lucida Sans",
    "Lucida Sans Typewriter",
    "Lucida Sans Unicode",
    "Microsoft Sans Serif",
    "Monaco",
    "Monotype Corsiva",
    "MS Gothic",
    "MS Outlook",
    "MS PGothic",
    "MS Reference Sans Serif",
    "MS Sans Serif",
    "MS Serif",
    "MYRIAD",
    "MYRIAD PRO",
    "Palatino",
    "Palatino Linotype",
    "Segoe Print",
    "Segoe Script",
    "Segoe UI",
    "Segoe UI Light",
    "Segoe UI Semibold",
    "Segoe UI Symbol",
    "Tahoma",
    "Times",
    "Times New Roman",
    "Times New Roman PS",
    "Trebuchet MS",
    "Verdana",
    "Wingdings",
    "Wingdings 2",
    "Wingdings 3"
]

fonts_info = {
    "change_index": [random.choice([0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0]) for _ in range(500)],
    "height": [random.choice(font_names) for _ in range(500)],
    "width": [random.choice(font_names) for _ in range(500)],
}
windows_webgl = [
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3090 Direct3D11 vs_5_0 ps_5_0, D3D11)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 Ti Direct3D12 vs_5_0 ps_5_0, D3D12)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Ti Direct3D12 vs_5_0 ps_5_0, D3D12)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D12 vs_5_0 ps_5_0, D3D12)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 2080 Ti Direct3D12 vs_5_0 ps_5_0, D3D12)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 2070 Super Direct3D12 vs_5_0 ps_5_0, D3D12)'],
    ['Google Inc.(NVIDIA)', 'ANGLE (NVIDIA, NVIDIA GeForce RTX 2080 Super Direct3D12 vs_5_0 ps_5_0, D3D12)'],
]
mac_webgl = [
    ["Google Inc. (Apple)", "ANGLE (Apple, Apple M1, OpenGL 4.1)"],
    ["Google Inc. (ATI Technologies Inc.)",
     "ANGLE (ATI Technologies Inc., AMD Radeon Pro 5300M OpenGL Engine, OpenGL 4.1)"],
    ["Google Inc. (Intel Inc.)", "ANGLE (Intel Inc., Intel(R) Iris(TM) Plus Graphics 655, OpenGL 4.1)"],
    ["Google Inc. (Apple)", "ANGLE (Apple, Apple M2, OpenGL 4.1)"]
]

webrtc = True
headless_check = True

canvasfeature = {
    "height": random.randint(-5, 5),
    "width": random.randint(-5, 5),
    "r": random.randint(-5, 5),
    "g": random.randint(-5, 5),
    "b": random.randint(-5, 5),
    "a": random.randint(-5, 5)
}

videofeature = {
    "start_index": 265,
    "random_value": random.random()
}

clientrectfeature = False
navigator_hardware_concurrency = random.choice([8, 4, 16])
env_data = {
    "Win64": {
        "webgl_infos": random.choice(windows_webgl),
        "sys_platform": "Windows"
    },
    "MacIntel": {
        "webgl_infos": mac_webgl,
        "sys_platform": "macOS"
    },
    "Linux x86_64": {
        "webgl_infos": random.choice(windows_webgl),
        "sys_platform": "Windows"
    },
    "webrtc": webrtc,
    "headless_check": headless_check,
    "canvasfeature": canvasfeature,
    "videofeature": videofeature,
    "clientrectfeature": clientrectfeature,
    "languages": ['en-US', 'en'],
    "language": 'en-US',
    "navigator_hardware_concurrency": navigator_hardware_concurrency,
    "device_memory": navigator_hardware_concurrency,
    "is_mobile": False,
    "fontsfeature": fonts_info,
    "cssfeature": css_info,
    "screen_color_depth": random.choice([24, 30])
}
