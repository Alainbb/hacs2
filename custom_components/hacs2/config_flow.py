"""Config flow for HACS2 integration."""

from homeassistant import config_entries

class Hacs2ConfigFlow(config_entries.ConfigFlow, domain="hacs2"):
    """Handle a config flow for HACS2."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="HACS2", data={})
        return self.async_show_form(step_id="user")
