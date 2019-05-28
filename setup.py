from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="aa",  # 这里是pip项目发布的名称
    version="0.0.1",  # 版本号，数值大的会优先被pip
    keywords=("pip", "SICA", "featureextraction"),
    description="An feature extraction algorithm",
    long_description="An feature extraction algorithm, improve the FastICA",
    license="MIT Licence",
    
    url="https://github.com/congrenya/aa.git",  # 项目相关文件地址，一般是github
    author="Stephen Yao",
    author_email="a1123547734@163.com",
    
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["numpy"]  # 这个项目需要的第三方库
)
