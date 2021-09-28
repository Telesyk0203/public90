__git add__ - add file to commite & get status "staged" підготовлений 
<br>
**git commit** - status "committed" зафіксований
<br>
**git commit -m "_Change file_** - do commit 
<br>
**git log** - history commits
<br>
__git diff__ - difference between continue "unstaged" and last status(commit)
<br>
**git status** - review contiunue  "staged" status
<br>
__git diff --staged__ - difference between continue "staged" file and past status(commit)
<br>
 **HEAD** - поточний коміт , який є актуальним;
 <br>
 **HEAD~3** - переносимо актуальний коміт на 3 коміти назад;
 <br>
 **git reset** - видалити коміт з переведенням у невіслудковуємий трафік (--mixed) режим по замовчуванню
 <br>
 **--soft** - режим reset що переводить інформацію з коміта у _відслудковуємий_ трафік та видиляє сам коміт.
 <br>
**--mixed** - режим reset що переводить інформацію з коміта у _невідслудковуємий_ трафік та видиляє сам коміт.
<br>
**--hard** - режим reset що _видаляє повністю_  всю інформацію до певного коміта.
<br>
__git checkout__ - викорстовується для перегляду (переміщення) актуального комміту та версіями окремих файлів ,а також гілками(branch)