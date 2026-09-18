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




