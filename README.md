# Bilibili自动取关程序

本程序由B站Up主[BigJackson](https://www.runoob.com](https://space.bilibili.com/1549550569?spm_id_from=333.337.0.0) 制作并开源

以下是一个基于Python的简单B站自动取关工具的实现思路。需要注意的是，此代码仅用于学习和研究目的，请确保遵守哔哩哔哩（B站）的相关用户协议和法律法规。

程序1是自动取消关注的人

实现步骤：
登录账号：通过B站API或模拟登录获取用户的Cookies。
获取关注列表：调用B站API获取当前账号的关注列表。
取消关注：对指定用户执行取消关注操作。

注意事项：
Cookies获取：
SESSDATA 和 bili_jct 是登录后生成的必要参数，可以通过浏览器开发者工具在网络请求中找到。
替换代码中的 your_sessdata_here 和 your_bili_jct_here。
用户ID（mid）：
替换代码中的 your_mid_here 为你自己的B站UID。
API限制：
B站API有频率限制，请根据实际情况调整请求间隔或增加重试机制。
合法性：
使用本工具时，请确保符合B站的服务条款，不要滥用自动化工具进行恶意行为。

程序2是取消关注互粉的人

要实现自动取关互关用户的功能，我们需要对代码进行一些调整。具体来说：

获取互关用户列表：在 B站 API 中，互关用户的标识是 attribute 字段为 6 的用户。
修改取消关注逻辑：只对互关用户执行取消关注操作。

修改点说明：
互关用户判断：
在 get_following_list 返回的关注列表中，每个用户的 attribute 字段表示关系类型：
1：单向关注（你关注了对方）。
6：互相关注（你和对方互相关注）。
我们只需要对 attribute == 6 的用户执行取消关注操作。
函数调整：
新增 auto_unfollow_mutual 函数，专门用于取消互关用户。
日志输出：
在取消关注时，明确打印“成功取消关注互关用户”。

![BigJackson](/1.png)

本程序由B站Up主[BigJackson](https://www.runoob.com](https://space.bilibili.com/1549550569?spm_id_from=333.337.0.0) 制作并开源
