# Pi Lapse

Pi Lapse is a simple Python Script for the Raspberry Pi that takes photos at regular intervals.

### Changing Camera
Pi Lapse currently uses the [Raspberry Pi Camera Module](http://www.raspberrypi.org/help/camera-module-setup/) but can be changed to run any USB webcam. If you want to us a USB camera I would recommend installing `fswebcam` on your Pi and changing the line:

```python
subprocess.call("raspistill -w %d -h %d -e jpg -q 15 -o %s" % (image_width, image_height, filename), shell = True)
```
... with ...

```python
subprocess.call("fswebcam -r %dx%d %s" % (image_width, image_height, filename), shell = True)
```
