import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
df_data = pd.read_excel("D:/Temperature.xlsx",index_col=0)
print(df_data[4:8]["Season"])

# import requests
# x = requests.get("https://hocpython.org/data/")
# html = x.text
# print(html)
# vitridaubang = html.find("<table>")
# vitricuoibang = html.find("</table>")
# html = html[vitridaubang+7:vitricuoibang]
# html = html.replace("<tbody","")
# html = html.replace("</tbody>","")
# html = html.replace("<tr>","")
# html = html.replace("</tr","\n")
# html = html.replace("<td>","")
# html = html.replace("</td>",",")
# html = html.replace(",\n","\n")
#
# f = open("DataNHanVien.csv","w",encoding="utf8")
# f.write(html)
# f.close()
#
# print(html)



