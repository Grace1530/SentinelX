# SentinelX
## API Specification

## 1. API Overview

Base URL:

http://localhost:8000

API Prefix:

/api

---

# 2. Health

## GET /api/health

Returns the current backend status.

### Response

```json
{
  "status": "ok",
  "service": "SentinelX"
}are get/api a