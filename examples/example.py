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
