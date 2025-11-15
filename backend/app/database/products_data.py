# Comprehensive skincare knowledge base for RAG system
SKINCARE_KNOWLEDGE = """
SKIN DISEASE INFORMATION:

1. ACTINIC KERATOSIS
- Keratosis aktinik adalah pertumbuhan kasar dan bersisik pada kulit akibat paparan sinar matahari berlebihan
- Biasanya muncul di area yang sering terkena sinar matahari seperti wajah, tangan, dan lengan
- Perawatan: Gunakan sunscreen SPF 50+ setiap hari, hindari paparan sinar matahari langsung
- Konsultasikan dengan dokter kulit untuk treatment medis seperti cryotherapy atau krim topikal

2. BASAL CELL CARCINOMA
- Kanker kulit paling umum, biasanya muncul sebagai benjolan mengkilap atau luka yang tidak sembuh
- Disebabkan oleh paparan sinar UV jangka panjang
- Perawatan: Segera konsultasi dengan dokter kulit, mungkin memerlukan pembedahan atau terapi radiasi
- Pencegahan: Gunakan sunscreen broad-spectrum SPF 30+ setiap hari

3. DERMATOFIBROMA
- Benjolan keras jinak pada kulit, biasanya berwarna coklat atau merah
- Tidak berbahaya tetapi bisa terasa gatal atau nyeri jika tertekan
- Perawatan: Umumnya tidak memerlukan treatment, gunakan pelembab untuk menjaga kelembaban kulit
- Jika mengganggu, konsultasi dengan dokter untuk pengangkatan

4. MELANOCYTIC NEVUS (TAHI LALAT)
- Pertumbuhan kulit jinak yang berisi melanosit (sel pigmen)
- Normal memiliki tahi lalat, tetapi perhatikan perubahan bentuk, warna, atau ukuran
- Perawatan: Lindungi dari sinar matahari dengan sunscreen
- Konsultasi dokter jika tahi lalat berubah atau mencurigakan

5. PIGMENTED BENIGN KERATOSIS
- Pertumbuhan kulit jinak berwarna coklat atau hitam
- Umum terjadi seiring bertambahnya usia
- Perawatan: Gunakan produk dengan retinol atau vitamin C untuk mencerahkan kulit
- Sunscreen wajib untuk mencegah hiperpigmentasi

6. SEBORRHEIC KERATOSIS
- Pertumbuhan kulit jinak berwarna coklat, hitam atau kuning
- Terlihat seperti kutil tetapi tidak disebabkan oleh virus
- Perawatan: Tidak memerlukan treatment kecuali mengganggu, gunakan pelembab rutin
- Konsultasi dokter jika ingin diangkat untuk alasan estetika

7. SQUAMOUS CELL CARCINOMA
- Jenis kanker kulit yang berkembang dari sel skuamosa di epidermis
- Muncul sebagai benjolan keras atau luka bersisik yang tidak sembuh
- Perawatan: Segera konsultasi dokter kulit, memerlukan pembedahan atau terapi
- Pencegahan penting: Sunscreen SPF 50+ dan hindari paparan UV

8. VASCULAR LESION
- Kelainan pembuluh darah yang terlihat di kulit seperti hemangioma atau spider veins
- Bisa muncul sebagai bintik merah atau benang merah di kulit
- Perawatan: Gunakan produk yang menenangkan seperti centella atau niacinamide
- Konsultasi dokter untuk laser treatment jika mengganggu

GENERAL SKINCARE TIPS:
- Rutin membersihkan wajah 2x sehari dengan gentle cleanser
- Gunakan pelembab sesuai jenis kulit (oily, dry, combination)
- WAJIB pakai sunscreen SPF 30+ setiap hari, bahkan di dalam ruangan
- Hindari menggaruk atau memencet jerawat
- Minum air putih minimal 8 gelas per hari
- Tidur cukup 7-8 jam per hari
- Kelola stress dengan baik
- Konsumsi makanan bergizi tinggi antioksidan
"""

