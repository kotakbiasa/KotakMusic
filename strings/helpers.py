HELP_1 = """<b><u>Perintah Admin :</b></u>

Hanya tambahkan <b>c</b> di awal perintah untuk menggunakannya di dalam kanal.


/pause : Jeda pemutaran aliran saat ini.

/resume : Lanjutkan aliran yang sedang dijeda.

/skip : Lewati aliran yang sedang diputar dan mulai streaming trek berikutnya dalam antrian.

/end atau /stop : Bersihkan antrian dan akhiri aliran yang sedang diputar.

/player : Dapatkan panel pemutar interaktif.

/queue : Tampilkan daftar trek yang ada dalam antrian.
"""

HELP_2 = """
<b><u>Pengguna Berizin :</b></u>

Pengguna berizin dapat menggunakan hak admin dalam bot tanpa hak admin di obrolan.

/auth [nama_pengguna/id_pengguna] : Tambahkan pengguna ke daftar pengguna berizin bot.
/unauth [nama_pengguna/id_pengguna] : Hapus pengguna berizin dari daftar pengguna berizin.
/authusers : Tampilkan daftar pengguna berizin dari grup.
"""

HELP_3 = """
<u><b>Fitur Siaran</b></u> [Hanya untuk pengguna berizin]:

/broadcast [pesan atau balas ke pesan] : Menyiarkan pesan ke obrolan server bot.

<Mode Siaran>:
<b>-pin</b> : Menyematkan pesan siaran Anda di obrolan server.
<b>-pinloud</b> : Menyematkan pesan siaran Anda di obrolan server dan mengirimkan pemberitahuan ke anggota.
<b>-user</b> : Menyiarkan pesan ke pengguna yang telah memulai bot Anda.
<b>-assistant</b> : Menyiarkan pesan Anda dari akun asisten bot.
<b>-nobot</b> : Memaksa bot untuk tidak menyiarakan pesan.
"""

HELP_4 = """<u><b>Fitur Blacklist Chat:</b></u> [Hanya untuk Sudoers]

Membatasi obrolan sampah yang menggunakan bot kami.

/blacklistchat [ID obrolan]: Menyaring obrolan dari penggunaan bot.
/whitelistchat [ID obrolan]: Memberikan izin pada obrolan yang sudah di-blacklist.
/blacklistedchat: Menampilkan daftar obrolan yang telah di-blacklist.
"""

HELP_5 = """
<u><b>Blokir Pengguna:</b></u> [Hanya untuk Sudoers]

Memulai penggunaan bot untuk mengabaikan pengguna yang telah di-blacklist, sehingga mereka tidak dapat menggunakan perintah bot.

/block [nama pengguna atau balas ke pengguna]: Memblokir pengguna dari penggunaan bot kami.
/unblock [nama pengguna atau balas ke pengguna]: Membuka blokir pengguna yang telah diblokir.
/blockedusers: Menampilkan daftar pengguna yang telah diblokir.
"""

HELP_6 = """
<u><b>Perintah Pemutaran Channel:</b></u>

Anda dapat mengalirkan audio/video di saluran.

/cplay: Mulai streaming trek audio yang diminta di obrolan video saluran.
/cvplay: Mulai streaming trek video yang diminta di obrolan video saluran.
/cplayforce atau /cvplayforce: Berhentikan streaming saat ini dan mulai streaming trek yang diminta.
/channelplay [nama pengguna obrolan atau ID] atau [matikan]: Hubungkan saluran dengan grup dan mulai streaming trek dengan bantuan perintah yang dikirim dalam grup.
"""

HELP_7 = """
<u><b>Fitur Global Ban:</b></u> [Hanya untuk Sudoers]

/gban [nama pengguna atau balas ke pengguna]: Melakukan ban global terhadap pengguna yang tidak diinginkan dari semua obrolan yang dilayani dan melarang mereka menggunakan bot.
/ungban [nama pengguna atau balas ke pengguna]: Membuka larangan global terhadap pengguna yang diblokir secara global.
/gbannedusers: Menampilkan daftar pengguna yang diblokir secara global.
"""

HELP_8 = """
<b><u>Loop Stream:</b></u>

Mulai mengalirkan streaming berkelanjutan.

/loop [aktif/nonaktif]: Aktifkan/Nonaktifkan mode loop untuk streaming berkelanjutan.
/loop [1, 2, 3, ...]: Aktifkan mode loop untuk trek yang ditentukan.
"""

HELP_9 = """
<u><b>Mode Pemeliharaan</b></u> [Hanya untuk Sudoers] :

/logs: Dapatkan catatan aktivitas bot.
/logger [aktif/nonaktif]: Bot akan mulai mencatat aktivitas yang terjadi pada bot.
/maintenance [aktif/nonaktif]: Aktifkan atau nonaktifkan mode pemeliharaan bot Anda.
"""

HELP_10 = """
<b><u>Ping & Statistik:</b></u>

/start: Memulai bot musik.
/help: Dapatkan menu bantuan dengan penjelasan perintah-perintah bot.

/ping: Menampilkan ping dan statistik sistem bot.
/stats: Menampilkan statistik keseluruhan bot.
"""

HELP_11 = """
<u><b>Perintah Pemutaran:</b></u>

"v" mengacu pada video play (putar video), "force" mengacu pada perintah pemutaran paksa.

/play atau /vplay: Mulai mengalirkan trek audio yang diminta di obrolan video.
/playforce atau /vplayforce: Hentikan streaming berlangsung dan mulai mengalirkan trek yang diminta.
"""

HELP_12 = """
<b><u>Mengocok Antrian:</b></u>

/shuffle: Acak isi antrian.
/queue: Tampilkan antrian yang sudah diacak.
"""

HELP_13 = """
<b><u>Cari Pemutaran Stream:</b></u>

/seek [durasi dalam detik]: Geser pemutaran ke durasi yang diberikan.
/seekback [durasi dalam detik]: Geser pemutaran mundur ke durasi yang diberikan.
"""

HELP_14 = """
<b><u>Unduh Lagu:</b></u>

/song [nama lagu/URL YouTube]: Unduh trek dari YouTube dalam format MP3 atau MP4.
"""

HELP_15 = """
<b><u>Perintah Kecepatan:</b></u>

Anda dapat mengendalikan kecepatan pemutaran audio. [Hanya untuk admin]

/speed atau /playback: Untuk menyesuaikan kecepatan pemutaran audio di grup.
/cspeed atau /cplayback: Untuk menyesuaikan kecepatan pemutaran audio di obrolan saluran.
"""
