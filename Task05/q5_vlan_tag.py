"""Task 5: 802.1Q tag overhead and VLAN/broadcast-domain model."""
print('802.1Q tag added to Ethernet frame: 4 bytes (TPID 2 + TCI 2).')
print('Before segmentation: 1 shared Layer-2 broadcast domain (assumed flat VLAN).')
print('After segmentation: 3 broadcast domains: VLAN 10 Office, VLAN 20 CCTV, VLAN 30 Guest.')
print('Access ports are in one VLAN each; trunk carries tagged VLANs 10,20,30.')
print('Guest ACL blocks VLAN10 and VLAN20 destinations and permits other routed destinations; apply upstream internet policy/NAT as appropriate.')
