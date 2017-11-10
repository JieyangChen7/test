from keystoneauth1 import loading
from keystoneauth1 import session
from keystoneauth1.identity import v2

from glanceclient import Client as gClient
from novaclient.client import Client as nClient


class BeeAWSLauncher(object):

    # Authentication
    auth = v2.Password(username = 'cjy7117',
                   password = 'Wait4aTrain7!',
                   tenant_name = 'CH-819321',
                   auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v2.0')
    
    self.session = session.Session(auth=auth)
    
    self.gclient = gClient('2', session=session)

    self.nclient = nClient('2', session=session) 
    
    
