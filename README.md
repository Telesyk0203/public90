__git add__ - add file to commite & get status "staged" підготовлений 

**git commit** - status "committed" зафіксований

**git commit -m "_Change file_** - do commit 

**git log** - history commits

__git diff__ - difference between continue "unstaged" and last status(commit)

**git status** - review contiunue  "staged" status

__git diff --staged__ - difference between continue "staged" file and past status(commit)

 **HEAD** - поточний коміт , який є актуальним;
 
 **HEAD~3** - переносимо актуальний коміт на 3 коміти назад;
 
 **git reset** - видалити коміт з переведенням у невіслудковуємий трафік (--mixed) режим по замовчуванню

 **--soft** - режим reset що переводить інформацію з коміта у _відслудковуємий_ трафік та видиляє сам коміт.
 
**--mixed** - режим reset що переводить інформацію з коміта у _невідслудковуємий_ трафік та видиляє сам коміт.

**--hard** - режим reset що _видаляє повністю_  всю інформацію до певного коміта.

__git checkout__ - викорстовується для перегляду (переміщення) актуального комміту та версіями окремих файлів ,а також гілками(branch)