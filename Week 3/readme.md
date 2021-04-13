# OpenCV
OpenCV is a library of programming functions typically used in image and video processing. We will be utilizing this library to create an "invisibilty cloak" program.

## Steps
1. Taking a picture of the background
2. The "invisibilty cloak" is detected based on a distinct color (in this case red)
3. The cloak is covered with a "mask" which consists of the background
4. The final output is created

## Details
The background of the image is captured using a loop and stored for future use. 

Now we start capturing continous frames in a loop. For each frame, the BGR colors are converted to their corresponding HSV(Hue, Saturation, Value/intensity) values which allows us to detecting dinstinct colors much simpler. 

We create two masks, the first corresponding to the red color in the hue range (0,30) degrees and the second one in the hue range(330-360) degrees. Both of the masks are combined and morphed to produce a single mask with reduced noise.

Now, the detected cloak is masked by an image from the background, creating an effect which looks the person in the video has disappeared. Hence the "invisibility cloak".

The output stops when the escape key is pressed and the video is saved to a local storage device. 

## Morphology transformations used:
1. Dilate : A pixel remains bright if atleast one pixel under the kernel is also bright. Hence, the white region of the foreground is increased.

2. Opening: Opening is just erosion(eroding the boundaries of the foreground object) followed by dilation.

## Sources
https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html
