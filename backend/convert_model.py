"""
Manual model reconstruction and weight loading
"""
import os
os.environ["TF_USE_LEGACY_KERAS"] = "0"
os.environ["KERAS_BACKEND"] = "tensorflow"

import zipfile
import json
import h5py
import numpy as np
import keras
from keras import layers
from pathlib import Path

print(f"Using Keras: {keras.__version__}\n")

model_path = Path("app/models/weights/skin_model.keras")

# Step 1: Extract weights to temporary location
weights_path = "/tmp/skin_model_weights.h5"
print("📦 Extracting weights...")

with zipfile.ZipFile(model_path, 'r') as z:
    with z.open('model.weights.h5') as src:
        with open(weights_path, 'wb') as dst:
            dst.write(src.read())

print(f"✅ Weights extracted to {weights_path}")

# Step 2: Try to load using Keras 2 compatibility
print("\n🔧 Attempting TF Keras (legacy) loading...")

try:
    os.environ["TF_USE_LEGACY_KERAS"] = "1"
    import tensorflow as tf
    
    # Load with TF Keras
    loaded_model = tf.keras.models.load_model(
        str(model_path),
        compile=False,
        custom_objects=None
    )
    
    print("✅ SUCCESS with TF Keras!")
    print(f"📐 Input shape: {loaded_model.input_shape}")
    print(f"📊 Output shape: {loaded_model.output_shape}")
    
    # Save in compatible format
    new_path = "app/models/weights/skin_model_converted.h5"
    loaded_model.save(new_path, save_format='h5')
    print(f"\n✅ Model saved to: {new_path}")
    print("   Use this .h5 file instead!")
    
    # Test prediction
    test_input = np.random.rand(1, 512, 512, 3).astype(np.float32)
    output = loaded_model.predict(test_input, verbose=0)
    print(f"\n✅ Test prediction successful!")
    print(f"   Output shape: {output.shape}")
    
except Exception as e:
    print(f"❌ TF Keras failed: {e}")
    print("\n⚠️  Model requires conversion from training environment")
    print("   Please run this in the original training environment:")
    print("   ```python")
    print("   model.save('skin_model.h5', save_format='h5')")
    print("   # or")
    print("   model.save('skin_model_saved', save_format='tf')")
    print("   ```")
