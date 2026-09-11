+++
title = "Privacy-preserving and trustworthy AI in medicine"
weight = 30

publications = [
  "Kaiser, J., Ziller, A., Triantafillou, E., Rückert, D., & Kaissis, G. (2026). Your Privacy Depends on Others: Collusion Vulnerabilities in Individual Differential Privacy. *4th IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)*.",
  "Lockfisch, S., Schwethelm, K., Menten, M., Braren, R., Rueckert, D., Ziller, A., & Kaissis, G. (2025). On Arbitrary Predictions from Equally Valid Models. *AAAI Workshop on Navigating Model Uncertainty and the Rashomon Effect (MURE)*.",
  "Kaiser, J., Mueller, T., & Kaissis, G. (2025). Differential privacy in medical imaging applications. In *Trustworthy AI in Medical Imaging* (pp. 411–424). Academic Press.",
  "Koeken, A., Ziller, A., Knolle, M., & Rueckert, D. (2025). Sensitivity, Specificity, and Consistency: A Tripartite Evaluation of Privacy Filters for Synthetic Data Generation. *ICCV 2025 Workshop on Responsible Imaging*.",
  "Schwethelm, K., Kaiser, J., Kuntzer, J., Yiğitsoy, M., Rückert, D., & Kaissis, G. (2025). Differentially Private Active Learning: Balancing Effective Data Selection and Privacy. *IEEE SaTML* (pp. 858–878). doi:[10.1109/SaTML64287.2025.00053](https://doi.org/10.1109/SaTML64287.2025.00053).",
  "Schwethelm, K., Kaiser, J., Knolle, M., Lockfisch, S., Rueckert, D., & Ziller, A. (2025). Visual privacy auditing with diffusion models. *Transactions on Machine Learning Research*.",
  "Ziller, A., Mueller, T., Stieger, S., Feiner, L., Brandt, J., Braren, R., Rueckert, D., & Kaissis, G. (2024). Reconciling Privacy and Accuracy in AI for Medical Imaging. *Nature Machine Intelligence*.",
  "Kaess, P., Ziller, A., Mantz, L., Rueckert, D., Fintelmann, F. J., & Kaissis, G. (2024). Fair and private CT contrast agent detection. *MICCAI Workshop on Fairness of AI in Medical Imaging* (pp. 34–45). Springer.",
  "Kaissis, G., Kolek, S., Balle, B., Hayes, J., & Rueckert, D. (2024). Beyond the calibration point: Mechanism comparison in Differential Privacy. *International Conference on Machine Learning*.",
  "Tayebi Arasteh, S., Ziller, A., Kuhl, C., Makowski, M., Nebelung, S., Braren, R., Rueckert, D., Truhn, D., & Kaissis, G. (2024). Preserving fairness and diagnostic accuracy in private large-scale AI models for medical imaging. *Communications Medicine*.",
  "Hölzl, F. A., Rueckert, D., & Kaissis, G. (2023). Equivariant differentially private deep learning: Why DP-SGD needs sparser models. *16th ACM Workshop on Artificial Intelligence and Security* (pp. 11–22).",
  "Kaissis, G., Ziller, A., Kolek, S., Riess, A., & Rueckert, D. (2023). Optimal privacy guarantees for a relaxed threat model: Addressing sub-optimal adversaries in differentially private machine learning. *NeurIPS*.",
  "Mueller, T.T., Paetzold, J.C., Prabhakar, C., Usynin, D., Rueckert, D., & Kaissis, G. (2022). Differentially Private Graph Neural Networks for Whole-Graph Classification. *IEEE TPAMI*.",
  "Usynin, D., Ziller, A., Makowski, M., Braren, R., Rueckert, D., Glocker, B., Kaissis, G., & Passerat-Palmbach, J. (2021). Adversarial interference and its mitigations in privacy-preserving collaborative machine learning. *Nature Machine Intelligence*.",
  "Kaissis, G., Ziller, A., Passerat-Palmbach, J., Ryffel, T., Usynin, D., Trask, A., Lima Jr, I., Mancuso, J., Jungmann, F., Steinborn, M.M., & Saleh, A. (2021). End-to-end privacy preserving deep learning on multi-institutional medical imaging. *Nature Machine Intelligence*.",
  "Kaissis, G., Makowski, M.R., Rückert, D., & Braren, R.F. (2020). Secure, privacy-preserving and federated machine learning in medical imaging. *Nature Machine Intelligence*.",
]

