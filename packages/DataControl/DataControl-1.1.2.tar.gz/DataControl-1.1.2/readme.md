# README

- 文档

https://packaging.python.org/en/latest/tutorials/packaging-projects/



- 编译

```shell
python3 -m build
```



- 上传到测试PyPi源

```shell
python3 -m twine upload --repository testpypi dist/*
```



- 上传到PyPi源

```shell
python3 -m twine upload --repository pypi dist/*
```

