from setuptools import setup,find_packages
setup(
    name="ccsdsg",
    version="0.1",
    author="陈晨，杨病，冯经兴",
    #author_email='ccsdsg2016@gmail.com',
    #url="123.om",
    packages = find_packages("cc"), # 模块的保存目录
    package_dir = {"":"cc"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
    "":[".txt",".info","*.properties",".py"],
    "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)
