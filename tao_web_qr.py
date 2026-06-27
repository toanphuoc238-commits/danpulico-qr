# DANPULICO - Script tao QR code san pham den LED
# Chay: python tao_web_qr.py
# Yeu cau: pip install qrcode[pil] pillow
#
# HUONG DAN SU DUNG TU MAY TINH KHAC:
# 1. Tai file nay tu: github.com/toanphuoc238-commits/danpulico-qr
# 2. Dat file logo 'logo_danpulico.png.png' cung thu muc
# 3. Chay: python tao_web_qr.py
# 4. Upload file HTML moi len GitHub (Add file -> Upload files)

import qrcode, os, base64

TEN_CONG_TY = "Cong ty CP Chieu sang cong cong Da Nang"
DIEN_THOAI  = "0236.3565741"
LOGO_PATH   = "logo_danpulico.png.png"
GITHUB_USER = "toanphuoc238-commits"
GITHUB_REPO = "danpulico-qr"

DANH_SACH_SAN_PHAM = [
    {"ma_sp":"DPC09-100W","ten":"Den LED chieu sang 100W","cong_suat":"100W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"FL03-200W", "ten":"Den pha LED 200W","cong_suat":"200W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"DPC09-75W", "ten":"Den LED chieu sang 75W","cong_suat":"75W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"DPC09-150W","ten":"Den LED chieu sang 150W","cong_suat":"150W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"DPC09-120W","ten":"Den LED chieu sang 120W","cong_suat":"120W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"DPC09-180W","ten":"Den LED chieu sang 180W","cong_suat":"180W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
    {"ma_sp":"FL03-400W", "ten":"Den pha LED 400W","cong_suat":"400W","nhiet_do_mau":"4000K","do_kin":"IP66/IK08","nam_san_xuat":"2026"},
]

def doc_logo_base64(p):
    try:
        with open(p,"rb") as f: return base64.b64encode(f.read()).decode()
    except: return ""

def tao_html(sp, logo_b64, d):
    logo = f'<img src="data:image/png;base64,{logo_b64}" style="height:70px">' if logo_b64 else '<b style="color:white;font-size:24px">DANPULICO</b>'
    html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{sp["ten"]}</title>
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:Arial,sans-serif;background:#f0f4f8;display:flex;justify-content:center;padding:20px 12px}}.card{{background:white;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,.12);max-width:420px;width:100%;overflow:hidden}}.hdr{{background:linear-gradient(135deg,#1a237e,#283593);padding:24px 20px;text-align:center}}.hdr small{{color:#c5cae9;font-size:12px}}.tn{{background:#f5a623;color:white;text-align:center;padding:14px;font-size:18px;font-weight:700}}.ma{{text-align:center;background:#fff8e1;padding:6px;font-size:13px;color:#795548}}.ts{{padding:16px 20px}}.ts h3{{font-size:11px;text-transform:uppercase;color:#9e9e9e;margin-bottom:12px}}.row{{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #f5f5f5}}.row:last-child{{border-bottom:none}}.lb{{color:#757575;font-size:14px}}.vl{{color:#212121;font-size:14px;font-weight:600}}.ft{{background:#1a237e;color:white;padding:14px 20px;font-size:14px}}.ft a{{color:#c5cae9;text-decoration:none;font-weight:600}}</style></head>
<body><div class="card"><div class="hdr">{logo}<br><small>Cong ty CP Chieu sang cong cong Da Nang</small></div>
<div class="tn">{sp["ten"]}</div><div class="ma">Ma SP: <b>{sp["ma_sp"]}</b></div>
<div class="ts"><h3>Thong so ky thuat</h3>
<div class="row"><span class="lb">Cong suat</span><span class="vl">{sp["cong_suat"]}</span></div>
<div class="row"><span class="lb">Nhiet do mau</span><span class="vl">{sp["nhiet_do_mau"]}</span></div>
<div class="row"><span class="lb">Do kin / Chong va dap</span><span class="vl">{sp["do_kin"]}</span></div>
<div class="row"><span class="lb">Nam san xuat</span><span class="vl">{sp["nam_san_xuat"]}</span></div>
</div><div class="ft">📞 <a href="tel:02363565741">0236.3565741</a></div></div></body></html>"""
    open(f"{d}/{sp['ma_sp']}.html","w",encoding="utf-8").write(html)
    return f"{d}/{sp['ma_sp']}.html"

def tao_qr(sp, d):
    url = f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}/{sp['ma_sp']}.html"
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=4)
    qr.add_data(url); qr.make(fit=True)
    qr.make_image(fill_color="#1a237e",back_color="white").save(f"{d}/{sp['ma_sp']}.png")
    return url

if __name__ == "__main__":
    os.makedirs("danpulico_web/qr", exist_ok=True)
    logo = doc_logo_base64(LOGO_PATH)
    for sp in DANH_SACH_SAN_PHAM:
        tao_html(sp, logo, "danpulico_web")
        url = tao_qr(sp, "danpulico_web/qr")
        print(f"OK {sp['ma_sp']} -> {url}")
    print("Xong! Upload thu muc danpulico_web/*.html len GitHub.")
