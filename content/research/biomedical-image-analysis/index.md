+++
title = "AI for biomedical image analysis and interpretation"
weight = 10

publications = [
  "Hager, P., Jungmann, F., Holland, R., Bhagat, K., Hubrecht, I., Knauer, M.M., Vielhauer, J., Makowski, M., Braren, R., Kaissis, G., & Rueckert, D. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. *Nature Medicine, 30*, 2613–2622.",
  "Dima, A.F., Zimmer, V.A., Menten, M.J., Li, H.B., Graf, M., Lemke, T., Raffler, P., Graf, R., Kirschke, J.S., Braren, R.F., & Rueckert, D. (2023). 3D Arterial Segmentation via Single 2D Projections and Depth Supervision in Contrast-Enhanced CT Images. *MICCAI*.",
  "Turgut, Ö., Müller, P., Hager, P., Shit, S., Starck, S., Menten, M.J., Martens, E., & Rueckert, D. (2023). Unlocking the Diagnostic Potential of ECG through Knowledge Transfer from Cardiac MRI.",
  "Müller, P., Kaissis, G., & Rueckert, D. (2024). ChEX: Interactive Localization and Region Description in Chest X-rays. *European Conference on Computer Vision*.",
  "Mueller, T.T., Starck, S., Bintsi, K., Ziller, A., Braren, R., Kaissis, G., & Rueckert, D. (2024). Are Population Graphs Really as Powerful as Believed? *Trans. Mach. Learn. Res., 2024*.",
  "Sideri-Lampretsa, V., McGinnis, J., Qiu, H., Paschali, M., Simson, W., & Rueckert, D. (2024). SINR: Spline-enhanced implicit neural representation for multi-modal registration. *Medical Imaging with Deep Learning*.",
  "Berger, A.H., Stucki, N., Lux, L., Buergin, V., Shit, S., Banaszak, A., Rueckert, D., Bauer, U., & Paetzold, J.C. (2024). Topologically faithful multi-class segmentation in medical images. *MICCAI*.",
  "Dannecker, M., Kyriakopoulou, V., Cordero-Grande, L., Price, A., Hajnal, J.V., & Rueckert, D. (2024). CINA: Conditional Implicit Neural Atlas for Spatio-Temporal Representation of Fetal Brains. *MICCAI*.",
  "Starck, S., Sideri-Lampretsa, V., Ritter, J. J., Zimmer, V. A., Braren, R., Mueller, T. T., & Rueckert, D. (2024). Using UK Biobank data to establish population-specific atlases from whole body MRI. *Communications Medicine, 4*(1), 237.",
  "Zhang, Y., Chen, C., Shit, S., Starck, S., Rueckert, D., & Pan, J. (2024). Whole heart 3D+t representation learning through sparse 2D cardiac MR images. *MICCAI* (pp. 359–369). Springer.",
]

# Each lead is a name and the author page it links to.
[[leads]]
  name = "Huaqi (Harvey) Qiu"
  url = "/author/huaqi-harvey-qiu/"

# Figures live beside this file. The first is the one the slide shows;
# the rest are kept with their captions for whatever shows them next.
[[figures]]
  file = "figure.png"
  alt = "Deep learning segmentation of biomedical images: whole body segmentation (left) and spine segmentation from MR images (right)"
  caption = "One of the main focuses of our research is the use of deep learning approaches for the segmentation of biomedical images (e.g. left: whole body segmentation, right: spine segmentation from MR images)."

[[figures]]
  file = "figure-2.png"
  alt = "Registration of a pair of T1-weighted and T2-weighted brain MR images using implicit neural representation of deformation"
  caption = "Image registration is an essential task in medical image analysis. One of our research directions is exploring accurate, robust and efficient image registration. Here, for example, a pair of T1-weighted and T2-weighted brain MR images is registered using an implicit neural representation of deformation."

[[figures]]
  file = "figure-3.png"
  alt = "Multi-modal AI leveraging ECG and tabular data alongside cardiac MRI for cardiovascular analysis"
  caption = "We are developing multi-modal AI algorithms that can incorporate multiple modalities and sources of information. For example, the methods shown here leverage ECG and tabular data alongside cardiac MRI to improve cardiovascular analysis."

+++
Medical imaging allows doctors to examine the interior structure or function of the human body, often without the need for invasive surgical procedures. It comprises a range of different techniques, such as computed tomography (CT), magnetic resonance imaging (MR) and ultrasound (US). Clinicians rely on the information provided by medical imaging to monitor patients, diagnose illnesses and decide on treatment.

Our mission is to support doctors in the clinical process and improve patient care by developing advanced algorithms that use artificial intelligence (AI) techniques. To this end, we create and improve machine learning (ML) algorithms for various parts of the medical imaging pipeline. At the image level, we develop methods to tackle tasks such as segmentation of relevant anatomical structures, registration of images across time or modalities, and enhancement of image quality. At the decision level, we innovate solutions to extract clinically useful information from medical images, diagnose diseases and predict future outcomes.

Developing these algorithms in the medical domain presents many challenges which we are striving to overcome. Medical data is often sparse and annotations for algorithm training are costly to acquire, with problems such as domain shift plaguing the few available data, which could be detrimental to ML algorithms. For this, we are developing data-efficient and domain-robust solutions, as well as exploring opportunities provided by the increasing availability of large public datasets / biobanks. Medical images are usually accompanied by additional information from different sources such as doctor's notes, laboratory test results or genomics data, all of which should be considered when interpreting the images. Part of our research centers on developing multi-modal AI solutions that integrate these diverse data sources. Finally, to successfully deploy these algorithms in a hospital setting, we work in close collaboration with medical professionals to align our research with clinical value and to improve the interpretability of our ML algorithms to foster trust and facilitate adoption.
