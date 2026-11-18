"""Task 6: transparent sizing assumptions and campus uplink calculations."""
# Planning estimates, not measured demand. Replace with survey counts before procurement.
buildings={
 'Academic': {'users':1200,'devices':1500,'peak_mbps':3000},
 'Laboratories': {'users':600,'devices':650,'peak_mbps':2400},
 'Library': {'users':500,'devices':650,'peak_mbps':1000},
 'Hostels': {'users':3000,'devices':3600,'peak_mbps':4500},
 'Auditorium': {'users':800,'devices':850,'peak_mbps':1200},
 'Data Centre': {'users':100,'devices':250,'peak_mbps':5000},
}
for name,d in buildings.items(): print(f"{name}: users~{d['users']}, devices~{d['devices']}, estimated peak {d['peak_mbps']} Mbps")
print('Assumed uplinks: access-to-distribution 10 Gbps; distribution-to-core 40 Gbps; core-to-DC 2x100 Gbps; internet 2x10 Gbps.')
for name,d in buildings.items():
    cap=10_000 if name in ('Academic','Laboratories','Library','Hostels','Auditorium') else 40_000
    print(f"{name}: peak/uplink={d['peak_mbps']/cap:.2f}x demand ratio; uplink-to-demand oversubscription={d['peak_mbps']/cap:.2f}:1 (capacity/demand={cap/d['peak_mbps']:.2f}x)")
print('Address plan: 10.10.0.0/16; staff VLAN10 10.10.10.0/23; student VLAN20 10.10.20.0/20; guest VLAN30 10.10.40.0/21; CCTV VLAN40 10.10.50.0/23; servers VLAN50 10.10.60.0/24; network management VLAN99 10.10.99.0/24.')
print('Collapsed-core risk: one core switch failure can isolate all distribution blocks and both ISP paths; redundant dual-core avoids this single point of failure.')
