from pypdf import PdfReader, PdfWriter
import sys

def crack_pdf_password(pdf_path, dict_path, output_path):
    # PDFを読み込む
    reader = PdfReader(pdf_path)

    if not reader.is_encrypted:
        print("PDFは暗号化されていません。")
        return

    # 辞書ファイルを読み込む
    with open(dict_path, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]

    flg = False
    # パスワードを試す
    for password in passwords:
        try:
            print('パスワードを試行 ' + password + ' ...')
            if reader.decrypt(password):
                print(f"パスワードを発見: {password}")
                flg = True
                break
            print('パスワードを試行 ' + password.lower() + ' ...')
            if reader.decrypt(password.lower()):
                print(f"パスワードを発見: {password.lower()}")
                flg = True
                break
        except Exception as e:
            continue

    if flg == False:
        print("パスワードを見つけられませんでした。")
    else:
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        print(f"復号済みPDFを保存しました: {output_path}")

    return

# 使用例
if __name__ == "__main__":
    pdf_path = "encrypted.pdf"         # 暗号化されたPDFファイル
    dict_path = "dictionary.txt"        # 辞書ファイル（1行ごとにパスワード）
    output_path = "decrypted.pdf"      # 出力先

    crack_pdf_password(pdf_path, dict_path, output_path)
