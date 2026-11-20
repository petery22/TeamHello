## Contribution Summary
Because dataset integration is scheduled after cleaning, my work during this period focused on preparing the integration workflow. Looking at the datasets and their values, I designed a matching strategy. First, artists will be matched on ULAN IDs, and then Wikidata QIDs (after normalizing the Met's identifier format to match the other two datasets), and then on names combined with birth and death years. Records will be linked using a Jaro-Winkler similarity for names, combined with a birth year tolerance of ±1 years. The similarity threshold will be chosen during integration after testing values.

Aside from that, I also provided the datasets and SHA-256 checksums for those datasets that were recorded when first finding the datasets for the Course Project: Plan.

## Next steps
Once cleaning is complete, I will implement the matching strategy, choose the similarity threshold, and begin anlyzing artists overlap across museums.