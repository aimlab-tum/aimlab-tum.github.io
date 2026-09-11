+++
title = "Inverse problems in biomedical imaging"
weight = 20

publications = [
  "Schlemper, J., Caballero, J., Hajnal, J.V., Price, A.N. & Rueckert, D. (2017). A deep cascade of convolutional neural networks for dynamic MR image reconstruction. *IEEE Transactions on Medical Imaging*.",
  "Qin, C., Schlemper, J., Caballero, J., Price, A.N., Hajnal, J.V. & Rueckert, D. (2018). Convolutional recurrent neural networks for dynamic MR image reconstruction. *IEEE Transactions on Medical Imaging*.",
  "Hammernik, K., Schlemper, J., Qin, C., Duan, J., Summers, R.M. & Rueckert, D. (2021). Systematic evaluation of iterative deep neural networks for fast parallel MRI reconstruction with sensitivity-weighted coil combination. *Magnetic Resonance in Medicine*.",
  "Hammernik, K., Küstner, T., Yaman, B., Huang, Z., Rueckert, D., Knoll, F. & Akçakaya, M. (2023). Physics-Driven Deep Learning for Computational Magnetic Resonance Imaging. *IEEE Signal Processing Magazine*.",
  "Huang, W., Li, H.B., Pan, J., Cruz, G., Rueckert, D. & Hammernik, K. (2023). Neural implicit k-space for binning-free non-cartesian cardiac MR imaging. *IPMI*.",
  "Pan, J., Hamdi, M., Huang, W., Hammernik, K., Kuestner, T. & Rueckert, D. (2024). Unrolled and rapid motion-compensated reconstruction for cardiac CINE MRI. *Medical Image Analysis*.",
  "Pan, J., Huang, W., Rückert, D., Küstner, T. & Hammernik, K. (2024). Reconstruction-driven motion estimation for motion-compensated MR CINE imaging. *IEEE Transactions on Medical Imaging*.",
  "Ezhov, I., Scibilia, K., Giannoni, L., Kofler, F., Iliash, I., Hsieh, F., Shit, S., Caredda, C., Lange, F., Montcel, B., Tachtsidis, I., & Rueckert, D. (2024). Learnable real-time inference of molecular composition from diffuse spectroscopy of brain tissue. *Journal of Biomedical Optics*.",
  "Chung, H., Lee, D., Wu, Z., Kim, B. H., Bouman, K. L., & Ye, J. C. (2025). ContextMRI: Enhancing Compressed Sensing MRI through Metadata Conditioning. *arXiv:2501.04284*.",
  "Jiang, L., Mao, Y., Wang, X., Chen, X., & Li, C. (2023). Cola-diff: Conditional latent diffusion model for multi-modal MRI synthesis. *MICCAI* (pp. 398–408). Springer.",
  "Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. *CVPR* (pp. 10684–10695).",
]

# Each lead is a name and the author page it links to.
[[leads]]
  name = "Ivan Ezhov"
  url = "/author/ivan-ezhov/"

[[leads]]
  name = "Sevgi Gokce Kafali"
  url = "/author/sevgi-gokce-kafali/"

+++
Our group is working on inverse problems in biomedical imaging and their solution using artificial intelligence and machine learning.

The development of algorithms to solve inverse problems arising in sensor and imaging systems has a long tradition. Examples include compressed sensing approaches, e.g. for medical and computational imaging. Until recently, most algorithms for inverse problems were based on statistical or physical signal models, such as wavelets or sparse representations. Our research focuses on novel approaches based on deep learning to accelerate solving such problems.

We study how these deep learning-based approaches can be optimized for clinical applications and how they can be combined with image analysis methods. Deep learning-based approaches for reconstructing magnetic resonance imaging (MRI) or computed tomography (CT) provide efficient AI models, allowing the reconstruction of high-quality MRI images, and high-quality CT images from low-dose X-ray images. Recent works on generative models have shown great promise for accelerating reconstruction tasks to shorten the scan time in MRI, as well as generating images with much higher resolution than the acquired resolution (e.g. super-resolution). Here, we tackle these problems by utilizing AI (i.e., diffusion models) guided by readily available MR images from other organs/tissues, MRI scanning parameters, or other MRI physics-guided information.
