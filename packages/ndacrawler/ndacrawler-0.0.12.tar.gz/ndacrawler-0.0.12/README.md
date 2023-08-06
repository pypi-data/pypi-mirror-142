# NDA Website Crawler

This crawler helps extract information from the [National Drug Authority(NDA) website](https://www.nda.or.ug/) in Uganda. 

## Installation
```console
pip install ndacrawler
```

## Examples 
### Get list of  [licensed drugs](https://www.nda.or.ug/drug-register/)
    
```python
from ndacrawler import get_drugs
drugs = get_drugs()

# Data Extractors
herbal_human_drugs = drugs["Herbal Human"]
herbal_vet_drugs = drugs["Herbal Vet"]
human_drugs = drugs["Human"]
vet_drugs = drugs["Vet"]
local_traditional_human_herbal_drugs = drugs["Local Traditional Human Herbal"]

# Save to a csv file
herbal_human_drugs.to_csv("Herbal Human.csv")

# Display the headers of the data
# print(herbal_human_drugs.headers)

# Display the data
# print(herbal_human_drugs.data)


```