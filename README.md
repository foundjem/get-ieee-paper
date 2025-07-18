# get-ieee-paper
This script obtains an IEEE Xplore paper by piping a `wget` download through a remote host that has subscription access. The script calls the url `http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?arnumber=XXXXXXX` from the remote host, where `XXXXXXX` is the article number, and pipes the .pdf download to the local host.

## Setup
* `localhost`: machine where the script is run
* `remotehost`: another machine that satisfies the following requirements:
  * can access IEEE Xplore by subscription
  * has the `wget` utility
  * can be accessed from localhost with ssh keys by `ssh username@remotehost`
*  change the line
```
cmd = "ssh username@remotehost 'wget -q -O - \"%s\"' > %s.pdf" % (url, arnumber)
```
to be the appropriate ssh command for your setup.

## Example
```
localhost$ python get-ieee-paper.py 7402836
Executing command
> ssh username@remotehost 'wget -q -O - "http://ieeexplore.ieee.org/stampPDF/getPDF.jsp?arnumber=7402836"' > 7402836.pdf
```
At this point, the file 7402836.pdf is in the current directory on `localhost`.

## Academic Website
A basic Flask website is provided in the `academic_site` directory. It contains
simple pages for a home page, an about page and a publications list.

### Running the site
Install Flask and run the application:

```bash
pip install flask
python academic_site/app.py
```

Visit `http://localhost:5000` in your web browser to see the site.
