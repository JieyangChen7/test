from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient.client import Client

from keystoneauth1.identity import v2


#loader = loading.get_plugin_loader('password')
#auth = loader.load_from_options(auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v2.0',
#                                username = 'cjy7117',
#                                password = 'Wait4aTrain7!',
#                                project_id = '3e35a9401df74141b2e909ef1f28aef7')


auth = v2.Password(username = 'cjy7117',
                   password = 'Wait4aTrain7!',
                   tenant_name = 'CH-819321',
                   auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v2.0')


sess = session.Session(auth=auth)
nova = Client('2', session=sess)

nova.servers.list()
nova.flavors.list()
