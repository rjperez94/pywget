# pywget
A very basic Python implementation of the GNU Wget utility

Core Version
The aim of this part is to implement the core functionality of the “pywget” function allowing a
specified file to be downloaded locally. 
For example:

pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html ")

or

pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumpyCat.jpg ")

Will cause the following to happen:

1. The specified file is be downloaded to the current directory.
2. Downloaded files have the same name as specified in their URL.
3. Collisions are handled by inserting .x before the file’s extension. For example, running
the program three times to download GrumpyCat.jpg will result in three copies GrumpyCat.jpg, GrumpyCat.1.jpg and GrumpyCat.2.jpg.
