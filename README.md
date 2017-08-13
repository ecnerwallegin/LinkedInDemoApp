# LinkedInDemoApp

This is a basic application to help learn more about use of docker to build a python based web application using [flask](http://flask.pocoo.org) to retrieve information from LinkedIn (special reference to the useful LinkedIn python libray [python-linkedin](http://ozgur.github.io/python-linkedin/) which made this quite easy).

Prior to using it would propbaly be best to review the Docker getting started guide - check out (https://docs.docker.com/get-started/)[https://docs.docker.com/get-started/] if you haven't already done so.

To use the following guidance should help you:

1. Fetch code to a working directory

1. Within the working directory build your conatainer - something like <code>docker build -t linkedin_app .</code> should work

1. Having build the container it can simply be run using <code>docker run -p 8080:80 linkedin_app</code>. This will mean that the application is accessible on port 8080. You can access via a browser at <code>http://localhost:8080</code>

NB. It goes without saying that you'll need to authenticate with LinkedIn in orde to use the app so you'll need an account there.
