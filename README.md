<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Simple Flask login with Argon2id Hash

Simpel login sistem menggunakan argon2id.

## Installation

Buat virtualenv terlebih dahulu
```bash
virtualenv {nama_virtual}
virtualenv -p python3 {nama_virtual} (untuk python3, ubuntu biasanya menggunakan ini)
```
Masuk kedalam virtual
```bash
source {nama_virtual}/Scripts/activate

kalo pake Ubuntu
cd {nama_virtual}
source bin/activate
```
Install packages menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt

kalo pake python3 (biasanya dipakeubuntu)
pip3 install -r requirements.txt
```
Jalankan dengan perintah
```bash
python main.py

kalo pake python3 (biasanya dipakeubuntu)
python3 main.py
```

### Note
Untuk mengupload ke shared hosting [Silahkan baca panduannya](https://www.domainesia.com/panduan/cara-menjalankan-flask-python-di-hosting/)
