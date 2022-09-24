# Anaconda, Jupyter lab/notebook in Win
---

## 0. 콘다 사용을 시작할 때 좋은 습관
https://www.activestate.com/resources/quick-reads/how-to-manage-python-dependencies-with-conda/
Anaconda prompt (anaconda3) 를 실행시킨다.
- 업데이트
```bash
(base) C:\User\[user]\conda update -n base conda # 종종
(base) C:\User\[user]\conda update anaconda # 아주 가끔
``` 

## 1. 가상환경

### 1.1 보통 64-bit(x64) 환경으로 설치를 하게 된다.
Anaconda prompt (anaconda3) 를 실행시키다.
`conda env list`로 가상환경목록 확인
```bash
(base) C:\User\[user]\conda env list
```
1) 원하는 파이썬 버전(python=3.7)과 가상환경 이름(testvn)이 정해지면, 가상환경을 만든다.
```bash
(base) C:\User\[user]\conda create -n testvn python=3.7
```
2) 가상환경을 lab에서 사용하기 위해 가상환경으로 진입하여 `pip`을 최신버전으로 업그레이드 한 후, `ipykernel` 패키지를 설치하고, '테스트가상환경'이란 이름으로 lab의 kernela목록에 표시되도록 한다. (lab에서 디폴트로 `Python [cond env:testvn]`라는 이름이 주어지는데, `kernelspec`을 사용하여 다르게 지정할 수 있다.)
```bash
(base) C:\User\[user]\conda activate testvn
(testvn) C:\User\[user]\conda install ipykernel
(testvn) C:\User\[user]\python -m ipykernel install --user --name testvn --display-name 테스트가상환경
```
3) 가상환경을 빠져나와 lab을 실행시켜 가상환경 커널을 연결한다.
```bash
(testvn) C:\User\[user]\conda deactivate
(base) C:\User\[user]\jupyter lab
```
4) 가상환경내에 설치된 패키지 리스트를 파일로 보관하려면,
```bash
(testvn) C:\User\[user]\conda list -e > requirements.txt
```
또는 platform independent한 방법으로 install 히스토리만을 파일로 보관할 수 있다.  
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
```bash
(testvn) C:\User\[user]\conda env export --from-history > environment.yml
```
5) 반대로 `requirements.txt`파일, 혹은 `environment.yml`파일로 가상환경을 설치하려면
```bash
(base) C:\User\[user]\conda install -n <venv_name> requirements.txt
(base) C:\User\[user]\conda env create -n <venv_name> --file environment.yml
```
5) 삭제를 원하면 `(base)`콘다환경으로 빠져나온 다음, 'kernelspec' 목록 확인 후 삭제할 kernelspec 엔트리를 찾아 삭제하고, 콘다가상환경을 삭제한다.
```bash
(base) C:\User\[user]\conda env remove --name=testvn
(base) C:\User\[user]\jupyter kernelspec list
(base) C:\User\[user]\jupyter kernelspec uninstall testvn
```

### 1.2 32-bit(x86) 환경으로 파이썬 코딩하기 위한 가상환경구축
```bash
(base) C:\User\[user]\conda create -n <venv_name>
(base) C:\User\[user]\conda activate <venv_name>
(venv_name) C:\User\[user]\conda config --env --set subdir win-32
(venv_name) C:\User\[user]\conda install python=3.7
```

### 1.3 tensorflow/keras를 이용하기 위한 conda 가상환경구축
- conda 가상환경 위에 tensorflow를 인스톨하는 것이 아니라
- 설명서대로 텐서플로가상환경을 바로 구축한다.
- https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/
- To install the current release of CPU-only TensorFlow
```bash
(base) C:\User\[user]\conda create -n tf tensorflow
```
---
### 미분류 팁
- pip 업그레이드
```bash
(testvn) C:\User\[user]\python -m pip install --upgrade pip
```
- conda info
- platform
```bash
(testvn) C:\User\[user]\python
```
```python
>> import platform
>> print(platform.architecture())
('32bit', 'WindowsPE')
```
