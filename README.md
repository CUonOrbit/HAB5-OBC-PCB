# HAB5-OBC PCB

## Overview
This repository contains the KiCad project files for the HAB5 Onboard Computer (OBC), developed for the Carleton University CUonOrbit high-altitude balloon program.

## Design Documentation
The preliminary design documentation serves as the primary baseline for architectural specifications, pinouts, and component selections. Note that the preliminary design provides the high-level architecture; contributors must still incorporate standard supporting circuitry (such as decoupling capacitors, pull-up/pull-down resistors, and proper termination).

Access the HAB5 Preliminary Design Folder for the latest schematic drafts and design notes: 
https://drive.google.com/drive/folders/1-SSNnOxP_JfVVEODxDMg0MS5he3rxrQx?usp=drive_link

## KiCad Project Structure
- Overview of the main KiCad project files:
  - `HAB5-OBC.kicad_pro` — project configuration.
  - `HAB5-OBC.kicad_sch` — schematic.
  - `HAB5-OBC.kicad_pcb` — PCB layout.

## Subsystem Organization
Schematics are modularized into functional hierarchical sheets to isolate components and minimize merge conflicts:
- MCU (Root Sheet): Microcontroller core, clock generation, and core housekeeping.
- Power Systems: Voltage regulation, power distribution, and the INA228 power monitor.
- Positional: IMU and barometer.
- Temperature: Temperature sensors.
- Data Logging: External NOR flash memory storage.
- Debug & Expansion: Programming headers, UART/SWD interfaces, and breakout pins.

Inter-sheet connections (such as I2C, SPI, UART, and power rails) are routed cleanly using hierarchical labels and pins.

## Component Sourcing & JLCPCB Integration
All surface-mount components for this project are machine-assembled by JLCPCB. Consequently, every selected part must be verified as in-stock within the JLCPCB parts library before being added to the schematic.

### Adding New Parts
- Open the PCB editor in KiCad.
- Navigate to Tools > External Plugins > impartGUI.
- In the impartGUI menu, ensure the Library save location: Save local, in the project folder option is checked.
- Copy the manufacturer part number (MPN) or JLCPCB part number from the JLCPCB library.
- Import the part and place it into your schematic from the local library.

## Version Control and Collaboration Workflow
Git is used to track changes to schemas, PCB layouts, and project settings. Because KiCad source files (.kicad_sch and .kicad_pcb) are complex structured text files that can be difficult to auto-merge:
- Isolate Work: Keep edits focused on specific functional subsystem sheets. Avoid modifying the root sheet or shared layout files simultaneously unless coordinated.
- Descriptive Commits: Write clear, concise commit messages detailing what was changed and why (e.g., fix(power): adjust 3V3 regulator decoupling capacitor layout).
- Clean Working Tree: Do not commit temporary cache files, backup files (.kicad_sch-bak), or unverified auto-generated outputs.

## Design Workflow
1. Review the preliminary design documentation and relevant requirements.
2. Modify the appropriate schematic sheet.
3. Run the Electrical Rules Checker (ERC).
4. Update and review the layout as required.
5. Run the Design Rules Checker (DRC) if relevant.
6. Commit the validated changes to Git, and if merging to main create a pull request.

## Contributors
CUonOrbit C&DH team.
