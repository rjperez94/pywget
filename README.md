# pywget
A very basic Python implementation of the GNU Wget utility

## Core Version

The aim of this script is to implement the core functionality of the “pywget” function allowing a specified file to be downloaded locally.

For example:

`pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html ")`

or

`pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/images/GrumpyCat.jpg ")`

Will cause the following to happen:

1. The specified file is be downloaded to the current directory.
2. Downloaded files have the same name as specified in their URL.
3. Collisions are handled by inserting .x before the file’s extension. For example, running
the program three times to download GrumpyCat.jpg will result in three copies GrumpyCat.jpg, GrumpyCat.1.jpg and GrumpyCat.2.jpg.

##Completion Version

The aim of this part is to extend “pywget” to allow a specified html page (“root”) and its components (both html and images) to the current directory. All absolute links in the html page will be rewritten to local links pointing the downloaded components.

For example:

`pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html ")`

Will cause the following to happen:

1. The specified html file is downloaded to the current directory.
2. Each <strong>local</strong> link within the root html file, links and images, is followed and the referenced component is also downloaded to the current directory.
3. Each absolute link, referring to a downloaded component, within the root html file is rewritten to a local link. Other absolute links are left unmodified.

It copes with collisions to prevent overwriting files with the same name and when links are rewritten, it takes account of any adjustments to filenames done to prevent collisions.

##Challenge Version

The completion version of “pywget” stops at after it has downloaded the components referenced by the root html page. A recursive version would continue by following the links within every html page referenced. To deal with potential cycles, a common approach is to limit the number of times that a link can be followed. For example, the following tells “pywget”
to only follow links to a depth of 2:

`pywget(url=" http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html ", depth = 2)`

A considerable change to this version from the Completion version is that it follows the structure encoded in each URL.
