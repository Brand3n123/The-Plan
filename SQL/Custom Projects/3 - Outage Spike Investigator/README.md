Outage Spike Investigator

Overview
In this project, SQL was used to investigate a 15-minute service outage window recorded in the events table of the sql_log_analyzer.db database.
The goal was to isolate when failures peaked, which devices were impacted, and what error types caused the disruption.

Instructions

View recent events and confirm available timestamps.

Identify which minute within the outage window had the highest number of failed events.

Count how many times each device failed between 2025-10-22T13:15:00Z and 2025-10-22T13:30:00Z.

Use a CASE statement to group error_code values into categories:

E_AUTH → Provisioning Failure

E_TIMEOUT → Network Failure

NULL → Healthy

Else → Other

# From the project root:
sqlite3 db/sql_log_analyzer.db < queries/outage_spike_investigator.sql

# Or open an interactive session:
sqlite3 db/sql_log_analyzer.db
.read queries/outage_spike_investigator.sql