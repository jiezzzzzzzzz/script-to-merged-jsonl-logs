This is a script for merging logs in format:

{"log_level": "INFO", "timestamp": "2021-11-13 13:02:27", "message": "Something text"}
{"log_level": "ERROR", "timestamp": "2021-11-13 13:02:27", "message": "Something text"}

It support .jsonl and .json formats and sort records by timestamp in ascending order.
This script is written in a pure python. You can just downloads and run it on your computer, if python is there.
Commandline to run from cmd: script.py <path_to_log_1> <path_to_log_2>...<path_to_log_n> -o <path_to_merged_log\name_file.json(l)>

