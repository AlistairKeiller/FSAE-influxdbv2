import os, datetime
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
if not token:
    raise ValueError("INFLUXDB_TOKEN environment variable is not set")

org = "FSAE"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)

bucket="test"

write_api = client.write_api(write_options=SYNCHRONOUS)

point = (
  Point("measurement1")
  .tag("tagname1", "tagvalue1")
  .field("field1", 1)
  
)
write_api.write(bucket=bucket, org="FSAE", record=point)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", 1)
    .time(datetime.datetime.now())
  )
  write_api.write(bucket=bucket, org="FSAE", record=point)
