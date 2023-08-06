# Naro-Laser

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

setup.py, setup.cfg 방식을 혼합 사용한다.

# 개발 절차

## 빌드

```
python3 -m pip install --upgrade build
python3 -m build
```

## 업로드

```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

## 배치

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps packaging-tutorial-nash
```

