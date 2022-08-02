import streamlit as st
import time

st.set_page_config(page_title="Cybersecurity Education",
                   page_icon=":books:", layout="wide")

st.markdown(":newspaper: Article")
# st.title("Article")
st.sidebar.markdown(":newspaper: Article")

with st.spinner('Tunggu Sesaat...'):
    time.sleep(3)
    pass

with st.container():
    st.write('---')
    # isi dengan judul
    st.title("Lakukan 4 Langkah Ini Untuk Mengamankan Akun Media Sosialmu")
    st.subheader("1. Perhatikan penggunaan password")
    st.write("Langkah pertama yaitu penggunaan password. Password adalah hal yang paling penting untuk membuka akun media sosial. Maka dari itu, bila passwordmu diketahui oleh orang lain, maka orang lain tersebut bisa membuka akunmu kapan saja.")
    st.write("Dalam menentukan password, hindari penggunaan kombinasi kata yang mudah. Mungkin kamu bermaksud supaya kita selalu ingat atau supaya tidak susah diketikkan, tapi hal itu tidak berlaku lagi di zaman sekarang ini.Jangan pernah menggunakan nama, nama tempat tinggal atau tanggal kelahiran sebagai password media sosial. Selain itu hindari penggunaan password sederhana seperti 'qwerty' atau '123456'.")
    st.write("Usahakan untuk menggunakan kombinasi angka, huruf kapital dan kecil untuk memperkuat passsword. Kamu juga disarankan untuk mengecek kekuatan password terlebih dahulu sebelum menentukannya.")
    st.write("Yang paling penting, jangan pernah memberitahu orang lain tentang passwordmu. Hal ini tentu saja menjadi hal yang paling penting, karena sekali kamu memberitahukan ke orang lain, berarti akun tersebut sudah dapat diakses oleh orang lain selain dirimu sendiri. Dalam penggunaan password ini, bukan hanya akun media sosial saja yang membutuhkan hal ini, tapi gadget yang kamu pakaipun butuh password yang pas.")
    st.subheader("2. Memilih aplikasi atau website yang aman")
    st.write("Sekarang sudah sangat banyak aplikasi dan website yang bisa kamu pakai. Aplikasi maupun website tersebut tentunya memiliki kekuatan pengamanan masing-masing untuk pelanggannya.")
    st.write("Dalam memilih aplikasi-aplikasi tersebut, kamu harus memperhatikan sistemnya. Dalam aplikasi berkirim pesan atau messenger, kamu harus melihat apakah sistemnya sudah benar-benar terenkripsi, yang membuat pesan-pesan akan sulit untuk diakses.")
    st.subheader("3. Gunakan fitur verifikasi dua langkah")
    st.write("Beberapa media sosial seperti Facebook dan WhatsApp, maupun Gmail memiliki fitur verifikasi 2 langkah agar keamanan pengunanya semakin aman. Kamu harus memanfaatkan fitur ini sebaik mungkin untuk menghindari kemungkinan di-hack.")
    st.write("Fitur ini akan melakukan verifikasi ke akunmu yang lainnya setiap ada login ke media sosial kita. Bila mengaktifkan fitur ini, kamu biasanya akan diberikan kode melalui sms yang perlu kamu input ketika login media sosial.")
    st.subheader("4. Menggunakan perangkat yang terpercaya")
    st.write("Banyak orang yang kena hack karena dia pernah login di warnet atau di tempat tersedianya perangkat komputer yang digunakan secara publik lainnya. Sebaiknya, jangan pernah memasukkan akun pribadi di komputer untuk umum.")
    st.write("Banyak kejadian seperti ini, biasanya karena lupa logout atau karena menyimpan data akun di browser tersebut. Kadang kamu lupa logout karena kebiasaan di gadget sendiri tak pernah melakukannya. Kadang kamu juga lupa untuk tidak mencentang ingat password ini' pada saat login, sehingga riwayat login masih tersimpan di browser tersebut.")
    st.write("Bila memang terpaksa melakukannya, usahakan untuk mengubah password secepatnya setelah menggunakannya dan kamu sudah bisa mengaksesnya dengan gadget pribadi.")
    st.write("Dengan memperhatikan langkah-langkah sederhana diatas, kamu dapat mengurangi dan menghindari risiko akun media sosial kita terkena hack. Selama kamu menjaga kerahasiaan dan tidak sembarangan dalam login akun media sosial, seharusnya akunmu bisa tetap terjaga keamanannya.")


