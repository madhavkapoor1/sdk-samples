Application Name
================
daily_speedtest


Application Version
===================
1.0


NCOS Devices Supported
======================
ALL


External Requirements
=====================
None


Application Purpose
===================
daily_speedtest - run an ookla speedtest daily at configured hours and put results to user defined field (asset_id)

Testing hours and results field are configurable in SDK Appdata.  Default hours are 8am, 12pm, 4pm.

06:51:18 PM INFO daily_speedtest Daily speedtest scheduled for 12:00 -- Running now...
06:51:41 PM INFO daily_speedtest 51.48Mbps Down / 10.61Mbps Up / 105ms latency


Expected Output
===============
Speedtest results in asset_id.

