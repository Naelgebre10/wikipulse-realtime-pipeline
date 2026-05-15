# WikiPulse Technical Report

## Overview

WikiPulse is a real-time streaming pipeline that processes live Wikipedia edit events from Wikimedia EventStreams.

The system is designed to identify emerging global trends and breaking events using streaming analytics.

---

# Architecture

The architecture contains:

1. Data ingestion layer
2. Stream processing layer
3. MongoDB storage layer
4. Analytics layer

The ingestion service continuously receives events from Wikimedia streams.

The processing layer cleans, validates, and transforms the data before storing it in MongoDB.

---

# Design Decisions

## MongoDB

MongoDB was selected because:
- it supports flexible schemas
- it handles high write throughput
- it works well with JSON event data

## Event-Based Storage

Each event is stored as a separate document.

Benefits:
- simple ingestion
- easier scaling
- faster writes

---

# Scalability

The system supports scalability through:
- decoupled architecture
- asynchronous event streaming
- independent processing services

---

# Challenges

## Duplicate Events

Duplicate events may occur during streaming.

Solution:
Event IDs are used for deduplication.

## Bot Noise

Wikipedia contains many automated edits.

Solution:
Bot flags are stored for filtering and analysis.

---

# Conclusion

WikiPulse demonstrates a scalable real-time data engineering pipeline capable of processing and analyzing live Wikipedia edit streams.