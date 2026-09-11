+++
# An instance of the Blank widget — the Research section.
# Documentation: https://wowchemy.com/docs/page-builder/

widget = "blank"
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 20  # Order that this section will appear.

title = "Research"
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

[advanced]
  # Custom CSS.
  css_style = ""

  # CSS class.
  css_class = ""
+++


At the Lab for AI in Medicine at [TU Munich](https://www.tum.de/), we develop algorithms and models to improve medicine for patients and healthcare professionals. Our aim is to develop artificial intelligence (AI) and machine learning (ML) techniques for the analysis and interpretation of biomedical data. We focus on pursuing blue-sky research, including:

- AI for the early detection, prediction and diagnosis of diseases
- AI for personalized interventions and therapies
- AI for the identification of new biomarkers and targets for therapy
- Safe, robust and interpretable AI approaches
- Privacy-preserving AI approaches

We have a particularly strong interest in the application of imaging and computing technology to improve the understanding of brain development (in-utero and ex-utero), to improve the diagnosis and stratification of patients with dementia, stroke and traumatic brain injury, as well as for the comprehensive diagnosis and management of patients with cardiovascular disease and cancer.

The following research groups are based at our chair:

<div class="rw">
<div class="rc" hidden>
  <div class="rc-stage">
    <div class="rc-viewport" tabindex="0" role="region" aria-label="Research areas">
      <div class="rc-track"></div>
    </div>
    <div class="rc-arrows">
      <button type="button" class="rc-nav rc-prev" aria-label="Previous research area">&#8592;</button>
      <button type="button" class="rc-nav rc-next" aria-label="Next research area">&#8594;</button>
    </div>
  </div>
</div>

<section class="rw-area">

## AI for biomedical image analysis and interpretation

[Huaqi (Harvey) Qiu](/author/huaqi-harvey-qiu/)

Medical imaging allows doctors to examine the interior structure or function of the human body, often without the need for invasive surgical procedures. It comprises a range of different techniques, such as computed tomography (CT), magnetic resonance imaging (MR) and ultrasound (US). Clinicians rely on the information provided by medical imaging to monitor patients, diagnose illnesses and decide on treatment.

Our mission is to support doctors in the clinical process and improve patient care by developing advanced algorithms that use artificial intelligence (AI) techniques. To this end, we create and improve machine learning (ML) algorithms for various parts of the medical imaging pipeline. At the image level, we develop methods to tackle tasks such as segmentation of relevant anatomical structures, registration of images across time or modalities, and enhancement of image quality. At the decision level, we innovate solutions to extract clinically useful information from medical images, diagnose diseases and predict future outcomes.

Developing these algorithms in the medical domain presents many challenges which we are striving to overcome. Medical data is often sparse and annotations for algorithm training are costly to acquire, with problems such as domain shift plaguing the few available data, which could be detrimental to ML algorithms. For this, we are developing data-efficient and domain-robust solutions, as well as exploring opportunities provided by the increasing availability of large public datasets / biobanks. Medical images are usually accompanied by additional information from different sources such as doctor's notes, laboratory test results or genomics data, all of which should be considered when interpreting the images. Part of our research centers on developing multi-modal AI solutions that integrate these diverse data sources. Finally, to successfully deploy these algorithms in a hospital setting, we work in close collaboration with medical professionals to align our research with clinical value and to improve the interpretability of our ML algorithms to foster trust and facilitate adoption.

<div class="hrv-carousel">
  <div class="hrv-track">
    <figure class="hrv-slide" id="hrv-slide-1">
      <img src="/home/harvey_research_1.png" alt="Deep learning segmentation of biomedical images: whole body segmentation (left) and spine segmentation from MR images (right)" loading="lazy">
      <figcaption>One of the main focuses of our research is the use of deep learning approaches for the segmentation of biomedical images (e.g. left: whole body segmentation, right: spine segmentation from MR images).</figcaption>
    </figure>
    <figure class="hrv-slide" id="hrv-slide-2">
      <img src="/home/harvey_research_2.png" alt="Registration of a pair of T1-weighted and T2-weighted brain MR images using implicit neural representation of deformation" loading="lazy">
      <figcaption>Image registration is an essential task in medical image analysis. One of our research directions is exploring accurate, robust and efficient image registration. Here, for example, a pair of T1-weighted and T2-weighted brain MR images is registered using an implicit neural representation of deformation.</figcaption>
    </figure>
    <figure class="hrv-slide" id="hrv-slide-3">
      <img src="/home/harvey_research_3.png" alt="Multi-modal AI leveraging ECG and tabular data alongside cardiac MRI for cardiovascular analysis" loading="lazy">
      <figcaption>We are developing multi-modal AI algorithms that can incorporate multiple modalities and sources of information. For example, the methods shown here leverage ECG and tabular data alongside cardiac MRI to improve cardiovascular analysis.</figcaption>
    </figure>
  </div>
  <div class="hrv-dots">
    <a href="#hrv-slide-1" aria-label="Go to slide 1"></a>
    <a href="#hrv-slide-2" aria-label="Go to slide 2"></a>
    <a href="#hrv-slide-3" aria-label="Go to slide 3"></a>
  </div>
</div>



<details class="rw-pubs">
<summary>Key publications</summary>

- Hager, P., Jungmann, F., Holland, R., Bhagat, K., Hubrecht, I., Knauer, M.M., Vielhauer, J., Makowski, M., Braren, R., Kaissis, G., & Rueckert, D. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. *Nature Medicine, 30*, 2613–2622.
- Dima, A.F., Zimmer, V.A., Menten, M.J., Li, H.B., Graf, M., Lemke, T., Raffler, P., Graf, R., Kirschke, J.S., Braren, R.F., & Rueckert, D. (2023). 3D Arterial Segmentation via Single 2D Projections and Depth Supervision in Contrast-Enhanced CT Images. *MICCAI*.
- Turgut, Ö., Müller, P., Hager, P., Shit, S., Starck, S., Menten, M.J., Martens, E., & Rueckert, D. (2023). Unlocking the Diagnostic Potential of ECG through Knowledge Transfer from Cardiac MRI.
- Müller, P., Kaissis, G., & Rueckert, D. (2024). ChEX: Interactive Localization and Region Description in Chest X-rays. *European Conference on Computer Vision*.
- Mueller, T.T., Starck, S., Bintsi, K., Ziller, A., Braren, R., Kaissis, G., & Rueckert, D. (2024). Are Population Graphs Really as Powerful as Believed? *Trans. Mach. Learn. Res., 2024*.
- Sideri-Lampretsa, V., McGinnis, J., Qiu, H., Paschali, M., Simson, W., & Rueckert, D. (2024). SINR: Spline-enhanced implicit neural representation for multi-modal registration. *Medical Imaging with Deep Learning*.
- Berger, A.H., Stucki, N., Lux, L., Buergin, V., Shit, S., Banaszak, A., Rueckert, D., Bauer, U., & Paetzold, J.C. (2024). Topologically faithful multi-class segmentation in medical images. *MICCAI*.
- Dannecker, M., Kyriakopoulou, V., Cordero-Grande, L., Price, A., Hajnal, J.V., & Rueckert, D. (2024). CINA: Conditional Implicit Neural Atlas for Spatio-Temporal Representation of Fetal Brains. *MICCAI*.
- Starck, S., Sideri-Lampretsa, V., Ritter, J. J., Zimmer, V. A., Braren, R., Mueller, T. T., & Rueckert, D. (2024). Using UK Biobank data to establish population-specific atlases from whole body MRI. *Communications Medicine, 4*(1), 237.
- Zhang, Y., Chen, C., Shit, S., Starck, S., Rueckert, D., & Pan, J. (2024). Whole heart 3D+t representation learning through sparse 2D cardiac MR images. *MICCAI* (pp. 359–369). Springer.

</details>

</section>

<section class="rw-area">

## Inverse problems in biomedical imaging

[Ivan Ezhov](/author/ivan-ezhov/)  ·  [Sevgi Gokce Kafali](/author/sevgi-gokce-kafali/)

Our group is working on inverse problems in biomedical imaging and their solution using artificial intelligence and machine learning.

The development of algorithms to solve inverse problems arising in sensor and imaging systems has a long tradition. Examples include compressed sensing approaches, e.g. for medical and computational imaging. Until recently, most algorithms for inverse problems were based on statistical or physical signal models, such as wavelets or sparse representations. Our research focuses on novel approaches based on deep learning to accelerate solving such problems.

We study how these deep learning-based approaches can be optimized for clinical applications and how they can be combined with image analysis methods. Deep learning-based approaches for reconstructing magnetic resonance imaging (MRI) or computed tomography (CT) provide efficient AI models, allowing the reconstruction of high-quality MRI images, and high-quality CT images from low-dose X-ray images. Recent works on generative models have shown great promise for accelerating reconstruction tasks to shorten the scan time in MRI, as well as generating images with much higher resolution than the acquired resolution (e.g. super-resolution). Here, we tackle these problems by utilizing AI (i.e., diffusion models) guided by readily available MR images from other organs/tissues, MRI scanning parameters, or other MRI physics-guided information.

<details class="rw-pubs">
<summary>Key publications</summary>

- Schlemper, J., Caballero, J., Hajnal, J.V., Price, A.N. & Rueckert, D. (2017). A deep cascade of convolutional neural networks for dynamic MR image reconstruction. *IEEE Transactions on Medical Imaging*.
- Qin, C., Schlemper, J., Caballero, J., Price, A.N., Hajnal, J.V. & Rueckert, D. (2018). Convolutional recurrent neural networks for dynamic MR image reconstruction. *IEEE Transactions on Medical Imaging*.
- Hammernik, K., Schlemper, J., Qin, C., Duan, J., Summers, R.M. & Rueckert, D. (2021). Systematic evaluation of iterative deep neural networks for fast parallel MRI reconstruction with sensitivity-weighted coil combination. *Magnetic Resonance in Medicine*.
- Hammernik, K., Küstner, T., Yaman, B., Huang, Z., Rueckert, D., Knoll, F. & Akçakaya, M. (2023). Physics-Driven Deep Learning for Computational Magnetic Resonance Imaging. *IEEE Signal Processing Magazine*.
- Huang, W., Li, H.B., Pan, J., Cruz, G., Rueckert, D. & Hammernik, K. (2023). Neural implicit k-space for binning-free non-cartesian cardiac MR imaging. *IPMI*.
- Pan, J., Hamdi, M., Huang, W., Hammernik, K., Kuestner, T. & Rueckert, D. (2024). Unrolled and rapid motion-compensated reconstruction for cardiac CINE MRI. *Medical Image Analysis*.
- Pan, J., Huang, W., Rückert, D., Küstner, T. & Hammernik, K. (2024). Reconstruction-driven motion estimation for motion-compensated MR CINE imaging. *IEEE Transactions on Medical Imaging*.
- Ezhov, I., Scibilia, K., Giannoni, L., Kofler, F., Iliash, I., Hsieh, F., Shit, S., Caredda, C., Lange, F., Montcel, B., Tachtsidis, I., & Rueckert, D. (2024). Learnable real-time inference of molecular composition from diffuse spectroscopy of brain tissue. *Journal of Biomedical Optics*.
- Chung, H., Lee, D., Wu, Z., Kim, B. H., Bouman, K. L., & Ye, J. C. (2025). ContextMRI: Enhancing Compressed Sensing MRI through Metadata Conditioning. *arXiv:2501.04284*.
- Jiang, L., Mao, Y., Wang, X., Chen, X., & Li, C. (2023). Cola-diff: Conditional latent diffusion model for multi-modal MRI synthesis. *MICCAI* (pp. 398–408). Springer.
- Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. *CVPR* (pp. 10684–10695).

</details>

</section>

<section class="rw-area">

## Privacy-preserving and trustworthy AI in medicine

[Alexander Ziller](/author/alexander-ziller/)

Our group is developing the next generation of privacy-preserving, secure, and trustworthy AI algorithms for medical applications.

AI in medicine requires large, diverse, and representative datasets to train fair, generalizable, and reliable models. However, such datasets often contain sensitive personal information. Privacy-preserving machine learning bridges the gap between data utilization and data protection by enabling the training of AI models on private data while providing formal privacy guarantees. Our group focuses on:

- Differential privacy (DP) theory and applications to machine learning and deep learning, targeting both unstructured datasets (e.g., images) and structured data (e.g., tabular and graph databases).
- Generative models and their applications, such as large language models (LLMs) and agentic systems, integrating differential privacy to ensure secure and privacy-preserving outcomes.
- Data attribution techniques, which enable transparent and accountable data usage in training and inference.
- Developing techniques to mitigate trade-offs between privacy, model utility, and computational efficiency.
- AI security, including the study of vulnerabilities in collaborative machine learning protocols (e.g., federated learning) and designing robust defense mechanisms against adversarial attacks.

Building trust in AI necessitates a comprehensive approach encompassing privacy, reliability, and security. Our work on trustworthy machine learning includes quantifying uncertainty in model outputs, incorporating domain expertise, developing probabilistic models to counteract poorly calibrated predictions, employing computational Bayesian techniques, and exploring the intersection of probabilistic and privacy-preserving machine learning. As AI systems increasingly integrate generative models like LLMs, we also work on establishing formal guarantees of safety and reliability for agentic LLM applications, exploring robustness in generative systems, and ensuring alignment of generative models with human values and ethical guidelines, particularly in high-stakes domains like healthcare.

<div class="hrv-carousel">
  <div class="hrv-track">
    <figure class="hrv-slide" id="priv-slide-1">
      <img src="/home/privacy_research_2.png" alt="Threat models in privacy-preserving machine learning and their impact on the necessary privacy protection and model performance" loading="lazy">
      <figcaption><strong>a,</strong> Adversaries can have various capabilities depending on the setting. <strong>b,</strong> The combination of the adversary's capabilities defines the threat model. In a worst-case analysis, they have all capabilities. However, access to the database is a pessimistic, practically irrelevant scenario. <strong>c,</strong> The necessary privacy protection depends on the threat model. In a worst-case threat model, the adversary only needs to match the model and gradient to an image in the database. In a practically more relevant scenario, the image must be reconstructed from the model and gradient. Here, much less privacy protection is necessary. <strong>d,</strong> The more stringent the privacy protection is chosen, the higher the impacts on the model performance are. Thus, if a realistic threat model is considered appropriate, models can perform better.</figcaption>
    </figure>
    <figure class="hrv-slide" id="priv-slide-2">
      <img src="/home/privacy_research_1.png" alt="Integrated framework for privacy-preserving and secure AI across the machine learning lifecycle" loading="lazy">
      <figcaption>This diagram presents an integrated framework for privacy-preserving and secure AI, highlighting technologies that safeguard both data and algorithms throughout the machine learning lifecycle. Under the Private AI paradigm, techniques like differential privacy protect sensitive medical data from identity leakage and inference attacks. On the Secure AI side, methods such as federated learning, secure multiparty computation, and homomorphic encryption enable collaborative model training without direct data sharing, defending against model theft, inversion, and adversarial manipulation. Together, these methods ensure that both patient data and algorithmic integrity are preserved in sensitive domains like healthcare.</figcaption>
    </figure>
  </div>
  <div class="hrv-dots">
    <a href="#priv-slide-1" aria-label="Go to slide 1"></a>
    <a href="#priv-slide-2" aria-label="Go to slide 2"></a>
  </div>
</div>

<details class="rw-pubs">
<summary>Key publications</summary>

- Kaiser, J., Ziller, A., Triantafillou, E., Rückert, D., & Kaissis, G. (2026). Your Privacy Depends on Others: Collusion Vulnerabilities in Individual Differential Privacy. *4th IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)*.
- Lockfisch, S., Schwethelm, K., Menten, M., Braren, R., Rueckert, D., Ziller, A., & Kaissis, G. (2025). On Arbitrary Predictions from Equally Valid Models. *AAAI Workshop on Navigating Model Uncertainty and the Rashomon Effect (MURE)*.
- Kaiser, J., Mueller, T., & Kaissis, G. (2025). Differential privacy in medical imaging applications. In *Trustworthy AI in Medical Imaging* (pp. 411–424). Academic Press.
- Koeken, A., Ziller, A., Knolle, M., & Rueckert, D. (2025). Sensitivity, Specificity, and Consistency: A Tripartite Evaluation of Privacy Filters for Synthetic Data Generation. *ICCV 2025 Workshop on Responsible Imaging*.
- Schwethelm, K., Kaiser, J., Kuntzer, J., Yiğitsoy, M., Rückert, D., & Kaissis, G. (2025). Differentially Private Active Learning: Balancing Effective Data Selection and Privacy. *IEEE SaTML* (pp. 858–878). doi:[10.1109/SaTML64287.2025.00053](https://doi.org/10.1109/SaTML64287.2025.00053).
- Schwethelm, K., Kaiser, J., Knolle, M., Lockfisch, S., Rueckert, D., & Ziller, A. (2025). Visual privacy auditing with diffusion models. *Transactions on Machine Learning Research*.
- Ziller, A., Mueller, T., Stieger, S., Feiner, L., Brandt, J., Braren, R., Rueckert, D., & Kaissis, G. (2024). Reconciling Privacy and Accuracy in AI for Medical Imaging. *Nature Machine Intelligence*.
- Kaess, P., Ziller, A., Mantz, L., Rueckert, D., Fintelmann, F. J., & Kaissis, G. (2024). Fair and private CT contrast agent detection. *MICCAI Workshop on Fairness of AI in Medical Imaging* (pp. 34–45). Springer.
- Kaissis, G., Kolek, S., Balle, B., Hayes, J., & Rueckert, D. (2024). Beyond the calibration point: Mechanism comparison in Differential Privacy. *International Conference on Machine Learning*.
- Tayebi Arasteh, S., Ziller, A., Kuhl, C., Makowski, M., Nebelung, S., Braren, R., Rueckert, D., Truhn, D., & Kaissis, G. (2024). Preserving fairness and diagnostic accuracy in private large-scale AI models for medical imaging. *Communications Medicine*.
- Hölzl, F. A., Rueckert, D., & Kaissis, G. (2023). Equivariant differentially private deep learning: Why DP-SGD needs sparser models. *16th ACM Workshop on Artificial Intelligence and Security* (pp. 11–22).
- Kaissis, G., Ziller, A., Kolek, S., Riess, A., & Rueckert, D. (2023). Optimal privacy guarantees for a relaxed threat model: Addressing sub-optimal adversaries in differentially private machine learning. *NeurIPS*.
- Mueller, T.T., Paetzold, J.C., Prabhakar, C., Usynin, D., Rueckert, D., & Kaissis, G. (2022). Differentially Private Graph Neural Networks for Whole-Graph Classification. *IEEE TPAMI*.
- Usynin, D., Ziller, A., Makowski, M., Braren, R., Rueckert, D., Glocker, B., Kaissis, G., & Passerat-Palmbach, J. (2021). Adversarial interference and its mitigations in privacy-preserving collaborative machine learning. *Nature Machine Intelligence*.
- Kaissis, G., Ziller, A., Passerat-Palmbach, J., Ryffel, T., Usynin, D., Trask, A., Lima Jr, I., Mancuso, J., Jungmann, F., Steinborn, M.M., & Saleh, A. (2021). End-to-end privacy preserving deep learning on multi-institutional medical imaging. *Nature Machine Intelligence*.
- Kaissis, G., Makowski, M.R., Rückert, D., & Braren, R.F. (2020). Secure, privacy-preserving and federated machine learning in medical imaging. *Nature Machine Intelligence*.

</details>

</section>

<section class="rw-area">

## AI for vision

[Martin Menten](/author/martin-menten/)

The AI for Vision group focuses on blue-sky research in medical image analysis with a particular focus on the application of machine learning and computer vision algorithms in the field of ophthalmology. Specifically, we are working on:

**Self-supervised learning.** Labeling medical data is very expensive, as it is time-consuming and requires expert knowledge. Moreover, medical data often includes highly sensitive information, making it challenging to share without compromising the privacy of the subjects involved. To overcome the limited availability of large annotated medical datasets, we are researching self-supervised learning, leveraging unlabeled medical data to enable neural networks to extract meaningful features that can be effectively adapted to a wide range of downstream tasks.

**Multimodal deep learning.** Clinicians rarely rely on a single source of information when diagnosing patients and deciding on a course of action. They consider an array of multimodal data, such as demographic and genomic information, patient interviews, laboratory test results and biomedical images. Our research focuses on developing deep learning algorithms capable of integrating diverse multimodal data to support autonomous and effective clinical decision making.

**Deep learning for ophthalmology.** Good vision is essential for navigating our environment, communicating, and performing everyday activities. As of 2020, more than 200 million people worldwide suffered from moderate to severe vision impairment. Driven by the comparative ease of imaging the eye and obtaining large imaging datasets, ophthalmology has been an early adopter of deep learning in healthcare. Our group's work in machine learning for ophthalmology simultaneously evaluates new algorithmic innovations while aiming to improve medical care for patients affected by ocular diseases.

<details class="rw-pubs">
<summary>Key publications</summary>

- Holland, R., Leingang, O., Bogunović, H., Riedl, S., Fritsche, L., Prevost, T., Scholl, H. P. N., Schmidt-Erfurth, U., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2024). Metadata-enhanced contrastive learning from retinal optical coherence tomography images. *Medical Image Analysis, 97*:103296.
- Kreitner, L., Paetzold, J. C., Rauch, N., Chen, C., Hagag, A. M., Fayed, A. E., Sivaprasad, S., Rausch, S., Weichsel, J., Menze, B. H., Harders, M., Knier, B., Rueckert, D., & Menten, M. J. (2024). Synthetic optical coherence tomography angiographs for detailed retinal vessel segmentation without human annotations. *IEEE Transactions on Medical Imaging, 43*(6):2061–2073.
- Menten, M. J., Paetzold, J. C., Zimmer, V. A., Shit, S., Ezhov, I., Holland, R., Probst, M., Schnabel, J. A., & Rueckert, D. (2023). A skeletonization algorithm for gradient-based optimization. *ICCV*, 21394–21403.
- Holland, R., Leingang, O., Holmes, C., Anders, P., Kaye, R., Riedl, S., Paetzold, J. C., Ezhov, I., Bogunović, H., Schmidt-Erfurth, U., Scholl, H. P. N., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2023). Clustering disease trajectories in contrastive feature space for biomarker proposal in age-related macular degeneration. *MICCAI*, 724–734.
- Menten, M. J., Holland, R., Leingang, O., Bogunović, H., Hagag, A. M., Kaye, R., Riedl, S., Traber, G. L., Hassan, O. N., Pawlowski, N., Glocker, B., Fritsche, L. G., Scholl, H. P. N., Sivaprasad, S., Schmidt-Erfurth, U., Rueckert, D., & Lotery, A. J. (2023). Exploring healthy retinal aging with deep learning. *Ophthalmology Science, 3*(3):100294.
- Hager, P., Menten, M. J., & Rueckert, D. (2023). Best of both worlds: Multimodal contrastive learning with tabular and imaging data. *CVPR*, 23924–23935.
- Menten, M. J., Paetzold, J. C., Dima, A., Menze, B. H., Knier, B., & Rueckert, D. (2022). Physiology-based simulation of the retinal vasculature enables annotation-free segmentation of OCT angiographs. *MICCAI*, 330–340.

