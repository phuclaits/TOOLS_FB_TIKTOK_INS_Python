import requests
import os
from time import sleep
import random
os.system('cls')

luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
yellow = "\033[0;93m"
lightblue = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
hong = "\033[1;95m"

def logo():
    print(f'''
    {xduong} _______  __   __  __   __  _______    ___      _______ 
    {yellow}|       ||  | |  ||  | |  ||       |  |   |    |   _   |
    {xnhac}|    _  ||  |_|  ||  | |  ||       |  |   |    |  |_|  |
    {hong}|   |_| ||       ||  |_|  ||       |  |   |    |       |
    {luc}|    ___||       ||       ||      _|  |   |___ |       |
    {red}|   |    |   _   ||       ||     |_   |       ||   _   |
    {xduong}|___|    |__| |__||_______||_______|  |_______||__| |__|
    ''')

logo()

token=input(f'{yellow}TYPE YOUR TRAODOISUB TOKEN:{trang} ')
os.system('cls')
logo()
cookies_string =input(f'{yellow}TYPE YOUR TIKTOK COOKIE:{trang} ')
os.system('cls')
logo()
cookies = {}
var_list = cookies_string.split(';')
var_list.pop()
for var in var_list:
    var_att = var.split('=')
    #print(var_att)
    cookies[var_att[0]] = var_att[1]

tt_csrf_token=cookies_string.split('tt_csrf_token=')[1].split(';')[0]
msToken=cookies_string.split('msToken=')[1].split(';')[0]

#login
login=requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={token}').json()
if 'success' in login:
    user=login['data']['user']
    coin=login['data']['xu']
    coindie=login['data']['xudie']
    print(f'{lightblue}ACCOUNT  {red}</> {trang}{user} \n{lightblue}COIN NOW {red}</> {trang}{coin}\n{lightblue}COIN DIE {red}</> {trang}{coindie} ')
    print(f'{luc}[======================================]')

else:
    print(f'{red}TOKEN KHONG HOP LE!')
    print(f'{luc}[======================================]')

