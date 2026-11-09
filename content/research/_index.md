+++
# The Research section. This file is the /research/ page, which goes straight
# to the areas: each subfolder is one (opportunistic-cardiac-mri is a worked
# example of adding one), ordered by `weight`. The text below is the
# introduction on the homepage, whose Research widget shows its opening
# paragraph and builds its tiles from the areas, so nothing is written twice.
#
# One thing to know when editing these locally: `hugo server` does not notice
# that the homepage depends on them, so a change here will not live-reload.
# Restart ./view.sh to see it. A deploy build is always complete.
title = "Research"

[_build]
  render = true
  list = "never"

# The areas are parts of this page, not pages of their own.
[cascade._build]
  render = false
  list = "local"
+++

At the Lab for AI in Medicine at [TU Munich](https://www.tum.de/), we develop algorithms and models to improve medicine for patients and healthcare professionals. Our aim is to develop artificial intelligence (AI) and machine learning (ML) techniques for the analysis and interpretation of biomedical data. We focus on pursuing blue-sky research, including:

- AI for the early detection, prediction and diagnosis of diseases
- AI for personalized interventions and therapies
- AI for the identification of new biomarkers and targets for therapy
- Safe, robust and interpretable AI approaches
- Privacy-preserving AI approaches

We have a particularly strong interest in the application of imaging and computing technology to improve the understanding of brain development (in-utero and ex-utero), to improve the diagnosis and stratification of patients with dementia, stroke and traumatic brain injury, as well as for the comprehensive diagnosis and management of patients with cardiovascular disease and cancer.
