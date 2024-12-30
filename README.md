# RECOIL_GLEAM

RECOIL GHG Life-cycle Emission Assessment Module (GLEAM). Developed by the RECOIL team at West Virginia University (WVU).

## Overview

   This dataset provides information about greenhouse gas (GHG) emissions from different transportation modes, engine technologies, and fuel types. The data are extracted from GREET 2023rev1. The data includes the following keys:
   
     - `year`: 2025, 2030, 2035, 2040, 2045, and 2050.
     - `mode`: Describes the type of transportation.
     - `engine`: Specifies the technology used in the vehicle's engine.
     - `fuel`: Type of fuel used.

   Each record contains two fields:
   
     - `GHG`: The greenhouse gas emissions associated with the fuel usage.
     - `Unit`: The unit of measurement for GHG emissions (e.g., g/miles, g/ton. miles, g/mm.Btu).

## Data Content

   The following keywords can be used to identify data from 2025-2050 with 5-year increments:

- `mode = Long_Haul`:

  - `engine = CIDI`, available `fuel`: `Diesel`, `Biodiesel`, `Renewable-Diesel`, `DME`, and `LNG`.
  - `engine = SL`, available `fuel`: `CNG` and `LNG`.
  - `engine = Electric`, available `fuel`: `Electricity`.
  - `engine = Co-Optimized`, available `fuel`: `Algae-HTL` and `Wastewater-Sludge-HTL`.
  - `engine = MCCI`, available `fuel`: `Waste-Feedstock`.
  - `engine = Fuel-Cell`, available `fuel`: `GH2`, `LH2`.
- `mode = Short_Haul`:

  - `engine = CIDI`, available `fuel`: `Diesel`, `Biodiesel`, `Renewable-Diesel`, `DME`, and `LNG`.
  - `engine = SL`, available `fuel`: `CNG` and `LNG`.
  - `engine = Electric`, available `fuel`: `Electricity`.
  - `engine = Fuel-Cell`, available `fuel`: `GH2`, `LH2`.
- `mode = Rail`:

  - `engine`: `Diesel-Electric`, available `fuel`: `Diesel`, `LNG`, `LPG`, `DME`, `FTD`, `Biodiesel-20`, `Renewable-Diesel-II`, `Renewable-Gasoline`, `Gaseous-Hydrogen`, and `Electricity`.
- `mode = Marine`:

  - `engine = HFO`, available `fuel`: `HFO-2.7`, `HFO-0.5`, and `HFO-0.1`.
  - `engine = MDO`, available `fuel`: `MDO-1.92`, `MDO-0.5`, and `MDO-0.1`.
  - `engine = MGO`, available `fuel`: `MGO-1`, `MGO-0.5`, and `MGO-0.1`.
  - `engine = LNG`, available `fuel`: `LNG`.
  - `engine = FTD`, available `fuel`: `Natural-Gas`, `Biomass-Coal`, `Biomass-Natural-Gas`, and `Biomass`.
  - `engine = Renewable-Diesel`, available `fuel`: `Yellow-Grease-HFO` and `Yellow-Grease`.
  - `engine = SVO`, available `fuel`: `SVO`.
  - `engine = Bio-Oil`, available `fuel`: `Pyrolysis-Oil-Woody-Biomass`.
  - `engine = Biodiesel`, available `fuel`: `Biodiesel`.
  - `engine = MeOH`, available `fuel`: `Natural-Gas`, `Flare-Gas`, `Renewable-Natural-Gas`, and `Biomass`.

## Units

- `g/miles`: For most road transportation modes (`Long_Haul` and `Short_Haul`).
- `g/ton.miles`: For `Rail` and `Marine` transportations.

## Notes

- Negative GHG values indicate carbon savings or reductions.
- Please refer to the [`GREET_summary.pdf`](GREET_summary.pdf) document for detailed explanations about engine and fuel technologies.

### Example usage

- See [`usage.ipynb`](usage.ipynb)

# What's next
- Add GLEAM to the RECOIL Backend API Services
- Create a frontend companion tool for quick query