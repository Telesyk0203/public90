 -Наш Web разработчик написал нам сообщение, давай посмотрим, что там. 

Наш босс сказал разработать новый функционал для нашего сайта, но я такого никогда еще не делал, возможно сайт будет зависать или падать в процессе. 
Ты можешь что-нибудь придумать чтобы сайт не падал? 

Мы возьмем сайт с Git, сделаем dev ветку для разработки, соберем образ для Docker контейнера и построим pipeline CI/CD в системе непрерывной интеграции программного обеспечения Jenkins, который будет собирать сайт в Docker контейнере для нашего разработчика чтобы он мог спокойно вводить новые фичи не поломав нам основной сайт. 



# Встановити гід , скопіювати папку з кодом в свій гід, зробити нову ветку dev, добавити файл в нову вутку dev, зaкомітить та запушить в гідХАБ.

sudo apt install git

git --version
git clone git@github.com:MaKU2021/devops_lesson_trial.

git        copy from GitGub копіруєм файли сайта в свій гід

git checkout  -b dev                                                       створоєм ветку dev з якої буде брать інфу дженкінс 

echo "just file" > justfile                                                додаєм просто файл в ветку dev

git add .

git commit -m

git config --global user.name "Your Name"

git config --global user.name "Your Name"

git push --set-upstream origin dev                                         запушить змінені файли з новою веткой  

# 2.теперь нужно  положить наш сайт в докер.

docker run --name site -p 80:80 -d nginx                                    site will be run in container on ubuntu

docker exec -it site mkdir /var/www                                         створити папку внутрі контейнера

docker exec -it site nginx:nginx /var/www                                   власник і група папку nginx

docker exec -it site ls -l /var
docker cp /home/maxon/devops_lesson_trial/landing/ site:/var/www/           скопірувать  папку landing  з хоста  в докер  var/www/ 


Create conf.d                                                               створюємо конфіг для сайта 

server {

    server_name ip.your.vm.xx;

    access_log /var/log/nginx_access.log;

    error_log /var/log/nginx_error.log;

    root /var/www;

    location / {

                index  index.html index.htm index.php;

    }

}

docker cp /media/sf_DEVOPS/TASKS/site.conf site:/etc/nginx/conf.d            скопірувать config в контейнер, site - назва контейнера

docker restart site                                                          reload container with сайт

# CREATE AVTOMATIZATION

# ТОБТО РОБОМO ТЕ САМЕ ТІЛЬКИ ВСЕ ЗБЕРЕ ДОКЕРФАЙЛ

# CREATE DOCKERFILE

FROM nginx
RUN apt update && apt-get install -y locales
 
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen
 
ENV LANG ru_RU.UTF-8

ENV LANGUAGE ru_RU:ru

ENV LC_LANG ru_RU.UTF-8

ENV LC_ALL ru_RU.UTF-8
 
RUN  mkdir /var/www

RUN  rm -f /etc/nginx/conf.d/default.conf

COPY site.conf  /etc/nginx/conf.d/

COPY site/. /var/www/

RUN  chown nginx:nginx -R /var/www/

Перед зборкой перевірити щоб файли DOCKERFILE, conf.d, site                    знаходились в одній папці

docker build -f /home/maxon/DOCKER/build_Site/Dockerfile . -t web/dev         
 запуск биілда докерфайла

docker rm b7                                                          видаляєм старий контейнер          

docker run --name web -p 80:80 -d web/dev                                      запуск нового контейнера з зробленим  білдом

# 3. тепер потрібно налаштувати автоматизацію CI/CD за допомогою Jenkins, щоб при коміт в репо в ветку dev стврорювався новий контейнер з нуля,  з новими файлами. 
java -version
apt install openjdk-8-jre-headless                                - установить java

# SET_JENKINS

wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable 
binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update

sudo apt install jenkins

sudo systemctl status jenkins

sudo systemctl enable jenkins && sudo systemctl status jenkins 

