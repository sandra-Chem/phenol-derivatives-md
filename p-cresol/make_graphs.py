import os
import numpy as np
import matplotlib.pyplot as plt

OUT = "Graphs"
os.makedirs(OUT, exist_ok=True)

def read_xvg(filename):
    x = []
    y = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#") or line.startswith("@"):
                continue

            parts = line.split()
            if len(parts) >= 2:
                try:
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
                except ValueError:
                    pass

    return np.array(x), np.array(y)


def plot_xvg(filename, output, title, xlabel, ylabel):
    x, y = read_xvg(filename)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, output), dpi=300)
    plt.close()

    print("Saved:", output)


# -------------------------
# PHENOL
# -------------------------

phenol = "/home/sandra/GROMACS/Lysozyme_Project/Phenol_Project/MOL.amb2gmx"

plot_xvg(
    f"{phenol}/temperature.xvg",
    "Phenol_Production_Temperature.png",
    "Phenol Production MD Temperature",
    "Time (ps)",
    "Temperature (K)"
)

plot_xvg(
    f"{phenol}/density.xvg",
    "Phenol_Production_Density.png",
    "Phenol Production MD Density",
    "Time (ps)",
    "Density (kg/m³)"
)

plot_xvg(
    f"{phenol}/rdf_phenol_ow.xvg",
    "Phenol_OH_Water_RDF.png",
    "Phenol OH–Water RDF",
    "Distance (nm)",
    "g(r)"
)

plot_xvg(
    f"{phenol}/rdf_phenol_ring_ow.xvg",
    "Phenol_Ring_Water_RDF.png",
    "Phenol Ring–Water RDF",
    "Distance (nm)",
    "g(r)"
)

plot_xvg(
    f"{phenol}/phenol_ow_distance.xvg",
    "Phenol_OH_Water_Distance.png",
    "Phenol O1–Water O Minimum Distance",
    "Time (ps)",
    "Distance (nm)"
)

plot_xvg(
    f"{phenol}/rdf_cn.xvg",
    "Phenol_Coordination_Number.png",
    "Phenol OH–Water Coordination Number",
    "Distance (nm)",
    "Coordination number"
)

plot_xvg(
    f"{phenol}/phenol_msd.xvg",
    "Phenol_MSD.png",
    "Phenol Mean Squared Displacement",
    "Time (ps)",
    "MSD (nm²)"
)


# -------------------------
# P-CRESOL
# -------------------------

pcresol = "/mnt/c/Users/SANDRA/PCresol_Project"

plot_xvg(
    f"{pcresol}/nvt_temperature.xvg",
    "pCresol_NVT_Temperature.png",
    "p-Cresol NVT Temperature",
    "Time (ps)",
    "Temperature (K)"
)

plot_xvg(
    f"{pcresol}/pcresol_temperature.xvg",
    "pCresol_Production_Temperature.png",
    "p-Cresol Production MD Temperature",
    "Time (ps)",
    "Temperature (K)"
)

plot_xvg(
    f"{pcresol}/pcresol_density.xvg",
    "pCresol_Production_Density.png",
    "p-Cresol Production MD Density",
    "Time (ps)",
    "Density (kg/m³)"
)

plot_xvg(
    f"{pcresol}/rdf_pcresol_ow.xvg",
    "pCresol_OH_Water_RDF.png",
    "p-Cresol OH–Water RDF",
    "Distance (nm)",
    "g(r)"
)

plot_xvg(
    f"{pcresol}/pcresol_ow_distance.xvg",
    "pCresol_OH_Water_Distance.png",
    "p-Cresol O1–Water O Minimum Distance",
    "Time (ps)",
    "Distance (nm)"
)

plot_xvg(
    f"{pcresol}/rdf_cn.xvg",
    "pCresol_Coordination_Number.png",
    "p-Cresol OH–Water Coordination Number",
    "Distance (nm)",
    "Coordination number"
)

print("\nAll available project graphs have been saved in:")
print(os.path.abspath(OUT))
