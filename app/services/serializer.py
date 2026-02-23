from datetime import datetime, timezone


def build_payload(device_id, lane, counts):
    return {
        "schema_version": "1.0",
        "device_id": device_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "lane": lane,
        "counts": counts
    }