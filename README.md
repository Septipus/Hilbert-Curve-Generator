# Hilbert-Curve-Generator
Basic implementation of Hilbert Curve mapping for a given depth that avoids using the standard turtle/rigid implementations

I was inspired to find this solution by watching the 3Blue1Brown video [Hilbert's Curve: Is infinite math useful?](https://www.youtube.com/watch?v=3s7h2MHQtxc), which is just absolutely beautiful. Infact,I highly recommend you check out all his work, it never fails to inspire me.

More info on Hilbert Curves in specific & Space Filling curves generally can be found [here](https://en.wikipedia.org/wiki/Hilbert_curve) and [here](https://en.wikipedia.org/wiki/Space-filling_curve).

<p align="center">
  <img src="https://github.com/SubstanceIsFormAndContent/Hilbert-Curve-Generator/blob/master/Testing/images/HilbertCurve_Depth%3D8.svg" alt="Whoa, Now thats a curve." width="500"/>
</p>

### Solution Notes
What I do love about this solution is:
1. The simplicity of teh recursive component. It is itterating over a list of solutions while keeping the orderig pattern of the next recursion intact.
2. The Use of teh recurrence matrix allows for some very interesting results. This is one of them, I recommend you try one out. possibly make a Peano Curve.
3. delegating ploting to the end & applying independent traces (in the .ipynb notebook) allows for some cool drawing effects, for example playing with teh curve colors, and their transparency

### TODO
This is a re-hash of an old solution I did, when I first watched the video, that I have unfortunately since lost. There was a few extra functionalities that are not in this bare-bone version. 
The reason they are not here is because while it can produce hilbert curves, it's main intention was to explore pseudo-Space Filling Curves, Basically by introducing a few functions.
They were:
1. Allowing for 'None' indexing in the recurrence matrix. (basically allowing for specific recursions to be excluded from the next recursion layer). This was inspired by the process of creating the ['Cantor Dust'](http://mathworld.wolfram.com/CantorDust.html) Fractal
2. Implementing a 'Re-Order' opperation before every next recurrence operation. This was a reminant of the first implementation, before I discovered that it could be accomodated in the index reordering of the recurrence matrix. However, playing with it after-the-fact proved to provide some super interesting results, so it stayed.
3. From my work on Cellular Automata, I was inspired by this model to generate CA Rules for any specific order and Input Alphabet, what is beautiful here is that the generated pseudo-Space Filling Curves acted as a network graph through the CA Rules. Thats super cool for a few reasons that i'll address in my CA repository(ies).

So, I will leave this implementation as tidy as it is simply for the sheer beauty of the Hilbert Curve, and I will create a new repository for teh generalized form shown above.

On that note however, see the image below as an example of what the generalized form of this algorithm can produce. It is a network mapping of 123098 nodes all connected in a directed graph built as instruced by the generated output mapping of the generalized algorithm. [This is the fully zoomable image.](https://github.com/SubstanceIsFormAndContent/Hilbert-Curve-Generator/blob/master/Testing/images/Mangled_123098_nodes.png)

Enjoy. :)

<p align="center">
  <img src="https://github.com/SubstanceIsFormAndContent/Hilbert-Curve-Generator/blob/master/Testing/images/Mangled_123098_nodes.png" alt="Some serious Pseudo-Space Filling going on here..." width="500"/>
</p>
