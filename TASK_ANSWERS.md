# Assignment 4 – CO4: Task Answers and Design Notes

**Scope note:** The Python programs in this ZIP were executed locally. Cisco Packet Tracer is not installed in this execution environment, so no `.pkt` file, live switch output, crimped cable test, or Packet Tracer screenshot is claimed. Ready-to-enter configurations and topology diagrams are included. Open and test them in Packet Tracer before submission.

## Task 1 – Existing office and redesign

### 1.1 Complaints and weaknesses
- A single coaxial bus is a shared collision domain and a break/loose connector can interrupt the backbone for every attached station. Moving a desk can disturb the shared cable/terminator.
- A hub repeats every incoming bit to all ports; all users share the same half-duplex bandwidth and collisions/backoff reduce effective throughput. Month-end server transfers compete with all other traffic.
- If the home router is the only gateway, restarting or failing it removes the office's internet path. A router is not a substitute for a managed LAN switching design or a dedicated firewall.
- Further weaknesses: poor fault isolation, limited scalability, no VLAN/security segmentation, no redundant uplinks, coaxial cable handling/termination constraints, and a single point of failure at the hub/router.

### 1.2 Star redesign and bandwidth
Use managed access switches on each floor in an extended star, Cat6/Cat6A horizontal cabling to desks, fibre uplinks between floors/core, a server switch/10GbE server link, and a business router plus stateful firewall. Use UPS and redundant core/uplink where budget allows. Logical and physical diagrams are in `diagrams/`.

Assumptions for a transparent comparison: legacy bus is 10 Mbps shared by 30 users; switched star gives each desk a dedicated 1 Gbps full-duplex switch port, with a 10 Gbps server/core uplink. Ideal equal share on bus = 10/30 = **0.333 Mbps/user**. On the switched access link each user can negotiate **1,000 Mbps** to the switch; simultaneous server traffic is constrained by the shared 10 Gbps uplink (theoretical aggregate 10 Gbps, not 30 independent 1Gbps server paths). For Wi-Fi 6 comparison, assume 600 Mbps usable aggregate throughput on one AP: 600/30 = **20 Mbps/user** at equal sharing. Actual Wi-Fi throughput varies with channel width, signal, interference, client capability and airtime.

### 1.3 Defence (under 100 words)
Replacing the bus and hub with managed switches removes shared Ethernet collisions and isolates a desk/cable fault to that port. Structured Cat6/Cat6A cabling and labelled patch panels make desk moves predictable. Fibre between floors provides a high-capacity backbone. A business router and firewall replace the home router and add policy control; a redundant gateway/UPS can reduce internet downtime. The 10Gbps server uplink reduces the month-end bottleneck. Wi-Fi 6 improves mobility but one AP remains shared airtime, so it should complement—not replace—the wired server path.

## Task 2 – Hospital topology and costs

For five blocks, assume a fibre run is one link and each link uses two endpoint switch ports. Cost/link = ₹60,000 + 2×₹18,000 = **₹96,000**. The topology comparison uses the standard graph model: bus 4 segments, ring 5, star 4, full mesh 10 links. Port count is endpoint ports (2 per link); maximum device degree is shown by the code.

| Topology | Links | Endpoint ports | Fibre cost | Port cost | Total |
|---|---:|---:|---:|---:|---:|
| Bus (chain segments) | 4 | 8 | ₹2,40,000 | ₹1,44,000 | ₹3,84,000 |
| Ring | 5 | 10 | ₹3,00,000 | ₹1,80,000 | ₹4,80,000 |
| Star (DC centre) | 4 | 8 | ₹2,40,000 | ₹1,44,000 | ₹3,84,000 |
| Full mesh | 10 | 20 | ₹6,00,000 | ₹3,60,000 | ₹9,60,000 |

A single cut disconnects a branch in a bus/chain and disconnects a spoke block in a star. A ring survives any one link cut, but not arbitrary two cuts: two cuts partition the ring. Full mesh survives any one link cut and, for five nodes, any two link cuts while the graph remains connected (complete graph K5 has edge connectivity 4).

