# SentinelX Feature Extraction

The feature extraction subsystem converts network packets and
flows into structured numerical features for the ML detection
pipeline.

## Pipeline

```text
Raw Packet
    ↓
Packet Parser
    ↓
Flow Tracker
    ↓
Feature Extraction
    ↓
Feature Vector
    ↓
ML Model