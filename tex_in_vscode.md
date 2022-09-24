# LaTex in VSCode

- SyncTex from cursor: 미리보기에서 소스 커서 위치와 매칭되는 pdf 위치를 알려준다.
    - 참고:  
    https://tex.stackexchange.com/questions/538797/go-to-source-for-latex-on-vs-code-does-not-seem-to-work
    - 사전 설정
    "latex-workshop.synctex.synctexjs.enabled": true,  
    "latex-workshop.synctex.afterBuild.enabled": true,  
    "latex-workshop.view.pdf.viewer": "tab",  

    - from `code` to `pdf`:
        mac: `cmd`+`option`+`j`
        windows/linux: `ctrl`+`alt`+`j`
    - from `pdf` to `code`: `ctrl`+`click`

    - 관련 설정:  
    "latex-workshop.view.pdf.internal.synctex.keybinding": "ctrl-click"

- Jang Soo Kim 님의 [동영상](https://www.youtube.com/watch?v=aSdGb47jJtc)과 팁 [사이트](https://jangsookim.github.io/lectures/vscode/vscode_lecture0.html)가 도움이 된다.