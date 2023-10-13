# -*- coding: utf-8 -*-
import json
import random
from dataclasses import dataclass
from typing import Tuple, Optional, Dict

import pkg_resources
from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage


def from_file(name):
    """Read script from ./js directory"""
    return pkg_resources.resource_string('pjstealth', f'js/{name}').decode()


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
    'webdriver': 'delete Object.getPrototypeOf(navigator).webdriver',
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
    'chrome_videofeature2': from_file('chrome.videofeature2.js'),
    'chrome_canvasfeature2': from_file('chrome.canvasfeature2.js')
}


@dataclass
class StealthConfig(object):
    webgl_infos = [
        ["Google Inc. (Apple)", "ANGLE (Apple, Apple M1, OpenGL 4.1)"],
        ["Google Inc. (ATI Technologies Inc.)",
         "ANGLE (ATI Technologies Inc., AMD Radeon Pro 5300M OpenGL Engine, OpenGL 4.1)"],
        ["Google Inc. (Intel Inc.)", "ANGLE (Intel Inc., Intel(R) Iris(TM) Plus Graphics 655, OpenGL 4.1)"],
        ["Google Inc. (Apple)", "ANGLE (Apple, Apple M2, OpenGL 4.1)"]
    ]

    def __init__(self, **kwargs):
        # load script options
        self.webdriver: bool = True
        self.webgl_vendor: bool = True
        self.navigator_vendor: bool = True
        self.navigator_plugins: bool = True
        self.navigator_permissions: bool = True
        self.navigator_languages: bool = True
        self.navigator_language: bool = True
        self.navigator_platform: bool = True
        self.navigator_user_agent: bool = True
        self.media_codecs: bool = True
        self.iframe_content_window: bool = True
        self.chrome_runtime: bool = True
        self.chrome_load_times: bool = True
        self.chrome_csi: bool = True
        self.chrome_app: bool = True
        self.outerdimensions: bool = True
        self.hairline: bool = True
        self.chrome_cssfeature = True
        self.chrome_fontsfeature = True
        self.chrome_headless_check = True
        self.chrome_webrtc = True
        self.is_mobile = False
        self.is_user_agent_data = True
        self.navigator_hardware_concurrency_flag = True
        self.navigator_device_memory = True
        self.chrome_canvasfeature = True
        self.chrome_videofeature = True
        self.chrome_clientrectfeature = True

        # options
        self.vendor: str = 'Intel Inc.'
        self.renderer: str = 'Intel Iris OpenGL Engine'
        self.nav_vendor: str = 'Google Inc.'
        self.nav_user_agent: str = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        self.chrome_version = 116
        self.nav_platform: str = 'MacIntel'
        self.sys_platform: str = 'macOS'
        self.languages: Tuple[str] = ('en-US', 'en')
        self.language = 'en-US'
        self.runOnInsecureOrigins: Optional[bool] = None
        self.navigator_hardware_concurrency: int = 4
        self.device_memory = 8

        if kwargs:
            self.modify(kwargs)

    def modify(self, info):
        if info.get("webgl_random"):
            tmp_webgl_info = random.choice(self.webgl_infos)
            self.vendor = tmp_webgl_info[0]
            self.renderer = tmp_webgl_info[1]
        if info.get("vendor"):
            self.vendor = info.get("vendor")
        if info.get("renderer"):
            self.renderer = info.get("renderer")
        if info.get("nav_vendor"):
            self.nav_vendor = info.get("nav_vendor")
        if info.get("nav_user_agent"):
            self.nav_user_agent = info.get("nav_user_agent")
        if info.get("nav_platform"):
            self.nav_platform = info.get("nav_platform")
        if info.get("languages"):
            self.languages = info.get("languages")
            self.language = info.get("languages")[0]

        if info.get("runOnInsecureOrigins"):
            self.runOnInsecureOrigins = info.get("runOnInsecureOrigins")
        if info.get("chrome_version"):
            self.chrome_version = info.get("chrome_version")
        if info.get("navigator_hardware_concurrency"):
            self.navigator_hardware_concurrency = info.get("navigator_hardware_concurrency")
        if info.get("is_user_agent_data"):
            self.is_user_agent_data = info.get("is_user_agent_data")
        if info.get("device_memory"):
            self.device_memory = info.get("device_memory")

        if self.nav_platform.__eq__("MacIntel"):
            self.sys_platform = 'macOS'
        if self.nav_platform.__eq__("Win32"):
            self.sys_platform = 'Windows'

        self.webdriver = info.get("webdriver") if info.get("webdriver") is not None else self.webdriver
        self.webgl_vendor = info.get("webgl_vendor") if info.get("webgl_vendor") is not None else self.webgl_vendor
        self.navigator_vendor = info.get("navigator_vendor") if info.get(
            "navigator_vendor") is not None else self.navigator_vendor
        self.navigator_plugins = info.get("navigator_plugins") if info.get(
            "navigator_plugins") is not None else self.navigator_plugins
        self.navigator_permissions = info.get("navigator_permissions") if info.get(
            "navigator_permissions") is not None else self.navigator_permissions
        self.navigator_languages = info.get("navigator_languages") if info.get(
            "navigator_languages") is not None else self.navigator_languages
        self.navigator_language = info.get("navigator_language") if info.get(
            "navigator_language") is not None else self.navigator_language
        self.navigator_platform = info.get("navigator_platform") if info.get(
            "navigator_platform") is not None else self.navigator_platform
        self.navigator_user_agent = info.get("navigator_user_agent") if info.get(
            "navigator_user_agent") is not None else self.navigator_user_agent
        self.media_codecs = info.get("media_codecs") if info.get("media_codecs") is not None else self.media_codecs
        self.iframe_content_window = info.get("iframe_content_window") if info.get(
            "iframe_content_window") is not None else self.iframe_content_window

        self.chrome_runtime = info.get("chrome_runtime") if info.get(
            "chrome_runtime") is not None else self.chrome_runtime
        self.chrome_load_times = info.get("chrome_load_times") if info.get(
            "chrome_load_times") is not None else self.chrome_load_times
        self.chrome_csi = info.get("chrome_csi") if info.get("chrome_csi") is not None else self.chrome_csi
        self.chrome_app = info.get("chrome_app") if info.get("chrome_app") is not None else self.chrome_app
        self.outerdimensions = info.get("outerdimensions") if info.get(
            "outerdimensions") is not None else self.outerdimensions
        self.hairline = info.get("hairline") if info.get("hairline") is not None else self.hairline
        self.chrome_cssfeature = info.get("chrome_cssfeature") if info.get(
            "chrome_cssfeature") is not None else self.chrome_cssfeature
        self.chrome_fontsfeature = info.get("chrome_fontsfeature") if info.get(
            "chrome_fontsfeature") is not None else self.chrome_fontsfeature
        self.chrome_headless_check = info.get("chrome_headless_check") if info.get(
            "chrome_headless_check") is not None else self.chrome_headless_check
        self.chrome_webrtc = info.get("chrome_webrtc") if info.get("chrome_webrtc") is not None else self.chrome_webrtc
        self.is_mobile = info.get("is_mobile") if info.get("is_mobile") is not None else self.is_mobile
        self.is_user_agent_data = info.get("is_user_agent_data") if info.get(
            "is_user_agent_data") is not None else self.is_user_agent_data
        self.navigator_hardware_concurrency_flag = info.get("navigator_hardware_concurrency_flag") if info.get(
            "navigator_hardware_concurrency_flag") is not None else self.navigator_hardware_concurrency_flag
        self.navigator_device_memory = info.get("navigator_device_memory") if info.get(
            "navigator_device_memory") is not None else self.navigator_device_memory
        self.chrome_canvasfeature = info.get("chrome_canvasfeature") if info.get(
            "chrome_canvasfeature") is not None else self.chrome_canvasfeature
        self.chrome_videofeature = info.get("chrome_videofeature") if info.get(
            "chrome_videofeature") is not None else self.chrome_videofeature
        self.chrome_clientrectfeature = info.get("chrome_clientrectfeature") if info.get(
            "chrome_clientrectfeature") is not None else self.chrome_clientrectfeature

    @property
    def enabled_scripts(self):
        opts = json.dumps({
            'webgl_vendor': self.vendor,
            'webgl_renderer': self.renderer,
            'navigator_vendor': self.nav_vendor,
            'navigator_platform': self.nav_platform,
            'navigator_user_agent': self.nav_user_agent,
            'navigator_app_version': self.nav_user_agent.replace("Mozilla/", ""),
            'languages': list(self.languages),
            'language': self.language,
            'runOnInsecureOrigins': self.runOnInsecureOrigins,
            'navigator_hardware_concurrency': self.navigator_hardware_concurrency,
            'user_agent_data': {
                "brands": [{"brand": "Not)A;Brand", "version": "24"},
                           {"brand": "Chromium", "version": f"{self.chrome_version}"},
                           {"brand": "Google Chrome", "version": f"{self.chrome_version}"}], "mobile": self.is_mobile,
                "platform": self.sys_platform},
            "device_memory": self.device_memory
        })
        # defined options constant
        yield f'const opts = {opts}'
        # init utils and generate_magic_arrays helper
        yield SCRIPTS['utils']
        yield SCRIPTS['generate_magic_arrays']

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
        if self.navigator_languages:
            yield SCRIPTS['navigator_languages']
        if self.navigator_permissions:
            yield SCRIPTS['navigator_permissions']
        if self.navigator_plugins:
            yield SCRIPTS['navigator_plugins']
        if self.navigator_vendor:
            yield SCRIPTS['navigator_vendor']
        if self.webdriver:
            yield SCRIPTS['webdriver']
        if self.outerdimensions:
            yield SCRIPTS['outerdimensions']
        if self.webgl_vendor:
            yield SCRIPTS['webgl_vendor']
        if self.navigator_platform:
            yield SCRIPTS['navigator_platform']
        # if self.navigator_user_agent:
        #     yield SCRIPTS['navigator_user_agent']
        #     yield SCRIPTS['navigator_appVersion']
        if self.hairline:
            yield SCRIPTS['chrome_hairline']
        if self.chrome_cssfeature:
            yield SCRIPTS['chrome_cssfeature']
        if self.chrome_fontsfeature:
            yield SCRIPTS['chrome_fontsfeature']
        if self.chrome_webrtc:
            yield SCRIPTS['chrome_webrtc']
        if self.chrome_headless_check:
            yield SCRIPTS['hookfuc_headless']
        if self.is_user_agent_data:
            yield SCRIPTS['navigator_userAgentData']
        if self.language:
            yield SCRIPTS['navigator_language']
        if self.navigator_hardware_concurrency_flag:
            yield SCRIPTS['navigator_hardwareConcurrency']
        if self.navigator_device_memory:
            yield SCRIPTS['navigator_deviceMemory']
        if self.chrome_canvasfeature:
            yield SCRIPTS['chrome_canvasfeature']
            yield SCRIPTS['chrome_canvasfeature2']
        if self.chrome_videofeature:
            yield SCRIPTS['chrome_videofeature']
            yield SCRIPTS['chrome_videofeature2']
        if self.chrome_clientrectfeature:
            yield SCRIPTS['chrome_clientrectfeature']


def stealth_sync(page: SyncPage, config: StealthConfig = None):
    """teaches synchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        page.add_init_script(script)


async def stealth_async(page: AsyncPage, config: StealthConfig = None):
    """teaches asynchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        await page.add_init_script(script)
