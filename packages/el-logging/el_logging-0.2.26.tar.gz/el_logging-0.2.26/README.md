# Easily Launch Logging (el_logging)

Loguru based custom logging package for simple python projects.

## Features

* Loguru based logging
* Custom basic logging module
* Logging to files (all, error, json)
* Custom logging formats
* Custom options as a config
* Colorful logging
* Multiprocess compatibility (Linux, macOS - 'fork', Windows - 'spawn')

---

## Installation

### 1. Prerequisites

* **Python (>= v3.7)**
* **PyPi (>= v21)**

### 2. Install el-logging

#### A. [RECOMMENDED] PyPi install

```sh
# Install or upgrade el-logging package:
pip install --upgrade el-logging

# To uninstall package:
pip uninstall -y el-logging
```

#### B. Manually add to PYTHONPATH (Recommended for development)

```sh
# Clone repository by git:
git clone git@bitbucket.org:ellexiinc/el_logging.git
cd el_logging

# Install python dependencies:
pip install --upgrade pip
cat requirements.txt | xargs -n 1 -L 1 pip install --no-cache-dir

# Add current path to PYTHONPATH:
export PYTHONPATH="${PWD}:${PYTHONPATH}"
```

#### C. Manually compile and setup (Not recommended)

```sh
# Clone repository by git:
git clone git@bitbucket.org:ellexiinc/el_logging.git
cd el_logging

# Building python package:
pip install --upgrade pip setuptools wheel
python setup.py build
# Install python dependencies with built package to current python environment:
python setup.py install --record installed_files.txt

# To remove only installed el-logging package:
head -n 1 installed_files.txt | xargs rm -vrf
# Or to remove all installed files and packages:
cat installed_files.txt | xargs rm -vrf
```

### 3. Configuration (You can skip this step, if you don't want to configure)

* First, check **.env.example (environment variables)** file.
* Sample **.env.example** file - [https://bitbucket.org/ellexiinc/el_logging/src/master/.env.example](https://bitbucket.org/ellexiinc/el_logging/src/master/.env.example)
* Copy **.env.example** file to **.env** and change environment variables:

```sh
cp -v .env.example [PROJECT_DIR]/.env
cd [PROJECT_DIR]
nano .env
```

* Make **configs** directory inside project's base directory and copy **configs/logger.yaml** file into **configs**.
* Sample **logger.yml** config file - [https://bitbucket.org/ellexiinc/el_logging/src/master/configs/logger.yaml](https://bitbucket.org/ellexiinc/el_logging/src/master/configs/logger.yaml)
* Then edit variable options:

```sh
mkdir -vp [PROJECT_DIR]/configs

cp -v logger.yaml [PROJECT_DIR]/configs/logger.yaml
rm -vf logger.yaml
cd [PROJECT_DIR]
nano configs/logger.yaml
```

## Usage/Examples

* Sample python file - [https://bitbucket.org/ellexiinc/el_logging/src/master/sample.py](https://bitbucket.org/ellexiinc/el_logging/src/master/sample.py)
* Import el_logging module:

```python
from el_logging import logger


logger.trace('Tracing...')
logger.debug('Debugging...')
logger.info('Logging info.')
logger.success('Success.')
logger.warning('Warning something.')
logger.error('Error occured.')
logger.critical('CRITICAL ERROR.')


def divide(a, b):
    _result = a / b
    return _result

try:
    divide(10, 0)
except Exception as err:
    logger.exception("Failed to divide:")
```

---

## Running Tests

To run tests, run the following command:

```sh
python -m unittest tests/test_*.py
```

## Environment Variables

You can use the following environment variables inside **.env** file:

```bash
ENV=development
DEBUG=true
APP_NAME=tsc_vrae
LOGS_DIR="/var/log/app"
```

## Configuration

You can use the following sample configuration:

```yaml
logger:
    level: "INFO"
    use_color: true
    use_icon: false
    use_backtrace: true
    std_format_str: "[<c>{time:YYYY-MM-DD HH:mm:ss.SSS Z}</c> | <level>{lvlname:<5}</level> | <w>{file}</w>:<w>{line}</w>]: <level>{message}</level>"
    use_log_file: false
    file_format_str: "[{time:YYYY-MM-DD HH:mm:ss.SSS Z} | {lvlname:<5} | {file}:{line}]: {message}"
    rotate_when:
        at_hour: 0
        at_minute: 0
        at_second: 0
    rotate_file_size: 10000000
    backup_file_count: 50
    file_encoding: utf8
    all_log_filename: "{app_name}.std.all.log"
    err_log_filename: "{app_name}.std.err.log"
    use_log_json: false
    use_custom_json: false
    json_all_log_filename: "{app_name}.json.all.log"
    json_err_log_filename: "{app_name}.json.err.log"
    # logs_dir: /var/log/app
```

---

## References

* [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)
