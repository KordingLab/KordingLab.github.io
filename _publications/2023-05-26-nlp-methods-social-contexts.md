---
title: "Natural Language Processing Methods to Empirically Explore Social Contexts and Needs in Cancer Patient Notes"
collection: publications
permalink: /publications/2023-05-26-nlp-methods-social-contexts
date: 2023-05-26
venue: 'JCO Clinical Cancer Informatics' # journal/conference name
paperurl: '' # doi link preferred
citation: 'Natural Language Processing Methods to Empirically Explore Social Contexts and Needs in Cancer Patient Notes. Abigail Derton, Marco Guevara, <b>Shan Chen</b>, Shalini Moningi, David E. Kozono, Dianbo Liu, <b>Timothy A. Miller</b>, Guergana K. Savova, Raymond H. Mak, and Danielle S. Bitterman. JCO Clinical Cancer Informatics 2023 :7' #copy/pastable text. TODO bibtex?
---
Abstract:

PURPOSE
There is an unmet need to empirically explore and understand drivers of cancer disparities, particularly social determinants of health. We explored natural language processing methods to automatically and empirically extract clinical documentation of social contexts and needs that may underlie disparities.

METHODS
This was a retrospective analysis of 230,325 clinical notes from 5,285 patients treated with radiotherapy from 2007 to 2019. We compared linguistic features among White versus non-White, low-income insurance versus other insurance, and male versus female patients' notes. Log odds ratios with an informative Dirichlet prior were calculated to compare words over-represented in each group. A variational autoencoder topic model was applied, and topic probability was compared between groups. The presence of machine-learnable bias was explored by developing statistical and neural demographic group classifiers.

RESULTS
Terms associated with varied social contexts and needs were identified for all demographic group comparisons. For example, notes of non-White and low-income insurance patients were over-represented with terms associated with housing and transportation, whereas notes of White and other insurance patients were over-represented with terms related to physical activity. Topic models identified a social history topic, and topic probability varied significantly between the demographic group comparisons. Classification models performed poorly at classifying notes of non-White and low-income insurance patients (F1 of 0.30 and 0.23, respectively).

CONCLUSION
Exploration of linguistic differences in clinical notes between patients of different race/ethnicity, insurance status, and sex identified social contexts and needs in patients with cancer and revealed high-level differences in notes. Future work is needed to validate whether these findings may play a role in cancer disparities.