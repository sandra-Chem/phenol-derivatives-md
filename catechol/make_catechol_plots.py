import os
import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda


OUTPUT_DIR = "graphs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def read_xvg(filename):
    x = []
    y = []

    with open(filename) as f:
        for line in f:
            if line.startswith(("#", "@")):
                continue

            parts = line.split()
            if len(parts) >= 2:
                try:
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
                except ValueError:
                    pass

    return np.array(x), np.array(y)


def save_plot(x, y, xlabel, ylabel, title, filename):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename), dpi=300)
    plt.close()


# ---------------------------------------------------------
# 1. TEMPERATURE
# ---------------------------------------------------------

time, temperature = read_xvg("catechol_temperature.xvg")

save_plot(
    time,
    temperature,
    "Time (ps)",
    "Temperature (K)",
    "Catechol Production Temperature",
    "01_temperature.png",
)


# ---------------------------------------------------------
# 2. DENSITY
# ---------------------------------------------------------

time, density = read_xvg("catechol_density.xvg")

save_plot(
    time,
    density,
    "Time (ps)",
    "Density (kg/m³)",
    "Catechol Production Density",
    "02_density.png",
)


# ---------------------------------------------------------
# 3. RDF O1-WATER
# ---------------------------------------------------------

r1, rdf1 = read_xvg("catechol_rdf_O1_OW.xvg")

save_plot(
    r1,
    rdf1,
    "Distance (nm)",
    "g(r)",
    "Catechol O1–Water RDF",
    "03_O1_water_RDF.png",
)


# ---------------------------------------------------------
# 4. RDF O2-WATER
# ---------------------------------------------------------

r2, rdf2 = read_xvg("catechol_rdf_O2_OW.xvg")

save_plot(
    r2,
    rdf2,
    "Distance (nm)",
    "g(r)",
    "Catechol O2–Water RDF",
    "04_O2_water_RDF.png",
)


# ---------------------------------------------------------
# 5. MINIMUM O-WATER DISTANCE
# ---------------------------------------------------------

time1, distance1 = read_xvg("catechol_O1_OW_distance.xvg")
time2, distance2 = read_xvg("catechol_O2_OW_distance.xvg")

plt.figure(figsize=(8, 5))
plt.plot(time1, distance1, label="O1")
plt.plot(time2, distance2, label="O2")
plt.xlabel("Time (ps)")
plt.ylabel("Minimum O–OW distance (nm)")
plt.title("Catechol Minimum O–Water Distance")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "05_O_water_distance.png"),
    dpi=300
)
plt.close()


# ---------------------------------------------------------
# 6. COORDINATION NUMBER
# ---------------------------------------------------------

radius1, cn1 = read_xvg("catechol_O1_cn.xvg")
radius2, cn2 = read_xvg("catechol_O2_cn.xvg")

plt.figure(figsize=(8, 5))
plt.plot(radius1, cn1, label="O1")
plt.plot(radius2, cn2, label="O2")
plt.xlabel("Radius (nm)")
plt.ylabel("Coordination number")
plt.title("Catechol Water Coordination Number")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "06_coordination_number.png"),
    dpi=300
)
plt.close()


# ---------------------------------------------------------
# 7. HYDROGEN-BOND ANALYSIS
# ---------------------------------------------------------

u = mda.Universe("md.tpr", "md_center.xtc")

O1 = u.select_atoms("resname MOL and name O1")[0]
H1 = u.select_atoms("resname MOL and name H1")[0]

O2 = u.select_atoms("resname MOL and name O2")[0]
H6 = u.select_atoms("resname MOL and name H6")[0]

water_O = u.select_atoms("resname SOL and name OW")

distance_cutoff = 3.5
angle_cutoff = 150.0

times = []
O1_counts = []
O2_counts = []


def calculate_angle(v1, v2):
    cosang = np.dot(v1, v2) / (
        np.linalg.norm(v1) * np.linalg.norm(v2)
    )

    cosang = np.clip(cosang, -1.0, 1.0)

    return np.degrees(np.arccos(cosang))


