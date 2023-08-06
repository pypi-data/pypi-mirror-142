
"""Open garage"""
import asyncio
import logging

import aiohttp
import async_timeout

DEFAULT_TIMEOUT = 10

_LOGGER = logging.getLogger(__name__)


class OpenReisinger:
    """Class to communicate with the Reisinger Drive api."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        devip,
        devkey=None,
        verify_ssl=False,
        websession=None,
        timeout=DEFAULT_TIMEOUT,
    ):
        
        """Initialize the Reisinger Drive connection."""
        if websession is None:

            async def _create_session():
                _LOGGER.error("Creating session")
                return aiohttp.ClientSession()

            loop = asyncio.get_event_loop()
            self.websession = loop.run_until_complete(_create_session())
        else:
            self.websession = websession
        self._timeout = timeout
        self._devip = devip
        self._devkey = devkey
        self._verify_ssl = verify_ssl

    @property
    def device_url(self):
        """Device url."""
        return self._devip

    async def close_connection(self):
        """Close the connection."""
        await self.websession.close()

    async def update_state(self):
        """Update state."""
        return await self._execute("door/state")

    async def open_door(self):
        """Update state."""
        _LOGGER.error("invoking open door")        
        return await self._execute("door/open")

    async def open_door_temp(self):
        """Update state."""
        _LOGGER.error("invoking open door")        
        return await self._execute("door/opentemp")

    async def get_is_door_opened(self):
        """Reboot device."""
        result = await self._execute("door/state")
        if result is None:
            return None
        return result.get("opened")

    async def reboot(self):
        """Reboot device."""
        result = await self._execute("system/reboot")
        if result is None:
            return None
        return result.get("result")

    async def ap_mode(self):
        """Reset device in AP mode (to reconfigure WiFi settings)."""
        result = await self._execute("system/apmode")
        if result is None:
            return None
        return result.get("result")

    async def _execute(self, command, retry=2):
        """Execute command."""
        url = f"{self._devip}/{command}"
        try:
            async with async_timeout.timeout(self._timeout):
                resp = await self.websession.get(url, verify_ssl=self._verify_ssl)
            if resp.status != 200:
                _LOGGER.error(
                    "Error connecting to Reisinger Drive, resp code: %s", resp.status
                )
                return None
            result = await resp.json(content_type=None)
        except aiohttp.ClientError as err:
            if retry > 0:
                return await self._execute(command, retry - 1)
            _LOGGER.error("Error connecting to Reisinger Drive: %s ", err, exc_info=True)
            raise
        except asyncio.TimeoutError:
            if retry > 0:
                return await self._execute(command, retry - 1)
            _LOGGER.error("Timed out when connecting to Reisinger Drive device")
            raise

        return result