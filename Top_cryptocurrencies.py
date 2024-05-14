import scrapy
import os
import re
import csv

current_dir = os.path.abspath('.')
url = os.path.join(current_dir, "view-source_https___es.wikipedia.org_wiki_Criptomoneda_alternativa.html.html")
with open(url, 'r', encoding='utf-8') as _f:
    url_data = _f.read()

response = scrapy.http.TextResponse(url, body=url_data, encoding='utf-8')

# Make sure that the interesting data is available
table = response.xpath('//table')[0].xpath('tbody')
response.xpath('//table')[0].xpath('tbody').xpath('tr')
table = response.xpath('//table')[0].xpath('tbody')
table.xpath('tr')
html_strings = []

for tr in table.xpath('tr'):
    tr.xpath('td').extract()
    html_strings.append(tr.xpath('td').extract())

# Regular expression for extract the content of <td> tags
pattern = r'<td class="">(.+?)\n</td>'
important_values = []

for html_list in html_strings:
    values = []
    for html_string in html_list:
        match = re.search(pattern, html_string)
        if match:
            # Convert to float if is posible
            value = match.group(1)
            try:
                value = int(value)
            except ValueError:
                pass
            values.append(value)
    important_values.append(values)

for values in important_values:
    print(values)

# Remove the empty string at the beginning of important_values.
# if important_values and important_values[0] == []:
#     del important_values[0]

# Save to a CSV file
csv_file = "top_cryptocurrencies.csv"

# Convert to a single row
flattened_list = [value for sublist in important_values for value in sublist + ['\n']]

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(flattened_list)
