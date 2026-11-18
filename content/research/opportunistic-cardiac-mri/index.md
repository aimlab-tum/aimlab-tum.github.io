+++
# The fifth area, and a worked example of how to add one.
#
# Drop `draft = true` and this appears in the Research carousel: no template,
# no stylesheet and no script has to be touched, and the numbering, the anchor
# and the slide build themselves.
#
# It is a draft because the group was listed on the site without ever having a
# description - it was the one entry in the old list with nothing to link to.
draft = true

title = "AI for opportunistic cardiac MRI"
weight = 50

# publications = [
#   "Author, A. (2026). Title. *Journal*.",
# ]

[[leads]]
  name = "TODO"
  url = "/author/todo/"

# Figures live beside this file, and the first is the one the slide shows.
# [[figures]]
#   file = "figure.png"
#   alt = "What the picture shows, for a screen reader."
#   focus = "top"   # the band crops to fill; "top", "bottom" or a percentage
#   caption = "What the picture means."
+++

Our group focuses on various applications of artificial intelligence (AI) in the scope of opportunistic cardiac MRI. By utilizing AI to make the most of readily available MRI data that was originally acquired for different purposes, we aim to provide innovative strategies to reconstruct cardiac MR images as well as detect, quantify, or predict cardiac conditions.

### Assessment of cardiac health through opportunistic screening using MRI

Cardiac phenotypes are parameters that are derived by cardiac MRI acquisitions to assess the cardiac health. We need innovative techniques to simplify the derivation of the cardiac phenotypes, rather than fully relying on the complex cardiac MRI scans.

The premise of this project is to instead assess the cardiac health using artificial intelligence by inputting other readily available MRI images and electrocardiogram (ECG) data.

### Generative models for MR super resolution

In every MRI scan, there are certain trade-offs that clinicians face; good quality, high-resolution images with enough slices (body coverage) versus time. Recent works on generative models have shown great promise to reconstruct missing slices from various types of information, therefore enabling shorter scan times by acquiring fewer slices. Other works try to generate higher resolution MR images from lower resolution MR images, essentially incorporating an interpolation network.

Here, we tackle these problems by utilizing diffusion models conditioned (guided) on other readily available MR images, MRI scanning parameters, or other MRI physics-guided information.
