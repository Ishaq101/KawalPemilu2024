import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = webdriver.ChromeService(executable_path = './chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service,options=options)
driver.get('https://kawalpemilu.org')
driver.maximize_window()
wait = WebDriverWait(driver, 10)


# capture start time 
st = time.time()

# check if value is alphabetic word
def is_alpha(word):
    area_name = " ".join(re.findall("^[a-zA-Z]+\s+[a-zA-Z]+|\s*[a-zA-Z]*", word))
    return area_name.strip()

# get value for all column in a row of a table votes result
def get_table_data(prov_name,prov_id,kab_name,kab_id,kec_name,kec_id,kel_name,kel_id,row,vote_data=[],scroll=False):
    if scroll != True:
        # check missing value
        try:
            is_missing_value = [True for r in row if '-' in r][0] # True
        except:
            is_missing_value = False

        if ~is_missing_value:
            try:
                paslon1 = row[1].split(' ')[1]
                paslon1 = int(paslon1.replace(',',''))
                paslon1_perc = row[1].split(' ')[0]

                paslon2 = row[2].split(' ')[1]
                paslon2 = int(paslon2.replace(',',''))
                paslon2_perc = row[2].split(' ')[0]

                paslon3 = row[3].split(' ')[1]
                paslon3 = int(paslon3.replace(',',''))
                paslon3_perc = row[3].split(' ')[0]

                tot_tps_foto_approved_kawal_pemilu = row[4].split(' ')[1].split('/')[0]
                tot_tps_foto_approved_kawal_pemilu = int(tot_tps_foto_approved_kawal_pemilu.replace(',',''))

                tot_tps = row[4].split(' ')[1].split('/')[2]
                tot_tps = int(tot_tps.replace(',',''))

                tps_coverage_perc = row[4].split(' ')[0]
                # tot_tps_foto_sirekap_to_kawal_pemilu = row[4].split(' ')[1].split('/')[1]
                row_data = [prov_name,prov_id,kab_name,kab_id,kec_name,kec_id,kel_name,kel_id,paslon1,paslon1_perc,paslon2,paslon2_perc,paslon3,paslon3_perc,tot_tps_foto_approved_kawal_pemilu,tot_tps,tps_coverage_perc]
                vote_data.append(row_data)
                print(row_data)
            except:
                print(row_data)
        else:
            paslon1 = None
            paslon1_perc = None
            paslon2 = None
            paslon2_perc = None
            paslon3 = None
            paslon3_perc = None
            tot_tps_foto_approved_kawal_pemilu = None
            tot_tps = None
            tps_coverage_perc = None
            province_id = i
            row_data = [prov_name,prov_id,kab_name,kab_id,kec_name,kec_id,kel_name,kel_id,paslon1,paslon1_perc,paslon2,paslon2_perc,paslon3,paslon3_perc,tot_tps_foto_approved_kawal_pemilu,tot_tps,tps_coverage_perc]
            vote_data.append(row_data)
            print(row_data)
    else:
        # scrolling down
        try:
            is_missing_value = [True for r in row if '-' in r][0] # True
        except:
            is_missing_value = False

        if ~is_missing_value:
            try:
                paslon1 = row[1].split(' ')[1]
                paslon1 = int(paslon1.replace(',',''))
                paslon1_perc = row[1].split(' ')[0]

                paslon2 = row[2].split(' ')[1]
                paslon2 = int(paslon2.replace(',',''))
                paslon2_perc = row[2].split(' ')[0]

                paslon3 = row[3].split(' ')[1]
                paslon3 = int(paslon3.replace(',',''))
                paslon3_perc = row[3].split(' ')[0]

                tot_tps_foto_approved_kawal_pemilu = row[4].split(' ')[1].split('/')[0]
                tot_tps_foto_approved_kawal_pemilu = int(tot_tps_foto_approved_kawal_pemilu.replace(',',''))

                tot_tps = row[4].split(' ')[1].split('/')[2]
                tot_tps = int(tot_tps.replace(',',''))

                tps_coverage_perc = row[4].split(' ')[0]
                # tot_tps_foto_sirekap_to_kawal_pemilu = row[4].split(' ')[1].split('/')[1]
                row_data = [prov_name,prov_id,kab_name,kab_id,kec_name,kec_id,kel_name,kel_id,paslon1,paslon1_perc,paslon2,paslon2_perc,paslon3,paslon3_perc,tot_tps_foto_approved_kawal_pemilu,tot_tps,tps_coverage_perc]
                vote_data.append(row_data)
                print(row_data)
            except:
                print(row_data)
        else:
            paslon1 = None
            paslon1_perc = None
            paslon2 = None
            paslon2_perc = None
            paslon3 = None
            paslon3_perc = None
            tot_tps_foto_approved_kawal_pemilu = None
            tot_tps = None
            tps_coverage_perc = None
            row_data = [prov_name,prov_id,kab_name,kab_id,kec_name,kec_id,kel_name,kel_id,paslon1,paslon1_perc,paslon2,paslon2_perc,paslon3,paslon3_perc,tot_tps_foto_approved_kawal_pemilu,tot_tps,tps_coverage_perc]
            vote_data.append(row_data)
            print(row_data)
    return vote_data

province_table_xpath = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr'
wait.until(EC.element_to_be_clickable((By.XPATH,province_table_xpath)))

location_xpath = "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/thead/tr/th[1]"
location = driver.find_element(By.XPATH,location_xpath)
location = location.text.split(' ')[0]

province_table = driver.find_elements(By.XPATH,province_table_xpath)
province_names = [is_alpha(prov.text) for prov in province_table]
print(f"total {location}:",len(province_names))
home_xpath = "/html/body/app-root/div/header/div/a"

# initiate list, will be used as dataframe input
vote_data = []

# run based on last location id, inclusive to be re-run
# if there is intervention in the middle of running, then you can define the last location id here to continue from your last scraped data
# example: if the running code is stopped, check your last data in kawalpemilu.csv. Here is example of last scraped data
# |prov_name|prov_id|kab_name       |kab_id|kec_name    |kec_id|kel_name         |kel_id| ... |
# |ACEH     |1      |ACEH BARAT DAYA|2     |LEMBAH SABIL|5     |GEULANGGANG BATEE|3     | ... |
# then the variable will be
# last_prov_id = 1
# last_kab_id = 2
# last_kec_id = 5
# last_kel_id = 4

# Determine starting location you want to scrape, if all variable is assign to 1 then it will start from very begining
last_prov_id = 2
last_kab_id = 1
last_kec_id = 4
last_kel_id = 4

# you may adjust this constant, (min value=1)
scroll_down_constant = 2

####>>>>>>>         SCRAPER         <<<<<<<<##
try:
    for i in range(len(province_names)-(last_prov_id-1)):
        driver.refresh()
        time.sleep(0.25)
        i+=1
        province_id = int(i+(last_prov_id-1))
        if province_id<7:
            wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{province_id}]/td[1]/div/a[1]")))
            province_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{province_id}]/td[1]/div/a[1]"
            province = driver.find_element(By.XPATH,province_link_xpath)
            province_name = province.text
            print('>>',province_name,province_id)
        else:
            # scrolling down
            scroll_down_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{province_id-scroll_down_constant}]/td[1]/div/a[1]"
            wait.until(EC.element_to_be_clickable((By.XPATH,scroll_down_link_xpath)))
            scroll_down = driver.find_element(By.XPATH,scroll_down_link_xpath)
            scroll_down.location_once_scrolled_into_view

            province_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{province_id}]/td[1]/div/a[1]"
            wait.until(EC.element_to_be_clickable((By.XPATH,province_link_xpath)))
            province = driver.find_element(By.XPATH,province_link_xpath)
            province_name = province.text
            print('>>',province_name,province_id)

        #>>>>>>>>>>>>>>>>  kabupaten  <<<<<<<<<<<<<<#
        province.click()
        driver.refresh()
        time.sleep(0.25)
        table_xpath = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr'
        wait.until(EC.element_to_be_clickable((By.XPATH,table_xpath)))

        kabupaten_table = driver.find_elements(By.XPATH,table_xpath)
        kabupaten_names = [is_alpha(kab.text) for kab in kabupaten_table]

        if province_name!='LUAR NEGERI':
            for kab_i in range(len(kabupaten_names)-(last_kab_id-1)):
                driver.refresh()
                time.sleep(0.25)
                kab_i+=1
                kabupaten_id = int(kab_i+(last_kab_id-1))
                if kabupaten_id<7:
                    wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]")))
                    kab_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]"
                    kabupaten = driver.find_element(By.XPATH,kab_link_xpath)
                    kabupaten_name = kabupaten.text
                    print('>>->>',kabupaten_name,kabupaten_id)
                else:
                    scroll_down_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id-scroll_down_constant}]/td[1]/div/a[1]"
                    wait.until(EC.element_to_be_clickable((By.XPATH,scroll_down_link_xpath)))
                    scroll_down = driver.find_element(By.XPATH,scroll_down_link_xpath)
                    scroll_down.location_once_scrolled_into_view

                    wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]")))
                    kab_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]"
                    kabupaten = driver.find_element(By.XPATH,kab_link_xpath)
                    kabupaten_name = kabupaten.text
                    print('>>->>',kabupaten_name,kabupaten_id)

                #>>>>>>>>>>>>>>>>  kecamatan  <<<<<<<<<<<<<<#
                kabupaten.click()
                driver.refresh()
                time.sleep(0.25)
                table_xpath = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr'
                wait.until(EC.element_to_be_clickable((By.XPATH,table_xpath)))

                kecamatan_table = driver.find_elements(By.XPATH,table_xpath)
                kecamatan_names = [is_alpha(kec.text) for kec in kecamatan_table]

                for kec_i in range(len(kecamatan_names)-(last_kec_id-1)):
                    driver.refresh()
                    time.sleep(0.25)
                    kec_i+=1
                    kecamatan_id = int(kec_i+(last_kec_id-1))
                    if kecamatan_id<7:
                        wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kecamatan_id}]/td[1]/div/a[1]")))
                        kec_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kecamatan_id}]/td[1]/div/a[1]"
                        kecamatan = driver.find_element(By.XPATH,kec_link_xpath)
                        kecamatan_name = kecamatan.text
                        print('>>->>->>',kecamatan_name,kecamatan_id)
                    else:
                        scroll_down_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kecamatan_id-scroll_down_constant}]/td[1]/div/a[1]"
                        wait.until(EC.element_to_be_clickable((By.XPATH,scroll_down_link_xpath)))
                        scroll_down = driver.find_element(By.XPATH,scroll_down_link_xpath)
                        scroll_down.location_once_scrolled_into_view

                        wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kecamatan_id}]/td[1]/div/a[1]")))
                        kec_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kecamatan_id}]/td[1]/div/a[1]"
                        kecamatan = driver.find_element(By.XPATH,kec_link_xpath)
                        kecamatan_name = kecamatan.text
                        kecamatan_id = kec_i+(last_kec_id-1)
                        print('>>->>->>',kecamatan_name,kecamatan_id)
                    #>>>>>>>>>>>>>>>>  kel/desa   <<<<<<<<<<<<<<#
                    kecamatan.click()
                    driver.refresh()
                    time.sleep(0.25)
                    table_xpath = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr'
                    wait.until(EC.element_to_be_clickable((By.XPATH,table_xpath)))

                    kelurahan_table = driver.find_elements(By.XPATH,table_xpath)
                    kelurahan_names = [is_alpha(kel.text) for kel in kelurahan_table]

                    for kel_i in range(len(kelurahan_names)-(last_kel_id-1)):
                        driver.refresh()
                        time.sleep(0.25)
                        kel_i+=1
                        kelurahan_id = int(kel_i+(last_kel_id-1))
                        if kelurahan_id<7:
                            wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td[1]/div/a[1]")))
                            kel_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td[1]/div/a[1]"
                            kelurahan = driver.find_element(By.XPATH,kel_link_xpath)
                            kelurahan_name = kelurahan.text
                            print('>>->>->>->>',province_name,province_id,'/',kabupaten_name,kabupaten_id,'/',kecamatan_name,kecamatan_id,'/',kelurahan_name,kelurahan_id)
                            time.sleep(0.5)
                            wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td')))
                            row = driver.find_elements(By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td')
                            row = [r.text.replace('\n',' ') for r in row]          
                            try:          
                                get_table_data(prov_name=province_name,prov_id=province_id,kab_name=kabupaten_name,kab_id=kabupaten_id,kec_name=kecamatan_name,kec_id=kecamatan_id,kel_name=kelurahan_name,kel_id=kelurahan_id,row=row,vote_data=vote_data,scroll=False)
                            except:
                                print('ERROR:',row)
                        else:
                            scroll_down_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id-scroll_down_constant}]/td[1]/div/a[1]"
                            wait.until(EC.element_to_be_clickable((By.XPATH,scroll_down_link_xpath)))
                            scroll_down = driver.find_element(By.XPATH,scroll_down_link_xpath)
                            scroll_down.location_once_scrolled_into_view

                            wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td[1]/div/a[1]")))
                            kel_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td[1]/div/a[1]"
                            kelurahan = driver.find_element(By.XPATH,kel_link_xpath)
                            kelurahan_name = kelurahan.text
                            # kelurahan_id = kel_i+(last_kel_id-1)
                            print('>>->>->>->>',province_name,province_id,'/',kabupaten_name,kabupaten_id,'/',kecamatan_name,kecamatan_id,'/',kelurahan_name,kelurahan_id)
                            time.sleep(0.5)
                            wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td')))
                            row = driver.find_elements(By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kelurahan_id}]/td')
                            row = [r.text.replace('\n',' ') for r in row]      
                            try:              
                                get_table_data(prov_name=province_name,prov_id=province_id,kab_name=kabupaten_name,kab_id=kabupaten_id,kec_name=kecamatan_name,kec_id=kecamatan_id,kel_name=kelurahan_name,kel_id=kelurahan_id,row=row,vote_data=vote_data,scroll=True)
                            except:
                                print('ERROR:',row)
                    driver.back()
                    continue
                driver.back()
                continue
        elif province_name=='LUAR NEGERI':
            for kab_i in range(len(kabupaten_names)-(last_kab_id-1)):
                driver.refresh()
                time.sleep(0.25)
                kab_i+=1
                kabupaten_id = kab_i+(last_kab_id-1)
                if kabupaten_id<7:
                    wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]")))
                    kab_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]"
                    kabupaten = driver.find_element(By.XPATH,kab_link_xpath)
                    kabupaten_name = kabupaten.text
                    print('>>->>',kabupaten_name,kabupaten_id)
                    wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td')))
                    row = driver.find_elements(By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td')
                    row = [r.text.replace('\n',' ') for r in row]          
                    try:          
                        get_table_data(prov_name=province_name,prov_id=province_id,kab_name=kabupaten_name,kab_id=kabupaten_id,kec_name=None,kec_id=None,kel_name=None,kel_id=None,row=row,vote_data=vote_data,scroll=False)
                    except:
                        print('ERROR:',row)
                else:
                    scroll_down_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id-scroll_down_constant}]/td[1]/div/a[1]"
                    wait.until(EC.element_to_be_clickable((By.XPATH,scroll_down_link_xpath)))
                    scroll_down = driver.find_element(By.XPATH,scroll_down_link_xpath)
                    scroll_down.location_once_scrolled_into_view

                    wait.until(EC.element_to_be_clickable((By.XPATH,f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]")))
                    kab_link_xpath = f"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td[1]/div/a[1]"
                    kabupaten = driver.find_element(By.XPATH,kab_link_xpath)
                    kabupaten_name = kabupaten.text
                    print('>>->>',kabupaten_name,kabupaten_id)
                    wait.until(EC.element_to_be_clickable((By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td')))
                    row = driver.find_elements(By.XPATH,f'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-hierarchy/div/main/table/tbody/tr[{kabupaten_id}]/td')
                    row = [r.text.replace('\n',' ') for r in row]          
                    try:          
                        get_table_data(prov_name=province_name,prov_id=province_id,kab_name=kabupaten_name,kab_id=kabupaten_id,kec_name=None,kec_id=None,kel_name=None,kel_id=None,row=row,vote_data=vote_data,scroll=True)
                    except:
                        print('ERROR:',row)
            driver.back()
            continue    
        driver.back()
        continue       
except:
    print('stopped')
finally:
    if len(vote_data)!=0:
        try:
            prev_df = pd.read_csv('kawalpemilu.csv')
            kawal_pemilu_df = pd.DataFrame(vote_data,columns=['prov_name','prov_id','kab_name','kab_id','kec_name','kec_id','kel_name','kel_id','paslon1','paslon1_perc','paslon2','paslon2_perc','paslon3','paslon3_perc','tot_tps_foto_approved_kawal_pemilu','tot_tps','tps_coverage_perc'])
            new_df = pd.concat([prev_df,kawal_pemilu_df])
            new_df = new_df.drop_duplicates() # removing duplicates row
            new_df.to_csv('kawalpemilu.csv',index=False)
        except: # if there is no kawalpemilu.csv file yet in your directory (when you first time running with cloning kawalpemilu.csv)
            kawal_pemilu_df = pd.DataFrame(vote_data,columns=['prov_name','prov_id','kab_name','kab_id','kec_name','kec_id','kel_name','kel_id','paslon1','paslon1_perc','paslon2','paslon2_perc','paslon3','paslon3_perc','tot_tps_foto_approved_kawal_pemilu','tot_tps','tps_coverage_perc'])
            new_df = pd.concat([prev_df,kawal_pemilu_df])
            new_df = new_df.drop_duplicates() # removing duplicates row
            new_df.to_csv('kawalpemilu.csv',index=False)
    rt = time.time() - st
    print(f'runtime: {rt/60} mins')


