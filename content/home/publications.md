+++
# An instance of the Blank widget — the Research section.
# Documentation: https://wowchemy.com/docs/page-builder/

widget = "blank"
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 40  # Order that this section will appear.

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


The Lab for AI in Medicine at [TU Munich](https://www.tum.de/) develops algorithms and models to improve medicine for patients and healthcare professionals. Our aim is to develop artificial intelligence (AI) and machine learning (ML) techniques for the analysis and interpretation of biomedical data. The group focuses on pursuing blue-sky research, including:

- AI for the early detection, prediction and diagnosis of diseases
- AI for personalized interventions and therapies
- AI for the identification of new biomarkers and targets for therapy
- Safe, robust and interpretable AI approaches
- Privacy-preserving AI approaches

We have particularly strong interest in the application of imaging and computing technology to improve the understanding of brain development (in-utero and ex-utero), to improve the diagnosis and stratification of patients with dementia, stroke and traumatic brain injury, as well as for the comprehensive diagnosis and management of patients with cardiovascular disease and cancer.

The following research groups are based at the chair:

- [AI for biomedical image analysis and interpretation](#ai-for-biomedical-image-analysis-and-interpretation)
- [Inverse problems in biomedical imaging](#inverse-problems-in-biomedical-imaging)
- [Privacy-preserving and trustworthy AI in medicine](#privacy-preserving-and-trustworthy-ai-in-medicine)
- [AI for vision](#ai-for-vision)
- AI for opportunistic cardiac MRI

<div class="rw">
  <div class="rw-rail">
    <button type="button" class="rw-card" data-area="ai-for-biomedical-image-analysis-and-interpretation">
      <img class="rw-thumb" src="/home/harvey_research_1.png" alt="" loading="lazy">
      <span class="rw-card-body">
        <span class="rw-card-title">AI for biomedical image analysis and interpretation</span>
        <span class="rw-card-lead">Huaqi (Harvey) Qiu</span>
        <span class="rw-card-teaser">Medical imaging allows doctors to examine the interior structure or function of the human body, often without …</span>
      </span>
    </button>
    <button type="button" class="rw-card" data-area="inverse-problems-in-biomedical-imaging">
      <span class="rw-thumb rw-thumb-empty">No figure yet</span>
      <span class="rw-card-body">
        <span class="rw-card-title">Inverse problems in biomedical imaging</span>
        <span class="rw-card-lead">Ivan Ezhov · Sevgi Gokce Kafali</span>
        <span class="rw-card-teaser">Our group is working on inverse problems in biomedical imaging and their solution using artificial intelligenc…</span>
      </span>
    </button>
    <button type="button" class="rw-card" data-area="privacy-preserving-and-trustworthy-ai-in-medicine">
      <img class="rw-thumb" src="/home/privacy_research_2.png" alt="" loading="lazy">
      <span class="rw-card-body">
        <span class="rw-card-title">Privacy-preserving and trustworthy AI in medicine</span>
        <span class="rw-card-lead">Alexander Ziller</span>
        <span class="rw-card-teaser">Our group is developing the next generation of privacy-preserving, secure, and trustworthy AI algorithms for m…</span>
      </span>
    </button>
    <button type="button" class="rw-card" data-area="ai-for-vision">
      <span class="rw-thumb rw-thumb-empty">No figure yet</span>
      <span class="rw-card-body">
        <span class="rw-card-title">AI for vision</span>
        <span class="rw-card-lead">Martin Menten</span>
        <span class="rw-card-teaser">The AI for Vision group focuses on blue-sky research in medical image analysis with a particular focus on the …</span>
      </span>
    </button>
  </div>

<section class="rw-area" id="ai-for-biomedical-image-analysis-and-interpretation">
  <h2>AI for biomedical image analysis and interpretation</h2>
  <p class="rw-leads"><a href="/author/huaqi-harvey-qiu/">Huaqi (Harvey) Qiu</a></p>
  <p>Medical imaging allows doctors to examine the interior structure or function of the human body, often without the need for invasive surgical procedures. It comprises a range of different techniques, such as computed tomography (CT), magnetic resonance imaging (MR) and ultrasound (US). Clinicians rely on the information provided by medical imaging to monitor patients, diagnose illnesses and decide on treatment.</p>
  <p>Our mission is to support doctors in the clinical process and improve patient care by developing advanced algorithms that use artificial intelligence (AI) techniques. To this end, we create and improve machine learning (ML) algorithms for various parts of the medical imaging pipeline. At the image level, we develop methods to tackle tasks such as segmentation of relevant anatomical structures, registration of images across time or modalities, and enhancement of image quality. At the decision level, we innovate solutions to extract clinically useful information from medical images, diagnose diseases and predict future outcomes.</p>
  <p>Developing these algorithms in the medical domain presents many challenges which we are striving to overcome. Medical data is often sparse and annotations for algorithm training are costly to acquire, with problems such as domain shift plaguing the few available data, which could be detrimental to ML algorithms. For this, we are developing data-efficient and domain-robust solutions, as well as exploring opportunities provided by the increasing availability of large public datasets / biobanks. Medical images are usually accompanied by additional information from different sources such as doctor's notes, laboratory test results or genomics data, all of which should be considered when interpreting the images. Part of our research centers on developing multi-modal AI solutions that integrate these diverse data sources. Finally, to successfully deploy these algorithms in a hospital setting, we work in close collaboration with medical professionals to align our research with clinical value and to improve the interpretability of our ML algorithms to foster trust and facilitate adoption.</p>
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
    <summary>Key publications <span>10</span></summary>
    <ol>
      <li>Hager, P., Jungmann, F., Holland, R., Bhagat, K., Hubrecht, I., Knauer, M.M., Vielhauer, J., Makowski, M., Braren, R., Kaissis, G., & Rueckert, D. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. <em>Nature Medicine, 30</em>, 2613–2622.</li>
      <li>Dima, A.F., Zimmer, V.A., Menten, M.J., Li, H.B., Graf, M., Lemke, T., Raffler, P., Graf, R., Kirschke, J.S., Braren, R.F., & Rueckert, D. (2023). 3D Arterial Segmentation via Single 2D Projections and Depth Supervision in Contrast-Enhanced CT Images. <em>MICCAI</em>.</li>
      <li>Turgut, Ö., Müller, P., Hager, P., Shit, S., Starck, S., Menten, M.J., Martens, E., & Rueckert, D. (2023). Unlocking the Diagnostic Potential of ECG through Knowledge Transfer from Cardiac MRI.</li>
      <li>Müller, P., Kaissis, G., & Rueckert, D. (2024). ChEX: Interactive Localization and Region Description in Chest X-rays. <em>European Conference on Computer Vision</em>.</li>
      <li>Mueller, T.T., Starck, S., Bintsi, K., Ziller, A., Braren, R., Kaissis, G., & Rueckert, D. (2024). Are Population Graphs Really as Powerful as Believed? <em>Trans. Mach. Learn. Res., 2024</em>.</li>
      <li>Sideri-Lampretsa, V., McGinnis, J., Qiu, H., Paschali, M., Simson, W., & Rueckert, D. (2024). SINR: Spline-enhanced implicit neural representation for multi-modal registration. <em>Medical Imaging with Deep Learning</em>.</li>
      <li>Berger, A.H., Stucki, N., Lux, L., Buergin, V., Shit, S., Banaszak, A., Rueckert, D., Bauer, U., & Paetzold, J.C. (2024). Topologically faithful multi-class segmentation in medical images. <em>MICCAI</em>.</li>
      <li>Dannecker, M., Kyriakopoulou, V., Cordero-Grande, L., Price, A., Hajnal, J.V., & Rueckert, D. (2024). CINA: Conditional Implicit Neural Atlas for Spatio-Temporal Representation of Fetal Brains. <em>MICCAI</em>.</li>
      <li>Starck, S., Sideri-Lampretsa, V., Ritter, J. J., Zimmer, V. A., Braren, R., Mueller, T. T., & Rueckert, D. (2024). Using UK Biobank data to establish population-specific atlases from whole body MRI. <em>Communications Medicine, 4</em>(1), 237.</li>
      <li>Zhang, Y., Chen, C., Shit, S., Starck, S., Rueckert, D., & Pan, J. (2024). Whole heart 3D+t representation learning through sparse 2D cardiac MR images. <em>MICCAI</em> (pp. 359–369). Springer.</li>
    </ol>
  </details>
</section>

<section class="rw-area" id="inverse-problems-in-biomedical-imaging">
  <h2>Inverse problems in biomedical imaging</h2>
  <p class="rw-leads"><a href="/author/ivan-ezhov/">Ivan Ezhov</a> · <a href="/author/sevgi-gokce-kafali/">Sevgi Gokce Kafali</a></p>
  <p>Our group is working on inverse problems in biomedical imaging and their solution using artificial intelligence and machine learning.</p>
  <p>The development of algorithms to solve inverse problems arising in sensor and imaging systems has a long tradition. Examples include compressed sensing approaches, e.g. for medical and computational imaging. Until recently, most algorithms for inverse problems were based on statistical or physical signal models, such as wavelets or sparse representations. Our research focuses on novel approaches based on deep learning to accelerate solving such problems.</p>
  <p>We study how these deep learning-based approaches can be optimized for clinical applications and how they can be combined with image analysis methods. Deep learning-based approaches for reconstructing magnetic resonance imaging (MRI) or computed tomography (CT) provide efficient AI models, allowing the reconstruction of high-quality MRI images, and high-quality CT images from low-dose X-ray images. Recent works on generative models have shown great promise for accelerating reconstruction tasks to shorten the scan time in MRI, as well as generating images with much higher resolution than the acquired resolution (e.g. super-resolution). Here, we tackle these problems by utilizing AI (i.e., diffusion models) guided by readily available MR images from other organs/tissues, MRI scanning parameters, or other MRI physics-guided information.</p>
  <details class="rw-pubs">
    <summary>Key publications <span>11</span></summary>
    <ol>
      <li>Schlemper, J., Caballero, J., Hajnal, J.V., Price, A.N. & Rueckert, D. (2017). A deep cascade of convolutional neural networks for dynamic MR image reconstruction. <em>IEEE Transactions on Medical Imaging</em>.</li>
      <li>Qin, C., Schlemper, J., Caballero, J., Price, A.N., Hajnal, J.V. & Rueckert, D. (2018). Convolutional recurrent neural networks for dynamic MR image reconstruction. <em>IEEE Transactions on Medical Imaging</em>.</li>
      <li>Hammernik, K., Schlemper, J., Qin, C., Duan, J., Summers, R.M. & Rueckert, D. (2021). Systematic evaluation of iterative deep neural networks for fast parallel MRI reconstruction with sensitivity-weighted coil combination. <em>Magnetic Resonance in Medicine</em>.</li>
      <li>Hammernik, K., Küstner, T., Yaman, B., Huang, Z., Rueckert, D., Knoll, F. & Akçakaya, M. (2023). Physics-Driven Deep Learning for Computational Magnetic Resonance Imaging. <em>IEEE Signal Processing Magazine</em>.</li>
      <li>Huang, W., Li, H.B., Pan, J., Cruz, G., Rueckert, D. & Hammernik, K. (2023). Neural implicit k-space for binning-free non-cartesian cardiac MR imaging. <em>IPMI</em>.</li>
      <li>Pan, J., Hamdi, M., Huang, W., Hammernik, K., Kuestner, T. & Rueckert, D. (2024). Unrolled and rapid motion-compensated reconstruction for cardiac CINE MRI. <em>Medical Image Analysis</em>.</li>
      <li>Pan, J., Huang, W., Rückert, D., Küstner, T. & Hammernik, K. (2024). Reconstruction-driven motion estimation for motion-compensated MR CINE imaging. <em>IEEE Transactions on Medical Imaging</em>.</li>
      <li>Ezhov, I., Scibilia, K., Giannoni, L., Kofler, F., Iliash, I., Hsieh, F., Shit, S., Caredda, C., Lange, F., Montcel, B., Tachtsidis, I., & Rueckert, D. (2024). Learnable real-time inference of molecular composition from diffuse spectroscopy of brain tissue. <em>Journal of Biomedical Optics</em>.</li>
      <li>Chung, H., Lee, D., Wu, Z., Kim, B. H., Bouman, K. L., & Ye, J. C. (2025). ContextMRI: Enhancing Compressed Sensing MRI through Metadata Conditioning. <em>arXiv:2501.04284</em>.</li>
      <li>Jiang, L., Mao, Y., Wang, X., Chen, X., & Li, C. (2023). Cola-diff: Conditional latent diffusion model for multi-modal MRI synthesis. <em>MICCAI</em> (pp. 398–408). Springer.</li>
      <li>Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. <em>CVPR</em> (pp. 10684–10695).</li>
    </ol>
  </details>
</section>

<section class="rw-area" id="privacy-preserving-and-trustworthy-ai-in-medicine">
  <h2>Privacy-preserving and trustworthy AI in medicine</h2>
  <p class="rw-leads"><a href="/author/alexander-ziller/">Alexander Ziller</a></p>
  <p>Our group is developing the next generation of privacy-preserving, secure, and trustworthy AI algorithms for medical applications.</p>
  <p>AI in medicine requires large, diverse, and representative datasets to train fair, generalizable, and reliable models. However, such datasets often contain sensitive personal information. Privacy-preserving machine learning bridges the gap between data utilization and data protection by enabling the training of AI models on private data while providing formal privacy guarantees. Our group focuses on:</p>
  <p>Building trust in AI necessitates a comprehensive approach encompassing privacy, reliability, and security. Our work on trustworthy machine learning includes quantifying uncertainty in model outputs, incorporating domain expertise, developing probabilistic models to counteract poorly calibrated predictions, employing computational Bayesian techniques, and exploring the intersection of probabilistic and privacy-preserving machine learning. As AI systems increasingly integrate generative models like LLMs, we also work on establishing formal guarantees of safety and reliability for agentic LLM applications, exploring robustness in generative systems, and ensuring alignment of generative models with human values and ethical guidelines, particularly in high-stakes domains like healthcare.</p>
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
    <summary>Key publications <span>16</span></summary>
    <ol>
      <li>Kaiser, J., Ziller, A., Triantafillou, E., Rückert, D., & Kaissis, G. (2026). Your Privacy Depends on Others: Collusion Vulnerabilities in Individual Differential Privacy. <em>4th IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)</em>.</li>
      <li>Lockfisch, S., Schwethelm, K., Menten, M., Braren, R., Rueckert, D., Ziller, A., & Kaissis, G. (2025). On Arbitrary Predictions from Equally Valid Models. <em>AAAI Workshop on Navigating Model Uncertainty and the Rashomon Effect (MURE)</em>.</li>
      <li>Kaiser, J., Mueller, T., & Kaissis, G. (2025). Differential privacy in medical imaging applications. In <em>Trustworthy AI in Medical Imaging</em> (pp. 411–424). Academic Press.</li>
      <li>Koeken, A., Ziller, A., Knolle, M., & Rueckert, D. (2025). Sensitivity, Specificity, and Consistency: A Tripartite Evaluation of Privacy Filters for Synthetic Data Generation. <em>ICCV 2025 Workshop on Responsible Imaging</em>.</li>
      <li>Schwethelm, K., Kaiser, J., Kuntzer, J., Yiğitsoy, M., Rückert, D., & Kaissis, G. (2025). Differentially Private Active Learning: Balancing Effective Data Selection and Privacy. <em>IEEE SaTML</em> (pp. 858–878). doi:<a href="https://doi.org/10.1109/SaTML64287.2025.00053">10.1109/SaTML64287.2025.00053</a>.</li>
      <li>Schwethelm, K., Kaiser, J., Knolle, M., Lockfisch, S., Rueckert, D., & Ziller, A. (2025). Visual privacy auditing with diffusion models. <em>Transactions on Machine Learning Research</em>.</li>
      <li>Ziller, A., Mueller, T., Stieger, S., Feiner, L., Brandt, J., Braren, R., Rueckert, D., & Kaissis, G. (2024). Reconciling Privacy and Accuracy in AI for Medical Imaging. <em>Nature Machine Intelligence</em>.</li>
      <li>Kaess, P., Ziller, A., Mantz, L., Rueckert, D., Fintelmann, F. J., & Kaissis, G. (2024). Fair and private CT contrast agent detection. <em>MICCAI Workshop on Fairness of AI in Medical Imaging</em> (pp. 34–45). Springer.</li>
      <li>Kaissis, G., Kolek, S., Balle, B., Hayes, J., & Rueckert, D. (2024). Beyond the calibration point: Mechanism comparison in Differential Privacy. <em>International Conference on Machine Learning</em>.</li>
      <li>Tayebi Arasteh, S., Ziller, A., Kuhl, C., Makowski, M., Nebelung, S., Braren, R., Rueckert, D., Truhn, D., & Kaissis, G. (2024). Preserving fairness and diagnostic accuracy in private large-scale AI models for medical imaging. <em>Communications Medicine</em>.</li>
      <li>Hölzl, F. A., Rueckert, D., & Kaissis, G. (2023). Equivariant differentially private deep learning: Why DP-SGD needs sparser models. <em>16th ACM Workshop on Artificial Intelligence and Security</em> (pp. 11–22).</li>
      <li>Kaissis, G., Ziller, A., Kolek, S., Riess, A., & Rueckert, D. (2023). Optimal privacy guarantees for a relaxed threat model: Addressing sub-optimal adversaries in differentially private machine learning. <em>NeurIPS</em>.</li>
      <li>Mueller, T.T., Paetzold, J.C., Prabhakar, C., Usynin, D., Rueckert, D., & Kaissis, G. (2022). Differentially Private Graph Neural Networks for Whole-Graph Classification. <em>IEEE TPAMI</em>.</li>
      <li>Usynin, D., Ziller, A., Makowski, M., Braren, R., Rueckert, D., Glocker, B., Kaissis, G., & Passerat-Palmbach, J. (2021). Adversarial interference and its mitigations in privacy-preserving collaborative machine learning. <em>Nature Machine Intelligence</em>.</li>
      <li>Kaissis, G., Ziller, A., Passerat-Palmbach, J., Ryffel, T., Usynin, D., Trask, A., Lima Jr, I., Mancuso, J., Jungmann, F., Steinborn, M.M., & Saleh, A. (2021). End-to-end privacy preserving deep learning on multi-institutional medical imaging. <em>Nature Machine Intelligence</em>.</li>
      <li>Kaissis, G., Makowski, M.R., Rückert, D., & Braren, R.F. (2020). Secure, privacy-preserving and federated machine learning in medical imaging. <em>Nature Machine Intelligence</em>.</li>
    </ol>
  </details>
</section>

<section class="rw-area" id="ai-for-vision">
  <h2>AI for vision</h2>
  <p class="rw-leads"><a href="/author/martin-menten/">Martin Menten</a></p>
  <p>The AI for Vision group focuses on blue-sky research in medical image analysis with a particular focus on the application of machine learning and computer vision algorithms in the field of ophthalmology. Specifically, we are working on:</p>
  <p><em>*Self-supervised learning.</em>* Labeling medical data is very expensive, as it is time-consuming and requires expert knowledge. Moreover, medical data often includes highly sensitive information, making it challenging to share without compromising the privacy of the subjects involved. To overcome the limited availability of large annotated medical datasets, we are researching self-supervised learning, leveraging unlabeled medical data to enable neural networks to extract meaningful features that can be effectively adapted to a wide range of downstream tasks.</p>
  <p><em>*Multimodal deep learning.</em>* Clinicians rarely rely on a single source of information when diagnosing patients and deciding on a course of action. They consider an array of multimodal data, such as demographic and genomic information, patient interviews, laboratory test results and biomedical images. Our research focuses on developing deep learning algorithms capable of integrating diverse multimodal data to support autonomous and effective clinical decision making.</p>
  <p><em>*Deep learning for ophthalmology.</em>* Good vision is essential for navigating our environment, communicating, and performing everyday activities. As of 2020, more than 200 million people worldwide suffered from moderate to severe vision impairment. Driven by the comparative ease of imaging the eye and obtaining large imaging datasets, ophthalmology has been an early adopter of deep learning in healthcare. Our group's work in machine learning for ophthalmology simultaneously evaluates new algorithmic innovations while aiming to improve medical care for patients affected by ocular diseases.</p>
  <details class="rw-pubs">
    <summary>Key publications <span>7</span></summary>
    <ol>
      <li>Holland, R., Leingang, O., Bogunović, H., Riedl, S., Fritsche, L., Prevost, T., Scholl, H. P. N., Schmidt-Erfurth, U., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2024). Metadata-enhanced contrastive learning from retinal optical coherence tomography images. <em>Medical Image Analysis, 97</em>:103296.</li>
      <li>Kreitner, L., Paetzold, J. C., Rauch, N., Chen, C., Hagag, A. M., Fayed, A. E., Sivaprasad, S., Rausch, S., Weichsel, J., Menze, B. H., Harders, M., Knier, B., Rueckert, D., & Menten, M. J. (2024). Synthetic optical coherence tomography angiographs for detailed retinal vessel segmentation without human annotations. <em>IEEE Transactions on Medical Imaging, 43</em>(6):2061–2073.</li>
      <li>Menten, M. J., Paetzold, J. C., Zimmer, V. A., Shit, S., Ezhov, I., Holland, R., Probst, M., Schnabel, J. A., & Rueckert, D. (2023). A skeletonization algorithm for gradient-based optimization. <em>ICCV</em>, 21394–21403.</li>
      <li>Holland, R., Leingang, O., Holmes, C., Anders, P., Kaye, R., Riedl, S., Paetzold, J. C., Ezhov, I., Bogunović, H., Schmidt-Erfurth, U., Scholl, H. P. N., Sivaprasad, S., Lotery, A. J., Rueckert, D., & Menten, M. J. (2023). Clustering disease trajectories in contrastive feature space for biomarker proposal in age-related macular degeneration. <em>MICCAI</em>, 724–734.</li>
      <li>Menten, M. J., Holland, R., Leingang, O., Bogunović, H., Hagag, A. M., Kaye, R., Riedl, S., Traber, G. L., Hassan, O. N., Pawlowski, N., Glocker, B., Fritsche, L. G., Scholl, H. P. N., Sivaprasad, S., Schmidt-Erfurth, U., Rueckert, D., & Lotery, A. J. (2023). Exploring healthy retinal aging with deep learning. <em>Ophthalmology Science, 3</em>(3):100294.</li>
      <li>Hager, P., Menten, M. J., & Rueckert, D. (2023). Best of both worlds: Multimodal contrastive learning with tabular and imaging data. <em>CVPR</em>, 23924–23935.</li>
      <li>Menten, M. J., Paetzold, J. C., Dima, A., Menze, B. H., Knier, B., & Rueckert, D. (2022). Physiology-based simulation of the retinal vasculature enables annotation-free segmentation of OCT angiographs. <em>MICCAI</em>, 330–340.</li>
    </ol>
  </details>
</section>
</div>

<style>
/* Research areas: a horizontal rail of cards, with the selected area's full
   text below it. Prefixed .rw- so nothing collides with Bootstrap or the
   theme. Values follow Wowchemy: 1rem/1.5 body, headings at weight 500,
   #dee2e6 rules, rgba(0,0,0,.54) for secondary text. */
.rw-rail{display:flex;gap:1rem;overflow-x:auto;padding-bottom:.75rem;scroll-snap-type:x mandatory}
.rw-card{flex:0 0 15.5rem;scroll-snap-align:start;display:flex;flex-direction:column;overflow:hidden;
  border:1px solid #dee2e6;background:#fff;padding:0;text-align:left;font:inherit;color:#212529;cursor:pointer}
.rw-card:hover{border-color:#2962ff}
.rw-card[aria-current="true"]{border-color:#2962ff;box-shadow:inset 0 0 0 1px #2962ff}
.rw-thumb{height:6.5rem;width:100%;object-fit:cover;display:block;background:#f7f7f7}
.rw-thumb-empty{display:flex;align-items:center;justify-content:center;font-size:.875rem;color:rgba(0,0,0,.54)}
.rw-card-body{display:flex;flex-direction:column;gap:.3rem;padding:.75rem .875rem .875rem}
.rw-card-title{font-weight:500;line-height:1.3}
.rw-card-lead{font-size:.875rem;color:#2962ff}
.rw-card-teaser{font-size:.875rem;color:rgba(0,0,0,.54);line-height:1.45}
.rw-area{padding-top:1.25rem;border-top:1px solid #dee2e6;margin-top:.5rem}
.rw-area h2{font-size:1.5rem;font-weight:500;line-height:1.2;margin:0 0 .25rem}
.rw-leads{margin:0 0 1rem}
.rw-pubs{margin-top:1.125rem;border-top:1px solid #dee2e6;padding-top:.75rem}
.rw-pubs summary{cursor:pointer;font-weight:500}
.rw-pubs summary span{font-size:.875rem;color:rgba(0,0,0,.54);font-weight:400}
.rw-pubs ol{margin:.75rem 0 0;padding-left:1.25rem}
.rw-pubs li{margin-bottom:.5rem;font-size:.875rem;color:rgba(0,0,0,.54)}

/* Figure carousels inside an area - unchanged from the previous layout. */
.hrv-carousel{margin:1.5rem 0 2rem}
.hrv-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;
  -webkit-overflow-scrolling:touch;scrollbar-width:none}
.hrv-track::-webkit-scrollbar{display:none}
.hrv-slide{flex:0 0 100%;scroll-snap-align:center;margin:0;padding:0;text-align:center}
.hrv-slide img{width:100%;height:auto;display:block;object-fit:contain;background:#f7f7f7}
.hrv-slide figcaption{font-size:.875rem;color:rgba(0,0,0,.54);margin-top:.6rem;padding:0 .5rem;text-align:left}
.hrv-dots{display:flex;justify-content:center;gap:.6rem;margin-top:.9rem}
.hrv-dots a{width:11px;height:11px;border-radius:50%;background:#dee2e6}
.hrv-dots a:hover{background:rgba(0,0,0,.54)}
</style>

<script>
/* Progressive enhancement: without JavaScript every research area is visible
   and the rail is simply a set of links, which is how this section behaved
   before. With it, the rail selects one area at a time. Each area keeps its
   own id, so deep links such as #ai-for-vision still work - the handler below
   opens the matching card when the page loads on one. */
(function () {
  var cards = Array.prototype.slice.call(document.querySelectorAll('.rw-card'));
  var areas = Array.prototype.slice.call(document.querySelectorAll('.rw-area'));
  if (!cards.length || !areas.length) return;

  function select(slug, scroll) {
    areas.forEach(function (a) { a.style.display = (a.id === slug) ? '' : 'none'; });
    cards.forEach(function (c) { c.setAttribute('aria-current', c.dataset.area === slug); });
    if (scroll) {
      var el = document.getElementById(slug);
      if (el) el.scrollIntoView({ block: 'start', behavior: 'smooth' });
    }
  }
  cards.forEach(function (c) {
    c.addEventListener('click', function () { select(c.dataset.area, false); });
  });
  function fromHash() {
    var slug = decodeURIComponent(location.hash.slice(1));
    return areas.some(function (a) { return a.id === slug; }) ? slug : null;
  }
  window.addEventListener('hashchange', function () {
    var s = fromHash();
    if (s) select(s, true);
  });
  select(fromHash() || areas[0].id, false);
})();
</script>
