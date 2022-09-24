# Tips for Ubuntu Users

## 설치
- 과정: 0. 중요 파일 백업 -> 1. usb 제작 -> 2.설치 -> 3. 업데이트/업그레이드 -> 4. 자판설정 -> 5. 폰트설정 -> 6. IDE설치(VSCode) -> 7. 언어(Python, Anaconda, Java,..) 및 Extention 설치 및 설정  
- 글자들이 깨지는 현상이 나타나면 십중팔구 폰트를 바꿔주면 해결.
- vscode 단축키와 ubuntu 단축키(예, ibus) 겹침 문제가 있을 수 있다.
- 주요 프로그램들은 local repo 설치를 기본으로 한다.
- snap 설치는 한글이 안되는 경우가 있다고 들었다.
- 설치는 English(United States), 자판은 Korean으로 해야 terminal운용시 한글과 영문을 오가는 피곤한 번거로움이 줄어든다. 즉, 디렉토리 명 등이 영문으로 표기되어야 편하다.

## Terminal 에 관한 팁
- `#!/usr/bin/env` 과 같은 유형이 자주 등장한다.[참고](https://bcp0109.tistory.com/343)
    - `#` hash `!` Bang! 으로 유래(위키)했다고 하고 
    - ㅊ`#!` 은 2 Byte 의 매직 넘버 (Magic Number) 로 스크립트의 맨 앞에서 이 파일이
     어떤 명령어 해석기의 명령어 집합인지를 시스템에 알려주는 역할
    - `#!<interpreter> [optional-arg]` 
    - `#!/usr/bin/env` 로 설정하면 인터프리터의 위치를 찾아서 실행 (`env`라는 파일이 있다.)

## Ubuntu GUI 단축키
- `ctrl` + `alt` + `d` 또는 `super` + `d`: 바탕화면(모든 창 감춤)
- `ctrl` + `alt` + `del` : 로그아웃 창
- `ctrl` + `alt` + `t` : Terminal 창