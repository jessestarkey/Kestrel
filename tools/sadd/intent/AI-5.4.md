## Design Intent
Poisoning tests seed a controlled fraction of a training snapshot with backdoor triggers and flipped labels, and of the federated rounds with crafted updates. The real pipeline then trains in the evaluation environment. The tests measure how much contamination each model absorbs before its screens or the aggregator's defenses catch it.

## External Dependencies
None outside the boundary.
