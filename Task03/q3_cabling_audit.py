"""Task 3: cable-length audit and T568B reference."""
runs={'Consulting rooms':(35,80),'Pharmacy':(96,96),'Waiting-hall APs':(60,60),'Main building':(420,420)}
for name,(lo,hi) in runs.items():
    status='PASS' if hi<=90 else ('permanent-link limit exceeded; channel may be within 100 m' if hi<=100 else 'FAIL: exceeds 100 m channel')
    medium='Cat6 UTP' if hi<=90 else ('redesign route / fibre preferred for headroom' if hi<=100 else 'single-mode fibre recommended')
    print(f"{name}: {lo}-{hi} m | {status} | {medium}")
print('T568B: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown')
print('T568A at one end + T568B at the other = crossover wiring; Auto-MDIX usually handles it on modern Ethernet ports.')
