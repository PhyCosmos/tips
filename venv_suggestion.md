# 1. `pyenv` vs. `conda env`
pyenv 의 경우는 python version을 기준으로 virtual environment를 설정할 수 있다.   
이와 다르게 conda 에서는 virtual environment 디렉토리 별로 python version을 설정해야 한다.

# 2. `pyenv` 관련 이웃 패키지인 virtualenv는 사용하지 말자.
https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe

# 3. `pyenv` 현명한 사용법
`pyenv-virtualenv`를 설치하지 말고. 다음을 차례로 실행하는 것이 나아 보인다. 같은 venv 모듈을 사용하기 때문.
- 프로젝트(예를 들면, django tutorial에서의 `\mysite\`)에 사용될 python 버전`<3.x.x>`을 정한다.
- `pyenv install 3.x.x` 으로 해당 버전을 시스템에 설치한다.
- `pyenv global 3.x.x` 으로 해당 버전을 전역화한다.
- 프로젝트 디렉토리로 이동한다.
- `python -m venv venv` 으로 해당 버전의 가상환경 디렉토리`\venv\`를 프로젝트 디렉토리 안에 만든다.   
       - 첫 번째 venv는 모듈명이고 두 번째 venv가 내가 정한 가상환경 이름이다.  
       - `.gitignore`에 기록되는 일반적인 명칭으로 하는 것이 유리하기 때문.  
- `source ./venv/bin/activate` 으로 가상환경 `\venv\`를  활성화하면, `(venv)`가 프롬프트 앞에 태그된다.  
- `django-admin startproject config .` 또는 오피셜 튜토리얼에서처럼 `django-admin startproject mysite .`으로 프로젝트를 구성할 수 있다. 
  
# 4. `conda env` 현명한 사용법
가상환경 디렉토리를 프로젝트 외부에서 관리하므로 프로젝트가 깔끔하다는 장점이 있지만, 프로젝트에서 쓰인 가상환경정보를 직접 얻을 수 없는 불편함도 있다.
- `conda create -n <django> python=3.x.x`으로 보통은 프로젝트를 상기시키는 가상환경이름<django>을 사용하여 해당 버전의 python을 설치한다.
- `conda activate <django>`로 가상환경을 활성화한다.
  
