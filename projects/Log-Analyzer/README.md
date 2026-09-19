# Log Analyzer

A Python log analyzer that I built to learn about log parsing, authentication events, failed login detection, and basic security monitoring.

# Purpose

I made this project to understand how security logs can be processed programmatically to separate suspicious activity.

The personal goal for this project was to learn how to work with structured log files and build detection logic myself.

# What I'm Learning

Through this project, I've learnt:

- Python file handling
- CSS parsing
- Dictionaries and data structures
- Authentication logs
- Failed login detection
- IP address tracking
- Basic security monitoring
- Detection logic
- Error handling

# How It Works

The analyzer reads a log file containing entries in the following format:

DATE/TIME/DATETIME,IP,USER,STATUS

For example:

- 10:30,192.168.1.10,admin,success
- 10:31,192.168.1.25,admin,failed
- 10:32,192.168.1.25,admin,failed
- 10:33,192.168.1.25,admin,failed

The program:

1. Reads the log file.
2. Removes empty lines.
3. Splits each log entry into its individual fields.
4. Checks that the entry contains the expected format.
5. Identifies failed login attempts.
6. Counts failed attempts for ip addresses that have triggered a failed log-in.
7. Flags IP addresses that have exceeded the threshold failure value I provided.

# Example

Input:

- 10:30,192.168.1.10,admin,success
- 10:31,192.168.1.25,admin,failed
- 10:32,192.168.1.25,admin,failed
- 10:33,192.168.1.25,admin,failed
- 10:34,192.168.1.25,admin,failed
- 10:35,192.168.1.25,admin,failed

Output:

192.168.1.25 is suspicious with 5+ failed attempts

# Detection Logic

The current version counts failed login attempts based on the source IP address.

For example:

192.168.1.25 -> 5 failed attempts

If an IP reaches the threshold, it is added to the list of suspicious IPs.

This is a basic detection mechanism and does not simply mean the IP is malicious, it just means the IP needs to be investigated further.

# Comp Tech Used

- Python
- CSV/structured log files
- File handling
- Dictionaries
- Git & GitHub

Status:

Early development

The current version is intentionally simple.

# Future plans

- Better log validation
- More detailed reports
- Exporting results to CSV
- Configurable detection thresholds
- Multiple detection rules
- Improved error handling

# Ethical Use

This project is intended for educational and defensive purposes.

The sample logs used with this project are locally generated or authorized data. The analyzer should only be used on logs that you are authorized to access and analyze.
