# LINERLIB

This is the benchmark suite for liner shipping network design described in:

- Berit D. Brouer, J. Fernando Alvarez, Christian E. M. Plum, David Pisinger, Mikkel Sigurd: A Base Integer Programming Model and Benchmark Suite for Liner-Shipping Network Design. _Transportation Science_ 48(2): 281-312 (2014)

The benchmark suite originates from publicly available data and past data for Maersk Line.
The data was last viewed in January 2011.
External data sources are:

- [“Distances between ports - Pub. 151”](www.marcon.com/library/resources/DBP/DBP.html), National Imagery and Mapping Agency
- The Hamburg Index, [Vereinigung Hamburger Schiffsmakler und Schiffsagenten](www.vhss.de)
- “Charter Rates 2000–2010”, [Alphaliner charter rates 2000-2010](www.alphaliner.com)
- “Container Freight Rate Insight”, [Drewry Shipping Consultants](www.drewry.co.uk)
- [Hapag-Lloyd Freight rate quotes](www.hapaglloyd.com/en/schedules/interactive.html)

## Instances

There are 7 instances for which each demand and fleet file are specific.
The first line in all files are the headings.
Ports and distances are for all instances and contain all ports although they are not all part of every instance.
Ports are identified by their UNLOCODE where applicable.

Two distance files exist:

- `dist_dense.csv`, which is an all to all distance file with drafts and canal traversal indication where applicable.
- `dist_sparse.csv`, which constitute a port with its nearest ports and way points. A distance from any two ports is done through routing of the corresponding way points.

Due to the generation of the distances via NIMA there is a 5% error margin on the distances.

Fleet information is gathered in the `fleet_data.csv` file and contains all data on the 6 vessel types that are used throughout the 7 instances.
For every instance a fleet file provides a type and a quantity for the vessel types available in the instances.

It is possible to generate 3 instances (high, medium, and low) related to different capacities and demands of the 7 instances.
To generate the high and low instances, TC rates and quantity of vessels are adjusted according to the `fleet_data.csv` and `fleet_$INSTANCE$.csv` according to the following rules:

- To generate a high capacity case you need to:
    - Multiply TC Rates by 0.8 and round to nearest thousand
    - Multiply Quantity by 1.2 and round to nearest integer
- To generate a low capacity case you need to:
    - Multiply TC Rates by 1.4 and round to nearest thousand
    - Multiply Quantity by 0.8 and round to nearest integer

For more information on each cost parameter, data creation and sources, please consult the technical report.
We strongly urge you to stay informed about the LINERLIB project by following us on GitHub.

## Acknowledgements

We would like to thank Maersk Line, Network and Product for valuable insights and access to real
life data for the creation of the benchmark suite. In particular we would like to thank Niels Madsen
for valuable comments and suggestions for improvement. We also thank Jørgen Harling and Niels Rasmussen, Network and Product, Maersk Line.
This project would not have been possible without their support.

We are grateful to Vereinigung Hamburger Schiffsmakler und Schiffsagenten, Drewry Shipping Consultants, Alphaliner.com and
National Imagery and Mapping Agency for providing data to construct the benchmark suite data.

This project was supported in part by The Danish Strategical Research Council under the ENERPLAN project.

## History

- Version 1.0 released August 16, 2013
- Version 1.1 released in April 2014
    - Duplicate entries of `RULED` removed.
    - Lifting and port call cost in `ports.csv` rounded off to the nearest integer.
    - `README` file clarifies rounding of TC rates to nearest thousand as explained in the original article.
- Version 1.2.1 released in September 2015
    - New transit times for `WAF`, `MED`, `Pacific`, `WorldSmall`, and `EuropeAsia`, as some transit times were too tight.
    - `WAF` has 20 ports and 37 demands, not 19 ports and 38 demands as described in the article.
- Version 1.2.2 released in February 2024
    - Added an additional `Demand_WorldSmall.csv` file as demands above 1000 FFe where wrongfully truncated to a decimal number of `1.xx`.
      Original file is kept for benchmarks and new correct demand file added as `Demand_WorldSmall_Fixed_Sep.csv`.
    - Added port cost for single port which was null.

