# Complete Kaggle Training & Testing Workflow

## Overview

This document provides step-by-step instructions for training and testing the federated learning project on Kaggle.

---

## Before You Start

**Prerequisites:**
- Kaggle account (free tier available)
- Project files uploaded or Git repo linked
- 5-30 minutes depending on configuration

---

## Step 1: Create Kaggle Notebook

1. Go to **kaggle.com**
2. Click **Notebooks** (top menu)
3. Click **+ New Notebook**
4. Choose **Python** as kernel
5. Set **Accelerator** to **GPU** (Settings → Accelerator)
6. Name it: `Federated Learning Training`

---

## Step 2: Add Dataset Input

1. Click **+ Add input** (right side)
2. Search for and add: `nuclei-fyp-project` (your uploaded dataset)
3. Or import from GitHub if you linked it

---

## Step 3: Copy Test Notebook Cells

Copy these cells into your Kaggle notebook **in order**:

### **Cell 1: Environment Setup**
```python
# Install dependencies
!pip install -q torch torchvision torchaudio
!pip install -q flwr
!pip install -q scikit-image scikit-learn albumentations
!pip install -q opencv-python

print("✓ Dependencies installed")
```

### **Cell 2: Setup Path**
```python
import sys
sys.path.insert(0, '/kaggle/input/nuclei-fyp-project/nuclei_fyp_project')

print("✓ Project path configured")
```

### **Cell 3: Environment Check**
```python
import torch
import os

print(f"PyTorch Version: {torch.__version__}")
print(f"GPU Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("WARNING: No GPU available. Training will be slow on CPU.")
```

**Expected Output:**
```
PyTorch Version: 2.0.1+cu118
GPU Available: True
GPU Device: Tesla P100-PCIE-16GB (or similar)
GPU Memory: 16.0 GB
```

### **Cell 4: Test Imports**
```python
print("Testing imports...")

try:
    from models.model import MultiTaskUNet
    print("  ✓ Model imported")
    
    from utils.mock_data_generator import SyntheticHEImageGenerator
    print("  ✓ Data generator imported")
    
    from utils.normalization import ReinhardNormalizer
    print("  ✓ Normalizer imported")
    
    from federated.federated_utils import DiceLoss, average_weights
    print("  ✓ Federated utils imported")
    
    from federated.kaggle_training import KaggleTrainer
    print("  ✓ Kaggle trainer imported")
    
    print("\n✓✓ All imports successful!")

except Exception as e:
    print(f"✗ Import failed: {e}")
    raise
```

**Expected Output:**
```
Testing imports...
  ✓ Model imported
  ✓ Data generator imported
  ✓ Normalizer imported
  ✓ Federated utils imported
  ✓ Kaggle trainer imported

✓✓ All imports successful!
```

### **Cell 5: Test Model**
```python
import torch
from models.model import MultiTaskUNet

print("Testing model...")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create model
model = MultiTaskUNet(
    in_channels=3,
    out_channels_seg=1,
    out_channels_cls=4,
    depth=4
)
model = model.to(device)

# Count parameters
total_params = sum(p.numel() for p in model.parameters())
print(f"✓ Model created: {total_params:,} parameters")

# Test forward pass
model.eval()
test_input = torch.randn(1, 3, 256, 256).to(device)

with torch.no_grad():
    seg_out, cls_out = model(test_input)

print(f"✓ Segmentation output: {seg_out.shape}")
print(f"✓ Classification output: {cls_out.shape}")
print("✓ Model test passed!")
```

**Expected Output:**
```
Testing model...
✓ Model created: 2,151,172 parameters
✓ Segmentation output: torch.Size([1, 1, 256, 256])
✓ Classification output: torch.Size([1, 4])
✓ Model test passed!
```

### **Cell 6: Test Data Generation**
```python
import numpy as np
from utils.mock_data_generator import SyntheticHEImageGenerator

print("Testing data generation...")

generator = SyntheticHEImageGenerator(image_size=256)
images, seg_masks, cls_labels = generator.generate_dataset(num_images=5)

print(f"✓ Generated {len(images)} images")
print(f"  - Images shape: {images.shape}")
print(f"  - Masks shape: {seg_masks.shape}")
print(f"  - Labels shape: {cls_labels.shape}")

# Verify ranges
assert images.min() >= 0 and images.max() <= 255
assert seg_masks.min() >= 0 and seg_masks.max() <= 1
assert cls_labels.min() >= 0 and cls_labels.max() < 4

print("✓ Data generation test passed!")
```

**Expected Output:**
```
Testing data generation...
✓ Generated 5 images
  - Images shape: (5, 3, 256, 256)
  - Masks shape: (5, 1, 256, 256)
  - Labels shape: (5,)
✓ Data generation test passed!
```

