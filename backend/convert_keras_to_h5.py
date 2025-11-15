"""
Script untuk convert model Keras 3 (.keras) ke format .h5

CARA PAKAI:
1. Pastikan file skin_model.keras ada di backend/app/models/weights/
2. Jalankan: python convert_keras_to_h5.py
3. File skin_model.h5 akan dibuat di folder yang sama

REQUIREMENTS:
- TensorFlow 2.17+
- Keras 3.12+
"""

import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"  # Use legacy for .h5 compatibility

from pathlib import Path
import sys

print("="*80)
print("KERAS MODEL CONVERTER - .keras to .h5")
print("="*80)

# Paths
weights_dir = Path(__file__).parent / "app" / "models" / "weights"
keras_file = weights_dir / "skin_model.keras"
h5_file = weights_dir / "skin_model.h5"

print(f"\nInput:  {keras_file}")
print(f"Output: {h5_file}")

# Check if .keras file exists
if not keras_file.exists():
    print(f"\n❌ ERROR: File not found: {keras_file}")
    print("\nPastikan file skin_model.keras ada di folder:")
    print(f"   {weights_dir}/")
    sys.exit(1)

print(f"\n📦 Model size: {keras_file.stat().st_size / (1024**3):.2f} GB")

# Try to load and convert
try:
    print("\n🔧 Loading model...")
    
    # Try different loading methods
    loaded = False
    model = None
    
    # Method 1: Try with TF Keras (legacy)
    try:
        import tensorflow as tf
        print("   Trying TensorFlow Keras (legacy mode)...")
        model = tf.keras.models.load_model(str(keras_file), compile=False)
        loaded = True
        print("   ✅ Loaded with TF Keras!")
    except Exception as e1:
        print(f"   ⚠️  TF Keras failed: {str(e1)[:100]}")
        
        # Method 2: Try with Keras 3
        try:
            os.environ["TF_USE_LEGACY_KERAS"] = "0"
            import keras
            print("   Trying Keras 3...")
            
            # Try with custom objects
            try:
                from app.models.custom_layers import MBConvBlock
                model = keras.models.load_model(
                    str(keras_file),
                    custom_objects={'MBConvBlock': MBConvBlock},
                    compile=False
                )
            except:
                model = keras.models.load_model(str(keras_file), compile=False)
            
            loaded = True
            print("   ✅ Loaded with Keras 3!")
        except Exception as e2:
            print(f"   ❌ Keras 3 failed: {str(e2)[:100]}")
    
    if not loaded or model is None:
        raise Exception("Failed to load model with any method")
    
    print(f"\n📐 Model Info:")
    print(f"   Input shape:  {model.input_shape}")
    print(f"   Output shape: {model.output_shape}")
    print(f"   Layers: {len(model.layers)}")
    
    # Save as .h5
    print(f"\n💾 Saving to .h5 format...")
    os.environ["TF_USE_LEGACY_KERAS"] = "1"  # Switch back to legacy for saving
    
    import tensorflow as tf
    # Recompile with legacy
    legacy_model = tf.keras.models.clone_model(model)
    legacy_model.set_weights(model.get_weights())
    legacy_model.save(str(h5_file), save_format='h5')
    
    print(f"✅ SUCCESS! Model saved to: {h5_file}")
    print(f"📦 New file size: {h5_file.stat().st_size / (1024**3):.2f} GB")
    
    print("\n" + "="*80)
    print("CONVERSION COMPLETE!")
    print("="*80)
    print("\nSekarang restart backend untuk menggunakan model .h5:")
    print("   cd backend")
    print("   python run.py")
    
except Exception as e:
    print(f"\n❌ ERROR during conversion:")
    print(f"   {e}")
    print("\n📋 ALTERNATIF: Convert di training environment")
    print("\nJika script ini gagal, convert model di Colab/Kaggle:")
    print("""
    # Di notebook training kamu
    import keras
    
    # Load model
    model = keras.models.load_model('skin_model.keras')
    
    # Save as .h5
    model.save('skin_model.h5', save_format='h5')
    
    # Download file skin_model.h5
    # Copy ke: backend/app/models/weights/skin_model.h5
    """)
    sys.exit(1)
