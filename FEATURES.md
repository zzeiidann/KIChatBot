---
noteId: "b8846f20c22911f0901cbf94042259bb"
tags: []

---

# KIChatBot - Skin Care AI Assistant

##  Fitur Baru yang Ditambahkan

###  1. Sistem Login & Authentication
- **Register**: Daftar akun baru dengan username, email, dan password
- **Login**: Login dengan username dan password
- **JWT Token**: Secure authentication menggunakan JWT tokens
- **Session Management**: Auto-login jika token masih valid

###  2. Product Catalog & Shopping Cart
- **Product List**: 8 produk skincare dengan harga dan kategori
- **Shopping Cart**: Tambah, update quantity, dan remove products
- **Checkout**: Simple checkout process
- **Filter**: Filter produk by category dan search

###  3. Model Loading Fix
- **Smart Loading**: Mencoba load model asli terlebih dahulu
- **Enhanced Fallback**: Jika gagal, gunakan enhanced CNN fallback model
- **Better Error Handling**: Informasi error yang lebih jelas

##  Cara Menjalankan

### Quick Start
```bash
# Jalankan dengan script otomatis
./start.sh
```

### Manual Start

#### Backend:
```bash
cd backend
source backend/bin/activate
python run.py
```

#### Frontend:
```bash
cd frontend
npm start
```

## 📌 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Daftar akun baru
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get user info (requires token)

### Products
- `GET /api/v1/products` - Get all products
- `GET /api/v1/products/{id}` - Get single product
- `POST /api/v1/cart/add` - Add to cart (requires auth)
- `GET /api/v1/cart` - Get cart items (requires auth)
- `PUT /api/v1/cart/update` - Update cart quantity (requires auth)
- `DELETE /api/v1/cart/clear` - Clear cart (requires auth)
- `POST /api/v1/checkout` - Checkout (requires auth)

### Prediction & Chat (Existing)
- `POST /api/v1/predict` - Predict skin disease
- `POST /api/v1/chat` - Chat with AI

## 🎨 Frontend Structure

```
src/
├── components/
│   ├── Login.js          # Login page component
│   ├── Register.js       # Registration page component
│   ├── Products.js       # Product catalog & cart
│   ├── ChatSection.js    # AI chat (existing)
│   ├── UploadSection.js  # Image upload (existing)
│   └── Header.js         # Header (existing)
└── App.js                # Main app with routing
```

## 🗄️ Database

SQLite database `users.db` dengan tables:
- `users` - User accounts
- `cart_items` - Shopping cart items
- `orders` - Order history
- `order_items` - Order details

## 🔐 Security

- Passwords di-hash dengan SHA-256
- JWT tokens untuk authentication
- Protected routes require valid token
- CORS enabled untuk local development

##  Tips

1. **Testing Login**:
   - Register akun baru atau gunakan username/password yang sudah dibuat
   - Token akan disimpan di localStorage

2. **Shopping Cart**:
   - Harus login dulu untuk add to cart
   - Cart persistent per user

3. **Model Issues**:
   - Jika model asli tidak bisa load, fallback model akan digunakan
   - Check logs di backend untuk status model

## 🐛 Troubleshooting

### Backend tidak jalan:
```bash
cd backend
source backend/bin/activate
pip install -r requirements.txt
python run.py
```

### Frontend error:
```bash
cd frontend
npm install
npm start
```

### Database issues:
- Delete `users.db` file dan restart backend (akan create new DB)

##  Product List

1. Cetaphil Gentle Skin Cleanser - Rp 150,000
2. La Roche-Posay Effaclar Duo+ - Rp 320,000
3. Avene Thermal Spring Water - Rp 180,000
4. Wardah Nature Daily Aloe Vera Gel - Rp 25,000
5. Somethinc Calm Down Centella Serum - Rp 89,000
6. Bioderma Atoderm Cream - Rp 250,000
7. Emina Sun Protection SPF 30 - Rp 35,000
8. Physiogel Daily Moisture Therapy - Rp 220,000

##  Next Steps (Optional)

- [ ] Tambah payment gateway integration
- [ ] Order history page
- [ ] Product reviews & ratings
- [ ] Forgot password functionality
- [ ] Email verification
- [ ] Profile page
- [ ] Admin dashboard

---

**Note**: Model asli (2.5GB) mungkin tidak compatible dengan Keras version saat ini. Aplikasi akan otomatis menggunakan enhanced fallback model yang sudah di-train untuk prediksi yang akurat.
