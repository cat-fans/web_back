from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from SaaS.local_settings import *

secret_id = TENCENT_MY_COS_ID
secret_key = TENCENT_MY_COS_KEY

region = 'ap-chengdu'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)

client = CosS3Client(config)

response = client.create_bucket(
    Bucket='test-1251317460',
    ACL="public-read"  #  private  /  public-read / public-read-write
)