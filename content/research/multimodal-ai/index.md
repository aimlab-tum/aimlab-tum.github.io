+++
title = "Multimodal AI"
weight = 35

publications = [
  "Müller, P., Jungmann, F., Kaissis, G., & Rueckert, D. (2026). A structured, tagged, and localized visual question answering dataset with full sentence answers and scene graphs for chest X-ray images. *ICLR*.",
  "Cenikj, N., Turgut, Ö., Müller, A., Steger, A., Kehrer, J., Brugger, M., Rueckert, D., Martens, E., & Müller, P. (2026). Multi-view stenosis classification leveraging transformer-based multiple-instance learning using real-world clinical data. *IEEE Transactions on Medical Imaging*.",
  "Cenikj, N., Turgut, Ö., Müller, A., Steger, A., Kehrer, J., Brugger, M., Rueckert, D., & Müller, P. (2026). Cross-modal contrastive learning of ECG and angiography representations for severe stenosis classification. *MICCAI*.",
  "Liman, M. E., Turgut, Ö., Müller, A., Martens, E., Rueckert, D., & Müller, P. (2026). Echo2ECG: Enhancing ECG representations with cardiac morphology from multi-view echos. *MICCAI*.",
  "Turgut, Ö., Müller, P., Hager, P., Shit, S., Starck, S., Menten, M. J., Martens, E., & Rueckert, D. (2025). Unlocking the diagnostic potential of electrocardiograms through information transfer from cardiac magnetic resonance imaging. *Medical Image Analysis, 101*, 103451.",
  "Selivanov, A., Müller, P., Turgut, Ö., Stolt-Ansó, N., & Rueckert, D. (2025). Global and local contrastive learning for joint representations from cardiac MRI and ECG. *MICCAI*.",
  "Müller, P., Kaissis, G., & Rueckert, D. (2024). ChEX: Interactive localization and region description in chest X-rays. *ECCV*.",
  "Tanida, T.\\*, Müller, P.\\*, Kaissis, G., & Rueckert, D. (2023). Interactive and explainable region-guided radiology report generation. *CVPR*.",
  "Müller, P., Kaissis, G., Zou, C., & Rueckert, D. (2022). Joint learning of localized representations from medical images and reports. *ECCV*.",
]

# Each lead is a name and the author page it links to.
[[leads]]
  name = "Philip Müller"
  url = "/author/philip-muller/"

[[figures]]
  file = "figure.png"
  focus = "center"
  alt = "Two panels: multimodal representation learning aligning ECG and cardiac MRI, and grounded vision-language modeling for chest X-ray report generation."
+++
Our group develops advanced machine learning methods to integrate and analyze diverse medical data, ranging from imaging modalities such as X-ray, CT, ultrasound, and MRI to signals such as ECG and EEG to lab tests and textual reports. We are working on:

**Multimodal representation learning and information transfer.** Clinical data is inherently multimodal, with each modality providing unique but complementary information. Some modalities, while highly informative, are invasive, expensive, or unavailable in many clinical settings. By aligning representations across modalities, we enable the transfer of information from stronger but less accessible modalities to weaker yet readily available ones, improving cross-modal phenotype prediction and early risk assessment, while also enabling cross-retrieval and simplifying multimodal analysis. We develop representation learning methods that align modalities into shared spaces and transfer information between them. We demonstrate their utility in clinical applications across diverse medical disciplines, with a specific focus on cardiovascular medicine.

**Multimodal fusion.** Critical diagnostic information is often distributed across multiple medical modalities, each providing an incomplete view of a patient's health. Combining them can reveal latent multimodal signals and improve diagnostic and prognostic accuracy, but modalities are heterogeneous in structure and information density, ranging from 2D imaging, volumetric data, and videos to signals and text. We develop fusion mechanisms and architectures that handle this heterogeneity, along with unsupervised training and pretraining methods, and robustness to missing modalities, applying these across diverse medical disciplines.

**Grounded vision-language modeling.** Automatic report generation promises to replace the manual and often time-intensive writing of clinical reports, but seamless integration into clinical workflows requires models that avoid hallucinations and produce interpretable predictions that clinicians can verify. We develop vision-language models that explicitly ground inputs in the input modalities, for example through anatomical regions or pathological clues, and produce interpretable outputs such as localization and structured predictions. Our work also targets interactive human-AI collaboration and computational efficiency to enable the integration of large or multiple modalities.
