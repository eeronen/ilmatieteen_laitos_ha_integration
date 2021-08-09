DOMAIN = "weather_data"


async def async_setup(hass, config):
    hass.states.async_set("weather_data.setup_done", "true")

    # Return boolean to indicate that initialization was successful.
    return True