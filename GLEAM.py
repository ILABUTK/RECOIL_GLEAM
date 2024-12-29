#!/usr/bin/env python3
"""
-------------------
MIT License

Copyright (c) 2024  Zeyu Liu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-------------------
Description:
    The Life-cycle GHG Emission Assessment (GLEAM) module for RECOIL
-------------------
"""


class GLEAM():
    """
    GLEAM
    """
    def __init__(self):
        """
        init
        """
        # GLEAM data
        self.data = {
            'metadata': "RECOIL GLEAM data - extracted from GREET 2023rev1 "
            "- MIT License - Copyright (c) 2024 Dr. Zeyu Liu",
            2025: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1489.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 1303.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 405.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1609.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1427.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 1357.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1407.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 981.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 546.45,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 1266.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 761.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1254.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1736.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2753.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2408.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 748.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2974.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2694.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2504.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2600.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 938.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1342.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1858.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 18.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 13.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.61,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.82,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.88,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.90,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 16.04,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 16.09,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.97,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 16.04,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 16.09,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.59,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.28,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.87,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.85,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 1.05,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "Yellow-Grease-HFO": {
                            "GHG": 8.88,
                            "Unit": "g/ton.mile"
                        },
                        "Yellow-Grease": {
                            "GHG": 2.60,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.51,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "Pyrolysis-Oil-Woody-Biomass": {
                            "GHG": 1.77,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.66,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 23.11,
                            "Unit": "g/ton.mile"
                        },
                        "Flare-Gas": {
                            "GHG": 1.77,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Natural-Gas": {
                            "GHG": -64.45,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 4.24,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            },
            2030: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1342.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 1172.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 334.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1430.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1293.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 1215.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1277.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 524.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 469.27,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 1140.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 678.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1056.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1333.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2625.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2292.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 653.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2797.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2583.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2373.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2492.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 516.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1175.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1484.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 17.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 8.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.51,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.72,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.78,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.81,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 15.94,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 16.00,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.87,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 15.94,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 15.99,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.56,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.26,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.79,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.82,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 0.99,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "YG&HFO": {
                            "GHG": 8.80,
                            "Unit": "g/ton.mile"
                        },
                        "YG": {
                            "GHG": 2.50,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.39,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "PO-WB": {
                            "GHG": 1.43,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.48,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 22.74,
                            "Unit": "g/ton.mile"
                        },
                        "FG": {
                            "GHG": 1.41,
                            "Unit": "g/ton.mile"
                        },
                        "RNG": {
                            "GHG": -66.72,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 3.69,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            },
            2035: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1238.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 1081.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 301.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1316.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1293.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 1121.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1181.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 413.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 434.46,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 1051.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 623.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 933.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1160.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2537.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2215.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 617.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2697.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2498.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2292.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2410.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 421.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1080.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1342.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 17.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 7.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.49,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.70,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.76,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.79,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 15.93,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 15.98,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.85,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 15.91,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 15.97,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.56,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.25,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.77,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.81,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 0.96,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "YG&HFO": {
                            "GHG": 8.79,
                            "Unit": "g/ton.mile"
                        },
                        "YG": {
                            "GHG": 2.48,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.37,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "PO-WB": {
                            "GHG": 1.35,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.45,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 22.68,
                            "Unit": "g/ton.mile"
                        },
                        "FG": {
                            "GHG": 1.34,
                            "Unit": "g/ton.mile"
                        },
                        "RNG": {
                            "GHG": -67.12,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 3.88,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            },
            2040: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1238.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 1080.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 299.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1315.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1194.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 1120.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1181.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 396.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 432.55,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 1051.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 623.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 930.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1149.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2537.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2214.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 613.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2694.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2498.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2290.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2410.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 403.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1077.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1330.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 17.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 6.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.48,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.70,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.75,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.78,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 15.92,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 15.97,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.85,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 15.91,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 15.96,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.56,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.25,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.77,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.81,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 0.96,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "YG&HFO": {
                            "GHG": 8.78,
                            "Unit": "g/ton.mile"
                        },
                        "YG": {
                            "GHG": 2.47,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.37,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "PO-WB": {
                            "GHG": 1.34,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.44,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 22.66,
                            "Unit": "g/ton.mile"
                        },
                        "FG": {
                            "GHG": 1.32,
                            "Unit": "g/ton.mile"
                        },
                        "RNG": {
                            "GHG": -67.24,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 3.87,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            },
            2045: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1237.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 1080.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 298.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1313.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1194.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 1119.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1181.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 378.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 430.60,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 1050.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 622.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 928.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1139.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2536.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2213.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 610.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2690.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2498.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2289.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2410.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 385.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 1074.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1318.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 17.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 6.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.48,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.69,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.75,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.78,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 15.92,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 15.97,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.84,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 15.90,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 15.96,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.56,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.25,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.77,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.81,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 0.96,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "YG&HFO": {
                            "GHG": 8.78,
                            "Unit": "g/ton.mile"
                        },
                        "YG": {
                            "GHG": 2.46,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.36,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "PO-WB": {
                            "GHG": 1.32,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.43,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 22.64,
                            "Unit": "g/ton.mile"
                        },
                        "FG": {
                            "GHG": 1.30,
                            "Unit": "g/ton.mile"
                        },
                        "RNG": {
                            "GHG": -67.36,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 3.86,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            },
            2050: {
                "Long_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 1096.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 957.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 259.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 1162.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1050.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 994.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 1181.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 307.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Co-Optimized": {
                        "Algae-HTL": {
                            "GHG": 386.46,
                            "Unit": "g/mile"
                        },
                        "Wastewater-Sludge-HTL": {
                            "GHG": 931.00,
                            "Unit": "g/mile"
                        }
                    },
                    "MCCI": {
                        "Waste-Feedstock": {
                            "GHG": 550.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 789.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 962.00,
                            "Unit": "g/mile"
                        },
                    }
                },
                "Short_Haul": {
                    "CIDI": {
                        "Diesel": {
                            "GHG": 2425.00,
                            "Unit": "g/mile"
                        },
                        "Biodiesel": {
                            "GHG": 2116.00,
                            "Unit": "g/mile"
                        },
                        "Renewable-Diesel": {
                            "GHG": 573.00,
                            "Unit": "g/mile"
                        },
                        "DME": {
                            "GHG": 2571.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2391.00,
                            "Unit": "g/mile"
                        }
                    },
                    "SL": {
                        "CNG": {
                            "GHG": 2190.00,
                            "Unit": "g/mile"
                        },
                        "LNG": {
                            "GHG": 2306.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Electric": {
                        "Electricity": {
                            "GHG": 316.00,
                            "Unit": "g/mile"
                        }
                    },
                    "Fuel-Cell": {
                        "GH2": {
                            "GHG": 934.00,
                            "Unit": "g/mile"
                        },
                        "LH2": {
                            "GHG": 1139.00,
                            "Unit": "g/mile"
                        }
                    }
                },
                "Rail": {
                    "Diesel-Electric": {
                        "Diesel": {
                            "GHG": 26.00,
                            "Unit": "g/ton.mile"
                        },
                        "LNG": {
                            "GHG": 23.00,
                            "Unit": "g/ton.mile"
                        },
                        "LPG": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "DME": {
                            "GHG": 28.00,
                            "Unit": "g/ton.mile"
                        },
                        "FTD": {
                            "GHG": 27.0,
                            "Unit": "g/ton.mile"
                        },
                        "Biodiesel-20": {
                            "GHG": 22.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Diesel-II": {
                            "GHG": 9.00,
                            "Unit": "g/ton.mile"
                        },
                        "Renewable-Gasoline": {
                            "GHG": 4.00,
                            "Unit": "g/ton.mile"
                        },
                        "Gaseous-Hydrogen": {
                            "GHG": 16.00,
                            "Unit": "g/ton.mile"
                        },
                        "Electricity": {
                            "GHG": 6.00,
                            "Unit": "g/ton.mile"
                        }
                    }
                },
                "Marine": {
                    "HFO": {
                        "HFO-2.7": {
                            "GHG": 16.46,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.5": {
                            "GHG": 16.68,
                            "Unit": "g/ton.mile"
                        },
                        "HFO-0.1": {
                            "GHG": 16.73,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MDO": {
                        "MDO-1.92": {
                            "GHG": 15.76,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.5": {
                            "GHG": 15.90,
                            "Unit": "g/ton.mile"
                        },
                        "MDO-0.1": {
                            "GHG": 15.95,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MGO": {
                        "MGO-1": {
                            "GHG": 15.82,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.5": {
                            "GHG": 15.88,
                            "Unit": "g/ton.mile"
                        },
                        "MGO-0.1": {
                            "GHG": 15.94,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "LNG": {
                        "LNG": {
                            "GHG": 15.55,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "FTD": {
                        "Natural-Gas": {
                            "GHG": 18.25,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Coal": {
                            "GHG": 20.74,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass-Natural-Gas": {
                            "GHG": 11.80,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 0.92,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Renewable-Diesel": {
                        "YG&HFO": {
                            "GHG": 8.77,
                            "Unit": "g/ton.mile"
                        },
                        "YG": {
                            "GHG": 2.45,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "SVO": {
                        "SVO": {
                            "GHG": 2.35,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Bio-Oil": {
                        "PO-WB": {
                            "GHG": 1.26,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "Biodiesel": {
                        "Biodiesel": {
                            "GHG": 5.41,
                            "Unit": "g/ton.mile"
                        }
                    },
                    "MeOH": {
                        "Natural-Gas": {
                            "GHG": 22.60,
                            "Unit": "g/ton.mile"
                        },
                        "FG": {
                            "GHG": 1.27,
                            "Unit": "g/ton.mile"
                        },
                        "RNG": {
                            "GHG": -67.59,
                            "Unit": "g/ton.mile"
                        },
                        "Biomass": {
                            "GHG": 3.86,
                            "Unit": "g/ton.mile"
                        },
                    },
                }
            }
        }

    def query(self, year, mode, engine, fuel):
        """
        Retrieves the GHGs emission and emission unit.
        Please see README.md for detailed keywords.
        inputs:
        `year`: int, 2025, 2030, 2035, 2040, 2045, or 2050.
        `mode`: str, the transportation mode.
        `engine`: str, the engine technology.
        `fuel`: str, the fuel technology.
        outputs:
        (float, str): GHGs Emission and Emission Unit,
            or (None, None) if not found.
        """
        try:
            emission = self.data[year][mode][engine][fuel]["GHG"]
            unit = self.data[year][mode][engine][fuel]["Unit"]
        # If no match is found, return None
        except KeyError:
            return None, None
        return emission, unit
