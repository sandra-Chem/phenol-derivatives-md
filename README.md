# Phenol Derivatives Molecular Dynamics

A self-directed computational chemistry project using **RDKit, ACPYPE, and GROMACS** to study hydration and solute–water interactions of phenolic molecules.

## Objective

The project investigates how structural changes in phenolic molecules affect their local hydration environment, especially around hydroxyl groups.

### Molecules

- **Phenol** — baseline
- **P-Cresol** — para-methyl derivative of phenol
- **Catechol** — molecule with two hydroxyl groups
- **P-Nitrophenol** — planned

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

For the completed phenol, p-cresol, and catechol workflows:

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

## Analysis

The production trajectories were analyzed using:

### Radial Distribution Function (RDF)

Used to study how water oxygen atoms are spatially distributed around the hydroxyl oxygen.

### Minimum O–Water Distance

Used to determine the closest water-oxygen contact with the hydroxyl oxygen in each frame.

### Coordination Number

Used to estimate the number of water oxygens within a selected hydration-shell radius.

For consistency, the reported coordination numbers were evaluated at **0.342 nm**.

### Hydrogen-Bond Geometry

Hydrogen bonding was evaluated using:

- O···OW distance ≤ 3.5 Å
- O–H···OW angle ≥ 150°

### Simulation Stability

Temperature and density were checked to assess whether the simulated systems remained around the intended thermodynamic conditions.

## Phenol vs P-Cresol

| Metric | Phenol | P-Cresol |
|---|---:|---:|
| OH–water RDF peak | 0.290 nm | 0.282 nm |
| RDF peak height | 1.647 | 1.648 |
| Minimum O1–OW distance | 0.255 nm | 0.253 nm |
| Average minimum O1–OW distance | 0.2664 nm | 0.2660 nm |
| Coordination number @ 0.342 nm | 2.878 | 2.958 |
| Average OH–water H-bonds/frame | 0.756 | 0.7705 |
| H-bond occupancy | ~75.6% | ~77.0% |

Phenol and p-cresol show very similar local hydration around the phenolic OH group under the conditions studied.

## Catechol Results

Catechol contains two hydroxyl groups, so the hydration analysis was performed separately for the two hydroxyl sites.

| Metric | Catechol O1 | Catechol O2 |
|---|---:|---:|
| O–water RDF peak | 0.304 nm | 0.298 nm |
| RDF peak height | 1.445 | 1.532 |
| Minimum O–OW distance | 0.2520 nm | 0.2520 nm |
| Average minimum O–OW distance | 0.2816 nm | 0.2838 nm |
| Coordination number @ 0.342 nm | 2.972 | 2.900 |
| Average H-bonds/frame | 0.631 | 0.485 |
| H-bond occupancy | 63.1% | 48.5% |

### Catechol Stability

- Average production temperature: **300.132 K**
- Average production density: **970.947 kg/m³**
- Production length: **1 ns**

### Catechol Observation

The two hydroxyl groups show similar water coordination in the sampled trajectory, while their hydrogen-bond occupancy differs.

Because the simulation contains only one 1 ns trajectory for catechol, these differences are treated as **initial observations rather than definitive molecular behavior**.

## Comparative Results

| System | Main hydration feature |
|---|---|
| Phenol | Single phenolic OH; baseline hydration |
| P-Cresol | Very similar hydration to phenol |
| Catechol O1 | Similar water coordination with lower H-bond occupancy than phenol |
| Catechol O2 | Similar water coordination with lower H-bond occupancy than phenol |

### Main Project Observation

The current results suggest that the local hydration environment changes only modestly between phenol and p-cresol, while catechol introduces two hydroxyl sites with broadly similar water coordination but different sampled hydrogen-bond occupancy.

These observations are preliminary because the completed systems currently use a single 1 ns production trajectory without replicate simulations.

## Project Status

### Completed

- RDKit structure preparation
- Phenol MD workflow
- P-Cresol MD workflow
- Catechol MD workflow
- Core trajectory analysis
- Phenol vs p-cresol comparison
- Catechol hydration analysis

### Planned

- P-Nitrophenol
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
