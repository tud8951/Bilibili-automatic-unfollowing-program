import requests
import json

# B站API相关URL
FOLLOWING_LIST_URL = "https://api.bilibili.com/x/relation/followings"
UNFOLLOW_URL = "https://api.bilibili.com/x/relation/modify"

# 登录信息（需要替换为你的实际Cookies）
HEADERS = {
    "Cookie": "SESSDATA=your_sessdata_here; bili_jct=your_bili_jct_here",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://space.bilibili.com/"
}

def get_following_list(mid, pn=1):
    """
    获取关注列表
    :param mid: 用户ID
    :param pn: 页码
    :return: 关注列表
    """
    params = {
        "vmid": mid,
        "pn": pn,
        "ps": 50,  # 每页数量
        "order": "desc",
        "jsonp": "jsonp"
    }
    response = requests.get(FOLLOWING_LIST_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == 0:
            return data["data"]["list"]
    return []

def unfollow_user(target_id):
    """
    取消关注某个用户
    :param target_id: 要取消关注的用户ID
    :return: 是否成功
    """
    payload = {
        "fid": target_id,
        "act": 2,  # 2表示取消关注
        "re_src": 11,
        "csrf": HEADERS["Cookie"].split("bili_jct=")[1].split(";")[0]
    }
    response = requests.post(UNFOLLOW_URL, headers=HEADERS, data=payload)
    if response.status_code == 200:
        result = response.json()
        if result["code"] == 0:
            print(f"成功取消关注互关用户: {target_id}")
            return True
        else:
            print(f"取消关注失败: {result['message']}")
    return False

def auto_unfollow_mutual(mid):
    """
    自动取消关注所有互关用户
    :param mid: 当前用户的ID
    """
    page = 1
    while True:
        following_list = get_following_list(mid, pn=page)
        if not following_list:
            print("已处理完所有关注列表")
            break
        for user in following_list:
            # 判断是否为互关用户（attribute == 6 表示互关）
            if user["attribute"] == 6:
                unfollow_user(user["mid"])
        page += 1

if __name__ == "__main__":
    # 替换为你的B站UID
    YOUR_MID = "your_mid_here"
    auto_unfollow_mutual(YOUR_MID)