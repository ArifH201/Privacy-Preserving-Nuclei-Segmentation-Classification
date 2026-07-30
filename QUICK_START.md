# ⚡ QUICK START - Get Running in 5 Minutes

## 🚀 Fastest Path to Results

### 1. Open PowerShell in Project Directory

```powershell
cd "c:\Users\OP\New folder\nuclei_fyp_project"
```

### 2. Install Dependencies (One Time Only)

```powershell
pip install -r requirements.txt
```

### 3. Run the Demo!

```powershell
python run_system.py
```

That's it! The system will:
- ✅ Start server
- ✅ Launch 2 clients
- ✅ Train for 5 federated rounds
- ✅ Save trained model
- ✅ Show results summary

**Total time**: ~5-10 minutes

---

## 📊 View Results

Once training completes, run ONE of these:

### Option A: For FYP Defense (RECOMMENDED)
```powershell
jupyter notebook notebooks/testing_and_visualization.ipynb
```
- Shows all metrics, visualizations, and analysis

### Option B: Interactive Dashboard
```powershell
streamlit run ui/streamlit_app.py
```
- Upload images and see predictions in real-time

---

## ❓ Common Issues & Fixes

### "ModuleNotFoundError"
```powershell
pip install -r requirements.txt -U
```

### "Port 8080 already in use"
```powershell
python run_system.py --server_address 127.0.0.1:8081
```

### "CUDA out of memory" (GPU error)
Just wait - it will use CPU automatically

### Very slow (CPU training)
This is normal. Grab ☕ and wait 5-10 minutes

---

## 📁 What You'll Get

After `python run_system.py` completes:

```
✅ models/global_weights.pth        (Trained model)
✅ Federated learning logs           (Training progress)
✅ Ready for Jupyter notebook        (Analysis)
✅ Ready for Streamlit dashboard     (Demo)
```

---

## 🎯 Use Case: FYP Defense

```powershell
# Step 1: Run demo
python run_system.py

# Step 2 (In new terminal): Show live dashboard while training
streamlit run ui/streamlit_app.py

# Step 3: After training done, run notebook for detailed results
jupyter notebook notebooks/testing_and_visualization.ipynb
```

---

## ✨ Command Reference

| Command | What it does |
|---------|--------------|
| `python run_system.py` | Full demo (server + 2 clients) |
| `python validate_project.py` | Check if setup is correct |
| `jupyter notebook notebooks/testing_and_visualization.ipynb` | Analysis notebook |
| `streamlit run ui/streamlit_app.py` | Interactive dashboard |
| `python run_system.py --num_rounds 10` | More training rounds |
| `python run_system.py --num_clients 3` | More clients |

---

## 📈 What Happens

1. **Server starts** (port 8080)
   ```
   [SERVER] Global model created with 2,150,000 parameters
   [SERVER] Waiting for clients...
   ```

2. **Clients connect** (auto)
   ```
   [CLIENT 0] Initialized with 20 training batches
   [CLIENT 1] Initialized with 20 training batches
   ```

3. **Training rounds** (automatic)
   ```
   [CLIENT 0] Training on local data...
   [SERVER] Round 1 Evaluation: Dice=0.72, Acc=0.82
   ```

4. **Model saved**
   ```
   ✅ Global model weights saved to models/global_weights.pth
   ```

---

## 🎓 For Your Defense

**Show your examiner:**

1. Running `python run_system.py` 
   - "This starts server and clients automatically"
   - "They train in parallel on private data"

2. The Jupyter notebook
   - Run cells one by one
   - Show metrics and visualizations
   - Explain privacy guarantees

3. The Streamlit dashboard
   - Upload an image
   - Show segmentation and classification
   - Demonstrate real-time inference

---

## ⏱️ Timeline

| Step | Time | Status |
|------|------|--------|
| Install packages | 5 min | One time only |
| Run demo | 5-10 min | Each run |
| View Jupyter | 2 min | Instant |
| Streamlit demo | Live | Instant |

**Total**: ~15 minutes from now to fully trained model + results

---

## 🔒 Privacy Explained (For Defense Q&A)

```
Your Data (Hospital A) ────→ Train Locally ────→ 
                               ↓
                          Only weights sent
                               ↓
                           Server ────→ Combine weights
                               ↓
                          Send back global model
                               ↓
Your Data (Hospital A) ────→ Next round training
        
⭐ KEY: Your data NEVER leaves your hospital!
```

---

## ✅ Quick Checklist

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Validation passed (`python validate_project.py`)
- [ ] Demo runs (`python run_system.py`)
- [ ] Model saved (`models/global_weights.pth` exists)
- [ ] Notebook runs (`jupyter notebook notebooks/testing_and_visualization.ipynb`)
- [ ] Dashboard works (`streamlit run ui/streamlit_app.py`)

---

## 💡 Pro Tips

1. **First run**: Use default settings (`python run_system.py`)
2. **Later runs**: Customize with flags
3. **Save outputs**: Take screenshots of results
4. **CPU is fine**: Training on CPU takes longer but works great
5. **Don't restart**: Let it finish even if it seems slow

---

## 🆘 Need Help?

Check these in order:
1. Error message in terminal
2. [SETUP.md](SETUP.md) - detailed setup guide
3. [README.md](README.md) - full documentation
4. Code comments in the Python files

---

## 🎉 Ready?

```powershell
cd "c:\Users\OP\New folder\nuclei_fyp_project"
python run_system.py
```

**Go!** ⚡

---

*Time to trained model: ~10 minutes*
*Time to see results: ~12 minutes*  
*Time to impress your examiners: ∞*
