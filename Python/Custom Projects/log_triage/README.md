# Pi-hole Log Triage
Parse and summarize DNS log activity from a Pi-hole log file.

## Usage
```bash
python log_triage.py
Notes
Reads sample_pihole.log line by line.

Identifies two action types:

blocked → denied DNS requests.

query[A] → allowed DNS lookups.

Outputs:

summary.txt → totals parsed, skipped, allowed, blocked.

top_domains.txt → Top 5 requested domains and Top 5 sources.

Uses dictionaries to count occurrences, then sorts for the top N.

Skills Practiced
File I/O (with open, reading line by line).

String parsing and splitting.

Using dictionaries for counting.

Sorting dicts with lambda.

Writing summary reports to text files.
