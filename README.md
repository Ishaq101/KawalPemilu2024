<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instructions</title>
  <style>
    body {
      font-family: verdana, sans-serif;
      line-height: 1.5;
    }
    h1, h2 {
      margin-top: 1em;
      margin-bottom: 0.5em;
    }
    h1 {
      font-size: 1.5rem;
    }
    h2 {
      font-size: 1.25rem;
    }
    ul {
      list-style: disc;
      padding-left: 1.5em;
    }
    li {
      margin-bottom: 0.25em;
    }
    code {
      font-family: monospace;
      padding: 0.25em;
      background-color: #eee;
    }
    table {
      border-collapse: collapse;
      width: 100%;
    }
    th, td {
      padding: 0.5em;
      border: 1px solid #ddd;
    }
    .info {
      font-style: italic;
      margin-top: 0.5em;
    }
  </style>
</head>
<body>
  <h1>Instructions</h1>

  <h2>Requirements</h2>
  <ul>
    <li>Create a new Python virtual environment using:</li>
    <li><code>python -m venv (your-env-name)</code></li>
    <li>Activate the virtual environment:</li>
    <li><code>(your-env-name)\Scripts\activate</code> (Windows)</li>
    <li>Install requirements with:</li>
    <li><code>pip install -r requirements.txt</code></li>
    <li>Ensure a stable internet connection.</li>
  </ul>

  <h2 id="start-scraping">Start Scraping</h2>
  <ul>
    <li>Run the scraping script:</li>
    <li><code>python scraper.py</code></li>
  </ul>

  <div class="info">
    <h4>Resuming a stopped scrape</h4>
    <p>If the code stops mid-scrape, check the last row in your `kawalpemilu.csv` file. Modify the variables `last_prov_id`, `last_kab_id`, `last_kec_id`, and `last_kel_id` to the desired starting point. Remember these variables correspond to the location order (Province, Kabupaten, Kecamatan, Kelurahan) and start numbering from 1.</p>
    <p>Here's an example: If the last scraped data in `kawalpemilu.csv` is:</p>
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
    <p>Then the variables would be:</p>
    <ul>
      <li><code>last_prov_id = 1</code></li>
      <li><code>last_kab_id = 2</code></li>
      <li><code>last_kec_id = 5</code></li>
      <li><code>last_kel_id = 4</code></li>
    </ul>
  </div>

  <h2>Debugging</h2>
  <p>If you encounter "element not found" errors when elements are present on the website, try modifying the `scroll_down_constant` variable or the sleep time in specific code blocks.</p>
</body>
</html>