from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from SaaS.local_settings import *

secret_id = TENCENT_MY_COS_ID
secret_key = TENCENT_MY_COS_KEY
region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

# client.delete_object(
#     Bucket='wangyang-1251317460',
#     Key='p1.png'
# )


objects = {
    "Quiet": "true",
    "Object": [
        {
            "Key": "day2牛存果.py"
        },
        {
            "Key": "小米CC9e.jpg"
        }
    ]
}

client.delete_objects(
    Bucket='wangyang-1251317460',
    Delete=objects
)
