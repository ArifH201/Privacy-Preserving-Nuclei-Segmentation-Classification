# Privacy-Preserving Nuclei Segmentation & Tissue Classification using Federated Learning

## Overview

This project was developed as my Final Year Project for the BS Computer Science program at Bahria University.

The project focuses on nuclei segmentation and tissue classification from histopathology images using deep learning. It also implements Federated Learning to allow multiple clients to train a shared model without exchanging sensitive medical data. A Streamlit application was developed to provide an easy-to-use interface for image analysis and visualization.

---

## Features

- Nuclei segmentation using U-Net
- Tissue classification
- Federated Learning using Flower
- Medical image preprocessing
- Streamlit-based user interface
- Model training and evaluation

---

## Project Structure

```
Privacy-Preserving-Nuclei-Segmentation/

├── dataset/
├── federated/
├── models/
├── notebooks/
├── testing/
├── training/
├── ui/
├── utils/
├── README.md
├── requirements.txt
└── main.py
```

---

## Technologies Used

### Programming Language

- Python

### Deep Learning

- PyTorch
- U-Net

### Federated Learning

- Flower
- PySyft

### Computer Vision

- OpenCV
- MONAI

### Web Framework

- Streamlit

### Data Processing

- NumPy
- Pandas

---

## Dataset

The project uses the PanNuke dataset for nuclei segmentation and tissue classification.

The dataset is not included in this repository because of its large size.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/arifh201/Privacy-Preserving-Nuclei-Segmentation.git
```

Move to the project directory:

```bash
cd Privacy-Preserving-Nuclei-Segmentation
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the application using:

```bash
python main.py
```

or

```bash
streamlit run ui/streamlit_app.py
```

---

## Workflow

1. Load a histopathology image.
2. Apply image preprocessing.
3. Perform nuclei segmentation.
4. Classify the tissue type.
5. Train the model using Federated Learning.
6. Display the results in the Streamlit application.

---

## Results

The project successfully performs nuclei segmentation and tissue classification using deep learning. Federated Learning enables collaborative model training while preserving the privacy of medical data.

You can add screenshots of the application and prediction results in this section.

---

## Future Improvements

- Improve segmentation performance
- Deploy the application using Docker
- Support cloud-based Federated Learning
- Extend the system with additional tissue classes
- Optimize model training and inference

---

## Author

**Arif Hussain**

BS Computer Science  
Bahria University, Islamabad

Email: arif.Hussainn201@gmail.com

GitHub: https://github.com/arifh201
