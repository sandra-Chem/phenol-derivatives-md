# Phenol Derivatives Molecular Dynamics

A self-directed computational chemistry project using **RDKit, ACPYPE, and GROMACS** to study hydration and solute–water interactions of phenolic molecules.

## Objective

The project investigates how structural changes in phenolic molecules affect the local hydration environment around the phenolic hydroxyl group.

### Molecules

- **Phenol** — baseline
- **p-Cresol** — para-methyl derivative of phenol
- **Catechol** — second hydroxyl derivative; simulation in progress
- **p-Nitrophenol** — planned

## Computational Workflow

```text
Molecular structure
        ↓
      RDKit
        ↓
       SDF
        ↓
     ACPYPE
        ↓
GAFF2 + AM1-BCC
        ↓
   SPC solvation
        ↓
Energy minimization
        ↓
    NVT equilibration
        ↓
    NPT equilibration
        ↓
   Production MD
        ↓
Trajectory analysis
        ↓
Chemical interpretation
```

## Software and Methods

- **RDKit** — molecular structure preparation and 3D coordinate generation
- **ACPYPE / AmberTools** — small-molecule parameterization and GROMACS file generation
- **GAFF2** — force-field parameters for the organic molecules
- **AM1-BCC** — partial atomic charges
- **SPC** — explicit water model
- **GROMACS** — molecular dynamics simulations
- **VMD** — trajectory visualization and inspection
- **Python / NumPy / Matplotlib** — numerical analysis and plotting
- **MDAnalysis** — geometry-based hydrogen-bond analysis

## What the Main GROMACS Files Mean

| File | Purpose |
|---|---|
| `.sdf` | Starting molecular structure and coordinates |
| `.gro` | Atomic coordinates and simulation-box dimensions |
| `.itp` | Molecular topology and force-field parameters |
| `.top` | Complete system topology and molecule counts |
| `.mdp` | Simulation settings |
| `.tpr` | Compiled GROMACS run input |
| `.xtc` | Compressed trajectory |
| `.edr` | Energy and thermodynamic data |
| `.log` | GROMACS run log |

A useful distinction is:

**Topology = how the molecule is defined and how it interacts.**  
**Coordinates = where the atoms are.**

## Simulation Protocol

For the completed phenol and p-cresol workflows:

| Parameter | Setting |
|---|---|
| Temperature | 300 K |
| NPT / production pressure | 1 bar |
| Timestep | 2 fs |
| NVT equilibration | 100 ps |
| NPT equilibration | 100 ps |
| Production MD | 1 ns |
| Water model | SPC |
| Organic force field | GAFF2 |
| Partial charges | AM1-BCC |

The same general protocol is being applied to catechol so that comparisons between molecules remain consistent.

## Analysis

The production trajectories are analyzed using:

### Radial Distribution Function (RDF)

Used to study how water oxygen atoms are spatially distributed around the phenolic oxygen.

### Minimum O–Water Distance

Used to determine the closest water-oxygen contact with the phenolic oxygen in each frame.

### Coordination Number

Used to estimate the number of water oxygens within a selected hydration-shell radius.

### Hydrogen-Bond Geometry

Hydrogen bonding was evaluated using:

- O···O distance ≤ 3.5 Å
- O–H···O angle ≥ 150°

### Simulation Stability

Temperature and density were checked to assess whether the simulated system remained around the intended thermodynamic conditions.

## Phenol vs P-Cresol Results

| Metric | Phenol | p-Cresol |
|---|---:|---:|
| OH–water RDF peak | 0.290 nm | 0.282 nm |
| RDF peak height | 1.647 | 1.648 |
| Minimum O1–OW distance | 0.255 nm | 0.253 nm |
| Average minimum O1–OW distance | 0.2664 nm | 0.2660 nm |
| Coordination number at 0.342 nm | 2.878 | 2.958 |
| Average OH–water H-bonds/frame | 0.756 | 0.7705 |
| H-bond occupancy | ~75.6% | ~77.0% |
| Production temperature | ~300.06 K | 300.105 K |
| Production density | ~969 kg/m³ | 969.741 kg/m³ |

## Main Observation

Phenol and p-cresol show **very similar local hydration around the phenolic OH group** under the conditions used.

The p-cresol RDF peak is slightly closer to the phenolic oxygen, while the peak height is essentially unchanged. Coordination number and hydrogen-bond occupancy also differ only slightly.

Because the completed trajectories are only 1 ns long and do not include replicate simulations, these differences should be treated as an initial comparative observation rather than a strong mechanistic conclusion.

## Project Status

### Completed

- RDKit structure preparation
- Phenol MD workflow
- P-Cresol MD workflow
- Core trajectory analysis
- Phenol vs p-cresol comparison

### In Progress

- Catechol MD simulation and analysis

### Planned

- p-Nitrophenol
- Comparative analysis across the full phenol-derivative set

## Troubleshooting and Learning

A major part of the project involved understanding and resolving practical GROMACS problems, including:

- topology include errors
- missing molecule definitions
- SPC water topology setup
- incorrect starting coordinates
- energy-minimization convergence
- trajectory-selection and residue-name issues

These problems helped me understand how the topology, coordinates, simulation parameters, and analysis stages depend on one another.

## Limitations

- Production trajectories are 1 ns long.
- Only one trajectory was used for each completed system.
- Replicate simulations and rigorous uncertainty analysis were not performed.
- The p-cresol minimization reached machine precision but retained a maximum force of about 17.7 kJ mol⁻¹ nm⁻¹ rather than the nominal 10 threshold.
- The current study is an initial computational comparison rather than a publication-level statistical study.

## Project Learning Outcome

This project provided hands-on experience with a complete small-molecule molecular-dynamics workflow:

**structure preparation → parameterization → topology → solvation → minimization → equilibration → production MD → trajectory analysis → interpretation**

The project also strengthened my understanding of how computational results should be checked, interpreted, and reported without overclaiming conclusions.

## Repository Structure

```text
phenol-derivatives-md/
├── README.md
├── rdkit/
├── phenol/
├── p-cresol/
├── catechol/
├── analysis/
└── figures/
```
