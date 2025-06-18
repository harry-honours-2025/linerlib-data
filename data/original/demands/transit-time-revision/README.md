# Transit Time Revision

The demand files in this folder are a consequence of revising transit times in an era where slow-steaming is much more common.
It is also a result of liner shipping network design models operating with an average speed and hence not being able to set individual voyage speeds on a service in order to meet critical transit times.

The origin-destination pairs, quantities, and revenues are identical to the orginal demand files.
For most of the origin-destination pairs the transit time is also identical, but for some the transit time has been revised.
The demand pairs that have been revised are the origin-destination pairs where a direct sailing at 14 knots average speed is not possible within the allowed transit times.
They have been revised according to current transit times found on the internet.

Below is the number of revised transit times for the given instances:

- `WAF`: 6 origin-destination pairs
- `Pacific`: 15 origin-destination pairs
- `WorldSmall`: 106 origin-destination pairs
- `EuropeAsia`: 32 origin-destination pairs
- `WorldLarge`: 112 origin-destination pairs
