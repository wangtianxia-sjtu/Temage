import os
# 生成文件当前所在目录的绝对路径
BASE_DIRS = os.path.dirname(__file__)

# 参数
options = {
    "port": 8000
}


# 配置
settings = {
    # 修改代码后自动重启服务
	
    "static_path": os.path.join(BASE_DIRS, 'static'),
	"model_path": os.path.join(BASE_DIRS, 'model'),
    "template_path": os.path.join(BASE_DIRS, 'templates'),
	"db":{
		'dbname':'temage',
		'user':'root',
		'password':'',
		'host':'127.0.0.1',
		'port':'3306',
	},
    # （不）进入调试模式（默认False）
    "debug": True
}