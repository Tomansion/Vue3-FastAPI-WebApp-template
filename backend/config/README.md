# Configuration

This folder contains the configuration files and services for the application backend.

## Files

### [`init_config.py`](./init_config.py) file, the configuration loader

This file is the configuration loader, it loads the configuration first from the `config.ini` file, then from the environment variables. If some required configuration elements are missing from the configuration file or the environment variables, the application will raise an exception.

### [`config.ini.example`](./config.ini.example) file, the configuration example file

This file is a configuration example file, it serves as a documentation for new developers.

### [`config.env`](./config.env) file, the environment file

This file documents the environment variables that the backend application uses. This file is used for documentation purposes only.

### [`config.ini`](./config.ini) file, the configuration file

This file is the configuration file for the backend application, it will be used by the application to load the configuration.

You can create a new configuration file by copying and modifying the `config.ini.example` file.

```bash
cp backend/config/config.ini.example backend/config/config.ini
nano backend/config/config.ini
```

Do not commit the `config.ini` file to the repository, it contains sensitive information.

## Adding new configuration elements

Here are the steps to add new configuration elements in case the application needs it:

1. Update the `init_config.py` file to load the new configuration elements
2. Add the new configuration elements your local `config.ini` file
3. Document the new configuration elements in the `config.ini.example` file
4. Document the new configuration environment variables in the `config.env` file
