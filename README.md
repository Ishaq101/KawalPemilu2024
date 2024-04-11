## Instruction

### Requirements
- I recommend to create a new python virtual environment using 
```python -m venv <your-env-name>```
- After your virtual env is created, you could activate it using 
```<your-env-name>\Scripts\activate```
- Once you are using your virtual environment, install the requirement with
```pip install -r requirements.txt```
- Please make sure your internet is stable
- Info: my env using python 3.11

### Start Scraping
- You can start scraping with this simple code
```python scraper.py```
- Info: If the code is stopped in middle of scraping, just check what is last row in your kawalpemilu.csv then modify variables last_prov_id,last_kab_id,last_kec_id,last_kel_id to where you want to start. Remember these variables based on location ordering for every location (like Province,Kabupaten,Kecamatan,Kelurahan) and start from 1 numbering. 
example: if the running code is stopped, check your last data in kawalpemilu.csv. Here is example of last scraped data
|prov_name|prov_id|kab_name       |kab_id|kec_name    |kec_id|kel_name         |kel_id| ... |
|ACEH     |1      |ACEH BARAT DAYA|2     |LEMBAH SABIL|5     |GEULANGGANG BATEE|3     | ... |
then the variable will be
last_prov_id = 1
last_kab_id = 2
last_kec_id = 5
last_kel_id = 4

### Debugging 
- If you are facing error like element not found, while it is actually appeared in website, you could modify the variable scroll_down_constant or the sleep time in particular block of code