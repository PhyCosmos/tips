# Git & GitHub

## 다른 머신으로 기존 계정에 연결하기.
> ---
> 다른 컴퓨터를 이용해서 자신의 GitHub 리포로 접근하려니 문제가 발생했다.  
> 지정된 user 정보가 달랐기 때문인데, 기존 컴퓨터와 user 정보를 통일한 후에 접속하면 된다. 

```zsh
git config --list
git config --global user.name <username>
git config --global user.email <useremail>
```
- 기존 디렉토리와 연결할 경우
```terminal
git remote add origin <https://...git> 
```
- 클론으로 가져올 경우.
```
git clone <https://...git> 
```

## staged files to be unstaged
If you want to reset your `git add` command,
```
git reset
git reset <filepath>
```
## compare local files with remote repository
```
git diff <local/branch> <remote>/<remote/branch>
git diff main origin/main
```

## `.gitignore` cover **except** some.
If you want to exclude some `<file/or/directory>` among the  
`<ignore/list> in the `.gitignore` file, to be carful the written order,
> `.gitignore`
```
<ignore/list>
!<file/or/directory>
```

## Ignore Files that have already been commited to the repo?
- 1. make sure right patterns writtne in`.gitignore`.
- 2. Commit or stash any local changes.
- 3. Clean up cache.
```
git rm -r --caches .
```
- 4. recommit all
```
git add .
git commit -m "clean up the ignored"
```
5. and push to the origin
```
git push origin main
```

## How can I delete commit-history log containing sensitive data from remote repo