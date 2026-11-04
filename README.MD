# Personal Portfolio Website - PBP B
Name : Justin Evan Halim Saputra
NPM : 2506549386
Class : PBP B
Year : 2

Repositori ini berisi kode sumber (*source code*) untuk website portofolio pribadi yang dikembangkan sebagai pemenuhan tugas dari mata kuliah Pemrograman Berbasis Platform (PBP) Fasilkom UI. 

## PWS Deployment Link
* [PWS Deployment Link](https://justin-evan-myportofolio.pws.cs.ui.ac.id/)

## Setup & Cara Menjalankan Secara Lokal
Proyek ini memakai Django, template Django, JavaScript `fetch()`, dan Django REST Framework (DRF). Halaman harus dijalankan melalui server Django agar URL, sesi, CSRF, dan database bekerja.

Lingkungan yang diperiksa pada 5 November 2026: Django **5.2.19** dan DRF **3.18.3** dalam `.venv`. Rentang dependensi ada di [requirements.txt](requirements.txt); dependensi belum dikunci seluruhnya dengan lockfile. Siapkan Python yang kompatibel dengan paket tersebut, Git, dan pip.

Contoh PowerShell dari direktori tempat repositori akan disimpan:

```powershell
git clone https://github.com/jhalimsaputra-cloud/myportofolio.git
cd myportofolio
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py showmigrations
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Buka [halaman lokal](http://127.0.0.1:8000/), [Skills](http://127.0.0.1:8000/skills/), atau [Projects](http://127.0.0.1:8000/projects/). Instalasi baru tidak otomatis berisi data; buat Skill melalui akun pemilik. `image_filename` memakai nama gambar dalam `static/img/`, misalnya `python.png`.

`PRODUCTION` secara default bernilai `False` dan memakai SQLite lokal `db.sqlite3`. Pastikan konfigurasi menunjuk database yang dimaksud sebelum `migrate`; cadangkan database yang sudah berisi data penting. Gunakan migrasi yang tersedia: Tugas 6 tidak menambahkan perubahan model sehingga tidak memerlukan `makemigrations` baru. Jika `PRODUCTION=True`, konfigurasi menggunakan PostgreSQL dengan variabel `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, serta `SCHEMA` opsional. Jangan commit kredensial atau database.

Cookie sesi dan CSRF saat ini tetap `Secure=True`. Login serta mutasi berhasil diperiksa pada `http://127.0.0.1:8000` di browser pengujian, tanpa perubahan konfigurasi. Hasil tersebut belum membuktikan perilaku semua browser atau host HTTP lain. Konfigurasi deployment produksi perlu ditinjau tersendiri; hasil pemeriksaan lokal bukan sertifikasi kesiapan produksi.

Untuk menguji aplikasi:

```powershell
.\.venv\Scripts\python.exe manage.py test main
```

Gunakan label `main` agar skrip Selenium di luar aplikasi tidak ikut ditemukan bila tersedia. Django membuat database test tersendiri; data utama tidak digunakan sebagai fixture test otomatis. Ringkasan API dan hasil verifikasi Tugas 6 tersedia di bagian berikut setelah dokumentasi tugas sebelumnya.

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
1. Alur ketika pengguna membuka halaman Skills, dari request hingga tampil di browser:
Saat browser mengirim request GET ke path /skills/, Django pertama-tama mengeceknya di urls.py pada level proyek (root). Di sana terdapat pengaturan path('', include('main.urls')), sehingga request diteruskan ke urls.py milik aplikasi main. Di dalam urls.py aplikasi inilah path 'skills/' dicocokkan dan diarahkan ke view function show_skills (dengan name='show_skills', yang dapat dipanggil di template melalui {% url 'main:show_skills' %}). View kemudian mengambil data melalui model dengan memanggil Skill.objects.filter(skill_type='Software') dan Skill.objects.filter(skill_type='Systems'). Hasil query ini dibungkus ke dalam context dan dipanggil melalui render(request, 'main/skills.html', context). Template engine Django kemudian memproses skills.html, mengeksekusi template tag (seperti {% for %} dan {% empty %}), serta menyisipkan nilai dari context (misalnya {{ skill.name }}) menjadi HTML statis. Hasil HTML inilah yang dikirim kembali ke browser sebagai response, yang kemudian di-render bersama dengan style.css menjadi tampilan visual yang dilihat oleh pengguna.

2. Kenapa data sebaiknya disimpan di model, bukan ditulis langsung di template:
Penyimpanan data di model dilakukan untuk memisahkan logika data dari presentasi visual (Separation of Concerns). Jika data ditulis langsung di template (hardcoded), setiap kali ada penambahan atau perubahan data skill, saya harus mengedit source code dan melakukan deploy ulang aplikasi. Hal ini rawan memicu kesalahan ketik (typo) dan tidak scalable ketika jumlah skill bertambah banyak. Dengan menggunakan model dan database, saya dapat mengelola data melalui Django Admin Panel tanpa perlu menyentuh kode program. Selain itu, penggunaan struktur parameter seperti choices pada skill_type dapat mencegah kesalahan penulisan kategori. Data juga menjadi lebih mudah di-query dan difilter. Terakhir, pendekatan ini sangat berguna untuk unit testing. Saya bisa membuat atau menghapus objek Skill di database pengujian tanpa harus mengubah struktur HTML sama sekali.

3. Perbedaan makemigrations dan migrate, beserta contoh:
makemigrations berfungsi untuk membuat file migrasi berdasarkan perubahan atau perbedaan antara definisi model Python saat ini dengan riwayat migrasi sebelumnya. Perintah ini belum mengubah database sungguhan, melainkan hanya membuat "instruksi" atau draf perubahannya. migrate adalah perintah yang benar-benar mengeksekusi instruksi dari file migrasi tersebut ke dalam database, sehingga struktur tabel berubah menyesuaikan definisi model yang terbaru.

AI Disclosure

Dalam pengerjaan tugas ini, saya memutuskan untuk menambahkan satu halaman baru di dalam portofolio saya, yakni skills.html. Dalam membuat halaman ini, saya dibantu oleh generative AI (Gemini) untuk membuat kerangka dasar (HTML, CSS, dan unit test). Namun, terdapat beberapa ketidaksesuaian dan kekurangan dari hasil AI tersebut, sehingga saya harus melakukan analisis, modifikasi, dan penambahan elemen agar sesuai dengan spesifikasi aplikasi saya. Berikut adalah detail perbaikannya:

1. Data Skill Tidak Dikelompokkan Berdasarkan Kategori
* Output AI: Awalnya hanya memberikan satu loop {% for skill in skills %} yang menampilkan seluruh skill dalam satu list tercampur, tanpa memisahkan berdasarkan skill_type.
* Perbaikan: Saya memperbaiki ini dengan memisahkan query menjadi dua variabel di view (software_skills dan systems_skills), lalu membuat dua blok section terpisah di template agar setiap kategori tampil dengan judul dan grup masing-masing.

2. Tidak Ada Penanganan Kondisi Kosong (Empty State)
* Output AI: Kerangka dasar tidak menyediakan mekanisme ketika suatu kategori belum memiliki skill sama sekali (halaman hanya kosong tanpa keterangan).
* Perbaikan: Saya menambahkan blok {% empty %} pada masing-masing loop kategori, sehingga akan muncul pesan spesifik seperti "Belum ada skill Software Development yang ditambahkan" sesuai kondisi datanya.

3. Kesalahan Asumsi Tipe Field Gambar
* Output AI: AI menulis {% if skill.image %}(img src="{{ skill.image.url }}"), yang mengasumsikan field gambar bertipe ImageField atau FileField dengan konfigurasi upload otomatis.
* Perbaikan: Pada model saya, field gambar bertipe CharField dengan nama image_filename yang menyimpan nama file statis. Saya mengubahnya menjadi (img src="/static/{{ skill.image_filename }}") agar sesuai dengan struktur model sebenarnya.

4. Tata Letak (Layout) Kartu Skill yang Boros Ruang
* Output AI: CSS dasar dari AI menyusun logo dan teks secara vertikal dalam satu kolom sempit. Saat kartu melebar mengikuti sistem grid, banyak ruang kosong yang tersisa di samping teks pendek sehingga terlihat janggal.
* Perbaikan: Saya merombak class .skill-card menjadi layout dua kolom sejajar (logo di kiri, teks di kanan) dengan garis pembatas (border-right) di antara keduanya. Saya juga memperbesar ukuran logo supaya lebih proporsional dengan ruang kolom.

5. Inkonsistensi Palet Warna dengan Halaman Lain
* Output AI: Menggunakan tema warna gelap (slate/navy) mandiri yang berbeda total dari halaman Profile, Experience, dan Education yang sudah saya buat.
* Perbaikan: Saya menyesuaikan seluruh warna dan tipografi di halaman ini menggunakan CSS custom properties global yang sudah saya definisikan sebelumnya (--ink, --paper, --accent, dst.). Hal ini memastikan seluruh halaman portofolio memiliki kesatuan desain (cohesive).

6. Interaksi yang Statis Tanpa Animasi
* Output AI: Hanya memiliki transisi hover sederhana (bergeser sedikit ke atas dan mengubah warna border).
* Perbaikan: Saya menambahkan animasi entrance bertahap (stagger) untuk tiap kartu saat halaman dimuat, animasi garis aksen yang memanjang di bawah judul kategori, serta implementasi media query prefers-reduced-motion agar animasi tidak mengganggu pengguna yang mengaktifkan pengaturan pengurangan gerak di perangkatnya.

7. Cakupan Unit Test yang Kurang Menyeluruh
* Output AI: Unit test hanya mencakup 3 skenario wajib (URL & template cocok, data muncul, dan pesan kosong muncul). AI belum memverifikasi pemisahan data per kategori atau kondisi campuran.
* Perbaikan: Saya menambahkan asersi assertNotContains agar pesan kosong terverifikasi hilang saat data sudah ada. Saya juga membuat skenario uji campuran (test_empty_state_shown_only_for_type_without_data) dan menguji langsung dari response.context untuk memastikan software_skills dan systems_skills terisi dengan benar tanpa tertukar (test_skills_are_grouped_under_correct_type_in_context).

Berikut adalah link log saya dengan Gemini:
* https://share.gemini.google/w6YHjWF4ke7I

## Jawaban Pertanyaan Reflektif & AI Disclosure Tugas Individual 3 +++

1. Kenapa pakai ModelForm dan kenapa perlu {% csrf_token %}?
Saya pakai ModelForm karena lebih praktis dan nggak perlu bikin form HTML dari awal satu per satu. Field di form juga bisa langsung ngikutin model yang sudah saya buat, jadi lebih konsisten dan mengurangi kemungkinan salah. Selain itu, validasi data juga jadi lebih gampang karena Django sudah bantu ngecek sesuai aturan di model. Sementara {% csrf_token %} dipakai buat keamanan. Token ini membantu mencegah request palsu dari website lain yang mencoba mengirim data ke aplikasi kita tanpa izin user. Jadi setiap form yang mengirim data dengan method POST sebaiknya pakai csrf_token.

2. Kenapa JSON lebih sering dipakai daripada XML?
JSON lebih populer karena formatnya lebih simpel, lebih ringkas, dan gampang dibaca baik oleh manusia maupun program. Di JavaScript juga JSON bisa langsung diubah jadi object, jadi cocok banget buat komunikasi antara frontend dan backend. Dibanding XML, JSON biasanya butuh lebih sedikit karakter dan strukturnya juga nggak seribet tag-tag XML.

3. Kenapa model Django perlu diserialisasi sebelum dikembalikan sebagai JSON?
Karena object dari model Django nggak bisa langsung dikirim dalam bentuk JSON. Model Django masih berupa object Python yang punya struktur dan atribut khusus. Jadi perlu proses serialization dulu supaya datanya diubah ke format yang bisa dipahami sebagai JSON, misalnya string, angka, list, atau dictionary. Setelah itu baru datanya bisa dikirim ke frontend atau dipakai aplikasi lain.

AI Disclosure

Dalam pengerjaan tugas ini, saya menambahkan fitur CRUD untuk halaman Skills pada portofolio saya. Untuk membuat kerangka awalnya, saya dibantu oleh generative AI (Gemini), terutama untuk contoh implementasi model, form, view, URL, serta template dasar. Namun, kode awal yang diberikan masih cukup umum dan belum sesuai dengan struktur serta kebutuhan portofolio saya. Karena itu, saya melakukan beberapa analisis dan perubahan agar implementasinya lebih sesuai dengan desain dan requirement tugas. Berikut beberapa perubahan utama yang saya lakukan:

1. URL dan View Awalnya Masih Menggunakan Integer ID
* Output AI: URL awal menggunakan pola seperti <int:id> pada fungsi update dan delete karena model awal masih memakai ID bawaan Django.
* Perbaikan: Setelah saya menggunakan UUID pada model Skill, saya menyesuaikan URL menjadi <uuid:skill_id>. Parameter pada fungsi update_skill dan delete_skill juga saya ubah menjadi skill_id agar konsisten dengan URL dan model yang digunakan.

2. Form Create dan Update Awalnya Dibuat Terpisah
* Output AI: AI memberikan create_skill.html dan update_skill.html sebagai dua template yang berbeda, walaupun isi keduanya hampir sama.
* Perbaikan: Saya menggabungkan kedua form tersebut menjadi satu file yaitu skill_form.html. Template ini dapat mengetahui apakah sedang digunakan untuk menambah atau mengubah data berdasarkan keberadaan object skill di context. Dengan begitu, kode menjadi lebih ringkas dan tidak banyak duplikasi.

3. Delete Awalnya Hanya Menggunakan Konfirmasi Browser Biasa
* Output AI: Tombol delete awal menggunakan onclick="return confirm(...)" dan langsung mengirim form POST.
* Perbaikan: Saya menggantinya dengan komponen modal khusus skill_delete_modal.html. Modal ini menampilkan konfirmasi sebelum data benar-benar dihapus. Proses delete tetap menggunakan method POST dan {% csrf_token %} supaya lebih aman. Saya juga memisahkan modal tersebut ke folder components agar template utama tidak terlalu penuh.

4. Tampilan Awal Tidak Konsisten dengan Halaman Portofolio Lain
* Output AI: CSS awal menggunakan warna dan class sendiri seperti .btn-add, .btn-update, dan .btn-delete, serta menggunakan styling langsung di dalam template.
* Perbaikan: Saya memindahkan styling ke file CSS utama dan menggunakan kembali variabel global seperti --ink, --paper, --accent, --line, dan --radius. Saya juga menyesuaikan layout Skill Card agar logo berada di kiri dan informasi skill di kanan, serta membuat tombol Update dan Delete sejajar dengan tampilan yang sama seperti elemen lain di website.

5. Alur JSON Awalnya Hanya Digunakan di JavaScript
* Output AI: Data diambil menggunakan fetch() pada JavaScript, kemudian langsung dirender ke HTML dari sisi browser.
* Perbaikan: Saya menyesuaikan mekanismenya dengan requirement tugas. Fungsi get_skills_json() melakukan serialization terhadap data Skill, lalu show_skills() mengambil response JSON tersebut dan melakukan serializers.deserialize() sebelum datanya diteruskan ke template. Dengan begitu, bagian serialization dan deserialization JSON dapat terlihat jelas pada implementasi Django saya.

6. Fungsi View Awalnya Belum Sesuai dengan Alur Halaman Saya
* Output AI: Fungsi create_skill() dan update_skill() awalnya melakukan redirect ke show_main atau show_skill, serta menggunakan parameter umum bernama id. Selain itu, create dan update diarahkan ke template yang berbeda.
* Perbaikan: Saya mengubah redirect keduanya menjadi main:show_skills agar setelah create atau update pengguna kembali ke halaman Skills. Pada update_skill(), saya menggunakan get_object_or_404(Skill, pk=skill_id) untuk mengambil data berdasarkan UUID, kemudian menghubungkannya ke SkillForm menggunakan instance=skill. Create dan update juga saya arahkan ke satu template yang sama, yaitu skill_form.html.

Berikut adalah link log saya dengan Gemini:
* https://share.gemini.google/eTITSlshYxYc

## AI Disclosure Tugas Individual 4 +++

AI Disclosure

Dalam pengerjaan tugas ini, saya memutuskan untuk mengimplementasikan access permission di halaman skills saya. Saya menambah fitur toggle star bagi para pengguna yang sudah login. Saya juga memberikan beberapa fitur yang hanya bisa diakses oleh editor(update) dan super user saja(update, delete, dan create). Sebagian besar referensi saya berasal dari Tutorial 3 sehingga saya jarang menggunakan AI. Saya hanya menggunakan Gemini untuk memberikan saya template awal HTML dan CSS. Berikut perbaikan dan analisisnya.

1. Status Star Belum Cukup Jelas
* Output AI: Tombol hanya menampilkan bintang dan angka. Pengguna harus melihat warna bintang untuk mengetahui apakah ia sudah memberi star.
* Perbaikan: Saya menambahkan tulisan Star dan Starred sesuai status pengguna. Warna tombol juga ikut berubah ketika skill sudah diberi star.

2. Tombol Belum Memiliki Keterangan yang Cukup
* Output AI: Tombol belum memberi penjelasan tambahan tentang aksi yang akan dilakukan.
* Perbaikan: Saya menambahkan keterangan Beri star atau Batalkan star melalui atribut title. Saya juga menambahkan aria-pressed untuk menunjukkan status tombol dan menandai ikon SVG sebagai elemen dekoratif.

3. Tampilannya Belum Cocok dengan Halaman Skill
* Output AI: Tombol berbentuk sederhana dan transparan, dengan warna abu-abu saat belum diberi star dan emas saat sudah diberi star.
* Perbaikan: Saya membuat desain baru dengan warna yang sesuai dengan portofolio saya. Tombol ditempatkan di sisi kanan atas judul skill, sedangkan jumlah star ditampilkan dalam kotak kecil di dalam tombol. Saya juga menambahkan efek saat tombol disorot, ditekan, dan dipilih menggunakan keyboard. Untuk pengguna yang mengaktifkan pengurangan animasi, efek geraknya saya nonaktifkan melalui prefers-reduced-motion.

Berikut adalah link log saya dengan Gemini:
* https://share.gemini.google/OBextQA5HM9A

## Jawaban Pertanyaan Reflektif & AI Disclosure Tugas Individual 5 +++
1. Apa itu debouncing dan kenapa penting untuk pencarian AJAX?
Debouncing adalah cara memberi jeda sebelum menjalankan suatu proses. Pada fitur pencarian saya, pencarian baru dijalankan setelah pengguna berhenti mengetik selama 300 milidetik. Kalau pengguna mengetik lagi sebelum jedanya selesai, waktu tunggunya dimulai ulang. Dengan begitu, aplikasi tidak akan mengirim request untuk setiap huruf yang diketik. Ini membantu mengurangi request ke server dan menghindari pencarian untuk kata yang belum selesai ditulis.

2. Apa fungsi await saat menggunakan fetch() dan apa yang terjadi kalau tidak dipakai?
await digunakan untuk menunggu hasil dari Promise sebelum melanjutkan baris berikutnya dalam fungsi async. Saat saya menulis const response = await fetch(url), kode menunggu sampai respons tersedia tanpa membuat seluruh halaman berhenti bekerja. Setelah itu, saya menggunakan await response.json() untuk menunggu isi respons selesai dibaca sebagai data JSON. Kalau await dihapus tanpa menggantinya dengan penanganan seperti .then(), variabel response masih berisi Promise. Akibatnya, kode yang langsung memanggil response.json() akan error karena responsnya belum didapatkan.

3. Apa itu XSS dan kenapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan dibandingkan template Django?
XSS atau Cross-Site Scripting adalah serangan ketika penyerang menyisipkan kode berbahaya yang kemudian dijalankan di browser pengguna. Risiko ini muncul kalau data dari pengguna dimasukkan langsung ke innerHTML karena browser bisa membacanya sebagai HTML. Sementara itu, template Django secara default melakukan escaping pada nilai variabel sehingga karakter HTML ditampilkan sebagai teks. Jadi, AJAX sendiri bukan penyebab XSS, yang menentukan adalah cara datanya ditampilkan. Pada kode saya, saya menggunakan escapeHtml() sebelum memasukkan data ke HTML, textContent untuk pesan teks, dan strip_tags() pada form di server sebagai perlindungan tambahan.

AI Disclosure

Dalam pengerjaan tugas ini, saya menggunakan bantuan generative AI, yakni Gemini, untuk membuat kode awal fitur AJAX di halaman Skills. Kode tersebut mencakup pengambilan data, pencarian, modal tambah skill, dan pengiriman form. Namun, beberapa bagian masih berupa contoh umum dan belum sesuai dengan aplikasi saya, sehingga saya menyesuaikannya sebagai berikut:

1. Nama Field dan URL Belum Sesuai
* Output AI: Kode awal menggunakan field title, proficiency_level, dan image_url. Nama URL yang digunakan juga berbeda dengan yang ada di aplikasi saya.
* Perbaikan: Saya menggantinya dengan field yang sesuai, yaitu name, skill_type, description, dan image_filename. Saya juga menyesuaikan nama URL menjadi toggle_star_skill dan create_skill_ajax.

2. Semua Skill Ditampilkan dalam Satu Grid
* Output AI: Semua skill ditampilkan dalam satu daftar tanpa dibedakan berdasarkan kategori.
* Perbaikan: Saya memisahkan skill menjadi dua bagian, yaitu Software Development dan Systems & Architecture, berdasarkan nilai skill_type. Saya juga menambahkan pesan ketika salah satu kategori tidak memiliki data.

3. Gambar dan Kartu Skill Belum Sesuai dengan Tampilan Saya
* Output AI: Kode awal menggunakan image_url untuk gambar dan struktur kartu yang masih umum.
* Perbaikan: Karena aplikasi saya menyimpan nama file gambar di image_filename, saya menggabungkannya dengan lokasi gambar statis. Struktur kartunya juga saya sesuaikan agar logo, nama, deskripsi, dan tombol mengikuti tampilan halaman Skills.

4. Pencarian Hanya Berjalan Setelah Tombol Cari Ditekan
* Output AI: Pencarian dijalankan saat form dikirim dan masih menggunakan parameter title.
* Perbaikan: Saya mengganti parameter menjadi name dan menambahkan debounce selama 300 milidetik. Dengan begitu, pencarian berjalan otomatis setelah pengguna berhenti mengetik. Tombol Cari dan Enter tetap bisa digunakan untuk mencari langsung.

5. Penanganan Pengambilan Data Perlu Dilengkapi
* Output AI: Kode awal sudah membatalkan permintaan sebelumnya menggunakan AbortController, tetapi belum memeriksa kembali apakah permintaan dibatalkan setelah JSON diterima.
* Perbaikan: Saya menambahkan pemeriksaan sebelum data ditampilkan. Jika pengambilan data gagal, halaman juga menampilkan pesan error dan toast agar pengguna mengetahui masalahnya.

6. Respons Server dan Pengiriman CSRF Perlu Disesuaikan
* Output AI: View awal mengembalikan form.errors, sedangkan JavaScript mengambil token CSRF dari cookie.
* Perbaikan: Saya menggunakan form.errors.get_json_data() agar pesan validasi lebih mudah dibaca oleh JavaScript. Token CSRF dikirim bersama FormData dari field {% csrf_token %}. Pemeriksaan superuser di view serta status respons 201, 400, dan 403 tetap saya gunakan.

7. Data dari JSON Belum Di-escape
* Output AI: Nama, deskripsi, dan data lain langsung dimasukkan ke innerHTML.
* Perbaikan: Saya menambahkan escapeHtml() agar karakter HTML pada data ditampilkan sebagai teks. Pada sisi server, saya juga menggunakan strip_tags() dalam metode pembersihan field di SkillForm.

8. Tombol Pengelolaan Skill Perlu Disesuaikan
* Output AI: Kode awal menyediakan tombol star dan tombol hapus dengan konfirmasi confirm().
* Perbaikan: Saya menambahkan tombol Update sesuai permission pengguna dan mengganti konfirmasi hapus dengan modal. Tombol Delete tetap khusus untuk superuser. Tampilan star juga saya sesuaikan agar menunjukkan status, jumlah star, dan pengguna yang memberi star.

Berikut adalah link log saya dengan Gemini:
* https://share.gemini.google/sz1nL3GX9Vi8

## Implementasi Individual Assignment 6

Bagian mandiri yang dilanjutkan dari Tugas 3–5 adalah **Skill**, bukan Project. Model Skill, UUID, kategori, data, dan relasi `starred_by` yang sudah ada digunakan kembali. API dan halaman **Project** dari Tutorial 07 tetap tersedia dengan aturan akses tutorialnya sendiri.

### Perubahan wajib dan struktur kode

- [main/serializers.py](main/serializers.py): `SkillSerializer` dengan field eksplisit `id`, `name`, `skill_type`, `description`, `image_filename`, `star_count`, dan `is_starred`. Identitas dan informasi star bersifat read-only; email, hash password, serta relasi akun tidak diekspos.
- Input teks dibersihkan melalui `validate_<field>` dengan `strip_tags` dan pemangkasan whitespace. Teks wajib yang menjadi kosong ditolak. Batas panjang dan pilihan kategori mengikuti field serializer dari model. `skill_type` diperiksa oleh ChoiceField sebelum validator field dijalankan.
- [main/permissions.py](main/permissions.py): `IsPortfolioOwnerOrEditorOrReadOnly` mengikuti izin `main.change_skill` dari view edit lama. Nama Group `Editor` saja tidak memberikan akses; izin dapat diberikan langsung atau melalui Group yang memiliki permission tersebut.
- [main/api_views.py](main/api_views.py): function-based API dengan `@api_view`, `SessionAuthentication`, dan `Response`. Permission mengatur akses, serializer memvalidasi input, view mengatur alur request. Star memakai `IsAuthenticated` dan selalu mengambil identitas dari `request.user`.
- [main/api_urls.py](main/api_urls.py): endpoint Skill berada pada prefix `/api/v1/` bersama Project dan menggunakan converter UUID.
- [templates/skill.html](templates/skill.html): daftar, cari, tambah, edit, hapus, dan star/unstar memakai API tanpa reload. Form tambah/edit mengirim JSON dengan POST/PATCH; hapus memakai DELETE. Semua mutasi mengirim `X-CSRFToken`. Token template tersedia bagi setiap peran; kesalahan API dan jaringan ditampilkan melalui toast.
- Teks pada markup kartu di-escape dengan `escapeHtml`; teks modal dan toast memakai `textContent`. Kontrol mengikuti peran, tetapi server tetap menjadi penentu izin. Endpoint JSON dan form lama dipertahankan untuk kompatibilitas.

### API dan hak akses

| Endpoint | Metode | Nama URL | Perilaku |
|---|---|---|---|
| `/api/v1/skills/` | GET, HEAD | `api:skill-list` | Daftar terurut menurut nama dan UUID |
| `/api/v1/skills/?name=python` | GET | `api:skill-list` | Pencarian nama, case-insensitive; whitespace parameter dipangkas |
| `/api/v1/skills/` | POST | `api:skill-list` | Membuat Skill |
| `/api/v1/skills/<uuid>/` | GET, HEAD | `api:skill-detail` | Detail Skill |
| `/api/v1/skills/<uuid>/` | PUT, PATCH | `api:skill-detail` | Mengganti seluruh field wajib atau memperbarui sebagian field |
| `/api/v1/skills/<uuid>/` | DELETE | `api:skill-detail` | Menghapus Skill |
| `/api/v1/skills/<uuid>/star/` | POST | `api:skill-star` | Toggle star untuk akun pada sesi |

Endpoint juga mendukung OPTIONS dari DRF. Project tetap berada di `/api/v1/projects/`, dengan detail dan star menggunakan pola yang sama seperti Tutorial 07. Izin Editor pada tabel berikut khusus Skill; API Project tetap membatasi penulisan data pada pemilik.

| Peran | Daftar/detail | Star/unstar | POST Skill | PUT/PATCH Skill | DELETE Skill |
|---|---|---|---|---|---|
| Tanpa login | Ya | Tidak | Tidak | Tidak | Tidak |
| Pengguna biasa | Ya | Ya | Tidak | Tidak | Tidak |
| Editor dengan `main.change_skill` | Ya | Ya | Tidak | Ya | Tidak |
| Pemilik/superuser | Ya | Ya | Ya | Ya | Ya |

Status respons: 200 untuk pembacaan/perubahan/star, 201 saat dibuat, 400 untuk input invalid, 403 untuk izin atau CSRF yang ditolak, 404 untuk objek yang tidak ditemukan, dan 204 tanpa isi setelah penghapusan. Status 404 untuk mutasi diperiksa menggunakan akun yang memang berhak; pengguna tanpa hak dapat ditolak 403 sebelum pencarian objek.

Contoh payload pembuatan atau PUT lengkap:

```json
{
  "name": "Python",
  "skill_type": "Software",
  "description": "Pengembangan backend Django",
  "image_filename": "python.png"
}
```

PATCH dapat mengirim hanya `{"description": "Deskripsi baru"}`. PUT tanpa field wajib menghasilkan 400. Field `id`, `star_count`, dan `is_starred` tidak dapat ditulis; payload `starred_by` tidak mengubah relasi star. Endpoint star tidak menerima identitas akun dari klien. Jangan mengulang POST star secara otomatis ketika respons jaringan tidak pasti, karena toggle kedua membatalkan toggle pertama.

### Cara mencoba halaman dan Browsable API

1. Jalankan server dan buka `/skills/`. Sebagai pengunjung, coba pencarian; login diperlukan untuk star.
2. Buat akun biasa melalui `/register/`, lalu login di `/login/`. Akun tersebut dapat star/unstar, tetapi tidak mengelola Skill.
3. Dengan superuser di `/admin/`, berikan permission aplikasi main untuk **change skill** kepada akun Editor, langsung atau melalui Group. Login ulang setelah mengganti permission sebelum memeriksa aksesnya.
4. Editor dapat membuka Update, mengubah isian, dan menyimpan melalui PATCH. Pemilik juga dapat memakai Add Skill dan modal konfirmasi Delete. Hasil server dimuat ulang ke daftar melalui API.
5. Untuk mencoba API secara langsung, buka `/api/v1/skills/`. Gunakan login Browsable API pada `/api-auth/login/`; ambil UUID dari daftar untuk membuka detail. Form JSON yang tersedia mengikuti metode yang diizinkan. Gunakan data yang boleh diubah untuk POST/PUT/PATCH/DELETE.

### Fitur ekstra dan kualitas kode

**Tambahan baru Tugas 6:** modal tambah/edit memfokuskan input nama saat dibuka, menjaga Tab/Shift+Tab di dalam modal, mendukung Escape, dan mengembalikan fokus ke tombol pemicu. Setelah PATCH membangun ulang kartu, fokus dicari kembali berdasarkan UUID; jika kartu tidak lagi tampil, tersedia fallback ke Add Skill atau pencarian. Petunjuk keyboard terhubung melalui `aria-describedby`. Ini membantu pengguna keyboard melanjutkan pekerjaan tanpa kehilangan posisi.

**Fitur yang dipertahankan dari Tugas 5:** debounce 300 ms, pembatalan request daftar lama, loading/error/empty state, dan pencegahan submit tambah ganda. Fitur lama tersebut tidak dihitung sebagai tambahan baru Tugas 6.

Daftar Skill memakai `prefetch_related("starred_by")` agar kedua field star memanfaatkan data yang sudah dimuat. `test_prefetch_keeps_list_query_count_constant` membuktikan request daftar berisi lima Skill oleh pengguna terautentikasi dengan `force_authenticate` menggunakan **2 query**. Angka ini hanya mencakup konteks test tersebut, bukan seluruh query sesi/login pada request produksi. Docstring dan komentar menjelaskan alasan permission, sanitasi, prefetch, serta pemulihan fokus setelah render ulang.

### Hasil verifikasi dan batasan

Pemeriksaan terakhir setelah perubahan aksesibilitas: **46 test `main` lulus**, termasuk test Tutorial 07. Detail pemetaan persyaratan dan bukti ada di [matriks audit](docs/assignment-6-plan.md).

| Jenis pemeriksaan | Hasil yang diamati |
|---|---|
| Otomatis: Skill API | Empat peran membaca; tamu/pengguna ditolak menulis; Editor PUT/PATCH dan ditolak POST/DELETE; pemilik CRUD; database diperiksa pada penolakan |
| Otomatis: validasi dan star | Sanitasi, input kosong/panjang/kategori, PUT wajib lengkap, PATCH parsial, field read-only, privasi, pencarian, 404, toggle star dan identitas payload diabaikan |
| Otomatis: CSRF | `.login()` dengan `APIClient(enforce_csrf_checks=True)` menolak mutasi tanpa token tanpa mengubah database; token valid memungkinkan edit Editor dan star pengguna |
| Otomatis: halaman dan regresi | Form sesuai peran, cookie CSRF, kategori/empty state, kompatibilitas JSON lama, dan test Project Tutorial 07 |
| Browser, database sementara | Pengunjung mencari; pengguna star/unstar; Editor edit dan toast 400; pemilik tambah/hapus; Browsable API daftar/detail; Project tampil, mencari, star/unstar |
| Browser, konfigurasi SQLite lokal asli | Login tiga peran, star/unstar, edit Editor, serta tambah/hapus pemilik berhasil tanpa mengubah settings; fixture dan akun uji dibersihkan setelah selesai |
| Browser, aksesibilitas | Fokus awal nama, Tab/Shift+Tab berputar, Escape/Batal mengembalikan fokus, dan fokus Update kembali setelah PATCH/render ulang berhasil |

Keterbatasan yang masih relevan:

- Review dokumentasi menemukan regresi terhadap Tugas 5: API Skill baru belum memuat nama pemberi star sehingga tooltip hanya menampilkan aksi dan jumlah. Pemulihan informasi tersebut perlu persetujuan perubahan kode tersendiri sebelum dokumentasi ini dianggap final.
- Belum ada pengukuran coverage, pengujian beban, race antar-request star bersamaan, atau pengujian lintas browser/perangkat dan screen reader. Test lulus tidak membuktikan semua skenario yang mungkin.
- Daftar belum memakai pagination. Prefetch pengguna pemberi star membatasi jumlah query, tetapi konsumsi memori tetap tumbuh bersama data.
- Peningkatan fokus keyboard baru berlaku pada modal tambah/edit; modal konfirmasi hapus tidak memperoleh focus trap baru pada tahap ini.
- Peringatan lama `models.W042` pada Mahasiswa dan folder `staticfiles` yang belum dikumpulkan tetap muncul saat test. Tidak menyebabkan test gagal; tidak diubah dalam lingkup Tugas 6 ini.
- Pengujian browser menggunakan server lokal. Deployment PWS, status publik repositori, waktu push prasyarat Tutorial 07, serta pengumpulan SCELE belum diverifikasi dalam sesi ini.



### Tugas 6

1. **REST, JSON, PUT, dan PATCH.** REST adalah gaya arsitektur dengan batasan client-server, stateless, cache, uniform interface, layered system, serta code-on-demand yang opsional. Uniform interface mencakup identitas resource, representasi, pesan yang menjelaskan dirinya, dan hypermedia. JSON hanya format data, sehingga respons JSON saja belum membuktikan API memenuhi batasan REST. Pada proyek ini, UUID mengidentifikasi Skill dan metode/status HTTP membedakan operasi; SessionAuthentication tetap memakai sesi server dan respons belum menyediakan hypermedia lengkap, sehingga saya tidak mengklaim kepatuhan REST penuh. [Sumber: Fielding, bab REST](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).

   PUT menyampaikan keadaan pengganti resource, sedangkan PATCH menyampaikan perubahan sebagian. Contoh pada API ini: PUT detail Skill membawa keempat field wajib; PATCH `{"description": "Deskripsi baru"}` hanya mengubah deskripsi. View memakai `partial=True` hanya untuk PATCH; PUT yang tidak lengkap ditolak 400. Pilih PUT ketika klien mengirim representasi lengkap dan PATCH ketika hanya sebagian field diubah. [RFC 9110, PUT](https://www.rfc-editor.org/rfc/rfc9110.html#name-put), [RFC 5789, PATCH](https://www.rfc-editor.org/rfc/rfc5789.html), [DRF partial updates](https://www.django-rest-framework.org/api-guide/serializers/#partial-updates).

2. **Serializer DRF.** Serializer menerjemahkan objek menjadi data primitif untuk respons serta memvalidasi dan menyimpan input. Dibanding dictionary manual dengan JsonResponse pada Tutorial 05, SkillSerializer memusatkan field keluaran, aturan input, dan proses create/update. Proyek menulis field secara eksplisit, membersihkan teks dalam validate_<field>, dan menghitung star_count/is_starred sebagai read-only. Karena itu daftar dan detail tidak perlu menyusun dictionary terpisah; kesalahan validasi juga dapat dikirim dengan struktur yang konsisten. Batas panjang dan pilihan field diturunkan ModelSerializer dari model, sedangkan aturan tambahan tetap perlu ditulis dan diuji. [Sumber: DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/).

3. **Autentikasi dan otorisasi.** Autentikasi menentukan siapa yang mengirim request; SessionAuthentication membaca sesi login Django dan mengisi request.user. Otorisasi menentukan tindakan yang boleh dilakukan akun tersebut. Pada Skill, permission class mengizinkan pembacaan publik, PUT/PATCH bagi akun dengan main.change_skill, dan CRUD penuh bagi superuser. Endpoint star memerlukan IsAuthenticated. Tombol tersembunyi hanya membantu tampilan: pengguna tetap dapat mengirim request sendiri dari luar halaman, sehingga server harus memeriksa izin sebelum mutasi. Test juga memastikan permintaan yang ditolak tidak mengubah database. [DRF authentication](https://www.django-rest-framework.org/api-guide/authentication/), [DRF permissions](https://www.django-rest-framework.org/api-guide/permissions/).

4. **SessionAuthentication dan CSRF.** Browser dapat mengirim cookie sesi secara otomatis; tanpa verifikasi CSRF, situs lain berpotensi mencoba tindakan memakai sesi korban. Karena itu POST, PUT, PATCH, dan DELETE pada sesi terautentikasi tetap memerlukan token CSRF valid. Halaman Skill menyediakan token template/cookie, dan requestSkill mengirim X-CSRFToken untuk mutasi. force_authenticate mengisi identitas secara langsung, melewati autentikasi sesi sehingga tidak membuktikan login ataupun CSRF. Test terpisah memakai APIClient(enforce_csrf_checks=True) dan .login(), memeriksa 403 tanpa token serta database tetap, lalu keberhasilan token valid. [DRF SessionAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#sessionauthentication), [DRF testing: CSRF validation](https://www.django-rest-framework.org/api-guide/testing/#csrf-validation).

### AI disclosure Tugas 6

Dalam pengerjaan Tugas 6 ini, saya menggunakan bantuan generative AI, yakni Gemini, untuk memahami konsep dasar dan membuat kerangka awal implementasi Django REST Framework (DRF) pada fitur Skills saya. Bantuan AI mencakup pembuatan serializer, permission classes, API views, hingga penulisan test. Namun, kode yang dihasilkan AI masih bersifat umum dan belum sepenuhnya memenuhi spesifikasi rubrik tugas, sehingga saya melakukan modifikasi dan analisis kritis sebagai berikut:

1. Penyesuaian Serializer dan Validasi Keamanan
  - Output: Contoh awal menggunakan django.core.serializers.serialize() untuk mengubah objek Skill menjadi JSON, tanpa memberikan implementasi serializer DRF dan field perhitungan star.
  - Perbaikan: Saya mengimplementasikan SkillSerializer berbasis ModelSerializer dengan daftar field eksplisit, termasuk name, skill_type, description, dan image_filename. Saya mengatur agar field perhitungan star bersifat read-only, dan memastikan respons tidak menyertakan data sensitif pengguna. Untuk validasi teks, saya menggunakan strip_tags() untuk membersihkan tag HTML, disertai escaping pada frontend untuk mengurangi risiko XSS.

2. Implementasi Hak Akses
  - Output: Contoh awal belum menyediakan permission DRF yang membedakan pengunjung, pengguna biasa, Editor, dan owner. Contoh awal juga menyarankan relasi kepemilikan Skill.user, yang tidak sesuai dengan model portofolio yang sudah digunakan.
  - Perbaikan: Saya mempertahankan model Skill yang sudah ada. Untuk API daftar dan detail, saya menggunakan IsPortfolioOwnerOrEditorOrReadOnly. Pengunjung hanya dapat membaca; pengguna login dapat memberi atau membatalkan star; Editor dengan permission main.change_skill dapat melakukan PUT/PATCH, tetapi tidak dapat membuat atau menghapus data. Owner yang direpresentasikan sebagai superuser memiliki akses penuh. Pada endpoint star, saya menggunakan IsAuthenticated dan mengambil identitas dari request.user.

3. Pembuatan API Views dan Penanganan Status HTTP
  - Output: Contoh menggunakan function-based views Django biasa untuk mengambil daftar dan menambahkan Skill. Contoh tersebut belum memakai DRF serta mengembalikan 404 ketika input tambah tidak lengkap.
  - Perbaikan: Saya mengimplementasikan function-based API views dengan dekorator @api_view dan SessionAuthentication. Saya menyesuaikan status respons menjadi: 201 untuk pembuatan berhasil, 400 untuk validasi gagal, 403 untuk akses yang ditolak, 404 untuk objek yang tidak ditemukan setelah pemeriksaan izin, dan 204 untuk penghapusan berhasil. Penanganannya menggunakan respons eksplisit serta mekanisme validasi dan exception DRF/Django. Saya juga menambahkan fitur pencarian melalui parameter query name pada endpoint daftar.

4. Integrasi Frontend, Fetch API, dan CSRF
  - Output: Contoh menyertakan token CSRF dalam form, tetapi endpoint tambah menggunakan @csrf_exempt, sehingga pemeriksaan CSRF pada endpoint tersebut dinonaktifkan. Contoh juga belum memeriksa response.ok dan memasukkan data langsung ke innerHTML tanpa escaping.
  - Perbaikan: Saya memastikan API perubahan data tetap menggunakan pemeriksaan CSRF. Saya membuat helper JavaScript untuk menyisipkan header X-CSRFToken pada setiap permintaan perubahan data, memeriksa respons API, dan menampilkan pesan kesalahan seperti 400 atau 403 melalui toast. Data juga saya escape terlebih dahulu sebelum dirender ke DOM. Saya mengimplementasikan modal edit yang mengirim permintaan PATCH tanpa reload halaman, sementara endpoint-nya juga tetap mendukung metode PUT.

5. Penambahan Pengujian API
  - Output: Percakapan awal belum memberikan implementasi pengujian.
  - Perbaikan: Saya menambahkan pengujian (test cases) untuk memeriksa keempat peran pengguna, fitur CRUD, pencarian, validasi serializer, serta aksi star/unstar. Selain mengecek status HTTP, tes yang saya tulis juga memastikan keadaan database sesuai harapan, termasuk memastikan data benar-benar tidak berubah ketika akses ditolak. Saya juga secara khusus menguji perlindungan CSRF menggunakan APIClient(enforce_csrf_checks=True) dan .login() agar pemeriksaan menggunakan autentikasi sesi.

Berikut adalah link log saya dengan Gemini:
- https://share.gemini.google/64hsksSNzUrR





