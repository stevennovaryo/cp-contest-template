## Struktur Soal

Sebuah soal terdiri atas setidaknya dua komponen:

1. Program generator test case (runner)
2. Program solusi utama soal (solution)

Soal-soal mungkin saja memiliki komponen sebagai berikut :

3. Program untuk verifikasi output peserta [kode: **scorer**] atau program untuk berinteraksi dengan kode peserta untuk soal interaktif [kode: **communicator**]

Untuk setiap soal, terdapat sebuah **slug** soal, yakni, kode nama soal. Slug pada soal-soal TOKI Regular Open Contest X ini telah disepakati bersama dan mengikuti format berikut: `troc-<X>-<judul soal singkat dan dipisahkan oleh dash>`. Contoh: `troc-1-absolute-winner`.

## Cara Kerja

1. Apabila belum pernah dilakukan, *clone* repositori ini, kemudian pastikan Anda sudah berada di direktori `troc-32`:
  ```
  git clone https://github.com/ia-toki/troc-32
  cd troc-32
  ```

2. Buat branch dengan format `<slug>`. Contoh: `troc-1-absolute-winner`. Caranya:
  ```
  git checkout master
  git checkout -b troc-1-absolute-winner
  ```

3. Kerjakan semua komponen tersebut pada branch tersebut dan pada direktori yang sesuai yaitu `<slug soal>`.

4. Penamaan berkas untuk masing-masing komponen:
  - `runner`: `spec.cpp`
  - `solution`: `solution.cpp`, `alt-solution.cpp`, `solution-max-flow.cpp`, `tle-solution.cpp`, dsb
  - `scorer`: `scorer.cpp`
  - `communicator`: `communicator.cpp`
  - `description`: `statement.txt`, `*.png`, `*.jpg`

  Yang dipakai untuk generate testcase adalah `solution.cpp`. File-file solution lainnya bersifat opsional dan hanya untuk kebutuhan testing.

5. Bila sudah selesai, add, kemudian commit. Ingat, hanya commit source code/text, jangan executablenya! Format commit messagenya terserah, yang penting informatif. Contoh:
  ```
  git add troc-1-absolute-winner/solution.cpp
  git commit -m "Add solution for TROC-1 Absolute Winner"
  ```

6. Push ke origin:
  ```
  git push origin troc-1-absolute-winner
  ```

7. Buka https://github.com/ia-toki/troc-32/pulls.
  - Buat pull request baru dari branch tersebut ke master.
  - Assign reviewer ke salah satu anggota Tim Panitia Inti TOKI Regular Open Contest.

8. Beritahukan kepada Tim Panitia Inti TOKI Regular Open Contest untuk minta tolong review.
9. Tim Panitia Inti TOKI Regular Open Contest memberikan review dan komentar.
10. Jika Anda ingin memperbaiki, dapat dilakukan dengan commit lagi ke branch tersebut, lalu push lagi. Merge requestnya akan ter-update dengan sendirinya.
11. Jika dirasa sudah selesai, Tim Panitia Inti TOKI Regular Open Contest akan merge branch tersebut ke master.

***

### Catatan-Catatan

#### Contoh

- Contoh berkas minimalis yang dapat digunakan sebagai acuan dapat dilihat pada folder `contoh/april-fools-2020-ab`.
- Contoh berkas TROC sebelumnya dapat dilihat di [sini](https://github.com/prabowo02/toki-regular-open-contest)

#### Umum

- Usahakan mempelajari git sendiri. Namun jika ada kesulitan, bisa hubungi Tim Panitia Inti TOKI Regular Open Contest.
- Karena kode akan di-review orang lain, mohon koding serapi mungkin.
- Jika sebuah komponen sudah selesai dibuat, maka Anda bisa mem-push dan meminta merge request (judul merge request bebas, sebaiknya informatif) pada komponen tersebut sebelum menyelesaikan komponen lainnya pada soal yang sama, sehingga Tim Panitia Inti TOKI Regular Open Contest bisa mengetahui progress Anda dan komponen-komponen apa saja yang belum diselesaikan.
- Jika Anda merasa tidak dapat menyelesaikan sebuah komponen yang dialokasikan pada Anda, beritahu Tim Panitia Inti TOKI Regular Open Contest secepatnya dan kami akan mencoba mengalokasikan kepada orang lain (termasuk anggota Tim Panitia Inti TOKI Regular Open Contest).
- Apabila Anda ingin menambahkan solusi alternatif Anda sendiri ke soal-soal lainnya, dapat dikerjakan di branch baru bernama `troc-32-solution-<nama_anda>`.

#### runner

- Gunakan tcframe 1.6.0.
- Kecuali memang benar-benar perlu berubah, gunakan Time Limit 1 detik dan Memory limit 256 MB.
- Test case tidak perlu terlalu banyak. Yang penting meng-cover banyak tricky case.
  - Untuk soal 2A/2B, sebisa mungkin tc tidak melebihi 10 (karena bakal ada submissions burst).
  - Untuk sisanya, sebisa mungkin tc tidak melebihi 30.
- Untuk mengimport tcframe, gunakan `#include "tcframe/runner.hpp"`. Jangan `#include "runner.hpp"`, atau `#include "../tcframe/runner.hpp"`, ataupun yang lainnya. Karena nantinya Tim Panitia Inti TOKI Regular Open Contest akan men-generate testcase menggunakan include folder tersebut.

#### communicator

- Cara menjalankan communicator dan solution secara bersamaan (untuk mengetes solution)
`mkfifo fifo`
`./communicator [file input] < fifo | ./solution > fifo`
