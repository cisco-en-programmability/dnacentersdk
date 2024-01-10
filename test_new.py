from dnacentersdk import api

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password, with DNA Center API version 2.3.5.3.
# and requests to verify the server's TLS certificate with verify=True.
dnac = api.DNACenterAPI(username="devnetuser",
                        password="Cisco123!",
                        base_url="https://sandboxdnac.cisco.com:443",
                        version='2.3.5.3',
                        verify=True)

# Find all devices that have 'Switches and Hubs' in their family
devices = dnac.devices.get_device_list(family='Switches and Hubs')

# Print all of demo devices
for device in devices.response:
    print('{:20s}{}'.format(device.hostname, device.upTime))

# Find all tags
all_tags = dnac.tag.get_tag(sort_by='name', order='des')
demo_tags = [tag for tag in all_tags.response if 'Demo' in tag.name ]

print(all_tags)