# Each lead is a name and the author page it links to.
[[leads]]
  name = "Alexander Ziller"
  url = "/author/alexander-ziller/"

# Figures live beside this file. The first is the one the slide shows;
# the rest are kept with their captions for whatever shows them next.
[[figures]]
  file = "figure.png"
  alt = "Threat models in privacy-preserving machine learning and their impact on the necessary privacy protection and model performance"
  caption = '''<strong>a,</strong> Adversaries can have various capabilities depending on the setting. <strong>b,</strong> The combination of the adversary's capabilities defines the threat model. In a worst-case analysis, they have all capabilities. However, access to the database is a pessimistic, practically irrelevant scenario. <strong>c,</strong> The necessary privacy protection depends on the threat model. In a worst-case threat model, the adversary only needs to match the model and gradient to an image in the database. In a practically more relevant scenario, the image must be reconstructed from the model and gradient. Here, much less privacy protection is necessary. <strong>d,</strong> The more stringent the privacy protection is chosen, the higher the impacts on the model performance are. Thus, if a realistic threat model is considered appropriate, models can perform better.'''

[[figures]]
  file = "figure-2.png"
  alt = "Integrated framework for privacy-preserving and secure AI across the machine learning lifecycle"
  caption = "This diagram presents an integrated framework for privacy-preserving and secure AI, highlighting technologies that safeguard both data and algorithms throughout the machine learning lifecycle. Under the Private AI paradigm, techniques like differential privacy protect sensitive medical data from identity leakage and inference attacks. On the Secure AI side, methods such as federated learning, secure multiparty computation, and homomorphic encryption enable collaborative model training without direct data sharing, defending against model theft, inversion, and adversarial manipulation. Together, these methods ensure that both patient data and algorithmic integrity are preserved in sensitive domains like healthcare."

+++
Our group is developing the next generation of privacy-preserving, secure, and trustworthy AI algorithms for medical applications.

AI in medicine requires large, diverse, and representative datasets to train fair, generalizable, and reliable models. However, such datasets often contain sensitive personal information. Privacy-preserving machine learning bridges the gap between data utilization and data protection by enabling the training of AI models on private data while providing formal privacy guarantees. Our group focuses on:

- Differential privacy (DP) theory and applications to machine learning and deep learning, targeting both unstructured datasets (e.g., images) and structured data (e.g., tabular and graph databases).
- Generative models and their applications, such as large language models (LLMs) and agentic systems, integrating differential privacy to ensure secure and privacy-preserving outcomes.
- Data attribution techniques, which enable transparent and accountable data usage in training and inference.
- Developing techniques to mitigate trade-offs between privacy, model utility, and computational efficiency.
- AI security, including the study of vulnerabilities in collaborative machine learning protocols (e.g., federated learning) and designing robust defense mechanisms against adversarial attacks.

Building trust in AI necessitates a comprehensive approach encompassing privacy, reliability, and security. Our work on trustworthy machine learning includes quantifying uncertainty in model outputs, incorporating domain expertise, developing probabilistic models to counteract poorly calibrated predictions, employing computational Bayesian techniques, and exploring the intersection of probabilistic and privacy-preserving machine learning. As AI systems increasingly integrate generative models like LLMs, we also work on establishing formal guarantees of safety and reliability for agentic LLM applications, exploring robustness in generative systems, and ensuring alignment of generative models with human values and ethical guidelines, particularly in high-stakes domains like healthcare.
