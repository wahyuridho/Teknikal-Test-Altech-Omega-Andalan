# Teknikal-Test-Web-Automation-PT-Altech-Omega-Andalan
Repositori ini dibuat untuk memenuhi tes yang diberikan pada proses recruitment karyawan

# How to Install
## Prerequisites
Make sure your PC/Laptop already install 
- Python 3.12
- Pip
- Pipenv

## Setup
1. Buka terminal kemudian ketikan "python --version", jika belum install python maka install terlebih dahulu
2. Kemudian ketikan "pip --version" untuk mengecek Pip, jika belum terinstall maka install terlebih dahulu
3. Kemudian silahkan ketik "pip install pipenv" untuk menginstall Pipenv, ini digunakan untuk membuat virtual environment
4. Jika requirement sudah terinstall silahkan clone repository dengan cara ketikan "git clone https://github.com/wahyuridho/Teknikal-Test-Altech-Omega-Andalan.git"
5. Jika sudah silahkan buka folder Teknikal-Test-Altech-Omega-Andalan di visual sutido code
![image](https://github.com/user-attachments/assets/3b54d407-15ce-4635-9874-e91ac8f50b52)
6. Kemudian buka terminal di vs code, kemudian ketikan "pinenv install", setelah itu sistem akan membuat virtual environtment dan menginstall library yang diperlukan dari file "Pipfile"
![image](https://github.com/user-attachments/assets/ccee96bf-ca79-472f-bece-c2ccd3d31cbc)
7. Kemudian setelah sukses ketikan "pipenv shell" untuk mengaktifkan virtual environtment di terminal vs code, jika berhasil maka akan ada nama virtual env di depan terminal
![image](https://github.com/user-attachments/assets/d6bd8be0-749b-454e-8a96-73f6c262b766)
8. Kemudian kita perlu untuk memilih interpreter yang digunakan vs code agar tidak muncul notif error, dengan cara tekan Ctrl + Shift + P, lalu pilih "python: select interpreter" lalu pilih virtual env yang sebelumnya dibuat
![image](https://github.com/user-attachments/assets/f3dfb86b-3d11-44ca-84f1-87847dc89e0a)
9. Setelah sukses jika muncul warning di terminal vs code silahkan close dan buka kembali terminalnya



# How to Run 
Untuk menjalankan tes anda bisa mengetikan perintah "pytest", maka secara otomatis seluruh test case yang ada akan dijalankan
![image](https://github.com/user-attachments/assets/7d58185e-9981-4123-bd64-1db1018226d8)
Namun jika ingin menjalankan test berdasarkan marker maka bisa dengan cara "pytest -m nama_marker". silahkan lihat file pytest.ini untuk melihat marker yang ada
![image](https://github.com/user-attachments/assets/1f323996-45d3-4f9d-8f84-97a6ed8f63d0)


# How to Generate report
Untuk membuat report kita bisa menambahkan perintah "pytest --html=./results/test-report.html --self-contained-html". Namun karna saya sudah menambahkan configurasi untuk menggenerate report di file pytest.ini maka setiap kita running test case, report akan otomatis dibuat.
silahkan lihat pada folder "results". disana terdapat file test-report.html, silahkan buka file tersebut di browser anda, maka kita dapat melihat hasil report dari test yang kita jalankan
![image](https://github.com/user-attachments/assets/24ac9c93-c180-4d48-8d8c-1e72469655f0)

