---
name: consulting-metrics-updater
description: Refresh the practice metrics and dashboard. Use monthly, after a deal changes state, or "update the dashboard/metrics". Good scheduled-task candidate.
---

# Consulting Metrics Updater

## Steps
1. Compute KPIs from the pipeline + clients: win rate, avg deal size, sales-cycle length, MRR, conversations/week, testimonials captured.
2. Refresh `operating/dashboard.html` (funnel counts, client table, KPI tiles).
3. Append a dated snapshot to `business/metrics/`.
4. Flag anomalies (e.g. acceptance >80% = underpriced; cycle lengthening).

Source: Ch. 21.
