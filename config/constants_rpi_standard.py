# config/constants.py
# 🌀 Code Style Variations
CODE_STYLES = [
    "functional"
]

# 📊 Complexity Tiers
COMPLEXITY_LEVELS = ["beginner", "intermediate", "advanced"]

# 🍓 Raspberry Pi Model Targets
PI_MODELS = [
    "Raspberry Pi 4 Model B",
    "Raspberry Pi 3 Model B+",
    "Raspberry Pi Zero W",
    "Raspberry Pi 5"
]

# 🔗 Integration Types
INTEGRATION_PATTERNS = [
    "standalone", 
    "with multiple sensors",
    "in distributed system"
]

# 🌎 Real-World Application Contexts
USE_CONTEXTS = [
    "educational setting", "hobbyist project", "professional monitoring system",
    "research application", "industrial automation", "smart agriculture",
    "robotics project", "wearable technology", "interactive art installation",
    "assistive technology", "environmental science", "home automation"
]

# ✅ Phase Progression Order (Pipeline Flow)
PROGRESSION_ORDER = [
    "sensor_reading",
    "actuators",
    "sensor_actuator_combo",
    "file_logging",
    "interrupt_driven",
    "camera_applications",
    "networking"
]

# 📦 Phase Categories and Subcategories
CATEGORIES = {
    # 🌱 Phase 1: Basic Sensor Input (Expanded)
    "sensor_reading": [
        "temperature sensor", "humidity sensor", "pressure sensor", "light sensor",
        "ultrasonic sensor", "PIR sensor", "soil moisture sensor", "IR sensor",
        "sound sensor", "vibration sensor", "gas sensor", "touch sensor",
        "hall effect sensor", "rain sensor", "water flow sensor", "tilt sensor",
        "flame sensor", "color sensor", "capacitive touch sensor",
        "weight/load cell sensor", "motion sensor", "alcohol sensor",
        "gyroscope sensor", "accelerometer", "magnetometer", "time of flight sensor"
    ],

    # ⚙️ Actuator Options (standalone)
    "actuators": [
        "servo motor", "DC motor", "stepper motor", "relay", "solenoid",
        "LED", "buzzer", "speaker", "vibration motor", "fan", "LCD display",
        "OLED screen", "RGB LED", "relay-controlled lamp", "heater", "cooling fan",
        "valve actuator", "electromagnetic lock"
    ],

    # ⚡ Phase 2: Sensor-Actuator Integration (Expanded)
    "sensor_actuator_combo": [
        "temperature sensor controlling a cooling fan",
        "humidity sensor triggering a dehumidifier",
        "PIR motion sensor activating a light or buzzer",
        "ultrasonic sensor controlling servo for parking assist",
        "soil moisture sensor turning on a water pump",
        "gas sensor activating a ventilation fan",
        "IR sensor triggering a relay to open a door",
        "sound sensor activating an alarm",
        "light sensor adjusting brightness of an LED strip",
        "load cell sensor triggering a locking mechanism",
        "time of flight sensor controlling a gate",
        "rain sensor closing a motorized window",
        "flame sensor activating buzzer and LED",
        "capacitive touch sensor toggling a relay"
    ],

    # 💾 Phase 3: File and Data Logging (Expanded)
    "file_logging": [
        "log temperature readings to a CSV file",
        "log motion detection timestamps to a text file",
        "log gas sensor values with timestamps",
        "write ultrasonic distance readings to a file every second",
        "create daily sensor log files for multiple sensors",
        "log light and sound levels with date/time",
        "store sensor threshold breaches to a log file",
        "save sensor calibration values to file",
        "record ADC readings from multiple channels into CSV",
        "read configuration threshold values from a JSON file"
    ],

    # 🚨 Phase 4: Interrupts and Real-Time Logic (Expanded)
    "interrupt_driven": [
        "motion sensor using GPIO interrupt to turn on light",
        "button interrupt to start or stop data logging",
        "vibration sensor triggering a shutdown routine",
        "PIR sensor GPIO interrupt activating buzzer",
        "external interrupt from a tilt switch",
        "IR receiver decoding input via interrupt",
        "hardware timer interrupt for consistent sampling",
        "Hall effect sensor rotation counting with interrupt",
        "ultrasonic trigger using echo pin interrupt"
    ],

    # 📷 Phase 5: Camera and Image Applications (Expanded)
    "camera_applications": [
        "USB camera capturing image every 10 seconds",
        "CSI camera capturing grayscale image and saving",
        "detect object presence and capture image",
        "apply blur filter to image captured via camera",
        "stream camera feed and log frame timestamps",
        "time-lapse photography using CSI camera",
        "save motion-triggered snapshots from camera",
        "capture image and resize to 320x240 before saving",
        "capture and convert image to black and white",
        "camera capture with filename based on timestamp"
    ],

    # 📤 Phase 6: Simple Communication and Networking (Expanded)
    "networking": [
        "send temperature sensor data over UDP",
        "receive command over TCP to activate actuator",
        "post humidity readings to a web server using HTTP",
        "subscribe to MQTT topic to get control signals",
        "send camera image snapshot to server via POST",
        "receive configuration from HTTP API",
        "stream video frames over MJPEG using TCP socket",
        "broadcast light levels over UDP multicast",
        "fetch thresholds for sensors from a cloud endpoint",
        "stream live sensor data over local web server"
    ]
}

# Create weighted distribution to favor interesting categories
PHASE_WEIGHTS = {
    "sensor_reading": 0.25,
    "actuators": 0.15,
    "sensor_actuator_combo": 0.2,
    "file_logging": 0.05,
    "interrupt_driven": 0.10,
    "camera_applications": 0.15,
    "networking": 0.10
}