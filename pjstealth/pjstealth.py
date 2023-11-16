from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage
from .stealth import StealthConfig


def stealth_sync(page: SyncPage, config: StealthConfig = None):
    """teaches synchronous playwright Page to be stealthy like a ninja!"""
    navigator_user_agent: str = page.evaluate("navigator.userAgent")
    navigator_platform = page.evaluate("navigator.platform")
    for script in (config or StealthConfig(navigator_user_agent, navigator_platform)).enabled_scripts:
        page.add_init_script(script)


async def stealth_async(page: AsyncPage, config: StealthConfig = None):
    """teaches asynchronous playwright Page to be stealthy like a ninja!"""
    navigator_user_agent: str = await page.evaluate("navigator.userAgent")
    navigator_platform = await page.evaluate("navigator.platform")
    for script in (config or StealthConfig(navigator_user_agent, navigator_platform)).enabled_scripts:
        await page.add_init_script(script)
