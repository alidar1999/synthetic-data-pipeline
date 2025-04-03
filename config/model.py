# 🌀 Decide for RPI Mode
RPI_PICO = False

MAX_RETRIES = 3

# Rate limiting settings
BASE_DELAY = 5  # Base delay between API calls in seconds
JITTER = 2      # Random jitter to add to delay (up to this many seconds)
MAX_REQUESTS_PER_MINUTE = 15  # Maximum requests per minute to avoid rate limiting

# You can inject API keys externally or load from config
API_KEYS = [
    "AIzaSyAQYwaLNflso2um_6k_hYHKgSXrKrLFauI",  # Key 1 - 4@gmail.com
    "AIzaSyBn84OtO0Y5prxrN-dWFe2_XG_IbFo4Z_Q",  # Key 2 - 6@gmail.com
    "AIzaSyAxKRgTsiVhRbY0oKCMfhUWCL3AipdemLo"   # Key 3 - 007@gmail.com
    # Add more as needed
]

BASE_DIR = f"D:/Personal/SDU/LLM - Thesis/Progress/Week 12/Data Pipeline/Phase 2/"