import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "update_dict",
        version = "1.0.3",
        author = "yutu-75",
        author_email = "xiao3952@foxmail.com",
        description = "Is a method of updating nested dictionaries",	#介绍
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/yutu-75/update_dict.git",#如果自己写的，在GitHub有就写GitHub地址，或者其他地址，没有就写pypi自己的url地址
        packages = setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
            ],#这个文件适用的python版本，安全等等，我这里只写入了版本
        )
