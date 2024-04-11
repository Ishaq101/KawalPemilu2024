<html>
<body>
<h1>Instruction</h1>

<h2>Requirements</h2>

<ul>
    <li>I recommend to create a new python virtual environment using <br> 
    <code>python -m venv (your-env-name)<code></li>
    <li>After your virtual env is created, you could activate it using <br>
    <code>(your-env-name)\Scripts\activate</code></li>
    <li>Once you are using your virtual environment, install the requirement with <br>
    <code>pip install -r requirements.txt</code></li>
    <li>Please make sure your internet is stable</li>
    <li>Info: my env using python 3.11</li>
</ul>

<h2>Start Scraping</h2>
<ul>
<li>You can start scraping with this simple code <br> 
<code>python scraper.py</code></li>
<li>Info: If the code is stopped in middle of scraping, just check what is last row in your kawalpemilu.csv then modify variables last_prov_id,last_kab_id,last_kec_id,last_kel_id to where you want to start. Remember these variables based on location ordering for every location (like Province,Kabupaten,Kecamatan,Kelurahan) and start from 1 numbering. <br>example: if the running code is stopped, check your last data in kawalpemilu.csv. Here is example of last scraped data</li>
<table>
<tr>
    <th>prov_name</th>
    <th>prov_id</th>
    <th>kab_name</th>
    <th>kab_id</th>
    <th>kec_name</th>
    <th>kec_id</th>
    <th>kel_name</th>
    <th>kel_id</th>
    <th>...</th>
</tr>
<tr>
    <td>ACEH</td>
    <td>1</td>
    <td>ACEH BARAT DAYA</td>
    <td>2</td>
    <td>LEMBAH SABIL</td>
    <td>5</td>
    <td>GEULANGGANG BATEE</td>
    <td>3</td>
    <td>...</td>
</tr>
</table>
then the variable will be <br>
last_prov_id = 1 <br>
last_kab_id = 2 <br>
last_kec_id = 5 <br>
last_kel_id = 4 <br>
</ul>
<h2>Debugging</h2>
<span>If you are facing error like element not found, while it is actually appeared in website, you could modify the variable scroll_down_constant or the sleep time in particular block of code.</span>
</body>
</html>