import urllib2, json

base_url = "HTTP LOCATION OF YOUR WEBSERVICE API"

class BetaUser(object):
    
    def __init__(self):
        """ Constructor """
        
        #Do setup here if needed

    def add_to_beta(self, email_address):
        beta_user = {}
        beta_user['email_address'] = email_address;        
        json_data = json.dumps(beta_user)
        
        request = RequestWithMethod("POST", "%s" % (base_url + "/beta/"))
        request.add_header('content-type', 'application/json')
        request.add_data(json_data)
        error = None
        response = None
        try:
            response = self.__send_request(request)
            
        except urllib2.HTTPError, err:
            pass
        else:
            print "No error received, do something here if needed"
                
        return (response, error)
        
    def __send_request(self, request):

        response = urllib2.urlopen(request)
        return response

# Subclass the urllib2.Request object and then override the HTTP method
class RequestWithMethod(urllib2.Request):

    def __init__(self, method, *args, **kwargs):
        self._method = method
        urllib2.Request.__init__(self, *args, **kwargs)
   
    def get_method(self):
        return self._method