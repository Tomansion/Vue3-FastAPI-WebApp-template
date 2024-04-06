from configparser import ConfigParser
from termcolor import colored

import os

config_path = "config/config.ini"
config_parser = ConfigParser()

DEBUG_COLOR = "light_blue"
DEBUG_SECONDARY_COLOR = "blue"
ERROR_COLOR = "light_red"
SUCCESS_COLOR = "green"

# Config descriptions
config_descriptions = {
    "NOTES": {
        "NOTES_NUMBER_MAX": {
            "default": 10,
            "type": int,
            "env": "APP_NOTES_NUMBER_MAX",
        },
        "NOTES_TITLE_LENGTH_MAX": {
            "default": 50,
            "type": int,
            "env": "APP_NOTES_TITLE_LENGTH_MAX",
        },
        "NOTES_CONTENT_LENGTH_MAX": {
            "default": 500,
            "type": int,
            "env": "APP_NOTES_CONTENT_LENGTH_MAX",
        },
    },
    "ARANGODB": {
        "HOST": {
            "type": str,
            "env": "APP_ARANGODB_HOST",
        },
        "PORT": {
            "type": int,
            "env": "APP_ARANGODB_PORT",
        },
        "DATABASE": {
            "type": str,
            "env": "APP_ARANGODB_DATABASE",
        },
        "USER": {
            "type": str,
            "env": "APP_ARANGODB_USER",
        },
        "PASSWORD": {
            "type": str,
            "env": "APP_ARANGODB_PASSWORD",
        },
    },
}

# Config values
config = {}


def get_config_value(section, key, config_parser):
    # Return the value of the key in the section of the config_parser
    # Or return the ENV_VAR if it exists

    value = None

    # Get the value from the config file
    if section in config_parser and key in config_parser[section]:
        return config_parser[section][key]

    # Get the value from the environment variables
    ENV_VAR = config_descriptions[section][key]["env"]
    if ENV_VAR in os.environ:
        return os.environ[ENV_VAR]

    if value is None:
        # No value found in the config or in the environment variables
        if "default" in config_descriptions[section][key]:
            print(
                " - Missing "
                + colored(section, DEBUG_SECONDARY_COLOR)
                + " / "
                + colored(key, DEBUG_SECONDARY_COLOR)
                + " in config or in "
                + colored(ENV_VAR, DEBUG_SECONDARY_COLOR)
                + " env var, using default value"
            )
            return config_descriptions[section][key]["default"]

        raise ValueError(
            "Missing "
            + colored(section + " / " + key, ERROR_COLOR)
            + " in "
            + config_path
            + " or in "
            + colored(ENV_VAR, ERROR_COLOR)
            + " env var.\n"
            + "Copy the "
            + colored(config_path, DEBUG_SECONDARY_COLOR)
            + ".example file to "
            + colored(config_path, DEBUG_SECONDARY_COLOR)
            + " and fill it."
        )

    return value


def set_config_value(section, key, value):
    global config

    # Set the value to the right type
    value_type = config_descriptions[section][key]["type"]
    if value_type == bool:
        if value.lower() not in ["true", "false"]:
            raise ValueError(
                " - "
                + colored(section, ERROR_COLOR)
                + " / "
                + colored(key, ERROR_COLOR)
                + " should be a boolean (true or false)"
            )
        value = value.lower() == "true"
    elif value_type == int:
        try:
            value = int(value)
        except ValueError:
            raise ValueError(
                " - "
                + colored(section, ERROR_COLOR)
                + " / "
                + colored(key, ERROR_COLOR)
                + " should be an integer"
            )
    elif value_type == str:
        value = str(value)

    # Set the value in the config
    print(" - Set " + colored(section, DEBUG_COLOR) + " / " + colored(key, DEBUG_COLOR))
    config[section][key] = value


def init_config():
    global config

    print("\nInitializing configuration...")

    # Read the config file
    config_parser.read(config_path)

    # Set the config values
    for section in config_descriptions.keys():
        config[section] = {}

        for key in config_descriptions[section].keys():
            # Get the value from the config file or the environment variables
            value = get_config_value(section, key, config_parser)

            # Set the value in the config according to its type
            set_config_value(section, key, value)


def get_config():
    if config == {}:  # If the config is not initialized
        init_config()
    return config