#job
while True:
    for lap in range(1,11):
        job=requests.get(f'https://traodoisub.com/api/?fields=tiktok_like&access_token={token}').json()
        try:
            id = job['data'][0]['id']
            link = job['data'][0]['link']
            idjob=id.split('_')[0]
        except:
            print(f'{red}[{hong}{str(lap)}{red}] Hết job hay sao ấy :(')
            sleep(3)
            continue

        headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ttp=28unjjBFv07SKsZIPVib48W7OmI; passport_csrf_token=2972d1101b290fbc2f28b7c2bc4f791b; passport_csrf_token_default=2972d1101b290fbc2f28b7c2bc4f791b; sid_guard=53e5f5dfb52b3f03e816859efc1cf0a0%7C1659061038%7C5184000%7CTue%2C+27-Sep-2022+02%3A17%3A18+GMT; uid_tt=4c914a7a0eb7e4d75798060fe4b8dec1fb1e4aa089eaa5ce570e8027113046dc; uid_tt_ss=4c914a7a0eb7e4d75798060fe4b8dec1fb1e4aa089eaa5ce570e8027113046dc; sid_tt=53e5f5dfb52b3f03e816859efc1cf0a0; sessionid=53e5f5dfb52b3f03e816859efc1cf0a0; sessionid_ss=53e5f5dfb52b3f03e816859efc1cf0a0; sid_ucp_v1=1.0.0-KDhmMmIwYjI2MWU5NjU2ZGNjYmRjOGRjMTUwOGI3NThkOGZjOTM3NWYKIAiCiKG6xIv9sF4QroaNlwYYswsgDDCP6ofzBTgHQPQHEAMaBm1hbGl2YSIgNTNlNWY1ZGZiNTJiM2YwM2U4MTY4NTllZmMxY2YwYTA; ssid_ucp_v1=1.0.0-KDhmMmIwYjI2MWU5NjU2ZGNjYmRjOGRjMTUwOGI3NThkOGZjOTM3NWYKIAiCiKG6xIv9sF4QroaNlwYYswsgDDCP6ofzBTgHQPQHEAMaBm1hbGl2YSIgNTNlNWY1ZGZiNTJiM2YwM2U4MTY4NTllZmMxY2YwYTA; store-idc=useast2a; store-country-code=vn; tt-target-idc=alisg; tt_csrf_token=m9kN5aXF-qvvFlHvQuqjVfjFsMP4cyUcBIhc; bm_sz=48A133F8C9A83A361D8C24DFD8B74B74~YAAQ3FFNGwSf9TeCAQAA3q6aUhAGc6z+qnoNRvCzc53XdD3BbPqBq14TWaKK3n6W3DCF7OskUl3U0GSqW8UF6fE7nRrUkMJY6UF4D5xEFN4dpr9+b6yatL8DGeOgmFROY8GzOHAzoqPfM0TGExcvuJ7SB07fd3R9OoC8zvnNXzh4UHYd030NQVjl5PrjVCxQQEOB3DO/dew75uZ2HW1m1Q6ReTBkxbQF7kVOmPAP0UDOUjY1+zj984GMytirBj6/LsynbS/46w26ePD6pTe6es/YQtTnQxv/6CJujGLS2/ujG0Y=~3749681~3359558; ak_bmsc=718DC0CC3004C86F0B269F98BC488A4C~000000000000000000000000000000~YAAQ3FFNGy6f9TeCAQAADdCaUhC7qAPs+aERHlq3jH1snhhRm90ibFSVHUYfRHUwPQMbgyVwbv1fb5jsbpBzewkRNvPnur3eczrJmTYcnMx/7pQRXfvAtjFVFt/PecY+GiBXJuGFD1bflkOaQ9sfZPQYLXceFqx5HDedSas+QyyRq+HfEQZKzbfvXEzHtZgyqkIZKfScML7vTjH45w4FYnVLcUk6EtkRCHwKBnSbCWuNH9Kq3yE1mh2SL6Xn+3Mc222bqYxTi7hcmWRrOE937Nciqqnd+cAohUAb/w+Fd09Q82vde4otso9fYGUwHx5zyo+E4Fb4TAzp5aoYgSHV3jVCkRs5YbNqGV9FQSqfrqCCWq9pn429HROUhssWp3UaaHZ5TenhKlOaTD8=; csrf_session_id=6b5c4804f1c96c4e1aa76445c4e8d57f; s_v_web_id=verify_l68un37o_QsavupWk_Yc16_4RaY_8r7E_XXo8GVv1dO4p; _abck=CCD3B98955E0DD57450FF4E0F3AD1EF5~-1~YAAQ3lFNG+BASh6CAQAA+cqcUgjgFupoF8l8JynmwHQNW8Vrp92NI7Z5AG4wv2PtlalDf6m3z5UtaS67Pd26Z6F7qU4d4Fd6+zPICzQlI22MtXiUtBexoGyYapPeud+1uRgLdaP9BrcgK11UHuS+mvjbBsJdtIjJXuxpVX9OzTB5cv16kE1jenLy8Bj5Mz55Q+yf2ZRkfmhwBhSthin9tB3I9NrrMu2DVkWsLCjF/aRTqGa4HjdjlgQg7IItfHGezEQOyruVw/uoRCrMYeOQygQFgAKhVc1qvzYPz+ehgwxc+BqIfhUH258y5MPHEV/IwfoUflJx3LZBcb3PSY1RxB+Y2N+NacJFKv2uwk/ZjAGLCH8l7iVxnoJ/1XZoAETd4Fs9hiSLEmhDQg==~-1~-1~-1; cmpl_token=AgQQAPOFF-RMpY5fGvvPep07-LAemTFW_4MOYMZvXg; odin_tt=79a32f76972b171e68f3ccb5d484410b9042e97c82b31f4d1873bc749d4dc07dedb468b248c2acdc5391739987a2c9247667bf60d904fa9161f8a9bfb8641f1064c115710340f8930f25105993184c41; ttwid=1%7CUTcPouf-Z-DlWKY6uOwbu3o0yJrUuFPDKgppkXSSGkg%7C1659244308%7Cfa45dcf5e8861c71b554b86bfdb96ed4498f694673ab07492d6d2bc0407d9f8c; bm_sv=95A35865AD734BF8F9D08D1BB8A0E62F~YAAQz1FNG53mIR+CAQAAbA+rUhCTbehhydI2+csCd6KcTOVgZqcHhawNpXF+TVUhqfHJzOvH2N17GGh90RpNPfGbmh2JoRPgAviGXm6MAIhpzB1mT5p7PRzcMEbKj6KTbadYwrkPJeWQktnYcmIm4NlWXROORNgxRwitDZcvjHjNMZmFNB2lxaxPsNFxcA5XzODU22j7EHlVuIHO5bA4LovcFJIG2oPns3rDjPqkA5QC4rLSK3cy0bqcj9vz3RqVgg==~1; msToken=ZMf4yytKZiEOmfu1K7XmRnOptacBsNe-hNXTptMRXLUJH8xc5dp6JH_HS9W0FHBX9hkdtvaMT5a_39OOEb_dFfEh86PsIekUh_ZKWiVQQCrkD45mB51F-wf7B7kvNsrx-7oKX6DC',
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        #'content-type': 'application/x-www-form-urlencoded',
        #'hTc6j8Njvn-a': 'hj6eYy9=HXe1kVL12xC9A5Ce2qwmwsJPYIpRSZcnHYlqoV=_D3YZmNKrkHzGK1PcFpoMaOo-LorHzXH9yInV2kIkdxDxMdQ-7cS7RFRKCMjPIP=rm9sF8loO3my1ImsmGI9kznX6c5f11txgCpPn93nLRiwTZEkYD2_gRmITL51qY1s=ZOqe93o79631j8kAFChyBeNQTdHeJAZA6CgnGbNqWsrlFUiiKU9OnQ=mwQwT5KZXLL08G3tExre=Q3G6JKKL3JqFw=eG-2DLjUcHYlwDry7cxbLfvEhFtrcyEWtmdwxjcKSBXBudoiGyIZJXaYrDqtos6CsJlagdIHa5TpWi=EHHPCbSC99C1h0oJa7Ud=rj-XuiWGkFkMKOQl00KujulBO6NvBDrnZt_K-E3A30pav_k-PBmhQ5Wh-kf7P=wLEn50xcJ0PjhhQFBoVerNfJzcGY1DOM61gCYzwrUGDAGBgaMBd_o9iedy-RohOXXCCSEEAS7pWE9elOrOXbBd8GFxQ9-e_ZiBoNk1HSw=GGsw11VxDrINtN3TUqSq5Rq=SrAko1QNH6ujcjCt0wKJEtHDkcPLH3lfcXv9w3zT9fYNcky2JSe29mUaiUbvS9kbKzCdG7VCJemnovdoKuzqrvWGj-Mg2neIQMbLBbkgnTbUtaKDfTQhE3EJDHnc5mgxuNE8V5RcksxO7k5tV1WYd=pXR73AELs87TRCZlqTCwlXh3I6mhv=IjLMAw=5YIKYix1QRUcv0Jdzx70F9r8i-cvP372yiKwryEhV9w9CyAzuVLfU8fQ1oLNERVxHevDM5of=P9BfX_KylilmbX6CHQxrzk3fp5W0uLiX_gCsXDc8ZmR30N9E3g97UwfA5xrsUjYG6GPh2_odMT67ALzDlRct6lg77yxeZ7XhJhR9Zh8iEEAFE_S9DvaA3gMfYCwGSXDZJcrUW7hSQTv3yCYw95aZ818YylwZvbeHm7fXXlddLr__tJAgM7c5YIWVUBF079C-VpHYZMuq-H=fRsBg7o5AbaFUdTNGKkeXNOt7Q-=Kx6UT-6mlIUW6saoEs9grnH3FzkD7QRINycfvgJRmQWIDKsOAl=VetKpNdMoqzfzwTTM_DQxaVbluYJMzYX1MYMGgSmd-GaG0TEsa2MFZfEv_J28pip2XGExuCNATddyt=AncLJuLiPT8_IeW_BKe5b5gjeBvNu7JkShmbARvqMaNE8cgulMhNg0zCDAkP5DPLMNUr7CcDhvLOKIosj6cxv6sB8OHpp5KYpBeBYzwTRRMtSGDZIQMzbomfHTWLivscWQpZRv-rZtpoX5hJIhtgh7OX-RuQ2QlhK6JYhHuUtoNz_Q3HrePTuviJwwEag2JuMPBj9WTfinfWQjB_XZZ_VlpgULbAyeACcYmkahlvK-FuowpGmQUBF_Go-tOXMalED=gx8AciOSM=M_cSGdIy7zjNuqM12eYmSWMRzef_God6ir7hhWXArBTnvnsRtn5lwn7HfAC=DpyL9PPUevDDSgC=VQbu02EhhHQaAgWJJsXatINEAF3Y0NQvjy6hmR_ejm5Vb5GinEwDQObmja691y9QQ5Mjfbj8G3KfHOHzoynKjExA_q15mgF5UN1B6UuS1pfBg_g_mrtx5COe_UumOqFuqRNKkB81DA5Cqca080Dydf8kWW2pvFUvxWFTP8dsBau_ydKDiDEwjOxIj8FgcHbzv0ySz_v9O3pST6rFJ9sqk1JK8ZUZ91IMEjcUp2TD3vFoUIIyX06sKu_B6v5__9FFAK68HAfDPfxcaCmjGafmk1Ljc_MMPgjnydDWTZENyooZvhfLA7I5t_n0_-LIEZRiDvLCXrcINMOPXfISW6lmdZMn-FZUgrAC8MaVe5fQUH5en8KHCtyNq1f3YDPs393oA-7ZTds1Mbtpy_0=arkRU9jBfW2fGqwsVfKR2=enpJHHh5uICHUKEf2CUqpVKLaPxQLW3h_7=lPGtqrXQKoAE6WBDFJNvdg6e_p2KzJrJtsD=dpRZqi6wasoIBoCwm89DZr0Z55KSYApR9CfAO8fxNitiIuXRL2jzR6OviMR9r7-GBJ0LpYAuoRhxBl=hcaG9AuYZNygMnnrZnmL3eUaxIiiEjbDf5Eli5ObWUUeKDGSuRssncdtD5BnlKwQNqofm_2JVPHrQteHQ0MThc3Ro9RXUvttkFkOdTvPP83uoG_E7uxbf1CyetxRhWHAy8F=hJ-nj_sTTwYOP6RkthyycS70gOaPBbcEoQ85nz5YNcZixG0PeUhN-b3XInYTcndr3uWHU2OpFTD0TyA0XQQN8AI=5t7JUw6ZLewg5WIGn6UkWRfJwsjNPevJUJmZj=BCZ6kq96l63KLjBulC9Z3lv-seoTHuW5ie0GNgxNuSkp3a2v7CV=1DnXVY3v3V8aVub8LFgs0I2LHLqxa2ihUw1XNIEx6wFUVDoGi6UjQl-E9b_lD-1B_Th-KwE5ADziTQevstYGnHaOg3kqvZj_5KhPfr2IV=PpwE_Pr8wsY-1tpbDkD0GIQB9OvmstnBc21ozaIJ5_WeFqZQWKmLUypOwkR=nRJTCc0sTgV2PbbOtzdLzQyTkQ1MAhh1tH2ggKjTg0pzggw9-vLFPH0vpDPQpY-HlRq92AveEZ9wKWpNpVzOKtTXd0ycCISuGnamXJOfJQy6uy2mCVVCKt-1M9-yIibWgo50kE61-OaoyTVOAfzNO5tPzvvmcT9psD_pp-F9woPItcxrfuXgPifTvTka1RmTStXAO0lydLu5T8g-6ABPRADns3HqMThUp9GLEs6W-bZgDIaPaDOmllJqAzq6RlWiEJ7n7zWLzZO7NdkhLiv_6EcSwoZs51ns2g8F51k_SiCj7jRKn8scpsRYVVhpj_d6SgJ67R_rkFjvVsIH8YOHcGRxLTspEdvLJEQdSlC_OSB32LY0dhfuk6=JJz0-S9FZm2KhNS9KEC_9V3USMjuEiwVT6_KfaIb8FMlSySrlMYqMZcxXl9XKCS2=JiSZYOH8BPTcECGAYKASZZLqPm330tnOqZHLP_wopz_R0lCdXjYN1mO8oGI3GedSgppXnx3lgCpnIJW0n3AOLLqdTvDHIlIx=xyEkQbjqzu5MiySLArMTWDoyfGunU-Bq2diP11TV79nekGiewKixoMagk_NNAdplT3Ix=k3sHw0ZARduhcgD2x_rkvDlW=5mZCZvVLObUeSFirf12WTxEZTsIl=x0arKUPrcEzYAc-GSKnB-t1vxNo-z85gL=v0co7a9Hbou0YEjrLyNptmDHF0SBGEeDRxAszduXWwx5fTGVIfwpMF8KEkKYifIn_81tCjGQM097EDQAPcY6x=8=7eQ2HuZd=KvpZOT1yzVROfplriZW533RJYPlVf6oNxvAJdk2SU=93qzWY9HKkhCe=-E9suoC5MXhYGIk8RIVkf1QrMBmQA_N5Fhi_-bHBA6X6ar6HQcppB3-PmDVQVMfX28SuNOmf2V6KhNVOJSLbGKHlDIeIbT_wUUcFtIzRajU7zAnLmIrCOAlLPD1OrG8XlU0Of26cmqcBludcGlEuxpNh7hx-ZuYT9Vlk7jqRNYYfFwFk_Lk-__FzeeOZREfXLpkgzQjd136BA7ejeaurk0wyMeQ6q_ppYFu5MtEbj60ueRioAgBw5OCV5-W=xZxJMlN9BmTCScKNEosDzMo6cluqsRsw6AO1UCYuMS2UtLrsRyJBTCrXTYx0tzghPZNctRJ=l=eDVxPz2GI5Z-EGx0pjCkXezHjC_r1hMFE0GJ163smC2VHNnl2i=y12gY3yy7ajoU-z9vF-VZP1osLJSuE6n9UqMOU1Iarfdioco5V6RSKf0OjJx=fJ-Sed8tjulSTv5duwZcj9E1a2nalKlLKnk2TDBy0pCkXQZOM2LZWu-yXtXYJrV-xg8pcTo7-QT928ATH86FnoTFvn7TfXIZADjTdExopWB0qzU=ptRMeXPpfIeaDXkAKhV1ebQM78vepCmsElIRcSAxmdrxH5s2Z_AFNIC=It57NRDXD=y2CTB3lGVP1AUkRnI2cGgmGzRB3dG76ijHQRwtvteRGep22jCnaTlI7WV1tixR5FZQRJkpLyzbTYM5NypfK1P3PVQzhXUaSHTKfEciKWPtvQbAh3LbEcnbgrQXYJuVDrNVXcLEZfGfSIJUB=6TcKx-WHjiPHFhctpxYp07ZeSeamGv1Q=ZM7PJZMK6GDc5DAZAraR=Fr_FQoBR1zWnw=UMWnzznCnxQKkQF--Xre31jAtyeMLcNnS7l2pQqLOESIn7fLGahp=VuX1N7j=CkShpHmYubmcKsyYSc2MNR2s_7-7PSCKc5E3Owk06=bWIYpw8to3V0kiBCw_cLwO3fBHFvyeEoTGuDcG=TJyCORylKfh155qFNldg37ptc=orW5qpUSJnRj_uFYI2FoIOdRSvYx9oHDZFt_tMt7MWPH5WOBWYhX_1Uhf_Kph6fljBGsPtJ-SUKQoO=WFglfoWzwabfEpDaPk=butoHWwVvr3CQkHo=LPdg2GzVhligY90aYKElqWtvHXJL6NApzEhUeZLetZ0REyA23k-hJmuoI5rsOPgZq6XikpeNRbs2jXDTM_l6MOAGHgy-ZH1yCxbkt=5FIGugeUd2GIbTKxOKawa6OqM0oSP2oq8R2FOR1jNhAh6wUsp6EI-KIOmQXD6DS_Ob58pk9-enCKCmMmuS5sQSN2-p2NzYFzq3iD=RtUlEmLcdSEaqqyuF96yGNU3RDJSUH2s0GCKbQWgBC=Tq800gC=8Kt=cYT5czPxrvkGCQSuFRmHEXH=QAxnrYOT_HRo2pjYE8E83QprQvMwaXul6wLwNvpHhS6enAJc8pzVE1umATC6wkSIqLF9ygXVC8rqmxenNnU_ctCQSIcvN6uELPD8BrmDBRFD_zBtDrdYfh0I7Fxkfubc1Fi_K63lZMRsw17WWdTlaoZp_Gj9-psk9yfShyLPdJeSgvHGr91yU2J3C5OGOqQ2Cw13_Op1MORCazQS5Ql63fYLpVx7=3InZmwmpqX03EIstc-7ddy8KCj_RIaIPlLmgewaPuyud9Ebid7R16prQ1QnkecdgFyZhOzfKhClAhNphpwk=u1rwRjd2usBreT_to5_-Z3w26esh=jrG9tx1bHfjDzMNEnBGp36GEIm3l5IFWIqQRbj0je6ZRwXJdkOISN9hfwTBZ0USb97qupT-gG0Ref9zg6rJB_Ruzp_jn9jtid2h0kqJ09jisciNSqBDzq-lz_NmCWTIJPjvhOk0xHgx7UrbuPX_pUbuiqq8P_8EdozvHZe5zJUt6aJjVAA20fE5COGRLMnTHhrQNnUBSlSVeOxOxB9fuH_PADHGOBOqNqrodkieik7i7QNmNLrc0reDfieX3W-w7CLYZLaYPpZXqRXWHDHIqf_WYuz2xSyFqkw-950in56RGbS9-w5QzNS=jaCYWgUktBOyZW6Red=XmrhVv7DEep0x3hxJXK26pmhBdloBVdhpUQi9-QAl=w=lsZUr3MkV=sGTIMdZPAZqQyuZADmlyvZM2FseL752XrGaNoKxBcQQBpbnott-CADD1EyoKGUleVXEw2mUWLf_h71DJcZkU8Kt5aWzz5lbnFSSTv1OpiYlK7sCwRnV5FrNgBRFvOe7symQYy0jxgPOBw2jNL7iJKazrc7ClgwCQOYpsdsd9jJZ9ydEDNEeN0_ssNkqRwMxWnLmKMgtwJw=kJxfTl3zrkj6U3YzopbmqHZELhiAMsnG30zy691Bf2tGY7oBrTAjN9wx-JoR1BNwlBs6qetK1=e05SWrgyFDu=DV6z5G=xEAZmDtkvG5zrGH-DEzJVDTtyRzrLORnoUOuL92mRSrolvYo=IEnq2lcqZwFZcoCPSF7ucqEQi8T8-azzjxBIwre5TeTLUuS5pt6BvXZwTXR-v53IcGdQKtDPrJnOI0T0tV9o6q-SdnqEF_E3zvr9DVJg37JYz_wsfuaSCxRASLUO3mH6iY',
        #'hTc6j8Njvn-b': '-covdp4',
        #'hTc6j8Njvn-c': 'AIAYoFKCAQAAZFLt43lcomqXq2UaWsCGxBylGXkS1W-74X9MJsHa2ndH5FdB',
        #'hTc6j8Njvn-d': 'ABaChIjBTKGNgUGAQZIQhISi0eIApJmhDgDB2tp3R-RXQQAAAABuAWLeAIrswFWW9kAXnRFSeg4yLsM',
        #'hTc6j8Njvn-f': 'A7neqlKCAQAAoOuVmRVUytpjBCOH1regtYZSORM9QtdcjS2rHcaz7yE4dZ0PAXRha82uci7ywH8AAEB3AAAAAA==',
        #'hTc6j8Njvn-z': 'q',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'tt-csrf-token': tt_csrf_token,
        }

        params = {
            'aid': '1988',
            'app_language': 'vi-VN',
            'app_name': 'tiktok_web',
            'aweme_id': idjob,
            'battery_info': '1',
            'browser_language': 'vi',
            'browser_name': 'Mozilla',
            'browser_online': 'true',
            'browser_platform': 'Win32',
            'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'channel': 'tiktok_web',
            'cookie_enabled': 'true',
            #'device_id': '7125735046828395777',
            'device_platform': 'web_pc',
            'focus_state': 'true',
            'from_page': 'video',
            'history_len': '4',
            'is_fullscreen': 'false',
            'is_page_visible': 'true',
            'os': 'windows',
            'priority_region': 'VN',
            'referer': '',
            'region': 'VN',
            'screen_height': '768',
            'screen_width': '1366',
            'type': '1',
            'tz_name': 'Asia/Saigon',
            #'verifyFp': 'verify_l68un37o_QsavupWk_Yc16_4RaY_8r7E_XXo8GVv1dO4p',
            'webcast_language': 'vi-VN',
            'msToken': msToken,
            #'X-Bogus': 'DFSzswVYs9hANjulSXBB1QYklT6T',
            #'_signature': '_02B4Z6wo00001DSF93QAAIDB6vOv0n4OM.A0hfPAAG.Oc3',
        }

        response = requests.post('https://t.tiktok.com/api/commit/item/digg/', params=params, cookies=cookies, headers=headers)
        print(f'{red}[{hong}{str(lap)}{red}] {red}</> {lightblue}LIKE {red}</> {trang}{idjob}')
        sleep(4)
        duyet=requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id={id}&access_token={token}').json()
        sleep(4)
    get=requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token={token}').json()
    if 'success' in get:
        xu=get['data']['xu']
        msg=get['data']['msg']
        print(f'{lightblue}LIKE SUCCESS {red}</> {trang}{msg} {red}</> {lightblue}COIN NOW </> {trang}{xu}')
    else:
        print(get,end='\r')
    print(f'{luc}[======================================]')
    sleep(7)



