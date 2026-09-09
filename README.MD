# Personal Portfolio Website - PBP B
Name : Justin Evan Halim Saputra
NPM : 2506549386
Class : PBP B
Year : 2

Repositori ini berisi kode sumber (*source code*) untuk website portofolio pribadi yang dikembangkan sebagai pemenuhan tugas dari mata kuliah Pemrograman Berbasis Platform (PBP) Fasilkom UI. 

## PWS Deployment Link
* [PWS Deployment Link](https://justin-evan-myportofolio.pws.cs.ui.ac.id/)

## Setup & Cara Menjalankan Secara Lokal
Untuk menjalankan proyek ini di komputer lokal Anda, ikuti langkah-langkah berikut:

1. Clone repositori ini ke perangkat lokal Anda:
   ```bash
   git clone [https://pws.cs.ui.id/justin.evan/myportofolio.git](https://pws.cs.ui.id/justin.evan/myportofolio.git)
2. Buka folder proyek melalui teks editor pilihan Anda (misalnya VS Code).
3. Jalankan file index.html menggunakan ekstensi Live Server di VS Code, atau buka langsung file tersebut menggunakan browser pilihan Anda.

## Jawaban Pertanyaan Reflektif & AI Disclosure Tugas Individual 1 +++

1. Penggunaan Elemen Semantik HTML 5
Ya, saya menggunakan elemen semantik HTML5 dalam merancang struktur static web ini. Pada halaman education, saya menggunakan elemen <section> untuk membagi kelompok konten utama seperti .education-section, .achievements-section, dan .gallery-section. Di dalam bagian timeline education, saya menggunakan tag <article> khusus untuk mengelompokkan setiap riwayat pendidikan (.education-card). Penggunaan elemen-elemen ini sangat membantu karena membuat struktur kode lebih mudah dibaca (dibandingkan menggunakan <div> secara berlebihan), memberikan struktur yang jelas bagi browser, dan meningkatkan aksesibilitas (SEO dan integrasi dengan screen reader) karena setiap blok informasi terdefinisi sesuai dengan fungsinya.

2. Tantangan Responsive Layout dan Prioritas Elemen
Tantangan terbesar saat mengatur CSS agar responsive adalah menangani perubahan tata letak timeline dan grid gambar. Pada tampilan desktop, timeline membutuhkan tata letak bersisian dengan logo sekolah dan kampus menggunakan grid-template-columns: 8.5rem 1fr dengan titik penanda di tengah. Namun, pada layar mobile (max-width: 600px), memaksakan dua kolom akan membuat teks terlalu sempit dan sulit dibaca. Saya menyadari bahwa keterbacaan teks adalah prioritas utama sehingga saya mengubah struktur menjadi satu kolom (grid-template-columns: 1fr) dan menggeser titik timeline ke sebelah kiri (left: -1.25rem; right: auto). Selain itu, pada bagian education-card, saya menggunakan flex-direction: column-reverse agar teks penjelasan muncul duluan sebelum logo institusi.

3. Batasan Static Web dan Rencana Fungsionalitas Dinamis
Batasan utama dari static web adalah tidak adanya pembaharuan konten secara otomatis. Setiap kali saya ingin menambahkan entri prestasi baru di dalam achievment list atau menambah foto di .gallery-grid, saya harus mengedit baris kode HTML secara manual. Proses ini tidak relevan seiring dengan bertambahnya portofolio. Berdasarkan batasan tersebut, fungsi dinamis yang paling ingin saya tambahkan pada tugas selanjutnya adalah pemanggilan data (fetching API). Saya ingin menyimpan data edukasi dan gambar galeri di dalam format JSON lalu menggunakan JavaScript (fetch) untuk merender elemen DOM secara otomatis saat halaman dimuat.

AI Disclosure 

Dalam tugas ini, saya memutuskan untuk menambahkan 1 halaman di dalam portofolio saya yakni education.html. Dalam membuat halaman ini saya dibantu menggunakan generative AI, yakni ChatGPT. Saya menggunakannya untuk membantu saya dalam membuat kerangka dasar. Namun, ada beberapa kesalahan dari hasil AI ini sehingga saya perlu menganalisis dan mengubah beberapa bagian sampai menambahkan elemen tertentu yang dibutuhkan. Berikut detilnya:

1. Perbaikan Kalkulasi Posisi Titik Timeline:
* AI awalnya memposisikan titik biru di timeline menggunakan angka statis right: -0.3rem. Hal ini menyebabkan titik tidak pernah benar-benar membelah garis vertikal secara presisi di berbagai ukuran layar.
* Saya memperbaikinya dengan menarik elemen ke batas kanan (right: 0) lalu menambahkan transform: translateX(50%) agar titik tersebut bergeser tepat setengah dari dimensinya, sehingga sentris sempurna terhadap garis.

2. Penanganan Layout Shift pada Teks Tahun:
* AI memberikan lebar kolom grid sebesar 6.5rem untuk bagian tahun. Akibatnya, teks "2025 — Present" menabrak garis dan merusak layout.
* Saya memperlebar kolom menjadi 8.5rem pada konfigurasi grid dan garis vertikal. Saya juga menambahkan text-align: right dan padding-right: 1.25rem agar teks memiliki ruang bernapas (white space) dan tidak menempel pada titik linimasa.

3. Penyelesaian Bug Double Border pada List:
* AI menambahkan border-bottom pada setiap tag <li> di bagian prestasi. Kemudian, dia juga memberikan border top untuk bagian gallery. Hal inimenciptakan ilusi ruang/sel kosong yang janggal di bagian bawah tabel karena harisnya berukuran sama yakni 1 px.
* Saya cukup simple menangani hal ini dengan cara membuat garis yang menjadi pembatas antara section saya tebalkan menjadi 4px

4. Restrukturisasi Galeri Responsive:
* AI hanya memberikan pengaturan galeri statis 2 kolom (grid-template-columns: repeat(2, 1fr))
* Saya meningkatkan desainnya menjadi 3 kolom di layar utama, menambahkan batasan transisi ke 2 kolom pada breakpoint max-width: 900px, dan mengecilkannya menjadi 1 kolom penuh di layar gawai (max-width: 600px) demi menjaga proporsi gambar.

Berikut adalah link log saya dengan ChatGPT:
* https://chatgpt.com/share/6a9c41c9-59d4-83ec-85c3-9b1ce87ab307
* https://chatgpt.com/share/6a9c4215-fe28-83ec-b179-5ee2f7112fa2

## Jawaban Pertanyaan Reflektif & AI Disclosure Tugas Individual 2 +++
1. Alur ketika pengguna membuka halaman Skills, dari request hingga tampil di browser
Saat browser mengirim request GET ke path Skills, Django pertama-tama mengeceknya di urls.py level proyek (root). Di sana ada path('', include('main.urls')), jadi request diteruskan ke urls.py milik aplikasi main. Di urls.py aplikasi inilah path 'skills/' dicocokkan dan diarahkan ke view function show_skills (dengan name='show_skills', dipanggil di template lewat {% url 'main:show_skills' %}). View kemudian mengambil data lewat model, memanggil Skill.objects.filter(skill_type='Software') dan Skill.objects.filter(skill_type='Systems') lalu membungkus hasilnya ke dalam context dan memanggil render(request, 'main/skills.html', context). Template engine Django kemudian memproses skills.html, mengeksekusi tag {% for %}/{% empty %} dan menyisipkan nilai dari context ({{ skill.name }}, dst) menjadi HTML statis. Hasil HTML ini dikirim balik ke browser sebagai response, yang lalu di-render bersama style.css menjadi tampilan halaman yang dilihat pengguna.

2. Kenapa data sebaiknya disimpan di model, bukan ditulis langsung di template?
Karena model memisahkan data dari presentasi. Kalau data ditulis langsung di template (hardcoded), setiap kali saya mau menambah atau mengubah skill, saya harus mengedit source code dan deploy ulang aplikasi, rawan salah ketik dan tidak scalable begitu skill-nya banyak. Dengan model + database, saya (atau siapa pun yang punya akses admin) bisa menambah/mengubah data lewat Django admin panel tanpa menyentuh kode sama sekali. Selain itu, skill_type yang terstruktur lewat choices mencegah typo kategori, data jadi bisa di-query dan difilter (seperti yang saya lakukan untuk memisahkan software_skills dan systems_skills), dan yang penting untuk unit test — saya bisa membuat/menghapus objek Skill di database testing tanpa perlu mengubah template atau HTML manapun.

3. Perbedaan makemigrations dan migrate, beserta contoh:
makemigrations membuat file migrasi berdasarkan perbedaan antara model Python saat ini dengan riwayat migrasi sebelumnya. Perintah ini belum mengubah database sungguhan, hanya membuat "instruksi" perubahannya. migrate yang benar-benar mengeksekusi instruksi tersebut ke database, mengubah struktur tabel sesuai definisi model terbaru. Contohnya, kalau saya menambahkan field baru ke model Skill, misalnya year_learned = models.IntegerField(default=2023), saya harus menjalankan python manage.py makemigrations dulu. Django akan mendeteksi field baru ini dan membuat file migrasi yang mendeskripsikan penambahan kolom year_learned. Tapi tabel Skill di database masih belum berubah sampai saya jalankan python manage.py migrate, yang baru benar-benar menambahkan kolom tersebut ke tabel. Kalau saya cuma jalankan makemigrations tanpa migrate, aplikasi akan error saat mencoba mengakses skill.year_learned karena kolomnya belum ada di database.

AI Disclosure

Dalam tugas ini, saya memutuskan untuk menambahkan 1 halaman baru di dalam portofolio saya yakni skill.html. Dalam membuat halaman ini saya dibantu menggunakan generative AI, yakni Gemini untuk membuat kerangka dasar (HTML, CSS, dan unit test). Namun, ada beberapa kesalahan dan kekurangan dari hasil AI ini sehingga saya perlu menganalisis dan mengubah beberapa bagian, sampai menambahkan elemen tertentu yang dibutuhkan. Berikut detilnya:

1. Data Skill Tidak Dikelompokkan Berdasarkan Kategori
* AI awalnya hanya memberikan satu loop {% for skill in skills %} yang menampilkan seluruh skill dalam satu list tercampur, tanpa memisahkan berdasarkan skill_type (Software Development vs Systems & Architecture).
* Saya memperbaikinya dengan memisahkan query menjadi dua variabel di view (software_skills dan systems_skills), lalu membuat dua blok section terpisah di template agar setiap kategori tampil dengan judul dan grup masing-masing.

2. Tidak Ada Penanganan Kondisi Kosong
* Kerangka dasar dari AI tidak menyediakan mekanisme untuk menampilkan pesan ketika suatu kategori belum memiliki skill sama sekali, halaman hanya akan kosong tanpa keterangan apa-apa.
* Saya menambahkan blok {% empty %} pada masing-masing loop kategori, sehingga muncul pesan spesifik seperti "Belum ada skill Software Development yang ditambahkan." sesuai kondisi datanya.

3. Kesalahan Asumsi Tipe Field Gambar
* AI menulis {% if skill.image %}<img src="{{ skill.image.url }}"> yang mengasumsikan field gambar bertipe ImageField/FileField dengan upload otomatis.
* Padahal di model saya, field gambar bertipe CharField bernama image_filename yang menyimpan nama file statis. Saya perbaiki menjadi <img src="/static/{{ skill.image_filename }}"> agar sesuai struktur model yang sebenarnya.

4. Layout Kartu Skill Boros Ruang Kosong
* CSS dasar dari AI menyusun logo dan teks secara vertikal dalam satu kolom sempit, sehingga saat kartu melebar mengisi grid, banyak ruang kosong di samping teks yang pendek, terlihat janggal terutama saat jumlah skill sedikit.
* Saya merombak .skill-card menjadi layout dua kolom sejajar (logo di kiri, teks di kanan) dengan garis pembatas (border-right) di antara keduanya, dan memperbesar ukuran logo supaya proporsional dengan ruang kolom.

5. Palet Warna Tidak Konsisten dengan Halaman Lain
* CSS dasar dari AI menggunakan tema warna gelap (slate/navy) yang berdiri sendiri, berbeda total dari halaman Profile, Experience, dan Education yang sudah saya buat sebelumnya.
* Saya menyesuaikan seluruh warna dan tipografi di halaman ini memakai CSS custom properties yang sama dengan yang sudah saya definisikan secara global (--ink, --paper, --accent, dst.), supaya seluruh halaman portofolio terlihat sebagai satu kesatuan desain, bukan halaman terpisah.

6. Interaksi Statis Tanpa Animasi
* Kerangka dasar hanya punya transisi hover sederhana (geser sedikit ke atas dan ganti warna border).
* Saya menambahkan animasi entrance bertahap (stagger) untuk tiap kartu saat halaman dimuat, animasi garis aksen yang tumbuh di bawah judul kategori, serta dukungan prefers-reduced-motion supaya animasi tidak memaksa pada pengguna yang mengaktifkan pengaturan pengurangan gerak di perangkatnya.

7. Unit Test Belum Menguji Pemisahan dan Kondisi Campuran
* Unit test dasar hanya mencakup 3 skenario wajib (URL & template, data muncul, pesan kosong muncul), tapi belum memverifikasi bahwa data benar-benar terpisah sesuai kategori, maupun kondisi campuran (satu kategori sudah terisi, kategori lain masih kosong).
* Saya menambahkan pengecekan assertNotContains agar pesan kosong benar-benar hilang saat data sudah ada, test skenario campuran (test_empty_state_shown_only_for_type_without_data), dan test yang memverifikasi langsung dari response.context bahwa software_skills dan systems_skills terisi dengan benar tanpa tertukar (test_skills_are_grouped_under_correct_type_in_context).

Berikut adalah link log saya dengan Gemini:
* https://share.gemini.google/w6YHjWF4ke7I
