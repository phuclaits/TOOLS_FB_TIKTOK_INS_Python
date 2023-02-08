from time import sleep
import requests
from undetected_chromedriver.v2 import Chrome, ChromeOptions
from urllib.parse import unquote
class Machine_liker:
    def __init__(self,cookies,list_id_post,token_captcha) -> None:
        self.cookies = cookies
        self.list_id_post = list_id_post
        self.token_captcha = token_captcha  
    def Run(self):
        stt = 0
        for i in range(10000):
            # Setting up the Chrome driver.
            options = {}
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--force-dev-mode-highlighting") 
            chrome_options.add_argument("--system-developer-mode")
            chrome_options.add_argument("--window-size=480,1000")
            driver = Chrome(seleniumwire_options=options, options=chrome_options)
            try:
                # Very cloudflare
                driver.get('https://www.machine-liker.com/login/')
                driver.execute_script("""window.open('https://www.machine-liker.com/login/')""") # nay de lam gi z
                driver.execute_script("""window.open('https://www.machine-liker.com/login/')""")
                # Trying to click on the cancel button of the pop-up.
                for i in range(15):
                    try:
                        driver.find_element('id','onesignal-slidedown-cancel-button').click()
                        break
                    except:
                        sleep(1)
                        continue
                # Scrolling down the page and getting the value of the input element.
                driver.execute_script(f'window.scrollTo(0,700)'),sleep(1)
                code = driver.find_element('xpath' ,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div/input').get_attribute("value")
                print(f'Very Code: {code}                 ',end = '\r')
                # The above code is used to verify the Facebook account.
                headers = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?1',
                    'save-data': 'on',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'none',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': self.cookies
                }
                check_dv = requests.get(f'https://mbasic.facebook.com/device?user_code={code}', headers=headers).text
                # Getting the fb_dtsg, jazoest, and qr values from the html code.
                try:
                    fb_dtsg = check_dv.split('name="fb_dtsg" value="')[1].split('" autocomplete="off"')[0]
                    jazoest = check_dv.split('name="jazoest" value="')[1].split('" autocomplete="off"')[0]
                    qr = check_dv.split('name="qr" value="')[1].split('"')[0]
                except:
                    print(f'Error Cookies Facebook')
                

                headers = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                            'sec-ch-ua-mobile': '?1',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://mbasic.facebook.com',
                            'content-type': 'application/x-www-form-urlencoded',
                            'save-data': 'on',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': f'https://mbasic.facebook.com/device?user_code={code}',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cookie': self.cookies
                        }
                data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'qr': qr,
                            'user_code': code
                        }
                url_c = requests.post('https://mbasic.facebook.com/device/redirect/', headers=headers, data=data).url
                url_f = unquote(url_c).split('next=1&next=')[1]
                headers = {
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cache-control': 'no-cache',
                    'cookie': self.cookies,
                    'pragma': 'no-cache',
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                }

                response = requests.get(url_f,headers=headers).text
                eav = response.split('eav=')[1].split('"')[0]

                scope = response.split('name="scope" value="')[1].split('"')[0]
                user_code = response.split('name="user_code" value="')[1].split('"')[0]
                logger_id = response.split('name="logger_id" value="')[1].split('"')[0]
                encrypted_post_body = response.split('name="encrypted_post_body" value="')[1].split('"')[0]
                headers = {
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cache-control': 'no-cache',
                    'cookie': self.cookies,
                    'origin': 'https://mbasic.facebook.com',
                    'pragma': 'no-cache',
                    'referer': url_f,
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                }

                params = {
                    'paipv': '0',
                    'eav': eav,
                }

                data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'scope': scope,
                    'display': 'touch',
                    'sdk': '',
                    'sdk_version': '',
                    'domain': '',
                    'sso_device': '',
                    'state': '',
                    'user_code': user_code,
                    'logger_id': logger_id,
                    'auth_type': 'rerequest',
                    'auth_nonce': '',
                    'code_challenge': '',
                    'code_challenge_method': '',
                    'encrypted_post_body': encrypted_post_body,
                    'return_format[]': 'code',
                }

                url = requests.post(
                    'https://mbasic.facebook.com/dialog/oauth/skip/submit/',
                    params=params,
                    headers=headers,
                    data=data,
                    )
                url = url.url
                url_z = unquote(url).split('next=')[1]
                # Sending a GET request to the URL with the headers.
                headers = {
                    'authority': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'cookie': self.cookies,
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                }

                response = requests.get(
                    url_z,
                    headers=headers,
                )
                print('Very code success!            ',end = '\r')
                # Clicking on the "Login" button.
                driver.find_element('xpath','/html/body/div[1]/div[2]/div/div[2]/div/div/div[4]/button').click()
                sleep(3)
                # The above code is trying to solve a captcha.
                driver.execute_script(f'window.scrollTo(0,400)')
                sleep(1)
                site_key = driver.page_source.split('data-sitekey="')[1].split('"')[0]
                link = 'https://www.machine-liker.com/verify/'
                a = requests.post(f'https://captcha69.com/in.php?key={self.token_captcha}&googlekey={site_key}&method=userrecaptcha&pageurl={link}').text
                token = a.split('|')[1]
                print('Very Captcha            ',end = '\r')
                for i in range(200):
                    response = requests.post(f'https://captcha69.com/res.php?key={self.token_captcha}&action=get&id={token}').text
                    if response == 'CAPCHA_NOT_READY':
                        print(i,response,end='\r')
                        sleep(0.1)
                    else:
                        gg = response.split('|')[1]
                        break   
                try:
                    driver.execute_script(f'''document.getElementById("g-recaptcha-response").innerHTML="{gg}"''')
                except:
                    print('Erro Captcha',end = '\r')
                    driver.execute_script(f'''document.getElementById("g-recaptcha-response").innerHTML="{gg}"''')
                driver.execute_script('window.document.querySelector("body > div.container > div:nth-child(3) > div > div > div > div > form > div.form-group.d-grid.mb-0 > button").click()')
                print('Very Captcha Success            ',end = '\r')
                check_live = True
                while True:
                    for post_id in self.list_id_post :
                        # Trying to get the cookies from the browser.
                        ckkk=[]
                        list_ck=[]
                        for z in range(10):
                            try:
                                for x in driver.get_cookies():
                                    ckkk.append(x['name']+'='+x['value'])
                                ck=';'.join(ckkk)+';'
                                list_ck.append(ck)
                                break
                            except:
                                pass
                        headers = {
                            'authority': 'www.machine-liker.com',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language': 'en-US,en;q=0.9',
                            'cache-control': 'max-age=0',
                            'cookie': ck,
                            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                        }
                        params = {
                            'post_id': post_id,
                        }
                        response = requests.get('https://www.machine-liker.com/send-reactions/', params=params, headers=headers).text
                        object_id = response.split('name="object_id" value="')[1].split('"')[0]
                        data = {
                            'object_id': object_id,
                            'reactions': '1,2',
                            'limit': '50',
                        }
                        response = requests.post('https://www.machine-liker.com/api/send-reactions/', headers=headers, data=data)
                        # The above code is a part of a program that is used to check if a post is live or
                        # not.
                        try:
                            buff = response.json()['info']['message']
                            stt = stt + 1
                            print(f'[{stt}] - {post_id} - Success                                                                    ')
                        except:
                            if self.list_id_post [-1] == post_id:
                                check_live = False
                                break
                            else:continue
                        if check_live == False:
                            driver.close()
                            break
                        else:pass
                        for i in range(605,-1,-1):
                            print(f'Wait {i}s!   ',end = '\r')
                            sleep(1)
            except:
                driver.close()
                continue
#Cookies Facebook
cookies = 'sb=3GKgYyp6Hh0bQHz8NLU5V737; datr=3GKgY-8ThrvMNpTxzEKEBgtS; c_user=100076703259563; xs=21:omfLkZKb38jVsg:2:1671455470:-1:13463; fr=0kVQydUv1b1E2SPMx.AWVHgSl2jL4fcyaDmaF-5G65VC0.BjoGLc.2a.AAA.0.0.BjoGLv.AWWaxJYbbSQ; wd=1348x961; presence=C{"t3":[],"utc3":1671455539283,"v":1}'
list_id_post = ['880042679788558','874904580302368'] #id post 
token_captcha = 'point_69de854eb94f80a22ce53ccb44de2c67' #Token Proxy
if __name__ == '__main__':
    Machine_liker(cookies, list_id_post, token_captcha).Run()


