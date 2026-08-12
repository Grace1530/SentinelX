# SentinelX Packet Capture

The packet capture subsystem is responsible for collecting
authorized network traffic and converting raw packets into
structured SentinelX data.

## Pipeline

```text
Network Interface
       ↓
Scapy
       ↓
Raw Packet
       ↓
Packet Parser
       ↓
Flow Tracker
       ↓
Packet Store
       ↓
Feature Extraction