for ts in u.trajectory:

    box = ts.dimensions[:3]

    O1_pos = O1.position.copy()
    H1_pos = H1.position.copy()

    O2_pos = O2.position.copy()
    H6_pos = H6.position.copy()

    count1 = 0
    count2 = 0

    for OW in water_O:

        OW_pos = OW.position.copy()

        # O1-H1...OW
        vec = OW_pos - O1_pos
        vec -= box * np.round(vec / box)

        distance = np.linalg.norm(vec)

        if distance <= distance_cutoff:

            v1 = O1_pos - H1_pos
            v2 = OW_pos - H1_pos

            v1 -= box * np.round(v1 / box)
            v2 -= box * np.round(v2 / box)

            angle = calculate_angle(v1, v2)

            if angle >= angle_cutoff:
                count1 += 1

        # O2-H6...OW
        vec = OW_pos - O2_pos
        vec -= box * np.round(vec / box)

        distance = np.linalg.norm(vec)

        if distance <= distance_cutoff:

            v1 = O2_pos - H6_pos
            v2 = OW_pos - H6_pos

            v1 -= box * np.round(v1 / box)
            v2 -= box * np.round(v2 / box)

            angle = calculate_angle(v1, v2)

            if angle >= angle_cutoff:
                count2 += 1

    times.append(ts.time)
    O1_counts.append(count1)
    O2_counts.append(count2)


times = np.array(times)
O1_counts = np.array(O1_counts)
O2_counts = np.array(O2_counts)

plt.figure(figsize=(8, 5))
plt.plot(times, O1_counts, label="O1–H1")
plt.plot(times, O2_counts, label="O2–H6")
plt.xlabel("Time (ps)")
plt.ylabel("H-bonds/frame")
plt.title("Catechol OH–Water Hydrogen Bonds")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "07_hydrogen_bonds.png"),
    dpi=300
)
plt.close()


# ---------------------------------------------------------
# 8. NUMERICAL SUMMARY
# ---------------------------------------------------------

with open(os.path.join(OUTPUT_DIR, "Catechol_Analysis_Summary.txt"), "w") as f:

    f.write("CATECHOL MD ANALYSIS SUMMARY\n")
    f.write("=" * 60 + "\n\n")

    f.write("SIMULATION STABILITY\n")
    f.write("-" * 60 + "\n")
    f.write(f"Average temperature: {np.mean(temperature):.3f} K\n")
    f.write(f"Temperature RMSD: {np.std(temperature):.3f} K\n")
    f.write(f"Average density: {np.mean(density):.3f} kg/m^3\n")
    f.write(f"Density RMSD: {np.std(density):.3f} kg/m^3\n\n")

    i1 = np.argmax(rdf1)
    i2 = np.argmax(rdf2)

    f.write("RDF\n")
    f.write("-" * 60 + "\n")
    f.write(
        f"O1 RDF peak: {r1[i1]:.3f} nm, "
        f"g(r) = {rdf1[i1]:.3f}\n"
    )
    f.write(
        f"O2 RDF peak: {r2[i2]:.3f} nm, "
        f"g(r) = {rdf2[i2]:.3f}\n"
    )
    f.write("\n")

    f.write("MINIMUM O-WATER DISTANCE\n")
    f.write("-" * 60 + "\n")
    f.write(
        f"O1 minimum: {np.min(distance1):.4f} nm\n"
    )
    f.write(
        f"O1 average minimum: {np.mean(distance1):.4f} nm\n"
    )
    f.write(
        f"O2 minimum: {np.min(distance2):.4f} nm\n"
    )
    f.write(
        f"O2 average minimum: {np.mean(distance2):.4f} nm\n"
    )
    f.write("\n")

    f.write("COORDINATION NUMBER\n")
    f.write("-" * 60 + "\n")

    i1 = np.argmin(np.abs(radius1 - 0.342))
    i2 = np.argmin(np.abs(radius2 - 0.342))

    f.write(
        f"O1 CN at {radius1[i1]:.3f} nm: "
        f"{cn1[i1]:.3f}\n"
    )
    f.write(
        f"O2 CN at {radius2[i2]:.3f} nm: "
        f"{cn2[i2]:.3f}\n"
    )
    f.write("\n")

    f.write("HYDROGEN BONDS\n")
    f.write("-" * 60 + "\n")

    f.write(
        f"O1-H1 average H-bonds/frame: "
        f"{np.mean(O1_counts):.3f}\n"
    )

    f.write(
        f"O2-H6 average H-bonds/frame: "
        f"{np.mean(O2_counts):.3f}\n"
    )

    f.write(
        f"O1-H1 occupancy: "
        f"{np.mean(O1_counts > 0) * 100:.1f}%\n"
    )

    f.write(
        f"O2-H6 occupancy: "
        f"{np.mean(O2_counts > 0) * 100:.1f}%\n"
    )

print("\nCatechol analysis plots generated successfully.")
print(f"Output folder: {OUTPUT_DIR}/")
print("Files:")
for name in sorted(os.listdir(OUTPUT_DIR)):
    print(" ", name)
