# CSV_script_agr - 
## скрипт для обработки CSV-файла

## поддерживающий операции: 
- фильтрацию с операторами «больше», «меньше» и «равно»
- агрегацию с расчетом среднего (avg), минимального (min) и максимального (max) значения

## примеры комманд:
```
python main.py --file products.csv
python main.py --file products.csv --where "price>500"
python main.py --file products.csv --aggregate "raiting=min" - тут опечатка в слове rating
python main.py --file products.csv --aggregate "rating=min"
python main.py --file products.csv --aggregate "price=avg"

```
![img1.JPG](img/img1.JPG) 
![img2.JPG](img/img2.JPG)
![img3.JPG](img/img3.JPG)
![Img4.JPG](img/Img4.JPG)



## Скрипт универсальный таблица может быть другого формата вот пример другой таблицы где я добавил еще один столбец
```
python main.py --file another.csv --aggregate "sold=avg"
```
![avg5.JPG](img/avg5.JPG)
