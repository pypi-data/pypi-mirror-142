# dictbox

#### 介绍
{**以下是 Gitee 平台说明，您可以替换此简介**
Gitee 是 OSCHINA 推出的基于 Git 的代码托管平台（同时支持 SVN）。专为开发者提供稳定、高效、安全的云端软件开发协作平台
无论是个人、团队、或是企业，都能够用 Gitee 实现代码托管、项目管理、协作开发。企业项目请看 [https://gitee.com/enterprises](https://gitee.com/enterprises)}

#### 软件架构
软件架构说明


#### 安装教程

1.  pip安装
```shell script
pip install dictbox
```
2.  pip安装（使用阿里镜像加速）
```shell script
pip install dictbox -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1.  demo
```python
import dictbox
test_dict = {
    'aaa': 'aaa',
    'bbb': 'bbb',
    'ccc': {
        'aa': 'aa'
    }
}
test_res = dictbox.dict_tiler(test_dict)
```
