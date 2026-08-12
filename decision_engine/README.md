# SentinelX Decision Engine

The decision engine converts detection results into security
actions.

## Pipeline

```text
ML Prediction
      ↓
Confidence
      ↓
Severity
      ↓
Risk Score
      ↓
Response Policy
      ↓
MONITOR / ALERT / BLOCK