</details>

</section>

</div>

<style>
/* Research areas: a horizontal rail of cards, with the selected area's full
   text below it. The cards are built from the sections themselves, so adding
   an area means adding one <section> wrapper around ordinary Markdown -
   nothing has to be repeated in two places.
   Values follow Wowchemy: 1rem/1.5 body, headings at weight 500, #dee2e6
   rules, rgba(0,0,0,.54) for secondary text. */
/* One area per slide. The viewport scrolls natively with snap points, so a
   swipe works on a touch screen with no JavaScript in the path and the arrows
   only automate what the finger already does. Values follow Wowchemy - 1rem/1.5
   body, headings at weight 500, #dee2e6 rules, rgba(0,0,0,.54) for secondary
   text, #2962ff for the accent - and the dark variation takes the theme's own
   greys rather than staying white, which is what the cards used to do. */
.rc{--rc-line:#dee2e6;--rc-bg:#fff;--rc-fg:#212529;--rc-muted:rgba(0,0,0,.54);
  --rc-accent:#2962ff;--rc-spark:#00c2ff;--rc-thumb:#f7f7f7;margin:1.5rem 0 .5rem}
.dark .rc{--rc-line:#44475a;--rc-bg:#282a36;--rc-fg:#f8f8f2;
  --rc-muted:rgba(248,248,242,.54);--rc-thumb:#23252f}
/* The shell is empty until the script fills it, and `hidden` alone would lose
   to the display below, so it is spelled out. With no JavaScript nothing is
   shown here and every area stays open underneath, as before. */
.rc[hidden]{display:none}

.rc-viewport{overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;
  -webkit-overflow-scrolling:touch;scrollbar-width:none}
.rc-viewport::-webkit-scrollbar{display:none}
/* 80% slides inside a track padded by 10% leave a tenth of the previous and the
   next one showing at rest, and let the first and last sit in the middle like
   every other slide rather than jamming against the end. */
.rc-track{display:flex;gap:1rem;padding:0 10%;align-items:stretch}
/* One column, not two. With the whole area folded in, a 5/7 split left the
   figure column empty for seventeen hundred pixels and squeezed the text into
   a 400px measure. Figure across the top, text under it at the full width of
   the slide. */
.rc-slide{flex:0 0 80%;min-width:0;scroll-snap-align:center;position:relative;
  display:flex;flex-direction:column;align-self:start;
  border:1px solid var(--rc-line);background:var(--rc-bg);color:var(--rc-fg);
  opacity:.3;transition:opacity .4s ease;cursor:pointer}
.rc-slide[data-active="true"]{opacity:1;cursor:default}
/* The one flourish: a hairline that draws itself across the slide you land on.
   Nothing moves on the page, so it is safe to leave running. */
.rc-slide::before{content:"";position:absolute;left:0;right:0;top:0;height:2px;z-index:1;
  background:linear-gradient(90deg,var(--rc-accent),var(--rc-spark));
  transform:scaleX(0);transform-origin:left;transition:transform .55s ease}
.rc-slide[data-active="true"]::before{transform:scaleX(1)}

.rc-figure{margin:0;background:var(--rc-thumb);display:flex;align-items:center;
  justify-content:center;overflow:hidden;padding:1rem;border-bottom:1px solid var(--rc-line)}
/* `contain`, not `cover`: these are figures from papers, and a panel cropped to
   fill the box loses the half of the diagram that carried the point. */
.rc-figure img{max-width:100%;max-height:13rem;width:auto;height:auto;
  object-fit:contain;display:block}
.rc-figure-empty{font-size:.875rem;letter-spacing:.04em;color:var(--rc-muted)}

.rc-body{padding:1.75rem 1.875rem;min-width:0}
/* Mono numerals and a rule running off to the edge: the technical register the
   section is about, without anything glowing. */
.rc-index{display:flex;align-items:center;gap:.75rem;margin:0 0 .75rem;
  font-family:"Roboto Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:.75rem;letter-spacing:.18em;color:var(--rc-muted)}
.rc-index::after{content:"";flex:1;height:1px;background:var(--rc-line)}

/* The area itself is moved into the slide rather than copied, so the text is
   never in two places and the heading keeps the id its deep link uses. The
   rule and spacing it carried as a standalone section come off here. */
.rc-slide .rw-area{border:0;margin:0;padding:0;display:block}
.rc-slide .rw-area h2{font-size:1.375rem;font-weight:500;line-height:1.25;
  margin:0 0 .35rem;color:var(--rc-fg)}
.rc-slide .rw-area p{font-size:.9375rem;line-height:1.6}
.rc-slide .rw-pubs li{color:var(--rc-muted)}
.rc-slide .rw-pubs{border-top-color:var(--rc-line)}

/* The arrows sit against the sides of the slides rather than in a row of their
   own. A slide is taller than the window, so a button centred on the slide
   would be several hundred pixels below the fold: the overlay is the full
   height of the stage and each button is sticky at the middle of the window,
   so it rides down beside whatever you are reading. */
.rc-stage{position:relative}
.rc-arrows{position:absolute;top:0;left:0;right:0;bottom:0;pointer-events:none;
  display:flex;align-items:flex-start;justify-content:space-between}
.rc-nav{pointer-events:auto;position:sticky;top:calc(50vh - 1.375rem);
  display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;
  width:2.75rem;height:2.75rem;padding:0;font:inherit;line-height:1;cursor:pointer;
  border:1px solid var(--rc-line);border-radius:50%;background:var(--rc-bg);color:var(--rc-fg)}
.rc-nav:hover:not(:disabled){border-color:var(--rc-accent);color:var(--rc-accent)}
.rc-nav:disabled{opacity:0;pointer-events:none}

@media (max-width:700px){
  /* A tenth of a neighbour is not worth the width on a phone; take a slimmer
     peek and stack the figure over the text. */
  .rc-track{gap:.75rem;padding:0 6%}
  .rc-slide{flex:0 0 88%}
  .rc-nav{width:2.5rem;height:2.5rem}
  .rc-figure img{max-height:11rem}
  .rc-body{padding:1.25rem}
  .rc-slide .rw-area h2{font-size:1.25rem}
}

/* The slide already carries the area's figure, so the figure carousel inside
   the area below it is the same picture a second time. Images at the top only.
   This hides rather than deletes: the second and third figures of an area, and
   every caption, still exist in the Markdown and come back by dropping this
   rule. */
.rw-area .hrv-carousel{display:none}

@media (max-width:700px){
  .rc-slide{grid-template-columns:minmax(0,1fr)}
  .rc-figure{min-height:0;max-height:11rem}
  .rc-body{padding:1.25rem}
  .rc-title{font-size:1.25rem}
}

.rw-area{padding-top:1.25rem;border-top:1px solid #dee2e6;margin-top:.5rem}
.rw-area h2{font-size:1.5rem;font-weight:500;line-height:1.2;margin:0 0 .25rem}
.rw-pubs{margin-top:1.125rem;border-top:1px solid #dee2e6;padding-top:.75rem}
.rw-pubs summary{cursor:pointer;font-weight:500}
.rw-pubs ul{margin:.75rem 0 0}
.rw-pubs li{margin-bottom:.5rem;font-size:.875rem;color:rgba(0,0,0,.54)}

/* Figure carousels inside an area - unchanged from the previous layout. */
.hrv-carousel{margin:1.5rem 0 2rem}
.hrv-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;
  -webkit-overflow-scrolling:touch;scrollbar-width:none}
.hrv-track::-webkit-scrollbar{display:none}
.hrv-slide{flex:0 0 100%;scroll-snap-align:center;margin:0;padding:0;text-align:center}
.hrv-slide img{width:100%;height:auto;display:block;object-fit:contain;background:#f7f7f7}
.hrv-slide figcaption{font-size:.875rem;color:rgba(0,0,0,.54);margin-top:.6rem;padding:0 .5rem;text-align:left}
/* The dot stays 11px, but on a touch screen an 11px target is not reachable,
   so each one carries an invisible 2.5rem square. The gap is widened to match
   it, otherwise the squares overlap and the last dot swallows its neighbours. */
.hrv-dots{display:flex;justify-content:center;gap:1.75rem;margin-top:.9rem}
.hrv-dots a{position:relative;width:11px;height:11px;border-radius:50%;background:#dee2e6}
.hrv-dots a::after{content:"";position:absolute;left:50%;top:50%;width:2.5rem;height:2.5rem;
  transform:translate(-50%,-50%)}
.hrv-dots a:hover{background:rgba(0,0,0,.54)}
</style>

<script>
/* Builds the carousel from the sections below it, so a new research area is
   still just another <section class="rw-area"> with ordinary Markdown inside -
   no slide to write, nothing repeated in two places.

   The area is MOVED into its slide rather than summarised onto it, so the text
   exists once, the <details> of key publications keeps working, and the heading
   carries its generated id along - #ai-for-vision still resolves.

   Progressive enhancement: with JavaScript off the carousel stays hidden and
   every area is visible in the order it was written, which is how this section
   behaved before it had a rail.

   Slides are 80% wide and snap to centre, so the previous and next one show at
   the edges, and the mono numerals on each slide say where in the run you are. A swipe needs none of this code; the arrows, the segmented bar,
   the arrow keys and a click on a neighbouring slide drive the same scroll. */
(function () {
  var root = document.querySelector('.rc');
  var areas = Array.prototype.slice.call(document.querySelectorAll('.rw-area'));
  if (!root || !areas.length) return;

  var viewport = root.querySelector('.rc-viewport');
  var track = root.querySelector('.rc-track');
  var prev = root.querySelector('.rc-prev');
  var next = root.querySelector('.rc-next');
  var total = areas.length;
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };

  var slides = areas.map(function (area, i) {
    var heading = area.querySelector('h2');
    var img = area.querySelector('img');

    var slide = document.createElement('article');
    slide.className = 'rc-slide';
    slide.dataset.target = heading ? heading.id : '';
    slide.innerHTML =
      '<figure class="rc-figure">' +
        (img ? '<img alt="" loading="lazy" src="' + img.getAttribute('src') + '">'
             : '<span class="rc-figure-empty">No figure yet</span>') +
      '</figure>' +
      '<div class="rc-body"><p class="rc-index">' + pad(i + 1) + ' / ' + pad(total) + '</p></div>';
    slide.querySelector('.rc-body').appendChild(area);
    slide.addEventListener('click', function () {
      if (slide.dataset.active !== 'true') go(i);
    });
    track.appendChild(slide);
    return slide;
  });

  var current = -1;

  function select(i) {
    if (i === current) return;
    current = i;
    slides.forEach(function (s, n) { s.dataset.active = n === i ? 'true' : 'false'; });
    /* Disabling the button that has focus drops focus to the document, and the
       next arrow key is then someone else's event. Read who had it first -
       setting `disabled` blurs it before we could ask - and hand focus to the
       arrow that is still live. */
    var focused = document.activeElement;
    prev.disabled = i === 0;
    next.disabled = i === total - 1;
    if (focused === next && next.disabled) prev.focus();
    if (focused === prev && prev.disabled) next.focus();
  }

  /* Slides snap to the centre, so the resting scroll position of slide i puts
     its middle over the middle of the viewport. */
  function offsetOf(i) {
    return slides[i].offsetLeft - track.offsetLeft
         + slides[i].offsetWidth / 2 - viewport.clientWidth / 2;
  }

  function go(i) {
    i = Math.max(0, Math.min(total - 1, i));
    viewport.scrollTo({left: offsetOf(i), behavior: 'smooth'});
    select(i);
  }

  prev.addEventListener('click', function () { go(current - 1); });
  next.addEventListener('click', function () { go(current + 1); });

  root.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { go(current - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { go(current + 1); e.preventDefault(); }
  });

  /* A swipe moves the viewport without going through go(), so read the resting
     position back and follow whichever slide is nearest the middle. */
  var settle;
  viewport.addEventListener('scroll', function () {
    clearTimeout(settle);
    settle = setTimeout(function () {
      var best = 0, bestGap = Infinity;
      for (var i = 0; i < slides.length; i++) {
        var gap = Math.abs(offsetOf(i) - viewport.scrollLeft);
        if (gap < bestGap) { bestGap = gap; best = i; }
      }
      select(best);
    }, 90);
  }, {passive: true});

  function fromHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    for (var i = 0; i < slides.length; i++) {
      if (slides[i].dataset.target === id) return i;
    }
    return null;
  }
  window.addEventListener('hashchange', function () {
    var i = fromHash();
    if (i !== null) { go(i); root.scrollIntoView({block: 'start'}); }
  });

  root.hidden = false;
  var start = fromHash();
  select(start === null ? 0 : start);
  if (start) viewport.scrollTo({left: offsetOf(start), behavior: 'auto'});
})();
</script>
