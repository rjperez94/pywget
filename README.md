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
2. Each link within the root html file ( '<a href>' and '<img>' ) is followed and the referenced component is also downloaded to the current directory.
3. Each absolute link (referring to a downloaded component) within the root html file is rewritten to a local link. Other absolute links are left unmodified.

It copes with collisions to prevent overwriting files with the same name and when links are rewritten, it takes account of any adjustments to filenames done to prevent collisions.
