import MDAnalysis as mda
import numpy as np

u = mda.Universe("md.tpr", "md_center.xtc")

# Catechol hydroxyl groups
O1 = u.select_atoms("resname MOL and name O1")[0]
H1 = u.select_atoms("resname MOL and name H1")[0]

O2 = u.select_atoms("resname MOL and name O2")[0]
H6 = u.select_atoms("resname MOL and name H6")[0]

# Water oxygens
water_O = u.select_atoms("resname SOL and name OW")

# Same criteria used for phenol and p-cresol
distance_cutoff = 3.5       # Å
angle_cutoff = 150.0        # degrees


def angle(a, b, c):
    v1 = a - b
    v2 = c - b

    cosang = np.dot(v1, v2) / (
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )

    cosang = np.clip(cosang, -1.0, 1.0)

    return np.degrees(np.arccos(cosang))


O1_counts = []
O2_counts = []


for ts in u.trajectory:

    box = ts.dimensions[:3]

    O1_pos = O1.position.copy()
    H1_pos = H1.position.copy()

    O2_pos = O2.position.copy()
    H6_pos = H6.position.copy()

    count_O1 = 0
    count_O2 = 0

    for OW in water_O:

        OW_pos = OW.position.copy()

        # -------------------------
        # O1-H1 ... OW
        # -------------------------

        O1_to_OW = OW_pos - O1_pos
        O1_to_OW -= box * np.round(O1_to_OW / box)

        distance_O1 = np.linalg.norm(O1_to_OW)

        if distance_O1 <= distance_cutoff:

            H1_to_O1 = O1_pos - H1_pos
            H1_to_OW = OW_pos - H1_pos

            H1_to_O1 -= box * np.round(H1_to_O1 / box)
            H1_to_OW -= box * np.round(H1_to_OW / box)

            # Use the PBC-corrected vectors for the angle
            v1 = H1_to_O1
            v2 = H1_to_OW

            cosang = np.dot(v1, v2) / (
                np.linalg.norm(v1) * np.linalg.norm(v2)
            )

            cosang = np.clip(cosang, -1.0, 1.0)

            angle_O1 = np.degrees(np.arccos(cosang))

            if angle_O1 >= angle_cutoff:
                count_O1 += 1

        # -------------------------
        # O2-H6 ... OW
        # -------------------------

        O2_to_OW = OW_pos - O2_pos
        O2_to_OW -= box * np.round(O2_to_OW / box)

        distance_O2 = np.linalg.norm(O2_to_OW)

        if distance_O2 <= distance_cutoff:

            H6_to_O2 = O2_pos - H6_pos
            H6_to_OW = OW_pos - H6_pos

            H6_to_O2 -= box * np.round(H6_to_O2 / box)
            H6_to_OW -= box * np.round(H6_to_OW / box)

            v1 = H6_to_O2
            v2 = H6_to_OW

            cosang = np.dot(v1, v2) / (
                np.linalg.norm(v1) * np.linalg.norm(v2)
            )

            cosang = np.clip(cosang, -1.0, 1.0)

            angle_O2 = np.degrees(np.arccos(cosang))

            if angle_O2 >= angle_cutoff:
                count_O2 += 1

    O1_counts.append(count_O1)
    O2_counts.append(count_O2)


print("Frames:", len(u.trajectory))

print("\nCatechol O1-H1...water H-bonds")
print("Average:", np.mean(O1_counts))
print("Maximum:", np.max(O1_counts))
print("Minimum:", np.min(O1_counts))

print("\nCatechol O2-H6...water H-bonds")
print("Average:", np.mean(O2_counts))
print("Maximum:", np.max(O2_counts))
print("Minimum:", np.min(O2_counts))
