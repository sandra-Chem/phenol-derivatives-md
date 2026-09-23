# Phenol Derivatives Molecular Dynamics

A self-directed computational chemistry project using **RDKit, ACPYPE and GROMACS** to study the hydration of phenolic molecules in water.

## Objective

The project investigates how structural changes in phenolic molecules affect their local solute–water interactions.

The completed comparison is:

- **Phenol** — baseline molecule
- **p-Cresol** — phenol with a para-methyl group

**Catechol** is currently in progress, and **p-nitrophenol** is planned as a future system.

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
    NVT (300 K)
        ↓
 NPT (300 K, 1 bar)
        ↓
  Production MD
        ↓
Trajectory analysis
 Software and Methods
RDKit — molecular structure preparation and 3D structure handling
ACPYPE / AmberTools — small-molecule parameterization and GROMACS file generation
GAFF2 — force-field parameters for the organic molecules
AM1-BCC — partial atomic charges
SPC — water model
GROMACS — molecular dynamics simulations
VMD — trajectory visualization and inspection
Python / NumPy / Matplotlib — numerical analysis and plotting
MDAnalysis — geometry-based hydrogen-bond analysis
Simulation Protocol

For the completed phenol and p-cresol simulations:

Parameter	Protocol
Temperature	300 K
NPT pressure	1 bar
Timestep	2 fs
NVT equilibration	100 ps
NPT equilibration	100 ps
Production MD	1 ns
Water model	SPC
Organic force field	GAFF2
Partial charges	AM1-BCC
Analysis

The production trajectories were analyzed using:

Radial distribution function (RDF) to examine water organization around the phenolic oxygen
Minimum O–water distance to characterize closest water contacts
Coordination number to estimate the number of water oxygens within a selected radius
Hydrogen-bond geometry to quantify OH–water hydrogen bonding
Temperature and density to check simulation stability
Results
Phenol vs p-Cresol
Metric	Phenol	p-Cresol
OH–water RDF peak	0.290 nm	0.282 nm
RDF peak height	1.647	1.648
Minimum O1–OW distance	0.255 nm	0.253 nm
Average minimum distance	0.2664 nm	0.2660 nm
Coordination number at 0.342 nm	2.878	2.958
Average OH–water H-bonds/frame	0.756	0.7705
H-bond occupancy	~75.6%	~77.0%
Main observation

Phenol and p-cresol show very similar local hydration around the phenolic OH group under the conditions studied.

The p-cresol RDF peak is slightly closer to the phenolic oxygen, while the peak height is essentially unchanged. The coordination number and hydrogen-bond occupancy also differ only slightly.

Because the completed trajectories are 1 ns long and do not include replicate simulations, these differences should be treated as an initial comparative observation rather than a strong mechanistic conclusion.

Project Status
Completed
RDKit structure preparation
Phenol molecular dynamics workflow
p-Cresol molecular dynamics workflow
Core trajectory analysis
Phenol vs p-cresol comparison
In Progress
Catechol molecular dynamics and analysis
Planned
p-Nitrophenol
Expanded comparative analysis across the phenol-derivative series
Limitations
Production trajectories are 1 ns long.
Only one trajectory was used for each completed system.
Replicate simulations and rigorous uncertainty analysis were not performed.
The p-cresol minimization reached machine precision but retained a maximum force of about 17.7 kJ mol^-1 nm^-1 rather than the nominal 10 threshold.
The project is an initial computational comparison rather than a publication-level statistical study.
What I Learned

This project gave me hands-on experience with a complete small-molecule molecular dynamics workflow:

structure preparation → parameterization → topology → solvation → minimization → equilibration → production MD → trajectory analysis → interpretation

A major part of the work also involved troubleshooting topology, solvent and simulation-input problems and understanding why each GROMACS stage was required.
