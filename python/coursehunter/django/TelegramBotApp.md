# Створення телеграм-бот додатку на Python
1. Відкриваємо додаток Телеграм та знаходимо контакт творця ботів `@BotFather` і починаємо з нип роботу по створенню і налаштуванню нашого бота :
    +   /newbot - комнада по створенню нового бота;

        BotFather, 
        Alright, a new bot. How are we going to call it? Please choose a name for your bot.
    +  Називаємо свого бота 
          Наприклад:  Прийом заявок з сайту

    + BotFather,  Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

    + створюємо унікальне ID для бота як радить нам  BotFather. 
        Наприклад : bot_for_Strikha_bot
    + Отрмимуємо таку інформацію
      ```
      Done! Congratulations on your new bot. You will find it at t.me/bot_for_Strikha_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

        Use this token to access the HTTP API:
        5505395694:AAH3itDIOxuK1cCa09es5zLZyGyFbWlWD4w
        Keep your token secure and store it safely, it can be used by anyone to control your bot.

        For a description of the Bot API, see this page: https://core.telegram.org/bots/api
        ```
        
2. Створюєм нову групу в Телеграмі та додаєм нашого бота до цієї групи через `@bot_for_Strikha_bot`
3. Встановлюємо бібліотеку requests : `pip install requests`
4.  Створюєм додаток в нашому фреймворці командою в терміналі :
   + `python manage.py startapp telebot`
5. Прописуєм його в файлі `settings.py` 
   + `INSTALLED_APPS = [ ''telebot.apps.TelebotConfig'' ` ...
6. Переходимо в файл `models.py` в додатку `telebot`  та створюємо класи `StatusCrm`, `Order`, `CommentCrm` від `model.Models` :
   ```
        from django.conf import settings
        import requests
        from .models import TeleSetting

        class sendTelegram():
            settings=TeleSetting.objects.get(pk=1)
            token=settings.tg_token
            chat_id=str(settings. tg_chat_id)
            text=str(settings.tg_text)
            time=str(settings.tg_time)
            api= 'https://api.telegram.org/bot'
            method= api + token + '/sendMessage'

            req= requests.post(method, data={
                'chat_id':chat_id,
                'text':text
            })

   ```
7. Реєстрація додатку в адмінпанелі в файлі `admin.py` в дерикторії самого додатку `telebot` :
   ```
   from django.contrib import admin
    from .models import TeleSetting
    # Register your models here.
    admin.site.register(TeleSetting)
   ```
8. Міграція даних для того щоб нові дані водобразилися в БД в терміналі вводимо команду:
      + `python manage.py makemigrations`

      + `python manage.py migrate`  переміщення додатків 
9.  Створюємо файл `sendmessage.py` в додатку `telebot`
     ```
        from django.conf import settings
        import requests
        from .models import TeleSetting

        class sendTelegram():
            settings=TeleSetting.objects.get(pk=1)
            token=settings.tg_token
            chat_id=str(settings. tg_chat_id)
            text=str(settings.tg_text)
            time=str(settings.tg_time)
            api= 'https://api.telegram.org/bot'
            method= api + token + '/sendMessage'

            req= requests.post(method, data={
                'chat_id':chat_id,
                'text':text
            })
     ```