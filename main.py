import edge_tts
import asyncio
import os

# Daftar Dialog Lengkap
dialogs = [
    ("Aris", "Halo semuanya, selamat datang di episode khusus A-P-B-D Unlocked. Hari ini kita bakal bedah dokumen riset tentang gimana teknologi digital pernah nyelametin duit warga Jakarta triliunan rupiah."),
    ("Geo", "Spill the tea, Ris! Gue denger ini soal drama paling legendaris antara Ahok sama D-P-R-D pas zaman itu kan?"),
    ("Aris", "Tepat banget. Kita bakal bahas E-Budgeting. Tapi sebelum masuk ke sana, kita harus tahu dulu betapa sus atau mencurigakannya sistem manual zaman dulu."),
    ("Geo", "Duh, kalau denger kata manual di birokrasi, pikiran gue langsung ke arah korupsi, pungli, sama tumpukan kertas yang berdebu."),
    ("Aris", "Gak salah sih. Riset ini nyebutin kalau dulu, proses anggaran itu gelap banget. Masyarakat nggak bisa akses drafnya, dan semuanya serba tertutup."),
    ("Geo", "Bau-bau konspirasi ya? Berarti dulu nggak ada yang tahu duit pajak kita lari ke mana sebelum anggarannya diketok palu?"),
    ("Aris", "Gak ada. Titik paling kritisnya itu pas tahap re-typing atau pengetikan ulang dokumen setelah rapat. Di situ tangan gaib mulai main."),
    ("Geo", "Bentar, pengetikan ulang? Jadi setelah dibilang Deal, dokumennya diketik lagi secara manual? Itu mah celah banget buat ganti angka!"),
    ("Aris", "Exactly. Makanya muncul istilah Anggaran Siluman. Program yang nggak pernah dibahas di rapat, tiba-tiba muncul pas dokumennya mau dicetak."),
    ("Geo", "Red flag parah sih itu. Terus, pas Ahok masuk, dia langsung ganti ke digital kan?"),
    ("Aris", "Iya, lewat Pergub Nomor seratus empat puluh lima Tahun dua ribu tiga belas. Dia ngenalin E-Budgeting yang punya fitur Digital Audit Trail."),
    ("Geo", "Audit trail? Bahasa manusianya apa tuh, Ris?"),
    ("Aris", "Singkatnya, setiap orang yang login dan ganti angka di sistem, namanya kecatat. Jam berapa dia ngubah, apa yang diubah, semuanya ada jejak digitalnya."),
    ("Geo", "Jadi nggak bisa lagi ya pakai jurus Saya nggak tahu, itu kesalahan staf? Kelihatan dong siapa yang nakal."),
    ("Aris", "Nggak bisa. Dan ada lagi yang namanya System Lock. Begitu anggaran disetujui, sistem otomatis ngunci datanya."),
    ("Geo", "Berarti kalau sudah deal, datanya nggak bisa diedit lagi di luar sistem?"),
    ("Aris", "Iya. Begitu disetujui melalui alur digital, datanya terkunci otomatis. Ini menghilangkan modus penyisipan program pasca-sidang paripurna."),
    ("Geo", "Berarti legitimasi anggaran pindah dari paraf fisik ke validasi digital berbasis akun ya, Ris?"),
    ("Aris", "Tepat! Dan yang paling berpengaruh buat kita adalah Transparansi Pra-Legislasi."),
    ("Geo", "Itu maksudnya masyarakat bisa lihat drafnya sebelum jadi hukum?"),
    ("Aris", "Betul. Versi awal R-A-P-B-D dan K-U-A P-P-A-S dipublikasikan di situs resmi agar bisa diakses siapa saja."),
    ("Geo", "Wah, jadi netizen bisa langsung geruduk kalau ada alokasi yang nggak masuk akal sejak tahap perencanaan?"),
    ("Aris", "Pernah kejadian kok. Publik memprotes anggaran revitalisasi kolam air mancur D-P-R-D senilai ratusan juta yang akhirnya dicoret."),
    ("Geo", "Power of Netizen emang nggak ada obat kalau dikasih data transparan!"),
    ("Aris", "Tapi sistem ini dapet ujian berat tahun dua ribu lima belas, yaitu insiden Anggaran Siluman dua belas koma satu Triliun."),
    ("Geo", "Itu angka yang gede banget! Gimana kronologinya sampai bisa ketahuan?"),
    ("Aris", "Padahal tanggal dua puluh tujuh Januari dua ribu lima belas, Pemprov dan D-P-R-D sudah setuju A-P-B-D tujuh puluh tiga koma nol delapan triliun."),
    ("Geo", "Tapi setelah itu ada yang main belakang lagi?"),
    ("Aris", "Iya. Di bulan Februari, Ahok mengungkap ada dana dua belas koma satu triliun yang disisipkan secara diam-diam oleh D-P-R-D."),
    ("Geo", "Gimana caranya Ahok bisa seyakin itu kalau ada penyisipan sebesar itu?"),
    ("Aris", "Karena dia cek di sistem E-Budgeting-nya. Dia nemu perbedaan antara dokumen cetak D-P-R-D dengan versi digital yang sudah terkunci."),
    ("Geo", "Jadi E-Budgeting berhasil jadi alat deteksi meskipun penyisipan itu tetap dicoba?"),
    ("Aris", "Betul. Salah satu item yang viral adalah pengadaan U-P-S senilai empat koma dua miliar untuk kelurahan."),
    ("Geo", "Sarkastik banget. Empat miliar buat satu U-P-S? Itu kelurahan apa pusat data n-a-s-a?"),
    ("Aris", "Itulah sebabnya Ahok menolak versi D-P-R-D dan mengirim versi E-Budgeting yang benar ke Kemendagri."),
    ("Geo", "Terus D-P-R-D pasti nggak terima dong kekuasaannya dipangkas teknologi?"),
    ("Aris", "Parah. Mereka menolak dokumen elektronik itu karena nggak ada tanda tangan fisik. Mereka akhirnya pakai Hak Angket."),
    ("Geo", "Jadi konflik ini bukan cuma soal duit, tapi soal siapa yang lebih berkuasa: Tanda tangan pejabat atau Sistem Digital?"),
    ("Aris", "Tepat. Kasus ini bahkan sampai ke ranah hukum. Ahok melaporkan temuan bukti digital ini ke K-P-K."),
    ("Geo", "Bukti digital dari E-Budgeting itu bisa dianggap sah secara hukum nggak sih?"),
    ("Aris", "Ahok menjadikannya fondasi utama untuk identifikasi manipulasi. Sistem ini jadi alat forensik digital."),
    ("Geo", "Terus gimana respon D-P-R-D pas dituduh gitu?"),
    ("Aris", "Mereka lapor balik Pemprov ke K-P-K dan Bareskrim, nuduh ada suap dan korupsi dua belas koma tujuh triliun."),
    ("Geo", "Nuduh balik? Dasar buktinya apa?"),
    ("Aris", "Mereka pakai dokumen versi mereka yang isinya juga aneh, kayak anggaran trilogi buku Ahok senilai tiga puluh miliar."),
    ("Geo", "Jadi ada dua versi anggaran yang beroperasi paralel ya? Satu yang bener, satu yang ajaib."),
    ("Aris", "Itulah kenapa B-P-K juga ikut mantau, meskipun mereka baru bisa audit setelah A-P-B-D disahkan."),
    ("Geo", "Berarti ada celah waktu di mana pengawasan eksternal belum berlaku, dan di situlah E-Budgeting jadi penjaga gawang."),
    ("Aris", "Benar. Keandalan sistem ini bukan cuma soal siapa yang dipenjara, tapi kemampuannya menghasilkan bukti yang solid."),
    ("Geo", "Jadi, apa warisan atau legacy jangka panjang dari sistem ini buat Jakarta?"),
    ("Aris", "Pertama, standar baru transparansi. Platform ini jadi model nasional yang bahkan dipuji Presiden Jokowi."),
    ("Geo", "Wah, dari Jakarta untuk Indonesia ya?"),
    ("Aris", "Iya. Tapi ada catatan penting: sistem ini hanya digital, bukan cerdas."),
    ("Geo", "Maksudnya bukan cerdas itu gimana? Nggak ada a-i-nya?"),
    ("Aris", "Belum ada validasi otomatis. Misalnya, kalau ada yang input harga Lem Aibon delapan puluh dua miliar, sistem nggak langsung nolak."),
    ("Geo", "Jadi tetap butuh manusia yang jujur dan teliti buat input datanya?"),
    ("Aris", "Betul. Keandalan E-Budgeting itu pada kemampuannya merekam setiap tindakan agar tidak bisa disembunyikan."),
    ("Geo", "Pelajaran buat kita, teknologi itu cuma alat, tapi alat yang bikin koruptor nggak bisa lagi main di ruang gelap."),
    ("Aris", "Tepat! Itulah kenapa partisipasi publik buat mantau data itu super penting."),
    ("Geo", "Gue ngebayangin orang-orang yang biasanya main belakang pasti panik banget pas sistem ini jalan."),
    ("Aris", "Panik parah! Kasus dua ribu lima belas itu jadi bukti operasional pertama tentang keandalan E-Budgeting."),
    ("Geo", "Pelajaran buat Gen Z, jangan cuma jago scroll sosmed, sesekali scroll draf A-P-B-D daerah masing-masing."),
    ("Aris", "Benar. Setiap intervensi ilegal sekarang meninggalkan jejak digital yang tak terhapus. Itu senjata kita."),
    ("Geo", "Makasih banyak Aris buat bedah risetnya. Gue jadi makin paham kalau teknologi itu kunci lawan korupsi."),
    ("Aris", "Sama-sama, Geo. Seneng bisa sharing hal yang edukatif tapi tetep asik."),
    ("Geo", "Jadi kesimpulannya, E-Budgeting itu bikin korupsi jadi High Risk, Low Reward ya?"),
    ("Aris", "Bagus banget bahasanya! Risiko ketahuannya tinggi, tapi hasil curiannya susah disembunyiin."),
    ("Geo", "Oke guys, sampai sini dulu podcast kita. Jangan lupa cek draf anggaran daerah kalian!"),
    ("Aris", "Sampai jumpa di episode selanjutnya. Stay digital, stay honest!"),
    ("Geo", "Bye-bye semuanya! See ya!"),
]

async def start_tts():
    if not os.path.exists("podcast_output"):
        os.makedirs("podcast_output")
    
    for i, (speaker, text) in enumerate(dialogs):
        voice = "id-ID-ArdiNeural" if speaker == "Aris" else "id-ID-GadisNeural"
        rate = "+10%" if speaker == "Geo" else "+0%"
        output_file = f"podcast_output/{i+1:02d}_{speaker}.mp3"
        
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(output_file)
        print(f"Berhasil: {output_file}")

if __name__ == "__main__":
    asyncio.run(start_tts())
    
