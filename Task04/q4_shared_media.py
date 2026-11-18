"""Task 4: ALOHA, CSMA/CD, ATM and WLAN calculations."""
import math
print(f"Pure ALOHA max throughput: 1/(2e) = {1/(2*math.e):.4f} = {100/(2*math.e):.2f}%")
print(f"Slotted ALOHA max throughput: 1/e = {1/math.e:.4f} = {100/math.e:.2f}%")
rate=10_000_000; distance=2500; propagation_speed=2e8 # standard assumed fibre/copper propagation order
prop=distance/propagation_speed
bits=2*prop*rate
print(f"Assuming propagation speed 2e8 m/s (brief prints 2 x 10 m/s): one-way={prop*1e6:.2f} us, min frame={bits:.0f} bits = {bits/8:.2f} bytes")
print(f"ATM overhead: 5/53 = {5/53*100:.2f}% of cell; payload efficiency={48/53*100:.2f}%")
print(f"Ethernet MAC header+FCS: 18/1518 = {18/1518*100:.2f}% for a 1500-byte payload frame (excluding preamble/IFG)")
print(f"Wi-Fi 6 planning: 300 clients / 6 APs = 50 clients/AP; 2.4 GHz reuse channels 1,6,11; assign distinct non-overlapping 5 GHz channels where regulatory domain permits.")
