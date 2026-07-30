"""
Project Initialization & Validation Script

Run this to verify the project is properly set up before running the demo.
"""

import sys
from pathlib import Path
import subprocess


def check_file(filepath: Path, description: str) -> bool:
    """Check if a file exists."""
    exists = filepath.exists()
    status = "✓" if exists else "✗"
    print(f"  {status} {description}")
    return exists


def check_directory(dirpath: Path, description: str) -> bool:
    """Check if a directory exists."""
    exists = dirpath.exists() and dirpath.is_dir()
    status = "✓" if exists else "✗"
    print(f"  {status} {description}")
    return exists


def main():
    """Validate project structure."""
    
    print("\n" + "=" * 70)
    print("Privacy-Preserving Nuclei Segmentation - Project Validation")
    print("=" * 70 + "\n")
    
    project_root = Path(__file__).parent
    all_ok = True
    
    # Check directories
    print("📁 Directory Structure:")
    required_dirs = [
        (project_root / "data", "data/"),
        (project_root / "models", "models/"),
        (project_root / "federated", "federated/"),
        (project_root / "utils", "utils/"),
        (project_root / "ui", "ui/"),
        (project_root / "notebooks", "notebooks/"),
    ]
    
    for dirpath, desc in required_dirs:
        if not check_directory(dirpath, desc):
            all_ok = False
    
    # Check core files
    print("\n📄 Core Files:")
    required_files = [
        (project_root / "requirements.txt", "requirements.txt"),
        (project_root / "run_system.py", "run_system.py (Main launcher)"),
        (project_root / "README.md", "README.md (Documentation)"),
        (project_root / "models" / "model.py", "models/model.py (Multi-Task U-Net)"),
        (project_root / "federated" / "server.py", "federated/server.py (Flower Server)"),
        (project_root / "federated" / "client.py", "federated/client.py (Flower Client)"),
        (project_root / "federated" / "federated_utils.py", "federated/federated_utils.py (Utils)"),
        (project_root / "utils" / "image_processing.py", "utils/image_processing.py"),
        (project_root / "utils" / "normalization.py", "utils/normalization.py (Stain Norm)"),
        (project_root / "utils" / "mock_data_generator.py", "utils/mock_data_generator.py (Synthetic Data)"),
        (project_root / "ui" / "streamlit_app.py", "ui/streamlit_app.py (Dashboard)"),
        (project_root / "notebooks" / "testing_and_visualization.ipynb", "notebooks/testing_and_visualization.ipynb"),
    ]
    
    for filepath, desc in required_files:
        if not check_file(filepath, desc):
            all_ok = False
    
    # Check Python version
    print("\n🐍 Python Version:")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"  ✓ Python {version.major}.{version.minor}.{version.micro}")
    else:
        print(f"  ✗ Python {version.major}.{version.minor}.{version.micro} (require 3.9+)")
        all_ok = False
    
    # Check dependencies
    print("\n📦 Dependencies:")
    dependencies = ['torch', 'flwr', 'numpy', 'cv2', 'pandas', 'streamlit', 'sklearn', 'matplotlib', 'albumentations']
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"  ✓ {dep}")
        except ImportError:
            print(f"  ✗ {dep} (Install with: pip install -r requirements.txt)")
            all_ok = False
    
    # Summary
    print("\n" + "=" * 70)
    if all_ok:
        print("✅ PROJECT VALIDATION SUCCESSFUL!")
        print("\n🚀 Ready to run:")
        print("   python run_system.py")
        print("\n📊 After training, view results:")
        print("   jupyter notebook notebooks/testing_and_visualization.ipynb")
        print("   streamlit run ui/streamlit_app.py")
    else:
        print("❌ Some issues found. Please fix them before running.")
        print("\n💡 Run this to install dependencies:")
        print("   pip install -r requirements.txt")
    
    print("=" * 70 + "\n")
    
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
