# INSTRUKSI: Convert Model dari Colab/Kaggle ke .h5

## Kalau kamu training di Colab/Kaggle, jalankan code ini:

```python
import keras
import tensorflow as tf

# 1. Load model yang sudah trained
model = keras.models.load_model('skin_model.keras')

print(f"✅ Model loaded!")
print(f"Input shape: {model.input_shape}")
print(f"Output shape: {model.output_shape}")

# 2. Save ke format .h5 (compatible dengan semua environment)
model.save('skin_model.h5', save_format='h5')

print(f"✅ Model saved as skin_model.h5")

# 3. Verify the saved model
test_model = tf.keras.models.load_model('skin_model.h5')
print(f"✅ Verified! Model can be loaded")

# 4. Download file
from google.colab import files
files.download('skin_model.h5')
```

## Setelah download:

1. Copy file `skin_model.h5` ke folder:
   ```
   backend/app/models/weights/skin_model.h5
   ```

2. Restart backend:
   ```bash
   cd backend
   python run.py
   ```

3. Backend akan otomatis detect dan load file .h5

## ATAU gunakan SavedModel format:

```python
# Save as TensorFlow SavedModel (alternative)
model.save('skin_model_saved', save_format='tf')

# Download folder
!zip -r skin_model_saved.zip skin_model_saved
files.download('skin_model_saved.zip')
```

Extract zip dan copy folder `skin_model_saved/` ke `backend/app/models/weights/`

---

## Troubleshooting:

**Q: Model masih gak ke-load?**
A: Pastikan:
- File ada di path yang benar
- File size sama dengan original (2.46GB)
- Format file: `.h5` atau folder `skin_model_saved/`

**Q: Error "custom layers not found"?**
A: Pakai format .h5, bukan .keras

**Q: Out of memory?**
A: Model butuh minimum 4GB RAM untuk load
