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
    },
    {
        "id": "11",
        "name": "Cosrx Advanced Snail 96 Mucin Power Essence",
        "price": 185000,
        "category": "Serum",
        "for_conditions": ["Kulit Kering", "Bekas Jerawat", "Anti Aging"],
        "description": "Essence dengan 96% Snail Secretion Filtrate untuk intense hydration dan skin repair. Mempercepat penyembuhan bekas jerawat, mengurangi fine lines, dan meningkatkan skin elasticity. Tekstur lightweight gel yang mudah menyerap. Hypoallergenic dan dermatologically tested. Cocok untuk semua jenis kulit.",
        "ingredients": "Snail Secretion Filtrate 96%, Betaine, Panthenol, Arginine",
        "usage": "Setelah toner, aplikasikan 2-3 tetes ke wajah, tap lembut. Gunakan pagi dan malam."
    },
    {
        "id": "12",
        "name": "Some By Mi AHA BHA PHA 30 Days Miracle Toner",
        "price": 145000,
        "category": "Toner",
        "for_conditions": ["Jerawat", "Komedo", "Kulit Kusam"],
        "description": "Toner eksfoliasi dengan AHA, BHA, dan PHA untuk deep cleansing pori-pori. Mengandung 10,000ppm Tea Tree untuk anti-bakteri. Mengurangi jerawat, komedo, dan mencerahkan kulit dalam 30 hari. pH balanced dan tidak membuat kulit kering.",
        "ingredients": "Tea Tree 10,000ppm, AHA, BHA, PHA, Niacinamide, Adenosine",
        "usage": "Setelah cleansing, tuang ke kapas atau telapak tangan, tap ke wajah. Gunakan 1-2x sehari. Wajib pakai sunscreen."
    },
    {
        "id": "13",
        "name": "Innisfree Green Tea Seed Serum",
        "price": 195000,
        "category": "Serum",
        "for_conditions": ["Kulit Kering", "Dehidrasi", "Kulit Kusam"],
        "description": "Serum dengan Fresh Green Tea Tri-biotics untuk deep hydration. Mengandung Green Tea Extract dari Jeju Island. Menyeimbangkan kelembaban kulit, memperkuat skin barrier, dan memberikan glow natural. Formula lightweight yang cepat menyerap.",
        "ingredients": "Green Tea Extract, Green Tea Seed Oil, Hyaluronic Acid, Panthenol",
        "usage": "Aplikasikan 2-3 pump setelah toner. Tap lembut hingga menyerap. Gunakan pagi dan malam."
    },
    {
        "id": "14",
        "name": "The Ordinary Hyaluronic Acid 2% + B5",
        "price": 95000,
        "category": "Serum",
        "for_conditions": ["Kulit Kering", "Dehidrasi", "Fine Lines"],
        "description": "Serum hydrating dengan Hyaluronic Acid multi-molecular weight untuk penetrasi berbagai layer kulit. Vitamin B5 meningkatkan surface hydration. Plumping effect untuk mengurangi fine lines. Water-based formula, lightweight, dan cocok untuk layering.",
        "ingredients": "Hyaluronic Acid 2%, Vitamin B5, Sodium Hyaluronate Crosspolymer",
        "usage": "Aplikasikan beberapa tetes ke wajah basah setelah cleansing. Lanjutkan dengan moisturizer. Gunakan AM dan PM."
    },
    {
        "id": "15",
        "name": "Hada Labo Gokujyun Premium Hyaluronic Lotion",
        "price": 125000,
        "category": "Toner",
        "for_conditions": ["Kulit Kering", "Dehidrasi", "Semua Jenis Kulit"],
        "description": "Hydrating lotion dengan 7 jenis Hyaluronic Acid untuk maximum moisture retention. Tekstur thick tetapi cepat menyerap. Fragrance-free, colorant-free, dan mineral oil-free. Meningkatkan kelembaban kulit hingga 5x lipat. Ideal untuk 7-skin method.",
        "ingredients": "7 Types Hyaluronic Acid, Urea, Sacran, Squalane",
        "usage": "Setelah cleansing, tuang ke telapak tangan, pat ke wajah. Dapat dilayer 2-3x untuk extra hydration."
    },
    {
        "id": "16",
        "name": "Paula's Choice 2% BHA Liquid Exfoliant",
        "price": 385000,
        "category": "Exfoliant",
        "for_conditions": ["Jerawat", "Komedo", "Pori Besar", "Kulit Berminyak"],
        "description": "Leave-on exfoliant dengan 2% Salicylic Acid untuk unclog pores dan mengurangi komedo. Memperbaiki tekstur kulit, mengurangi fine lines, dan mengontrol sebum. Gentle formula non-abrasive. Best-seller worldwide untuk acne-prone skin.",
        "ingredients": "Salicylic Acid 2%, Green Tea Extract, Methylpropanediol",
        "usage": "Setelah cleansing dan toner, aplikasikan dengan kapas atau tangan. Tidak perlu dibilas. Mulai 2-3x seminggu, bisa ditingkatkan. Wajib sunscreen."
    },
    {
        "id": "17",
        "name": "Kiehl's Ultra Facial Cream",
        "price": 425000,
        "category": "Pelembab",
        "for_conditions": ["Kulit Kering", "Kulit Sensitif", "Semua Jenis Kulit"],
        "description": "Lightweight moisturizer dengan 24-hour hydration. Mengandung Squalane dan Glacial Glycoprotein untuk strengthen skin barrier. Suitable untuk extreme weather conditions. Non-greasy, fragrance-free, dan cocok untuk semua jenis kulit termasuk sensitif.",
        "ingredients": "Squalane, Glacial Glycoprotein, Imperata Cylindrica Root Extract",
        "usage": "Aplikasikan ke wajah dan leher setelah serum. Gunakan pagi dan malam. Dapat digunakan di bawah makeup."
    },
    {
        "id": "18",
        "name": "Dear Klairs Freshly Juiced Vitamin Drop",
        "price": 245000,
        "category": "Serum",
        "for_conditions": ["Kulit Kusam", "Hiperpigmentasi", "Bekas Jerawat"],
        "description": "Vitamin C serum dengan 5% pure Ascorbic Acid untuk brightening dan anti-aging. Gentle formula cocok untuk sensitive skin. Mengurangi dark spots, meratakan skin tone, dan meningkatkan radiance. Essential oil-free dan hypoallergenic.",
        "ingredients": "Ascorbic Acid 5%, Centella Asiatica, Licorice Root Extract",
        "usage": "Gunakan 3-4 tetes setelah toner, sebelum moisturizer. Mulai 2x seminggu, tingkatkan bertahap. Gunakan PM atau dengan sunscreen di AM."
    },
    {
        "id": "19",
        "name": "Acnes Natural Care Foaming Wash",
        "price": 28000,
        "category": "Pembersih",
        "for_conditions": ["Jerawat", "Kulit Berminyak", "Komedo"],
        "description": "Facial wash dengan Isopropyl Methylphenol untuk anti-bakteri dan mencegah jerawat. Vitamin B3 dan Aloe Vera menenangkan kulit. Formula foam yang lembut membersihkan excess oil tanpa membuat kulit kering. pH balanced.",
        "ingredients": "Isopropyl Methylphenol, Vitamin B3, Aloe Vera, Glycerin",
        "usage": "Basahi wajah, buat busa, pijat lembut, bilas. Gunakan 2x sehari pagi dan malam."
    },
    {
        "id": "20",
        "name": "Senka Perfect Whip",
        "price": 42000,
        "category": "Pembersih",
        "for_conditions": ["Semua Jenis Kulit", "Kulit Berminyak"],
        "description": "Japanese facial foam dengan micro-bubble technology untuk deep cleansing. White Cocoon Extract mencerahkan dan menghaluskan kulit. Rich foam yang lembut mengangkat kotoran tanpa stripping. Cocok untuk daily use.",
        "ingredients": "White Cocoon Extract, Hyaluronic Acid, Collagen, Silk Protein",
        "usage": "Keluarkan 2cm, buat busa dengan air, aplikasikan ke wajah, pijat, bilas. Gunakan 2x sehari."
    },
    {
        "id": "21",
        "name": "Nivea Creme Soft Soap",
        "price": 18000,
        "category": "Pembersih",
        "for_conditions": ["Kulit Kering", "Kulit Normal"],
        "description": "Sabun wajah dan tubuh dengan Moisturizing Cream untuk cleansing tanpa membuat kulit kering. Cocok untuk sensitive skin. Memberikan soft dan smooth feeling setelah pemakaian. Affordable untuk whole family.",
        "ingredients": "Moisturizing Cream, Vitamin E, Glycerin",
        "usage": "Basahi kulit, buat busa dengan sabun, aplikasikan, bilas. Gunakan setiap mandi."
    },
    {
        "id": "22",
        "name": "Garnier Micellar Cleansing Water",
        "price": 35000,
        "category": "Pembersih",
        "for_conditions": ["Semua Jenis Kulit", "Kulit Sensitif"],
        "description": "Micellar water all-in-one: cleanser, makeup remover, dan toner. Micelle technology mengangkat makeup dan impurities tanpa harsh rubbing. No-rinse formula. Alcohol-free, fragrance-free, dan cocok untuk sensitive skin.",
        "ingredients": "Micelle Technology, Glycerin, Poloxamer 184",
        "usage": "Tuang ke kapas, usap lembut ke wajah hingga bersih. Tidak perlu dibilas. Gunakan pagi dan/atau malam."
    },
    {
        "id": "23",
        "name": "The Body Shop Tea Tree Skin Clearing Facial Wash",
        "price": 145000,
        "category": "Pembersih",
        "for_conditions": ["Jerawat", "Kulit Berminyak", "Komedo"],
        "description": "Gel cleanser dengan Community Fair Trade Tea Tree Oil untuk deep cleansing dan anti-blemish. Lemon Tea Tree dan Tamanu Oil menenangkan kulit. Mengurangi excess oil dan mencegah jerawat. Vegan dan cruelty-free.",
        "ingredients": "Tea Tree Oil, Lemon Tea Tree, Tamanu Oil, Salicylic Acid",
        "usage": "Aplikasikan ke wajah basah, massage, bilas. Gunakan AM dan PM. Hindari area mata."
    },
    {
        "id": "24",
        "name": "Neutrogena Hydro Boost Water Gel",
        "price": 265000,
        "category": "Pelembab",
        "for_conditions": ["Kulit Kering", "Dehidrasi", "Kulit Berminyak"],
        "description": "Gel-cream dengan Hyaluronic Acid untuk boost hydration. Unique water gel formula yang instantly hydrates dan menyerap cepat. Oil-free dan non-comedogenic. Locks in moisture selama 48 jam. Suitable untuk oily dan acne-prone skin.",
        "ingredients": "Hyaluronic Acid, Glycerin, Dimethicone, Olive Extract",
        "usage": "Aplikasikan ke wajah bersih pagi dan malam. Dapat digunakan setelah serum atau standalone."
    },
    {
        "id": "25",
        "name": "Laneige Water Sleeping Mask",
        "price": 315000,
        "category": "Masker",
        "for_conditions": ["Kulit Kering", "Kulit Kusam", "Dehidrasi"],
        "description": "Overnight mask dengan Sleep-tox technology untuk intensive hydration. Hunza Apricot dan Evening Primrose melembabkan dan mencerahkan kulit overnight. Bangun dengan glowing, plump skin. K-beauty essential.",
        "ingredients": "Hunza Apricot, Evening Primrose, Sleepscent, Hydro Ion Mineral Water",
        "usage": "Gunakan sebagai step terakhir skincare malam. Aplikasikan layer tebal, biarkan overnight, bilas pagi. 2-3x seminggu."
    },
    {
        "id": "26",
        "name": "Pixi Glow Tonic",
        "price": 275000,
        "category": "Toner",
        "for_conditions": ["Kulit Kusam", "Pori Besar", "Tekstur Kasar"],
        "description": "Exfoliating toner dengan 5% Glycolic Acid untuk gentle daily exfoliation. Ginseng dan Aloe Vera soothe dan tone skin. Memberikan radiant glow. Cult favorite untuk achieving glass skin. Alcohol-free.",
        "ingredients": "Glycolic Acid 5%, Ginseng, Aloe Vera, Horse Chestnut",
        "usage": "Setelah cleansing, swipe dengan kapas ke wajah. Tidak perlu dibilas. Gunakan AM atau PM. Wajib sunscreen."
    },
    {
        "id": "27",
        "name": "Bioré UV Aqua Rich Watery Essence SPF 50+",
        "price": 115000,
        "category": "Sunscreen",
        "for_conditions": ["Semua Jenis Kulit", "Kulit Berminyak"],
        "description": "Sunscreen dengan tekstur watery yang super light. SPF 50+ PA++++ untuk maximum protection. Water capsule technology memberikan fresh feeling. Water and sweat resistant. No whitecast. Best-selling Japanese sunscreen worldwide.",
        "ingredients": "Aqua Booster, Hyaluronic Acid, Royal Jelly, Citrus Extracts",
        "usage": "Shake well, aplikasikan generous amount ke wajah 15 menit sebelum sun exposure. Reapply tiap 2-3 jam."
    },
    {
        "id": "28",
        "name": "Innisfree Pore Clearing Clay Mask",
        "price": 145000,
        "category": "Masker",
        "for_conditions": ["Komedo", "Pori Besar", "Kulit Berminyak"],
        "description": "Clay mask dengan Jeju Volcanic Clusters untuk deep pore cleansing. Absorbs excess sebum dan impurities. AHA untuk gentle exfoliation. Skin tone menjadi lebih smooth dan refined. Suitable untuk oily dan combination skin.",
        "ingredients": "Jeju Volcanic Clusters, AHA, Walnut Shell Powder",
        "usage": "Aplikasikan layer tebal ke wajah kering, hindari mata dan bibir. Biarkan 10-15 menit, bilas. Gunakan 1-2x seminggu."
    },
    {
        "id": "29",
        "name": "Klairs Supple Preparation Facial Toner",
        "price": 235000,
        "category": "Toner",
        "for_conditions": ["Kulit Sensitif", "Kulit Kering", "Barrier Rusak"],
        "description": "Hydrating toner dengan essential ingredients untuk prep kulit. Centella, Licorice, dan Beta-Glucan menenangkan dan strengthen skin barrier. pH balanced dan alcohol-free. Suitable untuk 7-skin method. Vegan dan cruelty-free.",
        "ingredients": "Centella Asiatica, Licorice Root, Beta-Glucan, Hyaluronic Acid",
        "usage": "Tuang ke telapak tangan atau kapas, pat ke wajah. Dapat dilayer 2-3x. Gunakan AM dan PM."
    },
    {
        "id": "30",
        "name": "Axis-Y Dark Spot Correcting Glow Serum",
        "price": 185000,
        "category": "Serum",
        "for_conditions": ["Hiperpigmentasi", "Bekas Jerawat", "Kulit Kusam"],
        "description": "Brightening serum dengan 5% Niacinamide, Papaya Extract, dan Squalane. Mengurangi dark spots dan hyperpigmentation. Rice Bran Extract memberikan natural glow. Vegan, cruelty-free, dan fragrance-free.",
        "ingredients": "Niacinamide 5%, Papaya Extract, Rice Bran Extract, Squalane",
        "usage": "Aplikasikan 2-3 tetes setelah toner. Pat lembut. Gunakan pagi dan malam. Cocok untuk morning routine."
    }
]