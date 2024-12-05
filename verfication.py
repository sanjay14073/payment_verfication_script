from PIL import Image, UnidentifiedImageError
import pandas as pd
import easyocr
import requests
from io import BytesIO

def convert_to_direct_download(url):
    if "drive.google.com" in url:
        if "/file/d/" in url:
            file_id = url.split("/file/d/")[1].split("/view")[0]
            return f"https://drive.google.com/uc?export=download&id={file_id}"
    return url

df = pd.read_excel("verify.xlsx")
payment_series = df["payment_screenshot"]
entered_id_series = df["entered_id"]

my_final_list = []
reader = easyocr.Reader(['en'])

for i in range(len(payment_series)):
    try:
        download_url = convert_to_direct_download(payment_series[i])
        destination = f"{entered_id_series[i]}.jpeg"
        response = requests.get(download_url, stream=True)

        if response.status_code == 200:
            try:
                img = Image.open(BytesIO(response.content))
                img.save(destination, "JPEG")
            except UnidentifiedImageError:
                my_final_list.append([payment_series[i], entered_id_series[i], "Invalid Image"])
                continue
        else:
            my_final_list.append([payment_series[i], entered_id_series[i], "Download Failed"])
            continue

        result = reader.readtext(destination, detail=0)

        if str(entered_id_series[i]) in result:
            my_final_list.append([payment_series[i], entered_id_series[i], "Matched"])
        else:
            my_final_list.append([payment_series[i], entered_id_series[i], "Not Matched"])
    except Exception as e:
        my_final_list.append([payment_series[i], entered_id_series[i], f"Error: {str(e)}"])

final_dataframe = pd.DataFrame(my_final_list, columns=["Links", "Entered UTR No", "Result"])
final_dataframe.to_excel("verification_results.xlsx", index=False)

print("Verification completed. Results saved to 'verification_results.xlsx'.")
