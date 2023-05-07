from django.shortcuts import render

# Create your views here.
def index(request):

   return render(request,'index.html')

def setsession(request):
    request.session['name']='Ram'                            # set the object in session 
    request.session['lastname']='Sharma'                   
   #  request.session.set_expiry(3600)                       # set the session expiry date and default session expire in 14 days
    return render(request,'setsession.html')
 
 
def getsession(request):
    name=request.session['name']
    lastname=request.session['lastname']
    lastname=request.session.get('lastname')                 # another way to get the session data using get session
    expire_date=request.session.get_expiry_date()            # get the expiry date of session
    expire_age=request.session.get_expiry_age()              # get the expiry age of session
    session_key = request.session.keys()                     # get the key from the session
    session_items=request.session.items()                    # get the items from the session
    session_keys=request.session.session_key                 # get the session key 
    modified_data=request.session.modified                   # return true when data is modified otherwise return the false
    get_exp_br=request.session.get_expiry_at_browser_close() # get the session expiry when browser is close    
    context={
       'name':name,
       'lastname':lastname,
       'expire_date':expire_date,
       'expire_age':expire_age,
       'session_key':session_key,
       'session_items':session_items,
       'session_keys':session_keys,
       'modified_data':modified_data,
       'get_exp_br':get_exp_br,
       
    }
    return render(request,'getsession.html',context)
 
def delsession(request):
   #   del request.session['name']                          # delete the single obj from the session like name
   #   del request.session['lastname']
   #   request.session.clear()                              # remove the all data from the current session
      request.session.flush()                               # remove the complete session 
   #   request.session.pop()                                # delete the key from the session and returns its value
     
      return render(request,'deletesession.html')
   
# session are used for store the user information at serverside.It is more secure as compared to cookies
# when user are do a http request session id is stored in a cookies or key on server by server and when client comes again so session id is send to the server and server match the server key and session id and return the data which is stored on server side.
# default sessions age is 14 days but we set as per requirement
# By default django stored the session data in data based table for that we need to add session middleware and django.contrib.sessions in settings.py file 
# we store the session on four way --> default database , cache ,file based and cookies