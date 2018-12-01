import requests
import os, json, time,csv


cur_dir = os.getcwd()
fp = cur_dir+"\\"
f = open(fp+"Profile_Clothing.csv",'a',newline='')
f.writer = csv.writer(f)
#f2 = open(fp+"Profile.csv",'r',newline='')
f.writer.writerow(("Url", "Company", "Company Link", "Address", "Category"))
from lxml import html
domain = "https://www.indiacom.com"
url = ['https://www.indiacom.com/yellow-pages/industrial-shoes/',
'https://www.indiacom.com/yellow-pages/leather-shoes/',
'https://www.indiacom.com/yellow-pages/men-shoes/',
'https://www.indiacom.com/yellow-pages/metal-shoe-racks/',
'https://www.indiacom.com/yellow-pages/powder-coated-compact-shoe-racks/',
'https://www.indiacom.com/yellow-pages/safety-shoes/',
'https://www.indiacom.com/yellow-pages/shoe-brakes/',
'https://www.indiacom.com/yellow-pages/shoe-polish-mfrrs-&-supplrs-/',
'https://www.indiacom.com/yellow-pages/shoe-shine-machines/',
'https://www.indiacom.com/yellow-pages/sports-shoes/',
'https://www.indiacom.com/yellow-pages/steel-shoe-racks/',
'https://www.indiacom.com/yellow-pages/wedding-shoes/',
'https://www.indiacom.com/yellow-pages/foot-operated-impulse-sealing-machine/',
'https://www.indiacom.com/yellow-pages/footware-raw-material-suppliers/',
'https://www.indiacom.com/yellow-pages/footwear/',
'https://www.indiacom.com/yellow-pages/footwear-shops/',
'https://www.indiacom.com/yellow-pages/footwear-industrial/',
'https://www.indiacom.com/yellow-pages/footwear-mfrrs-/',
'https://www.indiacom.com/yellow-pages/cloth-material/',
'https://www.indiacom.com/yellow-pages/cloth-merchants/',
'https://www.indiacom.com/yellow-pages/cloth-transportation/',
'https://www.indiacom.com/yellow-pages/clothes/',
'https://www.indiacom.com/yellow-pages/clothes-wholesalers/',
'https://www.indiacom.com/yellow-pages/clothes-and-apparels/',
'https://www.indiacom.com/yellow-pages/clothes-drying-stands/',
'https://www.indiacom.com/yellow-pages/clothing-leather-and-skin-supplies/',
'https://www.indiacom.com/yellow-pages/clothing-industry-machine-and-equipment/',
'https://www.indiacom.com/yellow-pages/cloths-merchants/',
'https://www.indiacom.com/yellow-pages/garment-patterns/',
'https://www.indiacom.com/yellow-pages/garments-accessories/',
'https://www.indiacom.com/yellow-pages/garments-fabricators/',
'https://www.indiacom.com/yellow-pages/automobile/'
]
#?page={num}"# replace f2 As url
for u in url:
    x = u + "?page={num}"
    urls = [x.format(num=num) for num in range(1,250)]
    res_num = 0
    for A in urls:
        try:
            res = requests.get(A)
        except Exception:
            continue
        response = html.fromstring(res.text)
        if "Next" not in res.text:
            break
        
        try:
            data = response.xpath('//div[@class="b_listing"]')

        except Exception:
            continue
        for d in data:
            try:
                com = d.xpath('.//div[@class="b_name"]/strong/a/text()')[0]
            except:
                com = "na"
            try:
                com_p = d.xpath('.//div[@class="b_name"]/strong/a/@href')[0]
            except:
                com_p = "na"
            try:
                comp = domain + com_p
            except:
                comp = "na"
            try:
                add = d.xpath('.//div[@class="b_address"]/text()')[0]
            except:
                add = "na"
            try:
                cate = d.xpath('.//div[@class="b_category"]/b/text()')[0]
            except:
                cate = "na"

            f.writer.writerow((A, com, comp, add, cate))
            res_num+=1
            print(res_num, "Scraped")
f.close()
