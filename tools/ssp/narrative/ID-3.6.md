Every cloud secret will live in its own spoke's Key Vault, and nowhere else. Key Vault rotates each one automatically, and because no vault holds another team's secrets, a compromise in one spoke stays there. Secrets for the data center, the alternate site, and the fleet go into CyberArk instead.

The most sensitive keys are held in neither. The datalink and root signing keys, CCSD row 13, stay in the nShield HSMs and the datalink crypto modules, because their High confidentiality calls for hardware protection.
