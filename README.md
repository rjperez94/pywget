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

###How to run
CORE
import pywget from core
pywget (url="http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html")

Should download just index.html i.e. the exact page

NOTE: make sure that url is a web page NOT web directory, else MAY print
(depending on permissions):
print stack trace
print COMMAND ERROR. INVALID SYNTAX

Collision
If index.html exists then name as index.1.html and so on

====================

COMPLETION
import pywget from completion
pywget (url="http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html")

Should download index.html, felids.html, felines.html and GrumpyCat.jpg 
i.e. THIS page and ALL links and images on THIS page

NOTE: make sure that url is a web page NOT web directory, else MAY print
(depending on permissions):
print stack trace
print COMMAND ERROR. INVALID SYNTAX

Collision
If index.html exists then rename to index.1.html and so on
If GrumpyCat.jpg exists then name as GrumpyCat.1.jpg and so on

====================

CHALLENGE
import pywget from challenge
pywget (url="http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html", depth=2)

Should download index.html, felids.html, felines.html and GrumpyCat.jpg 
i.e. THIS page and ALL links and images on THIS page
It should follow file structure when downloaded

NOTES: 

1. make sure that url is a web page NOT web directory, else MAY print
(depending on permissions):
print stack trace
print COMMAND ERROR. INVALID SYNTAX

2. make sure dpeth is an integer (NOT string, decimal, float), else WILL print:
print stack trace
print COMMAND ERROR. INVALID SYNTAX

3. if depth specified is 0, print:
print COMMAND ERROR. Can't have [starting] depth of 0

4. if depth not specified, print:
TypeErr: pywget() missing one required positional argument depth

Collision
Look at the folder:
i.e. pywget (url="http://homepages.ecs.vuw.ac.nz/~ian/nwen241/index.html", depth=2)

if homepages.ecs.vuw.ac.nz NOT exist:
	make homepages.ecs.vuw.ac.nz folder
	put files in there, make sub-folders as necessary

homepages.ecs.vuw.ac.nz/
~ian/
nwen241/


if homepages.ecs.vuw.ac.nz exist
	RENAME to homepages.ecs.vuw.ac.nz.1 (and so on until available == .2, .3, .4)
	put files in there, make sub-folders as necessary

homepages.ecs.vuw.ac.nz.1/
~ian/
nwen241/
