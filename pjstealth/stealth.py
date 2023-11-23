# -*- coding: utf-8 -*-
import json
import random
import re
from dataclasses import dataclass
from typing import Optional, Dict
from .env_data import env_data
import pkg_resources


def from_file(name):
    """Read script from ./js directory"""
    return pkg_resources.resource_string('pjstealth', f'feature/{name}').decode()


SCRIPTS: Dict[str, str] = {
    'chrome_csi': from_file('chrome.csi.js'),
    'chrome_app': from_file('chrome.app.js'),
    'chrome_runtime': from_file('chrome.runtime.js'),
    'chrome_load_times': from_file('chrome.load.times.js'),
    'chrome_hairline': from_file('chrome.hairline.js'),
    'generate_magic_arrays': from_file('generate.magic.arrays.js'),
    'iframe_content_window': from_file('iframe.contentWindow.js'),
    'media_codecs': from_file('media.codecs.js'),
    'navigator_vendor': from_file('navigator.vendor.js'),
    'navigator_plugins': from_file('navigator.plugins.js'),
    'navigator_permissions': from_file('navigator.permissions.js'),
    'navigator_languages': from_file('navigator.languages.js'),
    'navigator_platform': from_file('navigator.platform.js'),
    'navigator_user_agent': from_file('navigator.userAgent.js'),
    'navigator_hardwareConcurrency': from_file('navigator.hardwareConcurrency.js'),
    'outerdimensions': from_file('window.outerdimensions.js'),
    'utils': from_file('utils.js'),
    'webdriver': from_file('chrome.webdriver.js'),
    'webgl_vendor': from_file('webgl.vendor.js'),
    'navigator_appVersion': from_file('navigator.appVersion.js'),
    'navigator_deviceMemory': from_file('navigator.deviceMemory.js'),
    'navigator_language': from_file('navigator.language.js'),
    'navigator_userAgentData': from_file('navigator.userAgentData.js'),
    'chrome_canvasfeature': from_file('chrome.canvasfeature.js'),
    'chrome_clientrectfeature': from_file('chrome.clientrectfeature.js'),
    'chrome_cssfeature': from_file('chrome.cssfeature.js'),
    'chrome_fontsfeature': from_file('chrome.fontsfeature.js'),
    'chrome_webrtc': from_file('chrome.webrtc.js'),
    'hookfuc_headless': from_file('hookfuc.headless.js'),
    'chrome_videofeature': from_file('chrome.videofeature.js'),
    'chrome_canvasfeature2': from_file('chrome.canvasfeature2.js'),
    'chrome_screen_colordepth': from_file('chrome.screen.colordepth.js'),
    'chrome_mouse_event': from_file('chrome.mouseevent.js')
}