### **Cell 7: Mini Training (2-3 minutes)**
```python
from federated.kaggle_training import KaggleTrainer

print("Running mini training test (1 round)...")
print("Expected time: 2-3 minutes\n")

trainer = KaggleTrainer()
model = trainer.train(
    num_rounds=1,
    num_clients=1,
    num_epochs=1,
    batch_size=16,
    learning_rate=0.001
)

print("\n✓ Mini training complete!")
print("Ready for full training!")
```

**Expected Output:**
```
Running mini training test (1 round)...
Expected time: 2-3 minutes

============================================================
FEDERATED LEARNING TRAINING (KAGGLE OPTIMIZED)
============================================================
Configuration:
  Rounds: 1
  Clients: 1
  Epochs per client: 1
  Batch size: 16
  Learning rate: 0.001
  Device: cuda

============================================================

[STEP 1] Generating synthetic H&E data for 1 clients...
  • Client 1/1: Generating 30 images...
✓ Generated 30 total images

[STEP 2] Setting up stain normalization...
✓ Stain normalizer fitted on reference images

[STEP 3] Starting federated training for 1 rounds...

============================================================
ROUND 1/1
============================================================

  Client 1/1 Local Training:
    Training for 1 epochs...
      Epoch 1/1: Loss = 0.7234
    Evaluating...
    ✓ Dice Score: 0.6842
    ✓ Accuracy: 0.8500

  Server Aggregation:
    ✓ Weights aggregated from 1 clients

  Round 1 Summary:
    Average Dice: 0.6842
    Average Accuracy: 0.8500

============================================================
TRAINING COMPLETE
============================================================

✓ Mini training complete!
Ready for full training!
```

### **Cell 8: Full Training (10-30 minutes)**
```python
from federated.kaggle_training import train_federated_kaggle

print("Starting full federated training...")
print("Expected time: 10-30 minutes (depends on config)\n")

# Full training configuration
model = train_federated_kaggle(
    num_rounds=3,          # 3 communication rounds
    num_clients=2,         # 2 federated clients
    num_epochs=2,          # 2 local epochs per round
    batch_size=8,          # Small batch for free tier
    learning_rate=0.001,
    output_path='/kaggle/working'
)

print("\n✓ Full training complete!")
print("Model saved to: /kaggle/working/federated_model.pth")
```

**Expected Output:**
```
Starting full federated training...
Expected time: 10-30 minutes (depends on config)

============================================================
FEDERATED LEARNING TRAINING (KAGGLE OPTIMIZED)
============================================================
Configuration:
  Rounds: 3
  Clients: 2
  Epochs per client: 2
  Batch size: 8
  Learning rate: 0.001
  Device: cuda

============================================================

[STEP 1] Generating synthetic H&E data for 2 clients...
  • Client 1/2: Generating 30 images...
  • Client 2/2: Generating 30 images...
✓ Generated 60 total images

[STEP 2] Setting up stain normalization...
✓ Stain normalizer fitted on reference images

[STEP 3] Starting federated training for 3 rounds...

============================================================
ROUND 1/3
============================================================

  Client 1/2 Local Training:
    Training for 2 epochs...
      Epoch 1/2: Loss = 0.6234
      Epoch 2/2: Loss = 0.5421
    Evaluating...
    ✓ Dice Score: 0.7123
    ✓ Accuracy: 0.8600

  Client 2/2 Local Training:
    Training for 2 epochs...
      Epoch 1/2: Loss = 0.5876
      Epoch 2/2: Loss = 0.5123
    Evaluating...
    ✓ Dice Score: 0.7456
    ✓ Accuracy: 0.8750

  Server Aggregation:
    ✓ Weights aggregated from 2 clients

  Round 1 Summary:
    Average Dice: 0.7290
    Average Accuracy: 0.8675

============================================================
ROUND 2/3
...
[Similar output for rounds 2 and 3]

============================================================
TRAINING COMPLETE
============================================================

✓ Full training complete!
Model saved to: /kaggle/working/federated_model.pth
```

