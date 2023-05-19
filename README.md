# RunnerCANA

A simple task bot made for the ARCANA research group
that run tasks given to it as-is and gives simple infomration about running time and error codes directly to your email!

Running runnercana
```
usage: runnercana [-h] [--send-to SEND_TO] [--subject SUBJECT] program

ARCANA Runner

positional arguments:
  program            Program to run in quotes ""

optional arguments:
  -h, --help         show this help message and exit
  --send-to SEND_TO  Email to send the program. Default picks from NETID
  --subject SUBJECT  Subject of email -- by default command and time
```

The email output will be as follows:
```
Subject: [18-May-23] Automated Execution Report | App: ls

Dear <user>,

The report of the most recent run here:

Return code: 0
Execution started at: 21:40:46 CDT
Execution finished at: 21:40:56 CDT
Execution time: 10.0253(s)
Full command: ls; sleep 10

Your friendly neighbourhood,
ArcanaBot ❤️
```