@dataclass
class StealthConfig(object):
    vendor: str = 'Intel Inc.'
    renderer: str = 'Intel Iris OpenGL Engine'
    nav_vendor: str = 'Google Inc.'
    runOnInsecureOrigins: Optional[bool] = None
    mouse_detail = 0
    mouse_button = 0
    mouse_buttons = 1

    webdriver: bool = True
    webgl_vendor: bool = True
    navigator_plugins: bool = True
    navigator_permissions: bool = True
    media_codecs: bool = True
    iframe_content_window: bool = True
    chrome_runtime: bool = True
    chrome_load_times: bool = True
    chrome_csi: bool = True
    chrome_app: bool = True
    outerdimensions: bool = True
    hairline: bool = True

    # 随机特征开启默认为false
    random_feature = True

    def __init__(self, navigator_user_agent, navigator_platform, **kwargs):
        # 匹配user-agent
        self.navigator_user_agent: str = navigator_user_agent
        self.navigator_platform = navigator_platform

        self.random_feature = kwargs.get("random_feature") if kwargs.get(
            "random_feature") is not None else self.random_feature

        if self.random_feature:

            self.navigator_languages = env_data.get("languages")
            self.navigator_language = env_data.get("language")
            # user-agent mac(m系列和非m系列)， windows版对应
            self.navigator_user_agent = env_data.get("user_agent") if env_data.get(
                "user_agent") is not None else self.navigator_user_agent
            self.browser_version = env_data.get("browser_version")

            if self.navigator_user_agent:
                if self.navigator_user_agent.lower().__contains__("(mac"):
                    self.navigator_platform = 'MacIntel'

                    if not self.navigator_user_agent.lower().__contains__("intel"):
                        while True:
                            tmp_webgl_info = random.choice(env_data.get(self.navigator_platform).get("webgl_infos"))
                            if str(tmp_webgl_info).lower().__contains__("m1") or str(
                                    tmp_webgl_info).lower().__contains__("m2"):
                                self.vendor = tmp_webgl_info[0]
                                self.renderer = tmp_webgl_info[1]
                                break
                    else:
                        while True:
                            tmp_webgl_info = random.choice(env_data.get(self.navigator_platform).get("webgl_infos"))
                            if str(tmp_webgl_info).lower().__contains__("m1") or str(
                                    tmp_webgl_info).lower().__contains__("m2"):
                                continue
                            else:
                                self.vendor = tmp_webgl_info[0]
                                self.renderer = tmp_webgl_info[1]
                                break

                if self.navigator_user_agent.lower().__contains__("(windows"):
                    self.navigator_platform = 'Win64'

                    self.vendor = env_data.get(self.navigator_platform).get("webgl_infos")[0]
                    self.renderer = env_data.get(self.navigator_platform).get("webgl_infos")[1]

                if self.navigator_user_agent.lower().__contains__("linux"):
                    self.navigator_platform = "Linux x86_64"
                    self.vendor = env_data.get(self.navigator_platform).get("webgl_infos")[0]
                    self.renderer = env_data.get(self.navigator_platform).get("webgl_infos")[1]

                self.browser_version = re.search(r"Chrome/(\d+)", self.navigator_user_agent).group(1)
            self.navigator_platform = self.navigator_platform if self.navigator_platform is not None else random.choice(
                ['MacIntel', 'Win64'])

            self.sys_platform = env_data.get(self.navigator_platform).get("sys_platform")

            self.navigator_hardware_concurrency = env_data.get("navigator_hardware_concurrency")
            self.device_memory = env_data.get("device_memory")
            self.cssfeature = env_data.get("cssfeature")
            self.fontsfeature = env_data.get("fontsfeature")
            self.webrtc = env_data.get("webrtc")
            self.canvasfeature = env_data.get("canvasfeature")
            self.videofeature = env_data.get("videofeature")
            self.clientrectfeature = env_data.get("clientrectfeature")
            self.headless_check = env_data.get("headless_check")

            self.is_mobile = False

            self.screen_color_depth = env_data.get("screen_color_depth")
        else:
            self.navigator_languages = kwargs.get("navigator_languages")
            self.navigator_language = kwargs.get("navigator_language")
            self.navigator_platform: str = kwargs.get("navigator_platform") if kwargs.get(
                "navigator_platform") else self.navigator_platform
            self.navigator_user_agent = kwargs.get("user_agent") if kwargs.get(
                "user_agent") is not None else self.navigator_user_agent
            if self.navigator_platform is not None:
                self.sys_platform = "Windows" if self.navigator_platform.startswith("W") else "macOS"
            else:
                self.sys_platform = None
            self.navigator_hardware_concurrency = kwargs.get("navigator_hardware_concurrency")
            self.device_memory = kwargs.get("device_memory")
            self.is_mobile = kwargs.get("is_mobile")
            self.browser_version = kwargs.get("browser_version")
            self.screen_color_depth = kwargs.get("screen_color_depth")
        self.vendor = kwargs.get("vendor") if kwargs.get("vendor") is not None else self.vendor
        self.renderer = kwargs.get("renderer") if kwargs.get("renderer") is not None else self.renderer
        self.nav_vendor = kwargs.get("nav_vendor") if kwargs.get("nav_vendor") is not None else self.nav_vendor
        self.runOnInsecureOrigins = kwargs.get("runOnInsecureOrigins") if kwargs.get(
            "runOnInsecureOrigins") is not None else self.runOnInsecureOrigins
        self.webdriver = kwargs.get("webdriver") if kwargs.get("webdriver") is not None else self.webdriver
        self.webgl_vendor = kwargs.get("webgl_vendor") if kwargs.get(
            "webgl_vendor") is not None else self.webgl_vendor
        self.navigator_plugins = kwargs.get("navigator_plugins") if kwargs.get(
            "navigator_plugins") is not None else self.navigator_plugins
        self.navigator_permissions = kwargs.get("navigator_permissions") if kwargs.get(
            "navigator_permissions") is not None else self.navigator_permissions
        self.media_codecs = kwargs.get("media_codecs") if kwargs.get(
            "media_codecs") is not None else self.media_codecs
        self.iframe_content_window = kwargs.get("iframe_content_window") if kwargs.get(
            "iframe_content_window") is not None else self.iframe_content_window
        self.chrome_runtime = kwargs.get("chrome_runtime") if kwargs.get(
            "chrome_runtime") is not None else self.chrome_runtime
        self.chrome_load_times = kwargs.get("chrome_load_times") if kwargs.get(
            "chrome_load_times") is not None else self.chrome_load_times
        self.chrome_csi = kwargs.get("chrome_csi") if kwargs.get("chrome_csi") is not None else self.chrome_csi
        self.chrome_app = kwargs.get("chrome_app") if kwargs.get("chrome_app") is not None else self.chrome_app
        self.outerdimensions = kwargs.get("outerdimensions") if kwargs.get(
            "outerdimensions") is not None else self.outerdimensions
        self.hairline = kwargs.get("hairline") if kwargs.get("hairline") is not None else self.hairline

        self.cssfeature = kwargs.get("cssfeature") if kwargs.get("cssfeature") is not None else self.cssfeature
        self.fontsfeature = kwargs.get("fontsfeature") if kwargs.get("fontsfeature") is not None else self.fontsfeature
        self.webrtc = kwargs.get("webrtc") if kwargs.get("webrtc") is not None else self.webrtc
        self.canvasfeature = kwargs.get("canvasfeature") if kwargs.get(
            "canvasfeature") is not None else self.canvasfeature
        self.videofeature = kwargs.get("videofeature") if kwargs.get("videofeature") is not None else self.videofeature
        self.clientrectfeature = kwargs.get("clientrectfeature") if kwargs.get(
            "clientrectfeature") is not None else self.clientrectfeature
        self.headless_check = kwargs.get("headless_check") if kwargs.get(
            "headless_check") is not None else self.headless_check

        self.opts = {
            "languages": self.navigator_languages,
            "language": self.navigator_language,
            "webgl_vendor": self.vendor,
            "webgl_renderer": self.renderer,
            "navigator_vendor": self.nav_vendor,
            "navigator_platform": self.navigator_platform,
            "navigator_user_agent": self.navigator_user_agent,
            "navigator_app_version": self.navigator_user_agent.replace("Mozilla/",
                                                                       "") if self.navigator_user_agent else None,
            "runOnInsecureOrigins": self.runOnInsecureOrigins,
            "navigator_hardware_concurrency": self.navigator_hardware_concurrency,
            "device_memory": self.device_memory,
            "user_agent_data": {
                "brands": [{"brand": "Not)A;Brand", "version": "24"},
                           {"brand": "Chromium", "version": f"{self.browser_version}"},
                           {"brand": "Google Chrome", "version": f"{self.browser_version}"}], "mobile": self.is_mobile,
                "platform": self.sys_platform} if self.browser_version is not None and self.is_mobile is not None and self.sys_platform is not None else None,
            "cssfeature": self.cssfeature,
            "fontsfeature": self.fontsfeature,
            "webrtc": self.webrtc,
            "canvasfeature": self.canvasfeature,
            "videofeature": self.videofeature,
            "clientrectfeature": self.clientrectfeature,
            "headless_check": self.headless_check,
            "fonts_start": 0,
            'screen_color_depth': self.screen_color_depth,
            "mouse_event": {
                "detail": self.mouse_detail,
                "button": self.mouse_button,
                "buttons": self.mouse_buttons
            }
        }

    @property
    def enabled_scripts(self):
        opts = json.dumps(self.opts)
        # defined options constant
        yield f'const opts = {opts}'
        # init utils and generate_magic_arrays helper
        yield SCRIPTS['utils']
        yield SCRIPTS['generate_magic_arrays']
        yield SCRIPTS['webgl_vendor']

        if self.chrome_app:
            yield SCRIPTS['chrome_app']
        if self.chrome_runtime:
            yield SCRIPTS['chrome_runtime']
        if self.chrome_load_times:
            yield SCRIPTS['chrome_load_times']
        if self.chrome_csi:
            yield SCRIPTS['chrome_csi']
        if self.iframe_content_window:
            yield SCRIPTS['iframe_content_window']
        if self.media_codecs:
            yield SCRIPTS['media_codecs']
        if self.navigator_plugins:
            yield SCRIPTS['navigator_plugins']
        if self.navigator_permissions:
            yield SCRIPTS['navigator_permissions']
        if self.webdriver:
            yield SCRIPTS['webdriver']
        if self.outerdimensions:
            yield SCRIPTS['outerdimensions']
        if self.hairline:
            yield SCRIPTS['chrome_hairline']

        if self.opts.get("navigator_languages"):
            yield SCRIPTS['navigator_languages']

        if self.opts.get("navigator_vendor"):
            yield SCRIPTS['navigator_vendor']

        if self.opts.get("navigator_platform"):
            yield SCRIPTS['navigator_platform']
        if self.opts.get("navigator_user_agent"):
            yield SCRIPTS['navigator_user_agent']
            yield SCRIPTS['navigator_appVersion']

        if self.opts.get("language"):
            yield SCRIPTS['navigator_language']

        if self.opts.get("user_agent_data"):
            yield SCRIPTS['navigator_userAgentData']

        if self.opts.get("navigator_hardware_concurrency"):
            yield SCRIPTS['navigator_hardwareConcurrency']

        if self.opts.get("device_memory"):
            yield SCRIPTS['navigator_deviceMemory']

        if self.opts.get("cssfeature"):
            yield SCRIPTS['chrome_cssfeature']
        if self.opts.get("fontsfeature"):
            yield SCRIPTS['chrome_fontsfeature']
        if self.opts.get("webrtc"):
            yield SCRIPTS['chrome_webrtc']
        if self.opts.get("headless_check"):
            yield SCRIPTS['hookfuc_headless']

        if self.opts.get("canvasfeature"):
            yield SCRIPTS['chrome_canvasfeature']
            yield SCRIPTS['chrome_canvasfeature2']
        if self.opts.get("videofeature"):
            yield SCRIPTS['chrome_videofeature']
        if self.opts.get("clientrectfeature"):
            yield SCRIPTS['chrome_clientrectfeature']

        if self.opts.get("screen_color_depth"):
            yield SCRIPTS['chrome_screen_colordepth']
        if self.opts.get("mouse_event"):
            yield SCRIPTS['chrome_mouse_event']
