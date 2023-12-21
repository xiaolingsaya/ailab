# ailab

# 231130
basicly it is the final project of my ailab class

bad news is that on the first day of pre i noticed that the robot might be hard to control by raspberry pi,since it runs on linux not windows

now today i am trying to learn how to manage my project on github.good luck to me.

# 231207
After setting up the environment I was devastated to find that the Raspberry PI could not bear this model (sketchkeras).

I found that path planning would be very difficult, so I needed to try to simplify the line draft.

First, use the method of inverse-Gaussian blur - color reduction to produce a preliminary line draft

according to the painting experience, if the degree of Gaussian blur is higher, it is possible to get a relatively simple line draft.

Finally, binarize for drawing. That's a preliminary thought for today.

# 231214
I found this pydobot thing and realiazed how to control dobot. tested basic movements.

created 2 styles of drawing,line or binary sketch. added trackbar to adjust ksize and shadow threshold value.

to draw, plan to do edge detection and save them as arrays. counters can be saved as single parts so I plan to lift up when changing parts and not to lift up arm when moving in a particular part.

when mate asked me how to fill those small gap between lines, I said just use a thicker marker. That is really useful,believe me!

# 231221
Unfortunately, I was informed last weekend that I have to spend a lot of time in a competition this week, so I may not have enough time to complete the project. Fortunately, I got back to school in time and came to class on time today. 

Today's main task is to make the machine manual, and today I and a classmate with a similar project got a slightly old robot hand. It has serious communication problems: sometimes it is not recognized at all, sometimes it is recognized but cannot communicate, sometimes it loses contact halfway through communication (which is a bug I often find at the end of the experiment), and even sometimes it blocks other devices (such as the mouse). 

The silver lining is that the path planning I ran with edge detection worked. In addition, I also understood the use of cv2.waitkey, and finally solved the problem of incorrect keyboard response. This is the result of today, and I will use the robot hand that broke the air pump to run the program, because its coordinate origin and direction will not jump at will. 

In addition, due to poor horizontal calibration, today's robot hand will roughly scratch the paper, even if the use of soft pen is no exception, there is a sense of intellectual crisis.
