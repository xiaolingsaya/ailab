#ailab
basicly it is the final project of my ailab class
bad news is that on the first day of pre i noticed that the robot might be hard to control by raspberry pi,since it runs on linux not windows
now today i am trying to learn how to manage my project on github.good luck to me.
# 231130

After setting up the environment I was devastated to find that the Raspberry PI could not bear this model (sketchkeras).
I found that path planning would be very difficult, so I needed to try to simplify the line draft.
First, use the method of inverse-Gaussian blur - color reduction to produce a preliminary line draft
according to the painting experience, if the degree of Gaussian blur is higher, it is possible to get a relatively simple line draft.
Finally, binarize for drawing. That's a preliminary thought for today.
# 231207

I found this pydobot thing and realiazed how to control dobot. tested basic movements.
created 2 styles of drawing,line or binary sketch. added trackbar to adjust ksize and shadow threshold value.
to draw, plan to do edge detection and save them as arrays. counters can be saved as single parts so I plan to lift up when changing parts and not to lift up arm when moving in a particular part.
when mate asked me how to fill those small gap between lines, I said just use a thicker marker. That is really useful,believe me!
# 231214
