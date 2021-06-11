import requests

cookies = {
            "_uab_collina":"162332710068890400102634",
            "abtest_env": "product",
            "zsxq_access_token": "B34E98AA-C92C-0487-1402-5E0C6A6E7E1B_178B61428B09DA67",
        }
headers = {
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "abtest_env=product; zsxq_access_token=B34E98AA-C92C-0487-1402-5E0C6A6E7E1B_178B61428B09DA67",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.3"
        }
group_id = "815118881285512"
base_url = f"https://api.zsxq.com/v2/topics/{group_id}/solutions"
params = {"count": "20", "direction": "backward"}
response = requests.get(url=base_url, headers=headers, verify=False, params=params)
print(response.json())