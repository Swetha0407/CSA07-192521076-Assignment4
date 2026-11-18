"""Task 1: compare shared bus, switched star and Wi-Fi 6 capacity."""
users=30
bus_mbps=10.0
switched_port_mbps=1000.0
star_uplink_mbps=10000.0
wifi6_aggregate_mbps=600.0  # assumed usable shared throughput, not PHY rate
print(f"Users: {users}")
print(f"Legacy 10 Mbps shared bus: {bus_mbps/users:.3f} Mbps/user (ideal equal share)")
print(f"Switched star: {switched_port_mbps:.0f} Mbps dedicated access port/user; shared 10 Gbps server uplink")
print(f"Wi-Fi 6: {wifi6_aggregate_mbps:.0f} Mbps assumed usable aggregate / {users} = {wifi6_aggregate_mbps/users:.1f} Mbps/user")
print("Conclusion: switched star is preferred for month-end large file transfers; Wi-Fi 6 is complementary access.")
