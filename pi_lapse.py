import subprocess
from datetime import datetime, timedelta
frame_counter = 1

# Time in seconds
# 1 Hour = 3600
# 1 Day  = 86400

# Time between each photo (seconds)
time_between_frames = 60

# Duration of Time Lapse (seconds)
duration = 86400

# Image Dimensions (pixels)
image_width = 1296
image_height = 972

total_frames = duration / time_between_frames

def capture_image():
    t = datetime.now()
    filename = "capture_%04d-%02d-%02d_%02d-%02d-%02d.jpg" % (t.year, t.month, t.day, t.hour, t.minute, t.second)
    subprocess.call("raspistill -w %d -h %d -e jpg -q 15 -o %s" % (image_width, image_height, filename), shell = True)
    print("Captured Image %d of %d, named: %s" % (frame_counter, total_frames, filename))

last_capture = datetime.now()

print("========== PiLapse Started ==========")
print("A photo will be taken every %d seconds for the next %d seconds." % (time_between_frames, duration))

while frame_counter < total_frames:
    if last_capture < (datetime.now() - timedelta(seconds = time_between_frames)):
        last_capture = datetime.now()
        capture_image()
        frame_counter += 1
