from flask import Flask, render_template, request, redirect, session
from linkedin import linkedin
import json


app = Flask(__name__)
app.secret_key = 'linkedindemoapp'

@app.route("/")
def get_profile(): 
  if 'token'in session:
    application = linkedin.LinkedInApplication(token=session['token'])
    profile_json  = application.get_profile()
    f_name = profile_json['firstName'] if profile_json['firstName'] else None
    l_name = profile_json['lastName'] if profile_json['lastName'] else None
    headline  = profile_json['headline'] if profile_json['headline'] else None
    url = profile_json['siteStandardProfileRequest']['url'] if profile_json['siteStandardProfileRequest']['url'] else None
    return render_template('profile.html',first_name=f_name, last_name=l_name, job_role=headline, profile_link=url)	  
  else:
    session['API_KEY']='77in7ezn6gf21x'
    session['API_SECRET']='rDnTVDUOmvI2ebmj'
    session['RETURN_URL']='http://localhost:8080/auth'
    authentication = linkedin.LinkedInAuthentication(session['API_KEY'], session['API_SECRET'], session['RETURN_URL'])
    auth_url = authentication.authorization_url
    authenticated = True		
    return render_template('index.html',link=auth_url)

@app.route("/auth")
def auth():
  code = request.args.get('code')
  authentication = linkedin.LinkedInAuthentication(session['API_KEY'], session['API_SECRET'], session['RETURN_URL'])
  authentication.authorization_code = code
  session['token'] = authentication.get_access_token()
  return redirect('/')
  	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
