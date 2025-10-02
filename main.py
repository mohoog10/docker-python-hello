import os, sys
from datetime import datetime, timezone

name = os.getenv("YOUR_NAME", "friend")
print(f"Hello, {name}! 👋")

# Use timezone-aware UTC (no deprecation warning)
now_utc = datetime.now(timezone.utc).isoformat()
print(f"Python {sys.version.split()[0]} • {now_utc}")
print("Have a great day! 🌞")