PRODUCTS = [
    {
        "id": "1",
        "name": "Cetaphil Gentle Skin Cleanser",
        "price": 150000,
        "category": "Pembersih",
        "for_conditions": ["Jerawat", "Kulit Sensitif", "Dermatitis"],
        "description": "Pembersih wajah lembut untuk kulit sensitif dan berjerawat. Formula non-soap, pH balanced, tidak mengandung pewangi. Cocok untuk pembersihan sehari-hari tanpa membuat kulit kering. Dermatologically tested dan hypoallergenic. Dapat digunakan dengan atau tanpa air. Ideal untuk kondisi acne, rosacea, dan post-procedure skin.",
        "ingredients": "Water, Cetyl Alcohol, Propylene Glycol, Sodium Lauryl Sulfate, Stearyl Alcohol",
        "usage": "Aplikasikan ke wajah basah, pijat lembut, bilas dengan air. Gunakan 2x sehari pagi dan malam."
    },
    {
        "id": "2",
        "name": "La Roche-Posay Effaclar Duo+",
        "price": 320000,
        "category": "Perawatan Jerawat",
        "for_conditions": ["Jerawat", "Bekas Jerawat", "Acne Prone Skin"],
        "description": "Treatment anti-jerawat dengan teknologi dual action. Mengandung 5.5% Niacinamide untuk mencerahkan bekas jerawat, Salicylic Acid untuk membersihkan pori, dan Piroctone Olamine sebagai antibakteri. Mengurangi jerawat hingga 50% dalam 4 minggu. Non-comedogenic dan oil-free. Cocok untuk kulit berminyak dan acne-prone.",
        "ingredients": "Niacinamide 5.5%, Salicylic Acid, Piroctone Olamine, La Roche-Posay Thermal Water",
        "usage": "Aplikasikan tipis ke seluruh wajah atau area berjerawat setelah cleansing, hindari area mata. Gunakan 1-2x sehari."
    },
    {
        "id": "3",
        "name": "Avene Thermal Spring Water",
        "price": 180000,
        "category": "Spray Thermal",
        "for_conditions": ["Kulit Sensitif", "Dermatitis", "Rosacea", "Sunburn"],
        "description": "Spray air thermal murni dari sumber Avene, Perancis. Mengandung mineral dan trace elements yang menenangkan kulit. Soothing, anti-inflammatory, dan mengurangi kemerahan. Steril dan bebas preservatives. Cocok untuk kulit sensitif, iritasi, sunburn, dan post-procedure. Dapat digunakan sebagai setting spray atau refresh skin.",
        "ingredients": "Avene Thermal Spring Water 100%",
        "usage": "Semprot ke wajah dari jarak 20cm, biarkan meresap 1-2 menit, tepuk lembut kelebihan air. Gunakan kapan saja."
    },
    {
        "id": "4",
        "name": "Wardah Nature Daily Aloe Vera Gel",
        "price": 25000,
        "category": "Pelembab",
        "for_conditions": ["Kulit Kering", "Luka Bakar Ringan", "Sunburn", "Iritasi"],
        "description": "Gel aloe vera murni 100% untuk melembabkan dan menenangkan kulit. Tekstur ringan, cepat menyerap, tidak lengket. Mengandung vitamin A, C, E untuk nutrisi kulit. Multi-fungsi: pelembab wajah, body lotion, hair mask, atau after-sun care. Hypoallergenic dan cocok untuk semua jenis kulit. Produk lokal berkualitas dengan harga terjangkau.",
        "ingredients": "Aloe Barbadensis Leaf Extract 100%, Vitamin A, C, E",
        "usage": "Aplikasikan secukupnya ke area yang diinginkan. Untuk wajah gunakan tipis-tipis. Dapat digunakan 2-3x sehari."
    },
    {
        "id": "5",
        "name": "Somethinc Calm Down Centella Serum",
        "price": 89000,
        "category": "Serum",
        "for_conditions": ["Jerawat", "Kulit Sensitif", "Kemerahan", "Barrier Rusak"],
        "description": "Serum dengan 100,000ppm Centella Asiatica untuk menenangkan kulit. Mengandung Madecassoside, Asiaticoside, Madecassic Acid untuk repair skin barrier. Plus 10% Niacinamide untuk brighten dan control sebum. Hypoallergenic, fragrance-free, alcohol-free. Cocok untuk acne-prone, sensitive skin, dan rosacea. Produk lokal dengan formula setara brand internasional.",
        "ingredients": "Centella Asiatica 100,000ppm, Niacinamide 10%, Madecassoside, Asiaticoside",
        "usage": "Aplikasikan 2-3 tetes ke wajah setelah toner, sebelum moisturizer. Gunakan pagi dan malam. Dapat dicampur dengan moisturizer."
    },
    {
        "id": "6",
        "name": "Bioderma Atoderm Cream",
        "price": 250000,
        "category": "Pelembab Intensif",
        "for_conditions": ["Eksim", "Dermatitis", "Kulit Sangat Kering", "Psoriasis"],
        "description": "Pelembab intensive untuk kondisi kulit sangat kering, eksim, dan dermatitis. Formula Skin Barrier Therapy dengan Lipigenium complex untuk restore lipid barrier. Mengandung Niacinamide dan Vitamin PP untuk anti-inflammatory. Tekstur rich dan creamy, melembabkan hingga 24 jam. Hypoallergenic, fragrance-free, dan non-comedogenic. Cocok untuk bayi, anak, dan dewasa.",
        "ingredients": "Lipigenium Complex, Niacinamide, Vitamin PP, Glycerin, Shea Butter",
        "usage": "Aplikasikan ke kulit bersih 1-2x sehari. Untuk area sangat kering aplikasikan lebih sering. Gunakan setelah mandi."
    },
    {
        "id": "7",
        "name": "Emina Sun Protection SPF 30 PA+++",
        "price": 35000,
        "category": "Sunscreen",
        "for_conditions": ["Semua Jenis Kulit", "Daily Protection"],
        "description": "Sunscreen broad-spectrum dengan SPF 30 PA+++ untuk perlindungan dari UVA dan UVB. Formula ringan, tidak lengket, cepat menyerap. Tidak meninggalkan whitecast. Water-resistant dan cocok sebagai base makeup. Non-comedogenic, oil-free, fragrance-free. Harga sangat terjangkau untuk penggunaan sehari-hari. Reapply setiap 2-3 jam untuk perlindungan optimal.",
        "ingredients": "Ethylhexyl Methoxycinnamate, Titanium Dioxide, Zinc Oxide, Vitamin E",
        "usage": "Aplikasikan sebagai step terakhir skincare 15 menit sebelum keluar rumah. Gunakan 2 jari amount untuk wajah dan leher. Reapply tiap 2-3 jam."
    },
    {
        "id": "8",
        "name": "Physiogel Daily Moisture Therapy",
        "price": 220000,
        "category": "Pelembab",
        "for_conditions": ["Kulit Kering", "Dermatitis", "Kulit Sensitif", "Barrier Rusak"],
        "description": "Pelembab dengan teknologi BioMimic untuk meniru lipid barrier alami kulit. Mengandung ceramides dan lipids untuk strengthen skin barrier. Hypoallergenic, fragrance-free, paraben-free, dan non-comedogenic. Clinically proven untuk kulit kering dan sensitif. Tekstur ringan tetapi moisturizing. Cocok untuk daily use dan dapat digunakan untuk bayi hingga dewasa.",
        "ingredients": "BioMimic Technology, Ceramides, Lipids, Glycerin, Dimethicone",
        "usage": "Aplikasikan ke wajah dan tubuh setelah cleansing. Gunakan 2x sehari pagi dan malam. Dapat digunakan sebelum sunscreen."
    },
    {
        "id": "9",
        "name": "Skintific 5X Ceramide Barrier Repair Moisturizer",
        "price": 135000,
        "category": "Pelembab",
        "for_conditions": ["Barrier Rusak", "Kulit Sensitif", "Kulit Kering"],
        "description": "Moisturizer dengan 5X Ceramide complex untuk intensive barrier repair. Mengandung 5% Niacinamide untuk brighten dan control sebum. Formula lightweight gel-cream yang cepat menyerap. Hypoallergenic, fragrance-free, dan alcohol-free. Cocok untuk semua jenis kulit terutama dehydrated dan sensitive skin. Produk lokal dengan teknologi Korea.",
        "ingredients": "5X Ceramide Complex, Niacinamide 5%, Hyaluronic Acid, Centella Asiatica",
        "usage": "Aplikasikan sebagai step terakhir skincare pagi dan malam. Untuk kulit sangat kering, layer 2-3x hingga fully absorbed."
    },
    {
        "id": "10",
        "name": "Azarine Hydrasoothe Sunscreen Gel SPF 45",
        "price": 55000,
        "category": "Sunscreen",
        "for_conditions": ["Semua Jenis Kulit", "Kulit Berminyak", "Acne Prone"],
        "description": "Sunscreen gel dengan SPF 45 PA++++ untuk maximum protection. Formula gel yang ultra-light, matte finish, tidak lengket. Mengandung Hyaluronic Acid dan Centella Asiatica untuk hydrate dan soothe. Tidak ada whitecast sama sekali. Cocok untuk kulit berminyak dan acne-prone. Water and sweat resistant. Harga affordable untuk pemakaian generous.",
        "ingredients": "Ethylhexyl Methoxycinnamate, Titanium Dioxide, Hyaluronic Acid, Centella Asiatica",
        "usage": "Aplikasikan generous amount (2 jari) ke wajah 15 menit sebelum aktivitas outdoor. Reapply setiap 2 jam atau setelah berkeringat."
    }
]