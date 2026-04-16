# Format Sitasi & Daftar Pustaka TA FPIK Unsoed

![GitHub Tag](https://img.shields.io/github/v/tag/willdone-mt/csl-fpik-unsoed?include_prereleases&sort=semver&style=for-the-badge&label=Latest%20Version&labelColor=%23202A44&color=%23005EB8)

**Author**: [Arya Bratasena Alhaq](mailto:baraktt30@gmail.com).
**Initial Contributor**: [Talitha Nada Aristawati](mailto:talitha.aristawati@mhs.unsoed.ac.id).

Uploaded here for documentation

## Ringkasan

<!-- Format ... ini merupakan adaptasi dari gaya sitasi dan daftar pustaka dari ... .
Citation Style Language adalah -->

## 🎮 Untuk Pengguna Akhir

### ✨ Mendeley

<details>
<summary>Instalasi pada Mendeley **Desktop** v1.19.8</summary>

- Pilih versi paling terbaru dari templat
  1. Pergi ke [Templat Sitasi dan Dafpus TA FPIK terbaru di sini](https://github.com/willdone-mt/csl-fpik-unsoed/releases/latest)
  2. Klik *drop down* `Assets` (Gulir ke bawah apabila tidak ditemukan)
  3. Klik kanan pada teks bertautan dengan akhiran `.xml` atau `.csl`
  4. Salin tautan tersebut

- Masukkan Templat ke Mendeley
  1. Buka `Mendeley Desktop`
  2. Pada menubar, **klik** `View` -> `Citation Style` -> `More Styles...`. Window `Citation Styles` akan muncul
  3. Di window `Citation Styles`, **klik tab `Get More Styles`**.
  4. Pada tab `Get More Styles`, di bagian paling bawah, ada label `Download Style` dengan entri bertuliskan "`Enter URL`".
  5. Di dalam entri tersebut, **masukkan tautan templat** yang disalin
  6. **Klik `Download`**, **tunggu** beberapa saat, dan akan dibawa ke tab `Installed`
  7. Pada tab `Installed`, **klik templat** yang telah diunduh, kemudian **klik `Use this Style`**

</details>

<details>
<summary>Instalasi pada Mendeley **Reference Manager**</summary>

-

  > WIP

</details>

<details>
<summary>Instalasi pada Mendeley **Cite** (Add-in untuk MS Word Online)</summary>
  
- Install Add-in Mendeley Cite
  1. Buka sebuah dokumen di Ms Word online
  2. **Alihkan ke tab `References`**
  3. di tab `References`, **Klik `Citations`**
  4. Pada menu yang dimunculkan `Citations`, seharusnya terdapat `Popular citation add-ins` yang **salah satunya adalah `Mendeley Cites`**
  5. **Klik `Add`** di add-ins tersebut
  6. Apabila `Mendeley Cites` tidak muncul di menu `Popular citation add-ins`, maka klik tombol `More add-ins` di bagian bawah menu tersebut
  7. Akan muncul jendela pop-up dengan judul `Office Add-ins`
  8. **Pastikan isi jendela tersebut berada di bagian `STORE`** dengan mengklik tombol dengan kata yang sama di bawah judul jendela tersebut
  9. **Isi borang pencarian** dengan kata "Mendeley"
  10. Akan muncul hasil pencarian berupa `Mendeley Cite`
  11. Klik `Add` pada hasil tersebut
  12. Akan muncul jendela pop-up persetujuan, **klik `Continue`** apabila menyetujui
  13. <!--  Test -->
  14. Add-in `Mendeley Cite` berhasil terinstal! :D

- Login ke Mendeley di `Mendeley Cite`
  1. Pada tab `Reference`, **klik Add-in `Mendeley Cite`**
  2. Akan muncul sidebar `Mendeley Cite` di sebelah kanan layar
  3. Klik `Login`/`Get Started`
  4. Ikuti langkah yang diperintahkan
  5. ***PASTIKAN AKUN MENDELEY CITE SAMA PERSIS DENGAN AKUN MS WORD ONLINE YANG DIPAKAI***

- Pembaruan format plugin Mendeley pada dokumen
  
  Apabila menggunakan dokumen yang sebelumnya menggunakan Mendeley Desktop, terkadang `Mendeley Cite` akan mengarahkan untuk memperbarui format plugin dari dokumen yang digunakan

  1. Di Ms Word desktop (bukan yang online), install `Mendeley Cite` via tab `Insert`, di bagian `Add-ins`, `Get Add-ins`
  2. Seharusnya `Mendeley Cite` terinstal di Ms Word Desktop
  3. **Pergi ke tab `References`**, dan klik `Mendeley Cite`
  4. Akan muncul sidebar `Mendeley Cite` di sebelah kanan layar
  5. **Login** ke `Mendeley Cite`
  6. Akan muncul peringatan di sidebar untuk memperbarui dokumen
  7. **Ikuti arahan** yang diperintahkan
  8. **APABILA INGIN MEMODIFIKASI DOKUMEN ONLINE, PASTIKAN DOKUMEN YANG DIPEBARUI BERASAL DARI ONLINE DAN BUKAN DOKUMEN BACKUP**
  9. Selesai memperbarui format plugin dokumen
  10. Periksa semua sitasi (karena terkadang sitasi yang lama akan berubah format fontnya, sehingga mengharuskan pemasukan ulang ataupun pengubahan format fontnya)

</details>

### Perangkat Lunak Pengelola Referensi Lainnya

### Pengajuan Masalah

Pengajuan masalah bisa menggunakan Github Issue

## 🐍 Untuk Kontributor (Pengodean)

Teks ini menganggap pembaca sudah tidak asing dengan menggunakan Git.
Sehingga, untuk memulai kontribusi dalam pemrograman ini,
gunakan `git clone` pada bash untuk mengklon repositori ini.

```bash
git clone https://github.com/willdone-mt/csl-fpik-unsoed.git
```

GitHub digunakan untuk merekam berbagai perubahan yang terjadi di dalam templat.
Kemudian perubahan ini dicatat dan diolah agar dapat dibaca oleh para pengguna.

Gunakan CSL Editor apa saja untuk mengedit/merevisi CSL.
Namun, disarakan menggunakan CSL Editor dengan link <https://editor.citationstyles.org/visualEditor/>.
Gunakan berkas-berkas `.json` di dalam [folder `preview_template/`](preview_template/) sebagai contoh sitasi dan  daftar pustaka.

Gunakan situs <https://validator.citationstyles.org/> untuk memvalidasi CSL yang sudah direvisi,
kemudian gunakan situs <https://formatter.citationstyles.org/> untuk memperbaiki pemformatan.

Diharuskan membuat laporan penelitian agar perubahan dilakukan secara logis dan terekam maksud dan prosesnya.

- Yang Harus dilakukan:
  [ ] Mengetahui dasar gaya atribusi TA FPIK (APA? IEEE?)
  
- Pemversian

  ```text
  vYYYY.X.Z
  ```

  - YYYY  = Tahun Format TA FPIK
  - X     = versi major
  - Z     = Perbaikan

### Pranala Penting

<https://citationstyles.org/>
<https://github.com/citation-style-language>
