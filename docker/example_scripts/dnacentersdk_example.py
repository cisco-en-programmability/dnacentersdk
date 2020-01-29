"""Testing the use of dnacentersdk Python package."""
from dnacentersdk import DNACenterAPI
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable annoying HTTP warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

which_dnac = "devnet"
devnet = {
    "debug": False,
    "username": "devnetuser",
    "password": "Cisco123!",
    "base_url": "https://sandboxdnac2.cisco.com:443",
    "public_cert": False,
}
pov = {
    "debug": True,
    "username": "admin",
    "password": "C1sco12345",
    "base_url": "https://100.64.0.101:443",
    "public_cert": False,
}

if which_dnac == "devnet":
    api = DNACenterAPI(
        username=devnet["username"],
        password=devnet["password"],
        base_url=devnet["base_url"],
        verify=devnet["public_cert"],
        debug=devnet["debug"],
    )
elif which_dnac == "pov":
    api = DNACenterAPI(
        username=pov["username"],
        password=devnet["password"],
        base_url=devnet["base_url"],
        verify=devnet["public_cert"],
        debug=devnet["debug"],
    )
else:
    print("No DNA Center connection information provided.  Exiting.")
    exit(0)

results = {}

print(api.devices.get_device_list())  # Permissions issue

'''
results["workflows"] = api.pnp.get_workflows()
results["client_health"] = api.clients.get_overall_client_health()
results["sites"] = api.sites.get_site()
results["all_device_configs"] = api.devices.get_device_config_for_all_devices()
'''

print(results)
