---
title: "A computable case definition for patients with SARS-CoV2 testing that occurred outside the hospital"
collection: publications
permalink: /publications/2023-10-01-computable-case-definition-covid
date: 2023-10-01
venue: 'JAMIA Open'
paperurl: 'https://doi.org/10.1093/jamiaopen/ooad047'
citation: '<b>Lijing Wang</b>, Amy R Zipursky, Alon Geva, Andrew J McMurry, Kenneth D Mandl, <b>Timothy A Miller</b>, A computable case definition for patients with SARS-CoV2 testing that occurred outside the hospital, JAMIA Open, Volume 6, Issue 3, October 2023, ooad047'
---
Abstract: 

Objective
To identify a cohort of COVID-19 cases, including when evidence of virus positivity was only mentioned in the clinical text, not in structured laboratory data in the electronic health record (EHR).

Materials and Methods
Statistical classifiers were trained on feature representations derived from unstructured text in patient EHRs. We used a proxy dataset of patients with COVID-19 polymerase chain reaction (PCR) tests for training. We selected a model based on performance on our proxy dataset and applied it to instances without COVID-19 PCR tests. A physician reviewed a sample of these instances to validate the classifier.

Results
On the test split of the proxy dataset, our best classifier obtained 0.56 F1, 0.6 precision, and 0.52 recall scores for SARS-CoV2 positive cases. In an expert validation, the classifier correctly identified 97.6% (81/84) as COVID-19 positive and 97.8% (91/93) as not SARS-CoV2 positive. The classifier labeled an additional 960 cases as not having SARS-CoV2 lab tests in hospital, and only 177 of those cases had the ICD-10 code for COVID-19.

Discussion
Proxy dataset performance may be worse because these instances sometimes include discussion of pending lab tests. The most predictive features are meaningful and interpretable. The type of external test that was performed is rarely mentioned.

Conclusion
COVID-19 cases that had testing done outside of the hospital can be reliably detected from the text in EHRs. Training on a proxy dataset was a suitable method for developing a highly performant classifier without labor-intensive labeling efforts.