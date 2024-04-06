# Configuration

This folder contains the configuration files for the backend application.

## Files

### `init_config.py` file, the configuration loader

This file is the configuration loader, it loads the configuration first from the `config.ini` file, then from the environment variables. If some required configuration elements are missing from the configuration file or the environment variables, the application will raise an exception.

### `config.ini.example` file, the configuration example file

This file is a configuration example file, it serves as a documentation for new developers.

### `config.env` file, the environment file

This file documents the environment variables that the backend application uses. This file is used for documentation purposes only.

### `config.ini` file, the configuration file

This file is the configuration file for the backend application, it will be used by the application to load the configuration.

You can create a new configuration file by copying and modifying the `config.ini.example` file.

```bash
cp backend/config/config.ini.example backend/config/config.ini
nano backend/config/config.ini
```

## Adding new configuration elements

Here are the steps to add new configuration elements:

1. Add the new configuration elements to the `config.ini` file
2. Add new configuration elements examples to the `config.ini.example` file
3. Add new configuration elements examples to the `config.env` file
4. Update the `init_config.py` file to load the new configuration elements
