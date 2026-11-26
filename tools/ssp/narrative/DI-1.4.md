The Security Team will read the inventory in Jira Service Management Assets without the right to change it. That separation keeps the team that investigates assets from also editing the record of them.

The same data reaches Splunk Enterprise Security as a lookup. Each alert there will carry its asset's owner, team, and criticality, and that is how the CSSP's analysts see the context too, from their host pool. The inventory also feeds vulnerability prioritization and incident response.
