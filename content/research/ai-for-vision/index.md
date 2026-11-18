+++
title = "AI for vision"
weight = 30

# The photograph on the area's tile (homepage) and beside its text on
# /research/, from assets/images. Without one the first figure stands in.
[card]
  image = "images/vision.jpg"
  alt = "A retinal fundus image beside an OCT scan and its thickness profile"

publications = [
  "Kreitner, L., Hager, P., Mengedoht, J., Kaissis, G., Rueckert, D., & Menten, M. J. (2026). Efficient numeracy in language models through single-token number embeddings. *ICML*.",
  "Mildenberger, D., Hager, P., Rueckert, D., & Menten, M. J. (2025). A tale of two classes: Adapting supervised contrastive learning to binary imbalanced datasets. *CVPR*, 10305–10314.",
  "Holland, R., Taylor, T. R. P., Holmes, C., Riedl, S., Mai, J., Patsiamanidi, M., Mitsopoulou, D., Hager, P., Müller, P., Paetzold, J. C., Scholl, H. P. N., Bogunović, H., Schmidt-Erfurth, U., Rueckert, D., Sivaprasad, S., Lotery, A. J., & Menten, M. J. (2025). Specialized curricula for training vision language models in retinal image analysis. *npj Digital Medicine, 8*(1):532.",
  "Holland, R., Leingang, O., Bogunović, H., Riedl, S., Fritsche, L., Prevost, T., Scholl, H. P. N., Schmidt-Erfurth, U., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2024). Metadata-enhanced contrastive learning from retinal optical coherence tomography images. *Medical Image Analysis, 97*:103296.",
  "Kreitner, L., Paetzold, J. C., Rauch, N., Chen, C., Hagag, A. M., Fayed, A. E., Sivaprasad, S., Rausch, S., Weichsel, J., Menze, B. H., Harders, M., Knier, B., Rueckert, D., & Menten, M. J. (2024). Synthetic optical coherence tomography angiographs for detailed retinal vessel segmentation without human annotations. *IEEE Transactions on Medical Imaging, 43*(6):2061–2073.",
  "Menten, M. J., Paetzold, J. C., Zimmer, V. A., Shit, S., Ezhov, I., Holland, R., Probst, M., Schnabel, J. A., & Rueckert, D. (2023). A skeletonization algorithm for gradient-based optimization. *ICCV*, 21394–21403.",
  "Holland, R., Leingang, O., Holmes, C., Anders, P., Kaye, R., Riedl, S., Paetzold, J. C., Ezhov, I., Bogunović, H., Schmidt-Erfurth, U., Scholl, H. P. N., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2023). Clustering disease trajectories in contrastive feature space for biomarker proposal in age-related macular degeneration. *MICCAI*, 724–734.",
  "Hager, P., Menten, M. J., & Rueckert, D. (2023). Best of both worlds: Multimodal contrastive learning with tabular and imaging data. *CVPR*, 23924–23935.",
  "Menten, M. J., Paetzold, J. C., Dima, A., Menze, B. H., Knier, B., & Rueckert, D. (2022). Physiology-based simulation of the retinal vasculature enables annotation-free segmentation of OCT angiographs. *MICCAI*, 330–340.",
]

# Each lead is a name and the author page it links to.
[[leads]]
  name = "Martin Menten"
  url = "/author/martin-menten/"

[[figures]]
  file = "figure.png"
  focus = "center"
  alt = "A figure showcasing how the research of the AI for Vision group spans ophthalmology, medical imaging, and computer vision."
  caption = "A figure showcasing how the research of the AI for Vision group spans ophthalmology, medical imaging, and computer vision."
+++

The AI for Vision group focuses on blue-sky research in medical image analysis with a particular focus on the application of machine learning and computer vision algorithms in the field of ophthalmology. Specifically, we are working on:

### Self-supervised learning

Labeling medical data is very expensive, as it is time-consuming and requires expert knowledge. Moreover, medical data often includes highly sensitive information, making it challenging to share without compromising the privacy of the subjects involved. To overcome the limited availability of large annotated medical datasets, we are researching self-supervised learning. This approach leverages unlabeled medical data to enable neural networks to extract meaningful features that can be effectively adapted to a wide range of downstream tasks.

### Multimodal deep learning

Clinicians rarely rely on a single source of information when diagnosing patients and deciding on a course of action. In order to place their observations into context, they consider an array of multimodal data, such as demographic and genomic information, patient interviews, laboratory test results and biomedical images. As the number of diagnostic modalities grows and the complexity of the obtained data increases, comprehensively evaluating all pieces of information is becoming more and more challenging for healthcare professionals. To address this, our research focuses on developing deep learning algorithms capable of integrating diverse multimodal data to support autonomous and effective clinical decision making.

### Deep learning for ophthalmology

Good vision is essential for navigating our environment, communicating, and performing everyday activities, such as reading, exercising, and working. Conversely, low vision or blindness severely impacts both the physical and emotional well-being of patients. As of 2020, more than 200 million people worldwide suffered from moderate to severe vision impairment. Research and treatment of eye diseases is increasingly being driven by sophisticated imaging modalities and advanced image processing methods. Driven by the comparative ease to image the eye and obtain large imaging datasets, ophthalmology has been an early adopter of deep learning in healthcare. Our group’s work in machine learning for ophthalmology simultaneously evaluates new algorithmic innovations while aiming to improve medical care for patients affected by ocular diseases.
