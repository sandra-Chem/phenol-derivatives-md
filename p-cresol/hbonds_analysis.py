import MDAnalysis as mda
import numpy as np

u = mda.Universe("md.tpr", "md_center.xtc")

O = u.select_atoms("resname MOL and name O1")[0]
H = u.select_atoms("resname MOL and name H6")[0]
water_O = u.select_atoms("resname SOL and name OW")

distance_cutoff = 3.5       # Å
angle_cutoff = 150.0        # degrees

hbond_counts = []

def angle(a, b, c):
    v1 = a - b
    v2 = c - b
    cosang = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cosang = np.clip(cosang, -1.0, 1.0)
    return np.degrees(np.arccos(cosang))

for ts in u.trajectory:
    O_pos = O.position
    H_pos = H.position
    box = ts.dimensions[:3]

    count = 0

    for OW in water_O:
        OW_pos = OW.position

        OH_to_OW = OW_pos - O_pos
        OH_to_OW -= box * np.round(OH_to_OW / box)

        distance = np.linalg.norm(OH_to_OW)

        if distance <= distance_cutoff:
            H_to_O = O_pos - H_pos
            H_to_OW = OW_pos - H_pos

            H_to_O -= box * np.round(H_to_O / box)
            H_to_OW -= box * np.round(H_to_OW / box)

            ang = angle(O_pos, H_pos, OW_pos)

            if ang >= angle_cutoff:
                count += 1

    hbond_counts.append(count)

print("Frames:", len(u.trajectory))
print("Average p-cresol OH...water H-bonds:", np.mean(hbond_counts))
print("Maximum:", np.max(hbond_counts))
print("Minimum:", np.min(hbond_counts))
