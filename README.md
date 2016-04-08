# get-ieee-paper
downloads an IEEE Xplore paper over ssh by generating the url
`http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?arnumber=XXXXXXX`, where `XXXXXXX` is the article number

## Setup
* `localhost`: machine where the script is run
* `remotehost`: another machine that satisfies the following requirements
  * can access IEEE Xplore by subscription
  * has the `wget` utility
  * can be accessed from localhost via ssh keys via `ssh username@remotehost`
*  change the line
```
cmd = "ssh username@remotehost 'wget -q -O - \"%s\"' > %s.pdf" % (url, arnumber)
```
to be the appropriate ssh command for your setup

## Example
```
localhost$ python get-ieee-paper.py 7402836
Executing command
> ssh username@remotehost 'wget -q -O - "http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?arnumber=7402836"' > 7402836.pdf
```
At this point, the file 7402836.pdf will be on `localhost`.