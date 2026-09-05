# Personal Portfolio Website - PBP B
Name : Justin Evan Halim Saputra
NPM : 2506549386
Class : PBP B
Year : 2

Repositori ini berisi kode sumber (*source code*) untuk website portofolio pribadi yang dikembangkan sebagai pemenuhan tugas dari mata kuliah Pemrograman Berbasis Platform (PBP) Fasilkom UI. 

## PWS Deployment Link
* [PWS Deployment Link]((https://pws.cs.ui.id/justin.evan/myportofolio))

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
Batasan utama dari static web adalah tidak adanya pembaharuan konten secara otomatis. Setiap kali saya ingin menambahkan entri prestasi baru di dalam <ul class="achievements-list"> atau menambah foto di .gallery-grid, saya harus mengedit baris kode HTML secara manual. Proses ini tidak relevan seiring dengan bertambahnya portofolio. Berdasarkan batasan tersebut, fungsi dinamis yang paling ingin saya tambahkan pada tugas selanjutnya adalah pemanggilan data (fetching API). Saya ingin menyimpan data edukasi dan gambar galeri di dalam format JSON lalu menggunakan JavaScript (fetch) untuk merender elemen DOM secara otomatis saat halaman dimuat.

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