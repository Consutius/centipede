In this game, you must solve a centipede. 
In other words, permute a list into correct order.

While the logic itself turned out to be very simple, the core idea behind it was to
recreate a thought experiment of mine. Imagine a centipede with an x amount of segments.
Each segment has one pair of legs - say we swapped the segments around now. To help the centipede
move again, we must put the segments back into correct order, also making sure that the legs remain
oriented correctly. Something something group theory, parity.

To solve it, you must input moves, those being very simple. 
All you have to do is input position (i) and direction (sign). Here's what an example solve 
would look like:

You must solve into: [1, 2, 3, 4]  
Your scrambled state is: [-2, 4, 3, -1]  
Input move: 4-  
Current state: [-2, 4, 1, -3]  
Input move: 2+  
Current state: [-2, -1, -4, -3]  
Input move: 3+  
Current state: [-2, -1, 3, 4]  
Input move: 2-  
Current state: [1, 2, 3, 4]  
Congratulations! You solved it in 4 moves!

I do realize that the sign flipping (what should've been parity) is a bit of a useless constraint
for now, but who are YOU to tell me I can't fix this later?

Thanks for reading. Have fun!