with st.container():
    st.write('---')
    st.title("Langkah Pelaporan Kejahatan Cyber Crime")
    st.subheader("1. Siapkan bukti yang cukup dan asli")
    st.write("Agar tidak terkena UU ITE atau justru menjadi bumerang karena tersandung kasus pencemaran nama baik atau pelaporan kejadian palsu, lebih baik jika sebelum melapor, hendaknya kamu benar-benar menyiapkan sejumlah bukti kongkret yang asli dan cukup untuk dijadikan penguat dari laporan kamu.")
    st.write("Bukti laporan dapat berupa screenshot atau tangkapan layar, baik itu di smartphone maupun layar PC kamu. Tidak hanya dapat berupa tangkapan layar, barang bukti juga dapat berupa URL yang aktif, foto atau mungkin video dari tindakan kejahatan siber yang kamu ketahui. Satu bukti valid akan sangat cukup kuat untuk mendukung laporan kamu.")
    st.write("Selanjutnya, simpan bukti tersebut ke dalam media penyimpanan, yang hanya berisi barang bukti digital tersebut. Media penyimpanan dapat berupa CD ataupun DVD Room, flashdisc, hardisk, memory card, dan lain sebagainya. Jangan menyerahkan bukti kepada kepolisian dalam bentuk Email atau pesan. Pastikan pula media penyimpanan yang kamu serahkan tersebut tidak rusak.")
    st.subheader("2. Datang ke Kantor Polisi")
    st.write("Setelah menyiapkan cukup bukti yang kuat dan valid, segera bergegaslah menuju kantor polisi untuk melaporkan kejahatan siber yang kamu ketahui. Semakin cepat dilaporkan, maka akan semakin baik karena gerakan para kriminalitas siber sangat lah cepat. Apabila terlambat melapor, maka bisa kehilangan jejak rekamnya.")
    st.write("Tingkatan kepolisian yang dianjurkan untuk melaporkan kejadian atau aduan kejahatan cyber crime,setidaknya adalah yang setingkat dengan Polres atau di atasnya. Di kantor poilisi, kamu bisa langsung menuju SPKT atau Sentra Pelayanan Kepolisian Terpadu, untuk melaporkan secara rinci dan menyerahkan bukti-bukti yang kamu simpan.")
    st.subheader("3. Proses Tanya Jawab")
    st.write("Selanjutnya, di ruang SPKT kamu akan dimintai keterangan yang lebih lanjut. Biasanya, petugas kepolisian akan segera melakukan proses tanya jawab. Jawablah dengan jujur dan apa adanya, sesuai dengan sepengetahuan kamu. Sekecil apapun informasi yang kamu ketahui, akan sangat memengaruhi hasil penyelidikan kepolisian selanjutnya.")
    st.write("Informasi yang pada umumnya akan ditanyakan adalah kronologis kejadian. kamu akan diminta memberikan keterangan, dan menceritakan bagaiman awal mula kamu bisa mengetahui keberadaan kejahatan cyber crime tersebut. Kapan waktu persis kamu mengetahui kejahatan cyber crime tersebut. Dan di mana situs atau siapa dalang kejadian yang kamu ketahui.")
    st.write("Selama proses tersebut, petugas kepolisian akan memeriksa pula barang bukti yang kamu serahkan, dan mencocokkan keterangan yang kamu beri. Apabila dianggap wajar dan kuat, kepolisian akan segera mencetak isi barang bukti tersebut, dan membuat laporan atau bukti berita acara pelaporan yang kamu berikan.")
    st.subheader("Menunggu kabar lebih lanjut")
    st.write("Setelah kamu melaporkan kejadian kejahatan cyber crime, menyerahkan bukti penguat laporan, serta memberikan sejumlah keterangan yang diperlukan kepolisian, maka kamu bisa kembali ke rumah dan menantikan pemberitahuan atau kabar lebih lanjut dari kepolisian. Petugas kepolisian tentu akan segera memproses ke atasan untuk bisa mendapat surat perintah penyelidikan.")
    st.write("Ketika penyelidikan mulai diproses dan dilakukan, kamu mungkin akan sesekali dihubungi atau diminta untuk kembali datang ke kantor kepolisian terkait, guna kembali dimintai keterangan. Selama proses penyelidikan tersebut berlangsung pula, kamu berkemungkinan akan ditetapkan sebagai Saksi yang akan dibutuhkan keterangannya sampai proses sidang.")
    st.write("Apabila kamu menemukan kejanggalan dan mengetahui adanya tindakan kejahatan cyber crime, jangan takut, dan segera gunakan hak bersuara kamu untuk melaporkan secara aktual tindak kriminalitas serangan siber yang kamu ketahui.")

with st.container():
    st.write('---')
    st.title("Lorem Ipsum")  # isi dengan judul
    st.subheader("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae volutpat nibh, volutpat facilisis est. Phasellus placerat nulla nibh, vel tempor nunc pretium id. Nullam faucibus tortor sed velit semper aliquet. Integer in odio ultrices, fringilla nunc in, varius justo. Donec egestas euismod cursus. Nullam finibus sapien diam, nec pretium nisl aliquet quis. Integer non mi ornare, convallis magna et, vestibulum dolor.")  # isi dengan artikel


with st.container():
    st.write('---')
    st.title("Penanganan Hoaks Covid 19")  # isi dengan judul
    st.image('https://web.kominfo.go.id/sites/default/files/kominfo-11072022_Statistik%20Penanganan%20Hoaks%20Covid-19%20(Dengan%20Hoaks%20Vaksin).jpg')
