# dashboard-exporter

A Python client to export a New Relic dashboard PDF or image programmatically.

## Installation

This is available on the Python Package Index (PyPI). You can install using pip.

```
virtualenv env
source env/bin/activate
pip install nrde
```

To install the development version, run:

```
pip install https://github.com/AnthonyBloomer/dashboard-exporter/archive/dev.zip
```

## Usage

Pass the GUID of a given Dashboard to the `exporter` function to download a snapshot of your dashboard. You can get the GUID by pressing the `info` button in your dashboard.

```python
import os
import time

from dashboard_exporter import exporter
import mimetypes

output = exporter(
    personal_api_key="Your personal API Key",
    guid="The New Relic Dashboard GUID",
    file_type="PDF",
)

content_type = output.headers["content-type"]
extension = mimetypes.guess_extension(content_type)

output_directory = os.getcwd()
filename = int(time.time())

of = "%s/%s%s" % (output_directory, filename, extension)

with open(of, "wb") as f:
    f.write(output.content)
    f.close()

```
