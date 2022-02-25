# Grafana CVE-2021-43798 Exploit Script

Script to demonstrate the Grafana directory traversal exploit (CVE-2021-43798) that affects Grafana versions 8.0.0-beta1 through 8.3.0.
Primarily used for a demonstration in a CTF. Written in python with standard library modules only. Only use this for   legitimate purposes e.g testing and CTFs please.

## Installation

``` bash
wget https://raw.githubusercontent.com/Jroo1053/GrafanaDirInclusion/master/exploit.py
```
## Usage

```bash

usage: exploit.py [-h] -u TARGET_URL -p TARGET_PORT [-o OUTPUT_FILE] -f TARGET_FILE

Grafana CVE-2021-43798 (File Read Exploit)

optional arguments:
  -h, --help      show this help message and exit
  -u TARGET_URL   Target URL
  -p TARGET_PORT  Target Port
  -o OUTPUT_FILE  Output File
  -f TARGET_FILE  Remote File To Read

```
