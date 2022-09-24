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
## Force push
```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to <origin/address>
```
If you reinit git and above messages bother your push, then 
do force push when you trust your local completely.
```
git push --set-upstream origin main --force
```
This will ignore the differences between remote and local repo and 
overwrite remote repo in github with your local repo.
## `.gitignore` cover **except** some.
If you want to exclude some `<file/or/directory>` among the  
`<ignore/list> in the `.gitignore` file, to be careful the written order,
> `.gitignore`
```
<ignore/list>
!<file/or/directory>
```
>
> **Take good care** of both order and \* 
> 
```
supdir/
!supdir/*.tex
```
`supdir/` will be registered in the not-tracking list but the files contained in it will not.
Hence, the line `!supdir/*.tex` has NOTHING in effect, because 
the line never exists in the git-tracking list.  
Meanwhile, 
```
supdir/*
!supdir/*.tex
```
every files including `supdir/*.tex` in `subdir/` will be registered in the not-tracking list. 
Hence, the line `!supdir/*.tex` take effect and the files are not ignored by git.  
>So the key is that `!` can only be applied to the files or directories in the registered not-tracking list.
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

## temporarily save the changes
```
git stash
git stash show
```
To clear the stash,
```
git stash clear
```

## delete branch
```
git branch -d <branchname>
``` 

## create a new independant branch
- I used this command to manage my github pages.
```
git checkout --orphan <branchname>
```

## How can I delete commit-history log containing sensitive data from remote repo