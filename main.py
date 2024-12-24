import requests
res_parse_list = []
response = requests.get("https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut")
response_text = response.text
response_parse = response_text.split("<td>")
for parse_elem_1 in response_parse:
    if parse_elem_1:
        for parse_elem_2 in parse_elem_1.split("</td>\n"):
            if parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)
for i in res_parse_list:
    print(i)