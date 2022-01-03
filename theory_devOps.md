## IaC 
__https://habr.com/ru/company/otus/blog/574278/__
__https://www.youtube.com/watch?v=LSgmwgSbGjQ&list=PLmxB7JSpraieS8C58ewR7fdTu5fS3z7HG&ab_channel=KirillSemaev__ - це відос про IaC 
## CI/CD
__https://itglobal.com/ru-ru/company/blog/methodology-ci-cd/__

__https://www.youtube.com/watch?v=7S1ndRRht6M&ab_channel=webDev__ -відос по CI/CD 

## Agile
__https://newfuture.site/podrobnoe-rukovodstvo-po-upravleniyu-proektami/__

__https://marketreading.com/ru/devops-interview-questions.html__

## Етапи роботи DevOps 

### Етап 1

Розробники створюють код, а вихідний код керується за допомогою інструментів контролю версій, таких як GIT.

### 2 етап

Передача коду до репозиторію GIT.

### 3 етап

Дженкінс витягує код із репозиторію за допомогою плагіна GIT і збирає його за допомогою таких інструментів, як Ant або Maven.

### 4 етап

Розгортання інструментів керування конфігурацією, таких як Puppet, та надання тестового середовища.

### 5 етап

Дженкінс випускає код у тестовому середовищі. Тестування проводиться за допомогою таких інструментів, як Selenium.

### 6 етап

Після тестування коду Jenkins відправляє його для розгортання на виробничому сервері, який надається та підтримується такими інструментами, як Puppet.

### 7 етап

Після розгортання він постійно контролюється такими інструментами, як Nagios.

### 8 етап

Контейнери Docker надають середовище тестування для тестування функцій збирання.