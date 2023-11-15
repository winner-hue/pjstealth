from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage
from .stealth import StealthConfig


def stealth_sync(page: SyncPage, config: StealthConfig = None):
    """teaches synchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig(page)).enabled_scripts:
        page.add_init_script(script)


async def stealth_async(page: AsyncPage, config: StealthConfig = None):
    """teaches asynchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig(page)).enabled_scripts:
        await page.add_init_script(script)
