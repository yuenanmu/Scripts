import requests
# session=requests.session()
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0',
#     "referer":"https://passport.17k.com/login/"
# }
# data={
#     'loginName':'18779046135',
#     'password':'@okokok123'
# }


# def login():
#     url="https://passport.17k.com/ck/user/login"
#     response=session.post(url,data=data)#
#     print(response.status_code)
#     print(response.text)
#     if response.status_code==200:
#         print("登录成功")
#         # print(session.cookies.get_dict())

# if __name__ == '__main__':
#     login()
resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
    'Cookies':'GUID=318036e1-5cc4-4e1e-a153-fdb811baab43; Hm_lvt_9793f42b498361373512340937deb2a0=1771326191; HMACCOUNT=466D580D91007B06; Hm_lvt_8b0c0daea10097cb3fd25e6e89b69499=1771326191; _c_WBKFRo=2VSo2lCKK6gPciJot8nDuiXabJNtYQNg1uJHvJnc; _nb_ioWEgULi=; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22318036e1-5cc4-4e1e-a153-fdb811baab43%22%2C%22%24device_id%22%3A%2219b0410e05a3220-0d237ed6da00f28-4c657b58-2359296-19b0410e05b349b%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%7D%2C%22first_id%22%3A%22318036e1-5cc4-4e1e-a153-fdb811baab43%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1771328125; Hm_lpvt_8b0c0daea10097cb3fd25e6e89b69499=1771328125; acw_tc=276077da17713282329657932eb4aa45b7e31955e21ed87ca98bce59b49a37; ssxmod_itna=1-Yui=GIxjOG7GCtG0GG2WD2tYDQGOlDl4BtGR0DIqGQGcD8OD0PXBKPc0KGknklKDGuh1=lP_0wCDBLrhiDnqD8UDQeDv4gSDitgWAwThI=7tiywKgDLwovX3x/TgqNPWRgtT0N8LGVtt7LxtGYXUKYeDU4GnD06s4xbD4R3Dt4DIDAYDDxDWj4DLDYoDYbWoxGp=q6nTyjRbD0YDzqDgfAm=xi3DA4Dj9lDyB7udpDDBDGUON/aDG4GflmqD0wwLgYAQgDGW9mnPL6m3b9qbd8TDjqPD/fD9o/B9svqaocl_BFE3v1FDtqDjpdrcA3eqN23TooUPExAeY1YGe4MBwKDmYlxPCGwADKemxghUjqGADNlDb8wCmqrK_UBjaIKPe_=teORXVo0=riqK4otYpCGl7vUBx1jG0ADGCICebcnqiC6_7GmWG5lD=8n4GAqZDxD; ssxmod_itna2=1-Yui=GIxjOG7GCtG0GG2WD2tYDQGOlDl4BtGR0DIqGQGcD8OD0PXBKPc0KGknklKDGuh1=lP_0wiDG3nxPhlAMxGait=bwPSD0vL4qI4wuns1wKz0BRUlAD65RqQsD=0BIhuI/8N9OqvX2GxQiQdQyFqQHnhjK9b0KWTUK4uvMnhw4I3dK6xAxzAdGCupqDWtHWGt9inrXRkDKHLDfGxrWZiiBD8n6YDj4Anq5a1fXGwhXSRIllhfhHIq31gxoMRn00INPZ7NNS4n0Dgt7f=CAhxF=dCin9ucPiTFWq46cEvr7U5CuNcQPwH_RyDl9RIFFUw4STanx1W0tKP5S_4Cwcl41jA5Q5gGD8Yuybp5uccfnWbGX3E41nteg3oPh/9NI_c3DCWq2Dw1FqE3_1/_NSb=yWL4318ixscIeKf90a8ncRognAop379qfjeQHK7YeFOWHHI1UcRAwt1crymP1ulYEV3aaY51DLHQKgz95MRHoTAAdGDEkILIYmLnep34F1uztDBDq_mAdiLtxE=bMT1h1mQoo3kfk_A8yznQ=grybzGw=mqD=oHt7aDbAFPGCW6Fy3aekdb77k6mcy_nhz38Hn1lwsyRfKlFneQQEexwcz/Arom2kuz8nhIf5btAaq3ixnrtKwF/Y7l/qltBybUoNYDqSHVBcrHTCiFNp_PZTkx_NOINq=NhGceIVdVW3GYemIUMMBXjBrmAYEob0on5BGCG5lhCr8R48O46ir7DbixD'
})

print(resp.status_code)
print(resp.text)