sudo cat /var/lib/jenkins/secrets/initialAdminPassword    копіруєм ключ з папкі

на реальном проде стоит подключить SSL, чтобы защитить данные передаваемые через веб-интерфейс. 

Оставлять Jenkins на белом адресе крайне не рекомендовано т.к. там есть еще несколько лазеек через которые сервер могут взломать. 

# Задачи у нас будут такие:

# Подключить репозиторий с сайтом к Jenkins. 

# Написать сборку контейнера, которая будет срабатывать каждый раз, когда в репозиторий будут пушить новый коммит. 
usermod -a -G docker jenkins                
         добавляємо дженкінс в групу докера

jenkins ALL=(ALL)  NOPASSWD:ALL                  
  прописуємо в sudo nano /etc/sudoers

Далі в дженкінс Create Job. 

git@github.com:MaKU2021/devops_lesson_trial.git     
 вказуємо джобу шлях до репозиторія в гітХабі (вкладка в new job)

GIT - ADD - SSH KEY (cat ~/.ssh/id_rsa) та вводемо його в поле, а відкритий ключ вже є в ГітХаб(коли робили для Git з Linux)

*/dev   вказуєм ветку з якою працюємо  та вводимо в build наступні команди для дженкінса:

# build
sudo mkdir -p ~/build/site  # Создаем папку для сборки

sudo chown root:jenkins -R ~/build/ # Даем Jenkins права на запись в этой папке

sudo chmod 775 -R ~/build/
 
sudo rsync -av $WORKSPACE/landing/ ~/build/site/    
Переносим сайт из WORKSPACE(змінна де дженкінс знає шлях до репо на ГітХаб) Jenkins в сборочную директорию
 
sudo echo "

server {
 
    server_name 192.168.0.135;
 
    access_log /var/log/nginx_access.log;
 
    error_log /var/log/nginx_error.log;
 
    root /var/www;
 
    location / {
 
                index  index.html index.htm index.php;
 
    }
 
} " > ~/build/site.conf
 
# Create container with ubuntu
sudo echo "FROM nginx
RUN apt update && apt-get install -y locales
 
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen
 
ENV LANG ru_RU.UTF-8

ENV LANGUAGE ru_RU:ru

ENV LC_LANG ru_RU.UTF-8

ENV LC_ALL ru_RU.UTF-8
 
RUN  mkdir /var/www

RUN  rm -f /etc/nginx/conf.d/default.conf

COPY site.conf  /etc/nginx/conf.d/

COPY site/. /var/www/
RUN  chown nginx:nginx -R /var/www/" > ~/build/Dockerfile
 
 
sudo docker rm -f web # Удаляем старый контейнер
 
cd ~/build/ # Помним что сборку нужно запускать из папки в которой находится Dockerfile
 
 
sudo docker build -f ~/build/Dockerfile . -t web/dev # Запускаем сборку образа
 
 
sudo docker run --name web -p 80:80 -d web/dev 
#Запускаем новый контейнер из собранного образа
 
sudo rm -rf ~/build/ # Убираем за собой

Время загрузить новые правки от нашего коллеги в dev ветку репозитория. Он как раз прислал их. 
wget http://distrib.yodo.me/first_commit.tar 
 
скачать отдельно в папку home

tar -xvf first_commit.tar                                     - розархивурувать в папку хом
cd first_commit

cp -a . /home/maxon/devops_lesson_trial/landing               - копірувать всі файли з архіва в папку landing яка повинна бути пуста

git add .

git commit -m "First commit"

git push

url 192.168.0.135:80

Далі говорими розрабу хай сам робить коміт в ветку dev, яку дженкінс раз в минуту моніторить та при змінах запускає job (Site)
Тобто я упаковывал сайты в Docker для дальнейшего обновления путем настройки CI/CD pipeline, используя Jenkins для непрерывной поставки обновлений в веб приложение.