from pathlib import Path
import subprocess,sys
base=Path(__file__).resolve().parent
for p in ['Task01/q1_office_redesign.py','Task02/q2_topology_failure.py','Task03/q3_cabling_audit.py','Task04/q4_shared_media.py','Task05/q5_vlan_tag.py','Task06/q6_campus_plan.py']:
 print(f"\n===== {p} =====")
 subprocess.run([sys.executable,str(base/p)],check=True)
