# Log-analysis
# Linux Log Analysis Project

## Overview

This project analyzes Linux authentication logs to detect suspicious activities such as failed login attempts, unknown user access attempts, successful logins, and network connections.

The goal is to simulate basic Security Operations Center (SOC) log analysis by identifying security events and summarizing them.

## Dataset

The log data used in this project comes from a structured Linux system log dataset. The relevant log messages were copied into a log file (`auth.log`) for analysis.

## Technologies Used

* Python
* Linux Log Data
* Basic Log Parsing Techniques

## Project Structure

```
Log Analysis Mini Project
│
├── logs
│   └── auth.log
│
├── analysis.py
├── report.txt
└── README.md
```

## What the Script Detects

The Python script scans each log entry and identifies key security events:

* Unknown user login attempts
* Authentication failures
* Successful login sessions
* User logout sessions
* Network connections
* Kerberos authentication failures
* Program crashes or abnormal exits

## Example Output

```
Unknown user attempts → 117
Authentication failures → 491
Program crashes → 43
Network connections → 909
Kerberos failures → 23

Successful logins:
<*> by (uid=<*>) -> 122
<*> by login(uid=<*>) -> 1

Logouts:
<*> -> 123
```

## Key Security Observations

* Multiple authentication failures suggest possible brute-force attempts.
* Unknown user login attempts indicate attackers trying invalid usernames.
* Numerous network connections may represent normal activity but require monitoring.
* Kerberos authentication failures indicate authentication service errors.

## Learning Outcomes

Through this project, the following SOC skills were practiced:

* Log analysis
* Pattern detection
* Security event classification
* Python scripting for automation
* Basic incident investigation

## Future Improvements

* Extract attacker IP addresses
* Detect brute-force login attempts
* Create real-time alerting
* Visualize attack statistics
