# IISc Second Semester — 2026
### Aadithya Iyer | Department of Computational and Data Sciences, IISc Bangalore

This repository contains coursework, assignments, and code from my second semester at IISc. I took Introduction to NLP, NSDE, PP, and PRNN. For detailed lecture notes across all courses, see my OneNote:

📓 **[Lecture Notes — Semester 2](https://indianinstituteofscience-my.sharepoint.com/:o:/r/personal/aadithyaiyer_iisc_ac_in/_layouts/15/Doc.aspx?sourcedoc=%7B36D6A089-B241-460A-B501-77813EC1F518%7D&file=Lecture%20Notes%20Sem%202&action=edit&mobileredirect=true&wdorigin=Sharepoint)**



And my PRNN Github Repository for all 3 Assignments:
📓 **[PRNN Github Repository](https://github.com/ExusBurn/PRNN_Assignments)**

The notes are the primary study resource for all courses. This repository is best used alongside them — particularly for PRNN, where the assignments show how the theory from lectures translates into working implementations.

---

## Courses

### 🧠 Pattern Recognition and Neural Networks (PRNN)
**Instructor:** Prathosh A P | ECE, IISc

The main reason to look at this repo. Three assignments covering classical ML, deep learning, and generative/ensemble/RL methods — all implemented from scratch without high-level wrappers.

- **Assignment 1** — Classical ML: OLS, hard/soft-margin SVM, Lasso via Coordinate Descent, Ridge regression, GMM + EM algorithm, Logistic Regression (OvR), KNN, Naive Bayes, Bias-Variance decomposition via bootstrapping, Bayesian MAP estimation. Worked on real-world inspired datasets: bio-optic sensor calibration, oncology genomic arrays, ICU telemetry, and emergency room EHR records.
- **Assignment 2** — Deep Learning with PyTorch: MLP, CNN, Vanilla RNN, LSTM, GRU, Transformer, Vision Transformer (ViT), Transfer Learning (ResNet18), Focal Loss. Datasets: Delhi Air Quality, PlantVillage Crop Disease, APTOS 2019 Blindness Detection.
- **Assignment 3** — Ensembles, Generative Models & RL: Random Forest, AdaBoost, Gradient Boosting, PCA vs Linear Autoencoder, VAE, DCGAN, FID score, SimCLR (InfoNCE), REINFORCE policy gradients.

A good amount of ML was covered here end-to-end — from deriving the math to debugging real numerical issues like underflow, singular matrices, vanishing gradients, and mode collapse.

---

### ⚙️ Parallel Programming (PP)
**Focus:** HPC, MPI, CUDA, OpenMP

Assignments covering parallel algorithm design and implementation on CPUs and GPUs.

- **Longest Common Subsequence** — Parallel dynamic programming implementation
- **Shiloach-Vishkin Algorithm** — Parallel connected components on graphs
- **One-Sided Communication for Sparse Triangular Solve** — MPI one-sided (RMA) communication for solving sparse triangular systems
- **Final Project** — [Distributed Krylov Quantum Diagonalization](https://github.com/ExusBurn/Distributed-Krylov-Quantum-Diagonalization): GPU-accelerated statevector simulator for ground state energy estimation on the Heisenberg spin chain, with hand-written CUDA kernels, MPI task parallelism across 3 GPUs, and a 6.2× speedup over the CUDA-Q baseline at 23 qubits.

---

### 📐 Numerical Solution of Differential Equations (NSDE)

Assignments on classical numerical methods for ODEs and PDEs.

- **Assignment 1** — Heat equation (explicit/implicit finite difference schemes), Spring system of a harmonic oscillator (time integration methods)
- **Assignment 2** — Finite Element Method (FEM); Fourier spectra analysis of FTCS, FTBS, and other schemes for the advection-diffusion equation (stability, dispersion, dissipation)

---

### 💬 Natural Language Processing (NLP)

Course notes available in the OneNote linked above. It's not that relevant, since most things are just fill in the blanks-related code that mostly everyone can do easily. However if you are having issues with converting class slides to notes, please feel free to see all the relevant things within the Lecture Notes for Sem 2 for your benefit :).

---

## Notes

All lecture notes are maintained in OneNote and linked at the top of this README. The repository is primarily useful for:
- Seeing PRNN assignment solutions and how theory maps to code
- Reference implementations of parallel algorithms (PP)
- Numerical methods code for PDEs and ODEs (NSDE)
