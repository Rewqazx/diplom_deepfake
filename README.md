# diplom_deepfake

Инструкция:

1. Разархивируйте и создайте папку media с видео, которые вы собираетесь проверять.
2. Откройте консоль в главной папке deepfake.
3. pip install -r requirements.txt
4. cd deepfake
5. python manage.py runserver

http://127.0.0.1:8000/ - страница для проверки видео
http://127.0.0.1:8000/admin - админка (тут можно посмотреть прошедшие проверки)


Instruction:

1. Unzip and create a media folder with the videos you are going to check.
2. Open a console in the main deepfake folder.
3. pip install -r requirements.txt
4. CD deepfake
5. python manage.py runserver

http://127.0.0.1:8000/ - video verification page
http://127.0.0.1:8000/admin - admin panel (here you can see past checks)


Программа проверяет видеоконтент на наличие внесенных изменений, предобработывая данные перед началом работы алгоритмов(ResNet101, InceptionV3, InceptionResNetV2).


The program checks the video content for changes made, preprocessing the data before the algorithms start working(ResNet101, InceptionV3, InceptionResNetV2).
