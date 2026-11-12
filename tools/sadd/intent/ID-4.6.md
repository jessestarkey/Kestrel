## Design Intent
Keep break-glass accounts for the identity provider, the cloud tenants, and the ground segment. The cloud and directory sets are sealed in the data center with a second set at the alternate site, so losing the data center does not lose them, and each operating site holds its own ground segment set. The two cloud accounts use different sign-in methods. The directory and ground segment accounts use console-only passwords under a tailored exception, since their recovery cannot depend on the PKI they may be recovering. The ground segment account matters most, since an identity outage must never stop operators from recovering an airborne aircraft.

## External Dependencies
None outside the boundary.
