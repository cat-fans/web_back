from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from SaaS.local_settings import *

secret_id = TENCENT_MY_COS_ID
secret_key = TENCENT_MY_COS_KEY
region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.upload_file(
    Bucket='wangyang-1251317460',
    LocalFilePath='code.png',  # 本地文件的路径
    Key='p1.png'  # 上传到桶之后的文件名
)
print(response['ETag'])
