# Packet Tracer build and verification checklist

## Task 2 – Hospital partial mesh
Create five 2960/3560 switches named DC, Emergency, OT, Laboratory, Administration. Connect DC to all four blocks and add Emergency–OT fibre. Configure routed or VLAN-based test subnets, then ping the patient-record server from Emergency and OT. Shut down one of the three triangle links at a time; Emergency and OT should retain a path to DC. Save as `Task02/Hospital_Hybrid.pkt`.

## Task 5 – VLAN isolation
Enter `Task05/q5_vlan_configs.txt` on the access switch and configure the matching trunk/core/router. Attach office, CCTV and guest PCs to the corresponding ports. Verify `show vlan brief` and `show interfaces trunk`. Confirm guest cannot ping Office/CCTV but can reach a simulated internet server after routing/NAT/firewall policy. Save as `Task05/Admin_VLANs.pkt`.

## Task 6 – Reduced campus
Build a redundant core pair, two building distribution/access switches, VLANs, router/firewall and two ISP/cloud links. Verify inter-building reachability within allowed VLAN policy, guest isolation, dual-ISP reachability and survival after shutting one core link. Save as `Task06/Campus_Reduced.pkt`.

Do not mark these checks complete until you have run them in Packet Tracer and captured your own screenshots/outputs.