**Least-cost compliant hybrid:** retain the four-link DC-centred star and add one direct fibre link between Emergency and Operation Theatres. The DC–Emergency–Theatres triangle ensures each critical block still reaches the data centre if either of its two incident triangle links is cut; cuts on the Laboratory or Administration spoke do not isolate either critical block. Links=5, endpoint ports=10, fibre=₹3,00,000, ports=₹1,80,000, total **₹4,80,000**. This assumes the data centre is the patient-record server location and each link has independent physical routing; physically diverse paths are essential. See `Task02` output and diagram.

Ring alternative: 5 links, 10 ports, total ₹4,80,000; any one cut survives; two cuts can disconnect it. The hybrid is also ₹4,80,000 under the stated unit prices, but protects the two named critical blocks with a targeted triangle while leaving noncritical blocks on single spokes. The ring offers broader single-link resilience to all blocks.

## Task 3 – Cabling, devices and BOM

- Consulting rooms 35–80m: within 90m permanent-link limit.
- Pharmacy 96m: exceeds 90m permanent link; although under 100m channel maximum if patch cords fit within the remaining 4m, redesign to ≤90m permanent link or place a local switch. Cat6A does not itself extend the standard 100m copper channel.
- Waiting-hall APs 60m: within limit.
- Main building 420m: copper Ethernet exceeds 100m; use fibre. Single-mode is preferred for 420m backbone/headroom; multimode may also support the distance at suitable optics, but verify optic reach and bandwidth.
- T568A at one end and T568B at the other makes a crossover cable. Auto-MDIX on modern switches/NICs usually detects and compensates; consistent T568B straight-through patching is still the standard practice.

Device selection: managed Layer-2 access switches for endpoint connectivity and VLANs; Layer-3 core/distribution switches for inter-VLAN routing and redundant fibre; routers for WAN/ISP routing; firewalls for policy/NAT; APs for WLAN. Avoid hubs. With three VLANs per block, each VLAN is a separate broadcast domain; each switch port is a separate collision domain on switched full-duplex Ethernet. Exact domain totals depend on the final number of VLANs and switch ports.

Illustrative outpatient BOM (confirm actual endpoint count/site survey): 1×24-port managed PoE+ access switch (24 access ports; choose 48-port if endpoint/AP count exceeds 24), 1×Layer-3 distribution switch with 10G SFP+ uplinks, 1×firewall/router uplink, 3×Wi-Fi 6 PoE APs (initial planning allowance), 1×24-port patch panel, 1×rack with PDU/UPS, Cat6/Cat6A horizontal cable, fibre uplink, SFP/SFP+ optics, keystone jacks, faceplates, patch cords, cable managers and labels. Measure aggregate route length L and procure 1.10L cable for 10% spare. Do not invent a total cable length before a floor plan is supplied.

T568B pin order: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown.

420m alternative: one fibre run avoids powered intermediate equipment and is immune to electromagnetic interference/lightning-induced ground potential between buildings (use proper outdoor-rated/armoured fibre and grounding for metallic armour). Cat6A copper is limited to 100m channel, so a 420m route needs at least three segments and two intermediate active switches (or a different medium); these require power, cabinets, cooling and surge protection. Fibre is the recommended backbone.

## Task 4 – Multiple access, WLAN, WAN

Pure ALOHA maximum normalized throughput = 1/(2e) = **18.4%**; slotted ALOHA = 1/e = **36.8%**. For 10Mbps, these correspond to about 1.84Mbps and 3.68Mbps. CSMA/CD minimum frame bits = 2×one-way propagation delay×bit rate. The brief's propagation-speed text appears as “2 × 10 m/s”, missing an exponent; using the conventional assumed 2×10^8m/s gives one-way delay 12.5µs and minimum frame 250 bits = 31.25 bytes. Ethernet's 64-byte minimum exceeds this. Switched full-duplex links have dedicated transmit/receive paths and no collisions, so CSMA/CD is unnecessary. Wi-Fi is a shared radio channel and uses CSMA/CA.

