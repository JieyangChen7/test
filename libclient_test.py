from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider

import libcloud.security
libcloud.security.VERIFY_SSL_CERT = True

Openstack = get_driver(Provider.OPENSTACK)

driver = Openstack('cjy7117', 'Wait4aTrain7!',
                   ex_force_auth_url='https://chi.tacc.chameleoncloud.org:5000/v2.0/tokens/',
                   ex_force_auth_version='2.0_password',
                   ex_tenant_name = "CH-819321",
                   ex_force_service_name='nova',
                   ex_force_service_region = "regionOne")

images = driver.list_images()
for image in images:
    print(image)

sizes = driver.list_sizes()
for size in sizes:
    print(size)

keys = driver.list_key_pairs()
for key in keys:
    print(key)


priv_key = driver.create_key_pair('bee_test_key')

print(priv_key.private_key)




driver.create_node()







driver.delete_key_pair(priv_key)

keys = driver.list_key_pairs()
for key in keys:
    print(key)
