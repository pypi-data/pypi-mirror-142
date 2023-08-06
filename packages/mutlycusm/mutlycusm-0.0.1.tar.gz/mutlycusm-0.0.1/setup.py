import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="mutlycusm", # Replace with your own username  #自定义封装模块名与文件夹名相同
    version="0.0.1", #版本号，下次修改后再提交的话只需要修改当前的版本号就可以了
    author="雒国林", #作者
    author_email="1348102133@qq.com", #邮箱
    description="调用此方法可打印9*9乘法表", #描述
    long_description='调用此方法可以打印9*9乘法表', #描述
    long_description_content_type="text/markdown", #markdown
    #url="https://github.com/tanxinyue/multable", #github地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", #License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  #支持python版本
)
