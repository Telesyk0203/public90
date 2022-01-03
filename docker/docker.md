## Встановлення Docker на Ubuntu
__https://docs.docker.com/engine/install/ubuntu/__

__https://rotoro-cloud.github.io/LabDock1num1/__ -тренування з docker <br>
### Створенння docker jenkins на основі alpine
1.проброс портів з контейнеру на хостовий інтерфейс<br> 
2.закріплення зберігання даних з контейнеру на хостовій пам'яті <br>
3. уточнення який юзер може запускати образ<br>
4. вибір образу для завантаження   
`docker run  -p 8080:8080 -v /home/ts90/DATA/jenkins/:/var/jenkins_home -u root jenkins/jenkins:lts-alpine`
<br>
5.також можна вказати параметр -d для прихованого (фонового) режиму . 