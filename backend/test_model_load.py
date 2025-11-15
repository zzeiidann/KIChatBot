"""
Script to convert Keras 3 model to compatible format
"""
import os
os.environ["TF_USE_LEGACY_KERAS"] = "0"

import zipfile
import json
import tensorflow as tf
import keras
from pathlib import Path

print(f"Using Keras: {keras.__version__}")
print(f"Using TensorFlow: {tf.__version__}")

model_path = Path(__file__).parent / "app" / "models" / "weights" / "skin_model.keras"

print(f"\n🔍 Loading model from: {model_path}")
print(f"📦 Size: {model_path.stat().st_size / (1024**3):.2f} GB\n")

# Extract and inspect
with zipfile.ZipFile(model_path, 'r') as z:
    print("📁 Archive contents:")
    for name in z.namelist():
        print(f"   - {name}")
    
    # Read config
    with z.open('config.json') as f:
        config = json.load(f)
    
    print(f"\n📋 Model class: {config.get('class_name')}")
    print(f"📋 Module: {config.get('module')}")
    
    # Check for custom objects
    if 'config' in config and 'layers' in config['config']:
        layers = config['config']['layers']
        custom_layers = set()
        for layer in layers:
            if layer.get('registered_name') and not layer['module']:
                custom_layers.add(layer['registered_name'])
        
        if custom_layers:
            print(f"\n⚠️  Custom layers detected: {custom_layers}")
            print("These need to be registered before loading!")

print("\n" + "="*60)
print("Attempting to load model...")
print("="*60 + "\n")

try:
    # Try to load
    model = keras.saving.load_model(str(model_path), compile=False)
    print("✅ SUCCESS! Model loaded!")
    print(f"📐 Input shape: {model.input_shape}")
    print(f"📊 Output shape: {model.output_shape}")
    print(f"🔢 Total layers: {len(model.layers)}")
    
    # Test prediction
    import numpy as np
    test_input = np.random.rand(1, 512, 512, 3).astype(np.float32)
    output = model.predict(test_input, verbose=0)
    print(f"\n✅ Test prediction successful!")
    print(f"   Output shape: {output.shape}")
    print(f"   Sum of probabilities: {output.sum():.6f}")
    
except Exception as e:
    print(f"❌ Failed to load: {e}")
    print(f"\nError type: {type(e).__name__}")
