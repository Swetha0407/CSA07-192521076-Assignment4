"""Complete-code exercise: link counts and single-link resilience."""
from itertools import combinations
from collections import deque

def links(kind, n):
    nodes=list(range(n))
    if kind=="bus": return [(i,i+1) for i in range(n-1)]
    if kind=="ring": return [(i,(i+1)%n) for i in range(n)]
    if kind=="star": return [("hub",i) for i in nodes]
    if kind=="mesh": return list(combinations(nodes,2))
    raise ValueError(kind)

def connected_after_failure(edges,n,broken):
    """Remove one edge; BFS from office 0; hub is an ordinary transit node."""
    remaining=list(edges)
    remaining.remove(broken)
    adj={i:[] for i in range(n)}
    adj['hub']=[]
    for a,b in remaining:
        adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
    seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v in adj.get(u,[]):
            if v not in seen: seen.add(v); q.append(v)
    return all(i in seen for i in range(n))

if __name__=='__main__':
    for n in (6,20):
        print(f"n={n}")
        for kind in ("bus","ring","star","mesh"):
            e=links(kind,n)
            nodes=set(x for edge in e for x in edge)
            ports=max(sum(x in edge for edge in e) for x in nodes)
            ok=sum(connected_after_failure(e,n,b) for b in e)
            print(f"{kind:<5} links {len(e):2d} max ports on one device {ports} single-link failures survived {ok}/{len(e)}")