For 300 phones, initial plan 6 APs at about 50 associated clients/AP, subject to airtime/capacity survey. In 2.4GHz use channels 1, 6 and 11 with a 1/6/11 reuse pattern; 5GHz use distinct non-overlapping channels permitted by local regulation and DFS rules. Wi-Fi 6 OFDMA schedules resource units to multiple clients; MU-MIMO serves multiple spatial streams; BSS colouring helps distinguish overlapping BSS traffic and improve spatial reuse. Bluetooth is suitable for low-rate peripherals and approved short-range medical sensors after safety/interference review, not as the hospital's primary high-throughput or mission-critical backbone.

ATM cell overhead = 5/53 = **9.43%**; payload efficiency = 48/53 = **90.57%**. For a 1500-byte Ethernet payload, 14-byte MAC header + 4-byte FCS = 18/1518 = **1.19%** (excluding preamble and inter-frame gap). Frame Relay uses DLCI, ATM uses VPI/VCI, MPLS uses labels to identify forwarding paths. For three clinics, an internet VPN is usually lower cost and flexible but performance depends on public internet; MPLS offers provider-managed QoS/SLA and predictable classes at a higher recurring cost. Prioritise video with DSCP/QoS only where provider supports end-to-end markings. Select MPLS if guaranteed delay/jitter and support justify the premium; otherwise dual-ISP IPsec VPN with QoS and failover is cost-effective.

## Task 5 – VLANs

The completed switch configuration is in `Task05/q5_vlan_configs.txt`. VLAN 10 Office = Fa0/1–12; VLAN 20 CCTV = Fa0/13–20; VLAN 30 Guest = Fa0/21–24; Gi0/1 trunk allows only 10,20,30. 802.1Q adds **4 bytes** to a tagged Ethernet frame. Router-on-a-stick subinterfaces provide gateways. The guest inbound ACL denies access to office and CCTV subnets and permits other destinations; add explicit firewall policy so “any” means internet only, not arbitrary internal networks. Before segmentation the flat LAN is one broadcast domain; after segmentation it is three. Inter-VLAN routing makes permitted traffic possible, but the ACL restricts guest access. Verify with `show vlan brief`, `show interfaces trunk`, and ping tests in Packet Tracer.

## Task 6 – Campus design challenge

Planning estimates and uplink calculations are in `Task06/q6_campus_plan.py`; these are explicit sizing assumptions, not measured campus demand. Use a redundant Layer-3 core pair, distribution switches in major buildings, access switches on each floor, dual fibre paths where possible, Wi-Fi 6/6E APs subject to local spectrum rules, and dual ISP edge routers/firewalls. Use a partial-mesh core and star access. Separate Staff, Student, Guest, CCTV, Server and Management VLANs; enforce ACL/firewall policy and central authentication. Use single-mode fibre campus backbone and Cat6A to endpoints/APs. Provide DHCP scopes, DNS, monitoring, NAC, UPS and configuration backups.

Address plan and example building demand are printed by the script. Uplink sizing must be validated against busy-hour measurements; estimated peak traffic divided by uplink capacity gives demand/capacity, while capacity divided by demand is the headroom multiple. The alternative collapsed core saves one device layer (distribution/core devices may be consolidated) but creates a larger failure domain: a single collapsed-core switch failure can disconnect all attached buildings, VLAN gateways and internet paths. For a ten-year campus, redundant core/distribution is preferred despite higher initial cost; quantify lifecycle cost against outage impact and support requirements.

## Evidence and limitations

Executed Python output is stored in `results/`. Logical topology illustrations are in `diagrams/`. Packet Tracer `.pkt` simulations, physical cable crimping, live pings, live ISP/VPN performance and real RF surveys require Cisco Packet Tracer/hardware and a campus floor plan; they are not fabricated in this package.
