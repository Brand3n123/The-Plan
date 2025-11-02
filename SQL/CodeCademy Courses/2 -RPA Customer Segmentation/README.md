# RPA Customer Segmentation (`rpa_segmentation_project_codecademy.sql`)

## Overview
Codecademy project: generate user lists for marketing segments from the `users` table. Queries focus on date filters, pattern matching, and simple completeness checks to target users for campaigns and tests.

---

## Challenge Instructions (from Codecademy)

**Scenario**

The marketing department of Reputable Product Agency (RPA) is looking to segment the company users by a number of different criteria.

In this context, a segment is a subset of users that meet different conditions. Segments are used to send marketing campaigns to users who meet specific criteria or to measure the performance of specific marketing campaigns.

Use SQL queries to generate user lists for the marketing department. The users dataset is imported into the workspace.
---

### Tasks

1) **Explore the dataset**

```sql
SELECT *
FROM users
LIMIT 20;
What are the column names?

Born in the ’80s

Find the email addresses and birthdays of users whose birthday is between 1980-01-01 and 1989-12-31.

Signed up prior to May 2017

Find the emails and creation date of users whose created_at date matches this condition.

A/B test: ‘bears’

Find the emails of the users who received the bears test.

Campaigns on site BBB

Campaign values: AAA-1, AAA-2, BBB-1, BBB-2.
Find the emails of all users who received a campaign on website BBB.

Ad copy 2

Find the emails of all users who received ad copy 2 in their campaign.

Received both a campaign and a test

Find the emails for all users who received both a campaign and a test.
(Users will have non-empty entries in the campaign and test columns.)

How to run
Use your course console or SQLite:

bash
Copy code
sqlite3 rpa.db < sql/rpa_segmentation_project_codecademy.sql.sql