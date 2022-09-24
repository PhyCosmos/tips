# 1. vim 명령어들 중, 워드 명령에 해당하는 것  
만을 추려보자.  

|word|이름|vim|내용|
|:---|:---|:---|:---|
|`ctrl` + `c`|  copy | y| yank |
|`Enter` | new line | `r` -> `Enter` | replace and enter, 개행 |
|`space` | space | `a` -> `space` -> `ESC` | 공백입력 후 Normal |
|block -> `ctrl`+ `c`|block copy| v -> y| 블록설정 후 yank|
|`ctrl` + 'x`|delete line| `dd`| 행 삭제 | 
|`ctrl` + `z`|undo| `u`| 되돌리기|`| 
|`ctrl` + `y`|redo| `ctrl`+`r`| 다시하기|
|`ctrl` + `f`|find| `f` 또는 `/`| 찾기|
|`back-space`|delete backward|`X` 즉, `shift` + `x`|거꾸로 삭제하기|  


# 2. Vim에서는 마우스를 사용을 최소화하므로
move/search/select 기능의 short-cut 이 다양하고 조합해 사용한다. 그 중에서 많이 쓰이는 것들 중 복잡해 보이는 것들을 추려본다.

|vim명령| |내용|
|:---|:---|:---|
|:%s/old/new/g|substitute old to new| 전체 old를 new로 바꾼다.|