### **Cell 9: Visualize Results (Optional)**
```python
import torch
import numpy as np
import matplotlib.pyplot as plt
from utils.mock_data_generator import SyntheticHEImageGenerator
from utils.normalization import ReinhardNormalizer

print("Generating visualization...")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load trained model
model.eval()

# Generate test images
gen = SyntheticHEImageGenerator(256)
test_images, test_masks, test_labels = gen.generate_dataset(num_images=4)

# Normalize
norm = ReinhardNormalizer()
norm.fit(test_images[:2])
norm_images = norm.normalize_batch(test_images)

# Tissue names
tissues = ['Tumor', 'Inflammatory', 'Stroma', 'Necrosis']

# Visualize
fig, axes = plt.subplots(4, 4, figsize=(16, 12))

with torch.no_grad():
    for i in range(4):
        img_tensor = torch.from_numpy(norm_images[i]).unsqueeze(0).float().to(device)
        seg_pred, cls_pred = model(img_tensor)
        
        seg_mask = (seg_pred[0, 0].cpu().numpy() > 0.5).astype(np.uint8)
        tissue = tissues[cls_pred[0].argmax().item()]
        
        # Original
        axes[i, 0].imshow(test_images[i].transpose(1, 2, 0).astype(np.uint8))
        axes[i, 0].set_title(f'Original {i+1}')
        axes[i, 0].axis('off')
        
        # Normalized
        axes[i, 1].imshow(norm_images[i].transpose(1, 2, 0).astype(np.uint8))
        axes[i, 1].set_title(f'Normalized {i+1}')
        axes[i, 1].axis('off')
        
        # Predicted Segmentation
        axes[i, 2].imshow(seg_mask, cmap='gray')
        axes[i, 2].set_title(f'Seg Pred {i+1}')
        axes[i, 2].axis('off')
        
        # Ground Truth
        axes[i, 3].imshow(test_masks[i, 0], cmap='gray')
        axes[i, 3].set_title(f'GT {i+1} ({tissue})')
        axes[i, 3].axis('off')

plt.tight_layout()
plt.savefig('/kaggle/working/results_visualization.png', dpi=100, bbox_inches='tight')
print("✓ Visualization saved to /kaggle/working/results_visualization.png")
plt.show()
```

### **Cell 10: Export Results**
```python
import os
import pandas as pd

output_dir = '/kaggle/working'
files = os.listdir(output_dir)

print("Output files ready for download:")
print("-" * 50)
for f in files:
    path = os.path.join(output_dir, f)
    size = os.path.getsize(path) / 1e6  # MB
    print(f"  • {f:<40} ({size:.1f} MB)")

print("\nDownload these files from Kaggle Notebook Output:")
print("  1. federated_model.pth - Trained model weights")
print("  2. model_weights.npy - Raw weight matrices")
print("  3. results_visualization.png - Segmentation results")
```

---

## Step 4: Run Notebook

1. Click **Run all** (or run cells individually)
2. Watch progress in the output
3. Cells 1-4 should complete in <1 minute
4. Cell 5-6 should complete in ~2-3 minutes
5. Cell 7 (mini training) should complete in 2-3 minutes
6. Cell 8 (full training) should complete in 10-30 minutes depending on config

---

## Step 5: Download Results

1. After training completes, click **Output** (right side)
2. Download:
   - `federated_model.pth` - Trained model
   - `model_weights.npy` - Weight matrices
   - `results_visualization.png` - Results images

---

## Configuration Recommendations

### For Free Tier (Limited GPU Time):
```python
num_rounds=2
num_clients=1
num_epochs=1
batch_size=16
# Total time: ~5-10 minutes
```

### For Pro Tier (More GPU Time):
```python
num_rounds=3
num_clients=2
num_epochs=2
batch_size=8
# Total time: ~15-25 minutes
```

### For Best Results (Max Time):
```python
num_rounds=5
num_clients=3
num_epochs=3
batch_size=8
# Total time: ~45-60 minutes
```

---

## Troubleshooting

### Issue: GPU Not Available
```python
import torch
if not torch.cuda.is_available():
    print("GPU not available. Check:")
    print("1. Settings → Accelerator = GPU")
    print("2. Try restarting kernel")
```

### Issue: Out of Memory
```python
# Reduce batch size
batch_size = 4  # instead of 8

# Or reduce other parameters
num_clients = 1
num_epochs = 1
```

### Issue: Timeout (9-hour limit)
```python
# Reduce training
num_rounds = 2
num_clients = 1
num_epochs = 1
```

### Issue: Import Errors
```python
# Reinstall dependencies at top of notebook
!pip install -q --upgrade torch flwr scikit-image albumentations
```

---

## Expected Results

| Metric | Value |
|--------|-------|
| **Training Time** | 5-30 min (depends on config) |
| **Model Size** | ~8.5 MB |
| **Segmentation Dice** | 0.65-0.80 |
| **Classification Accuracy** | 0.75-0.90 |
| **Privacy** | ✓ Data stays local |

---

## Making Notebook Public (Optional)

To share your notebook with others:

1. Click **Share** (top right)
2. Set to **Public**
3. Get shareable link
4. Anyone with link can view or run

---

## Next Steps

After successful Kaggle training:

1. ✅ Download trained model
2. ✅ Try different configurations
3. ✅ Use model for inference on new images
4. ✅ Modify architecture for better performance
5. ✅ Use real data instead of synthetic (optional)

