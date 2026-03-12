from config import Config
print(f"FACE_SAMPLES_COUNT: {Config.FACE_SAMPLES_COUNT}")
import os
print(f"ENV FACE_SAMPLES_COUNT: {os.environ.get('FACE_SAMPLES_COUNT')}")
