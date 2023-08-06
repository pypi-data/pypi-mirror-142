# CHANGELOG

## 1.1.1 - 2022-03-15

* Fix the ability to find defanged IOCs

## 1.1.0 - 2022-03-07

* Added 2 new inputs to parse_iocs: whitelist_domains, whitelist_ip_cidr_ranges
* Returned domains will now have the `www.` prefix stripped if it exists.
* improved handling of CSVs

## 1.0.0 - 2021-12-16
* Move functionality from swimbundle_utils.ioc into new repository
* Refactor code to get rid of class structure and use functions instead.
