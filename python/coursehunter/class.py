class CommentFromWebSite(): # Створення назви класу КемелКейс
    ''' Комнетарій до класу ''' # Коментар до класу 
    def __init__(self, data,text,likes) -> None:# Перший метод (функція) в класі конструктор
        self.data=data # Присвоюємо змінним значення атребута 
        self.text=text # Присвоюємо змінним значення атребута 
        self.likes=int(likes)# Присвоюємо змінним значення атребута 
    
    def showComment(self):#Метод для виводу коментаря
        '''Вивести коментарії в консоль'''
        print(f'\n Коментар з сайту, \n дата : {self.data}, 'f'\n текст: {self.text}, лайків : {self.likes}')

    def changeLikes(self):
        '''Додає один лайк'''
        self.likes=self.likes+1

    def changeComment(self, new_text):
        '''Зміна коментаря'''
        self.text= new_text
    
new_comment= CommentFromWebSite('11/02/20', 'Перший коментар!', '11') # Змінна використання  нашого класу 
new_comment2= CommentFromWebSite('22/03/19', 'Другий коментар!!!', '5')

new_comment2.showComment()
new_comment2.changeLikes()
new_comment2.changeLikes()
new_comment2.showComment()
new_comment.showComment()
new_comment.changeComment('Я змінив коментар !!!')
new_comment.showComment()
new_comment.changeLikes()
new_comment.showComment()#