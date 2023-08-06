from setuptools import setup,find_packages
setup(
    name="ylq-rich",
    version="0.1",
    author="ylq",
    packages = find_packages("src"), # 模块的保存目录
    package_dir = {"":"src"}, # 告诉 setuptools 包都在 ckh 下
    package_data = {
        "":[".txt",".info","*.properties",".py"],
        "":["data/*.*"],
    },
    exclude = ["*.test","*.test.*","test.*","test"]
)