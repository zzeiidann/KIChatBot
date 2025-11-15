# KIChatBot - AI Skin Disease Detection & E-Commerce Platform

Aplikasi web lengkap untuk deteksi penyakit kulit menggunakan AI dengan fitur chatbot RAG dan e-commerce skincare products.

## Fitur Utama

### AI & Machine Learning
- **Deteksi Penyakit Kulit**: Upload gambar untuk analisis menggunakan Vision Transformer (ViT)
- **RAG Chatbot**: Konsultasi dengan AI tentang kondisi kulit dan rekomendasi produk
- **8 Kategori Penyakit**: Actinic Keratosis, Basal Cell Carcinoma, Dermatofibroma, dll.

### E-Commerce
- **10 Produk Skincare**: Katalog lengkap dengan deskripsi detail
- **Shopping Cart**: Tambah, update, dan kelola keranjang belanja
- **Checkout System**: Proses pembelian yang mudah
- **Product Recommendations**: Rekomendasi produk berdasarkan kondisi kulit

### Authentication
- **Register & Login**: Sistem autentikasi JWT
- **User Management**: Profile management dan order history
- **Secure**: Password hashing dengan SHA-256

## Cara Menjalankan

### Quick Start - Jalankan Semua Service Sekaligus

**RECOMMENDED**: Gunakan script startup otomatis untuk menjalankan Backend, Ollama, dan Frontend sekaligus:

```bash
# Dari root directory project
./run.sh
```

Script ini akan otomatis:
- Start Backend dengan conda environment
- Start Ollama server (untuk chatbot)
- Start Frontend React dev server
- Pull model llama3.2 jika belum ada
- Install npm dependencies jika belum ada
- Buat log files di folder `logs/`

Tekan `Ctrl+C` untuk stop semua service.

---

### Manual Start (Alternative)

#### Backend (Python + FastAPI)

**PENTING**: Backend menggunakan **conda environment** karena PyTorch di macOS memerlukan binary compatibility khusus.

```bash
# 1. Pastikan conda sudah terinstall
cd backend

# 2. Jalankan menggunakan startup script
./start_backend.sh

# ATAU aktifkan conda environment manual
conda activate kichatbot
python run.py
```

Backend akan running di: `http://localhost:8000`

#### Frontend (React)

```bash
cd frontend

# Install dependencies
npm install

# Jalankan development server
npm start
```

Frontend akan running di: `http://localhost:3000`

#### Ollama (Chatbot AI)

```bash
# Install ollama (jika belum)
brew install ollama

# Start server
ollama serve

# Pull model (terminal baru)
ollama pull llama3.2
```

Ollama akan running di: `http://localhost:11434`

## Tech Stack

### Backend
- **FastAPI** 0.104.1 - Modern Python web framework
- **PyTorch** 2.5.1 - Deep learning framework
- **Transformers** 4.50.3 - HuggingFace model library
- **ChromaDB** 0.4.18 - Vector database untuk RAG
- **SQLite** - Database untuk users & products
- **Ollama** - Local LLM integration

### Frontend
- **React** 18.x - UI framework
- **TailwindCSS** - Styling (via CDN)
- **Fetch API** - HTTP requests

### AI Model
- **Model**: Vision Transformer (ViT) dari HuggingFace
- **Source**: `0xnu/skincare-detection`
- **Classes**: 184 skin conditions
- **Device**: CPU/MPS (Apple Silicon)

## Struktur Project

```
KIChatBot/
├── backend/
│   ├── app/
│   │   ├── models/          # AI model loading
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic (RAG, prediction)
│   │   └── database/        # DB connections & data
│   ├── start_backend.sh     # Startup script
│   ├── requirements.txt     # Python dependencies
│   └── README_CONDA.md      # Conda setup guide
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   └── services/        # API calls
│   └── package.json
└── chroma_store/            # Vector DB storage
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Daftar akun baru
- `POST /api/v1/auth/login` - Login user

### AI Features
- `POST /api/v1/predict` - Upload gambar untuk deteksi
- `POST /api/v1/chat` - Chat dengan AI tentang skincare

### E-Commerce
- `GET /api/v1/products` - List semua produk
- `POST /api/v1/cart/add` - Tambah produk ke keranjang
- `GET /api/v1/cart` - Lihat isi keranjang
- `PUT /api/v1/cart/update` - Update quantity
- `POST /api/v1/checkout` - Checkout pembelian

## Optimasi Frontend

Frontend telah dioptimalkan untuk performa:
- **Throttled mouse tracking** - Update setiap 50ms
- **Reduced animations** - Hanya 3 orbs instead of 5+
- **Hardware acceleration** - `translate3d()` untuk smooth animation
- **Static grid** - Grid background tidak bergerak
- **Lazy loading** - Components loaded on demand
- **No emoji overload** - Clean UI

## Troubleshooting

### Backend tidak bisa start

Pastikan menggunakan conda environment:
```bash
conda activate kichatbot
cd backend
python run.py
```

### PyTorch import error

Lihat `backend/README_CONDA.md` untuk solusi lengkap tentang PyTorch compatibility.

### Frontend slow/berat

- Bersihkan browser cache
- Tutup tab browser lain
- Restart React dev server

## Contributors

- **Backend**: FastAPI + PyTorch implementation
- **Frontend**: React + TailwindCSS optimization
- **AI Model**: HuggingFace Vision Transformer

## License

Educational project - Free to use and modify

---

**Note**: Project ini dibuat untuk pembelajaran AI, web development, dan e-commerce integration.
