# AELibrary

## Описание

Данная библиотека реализует набор методов для анализа данных акустической эмиссии(АЭ). Библиотека содержит несколько компонент основных подходов анализа данных АЭ: чтение файлов с АЭ данными, первичную обработку от простых шумов, локацию источников сигналов АЭ, построение супер сигналов на основе коэффициента Пирсона для дальнейшей классификации. Также в дальнейшем будет добавлена компонента кластеризации, которая на данный момент патентуется.

## Примеры использования

Основной формат файлов с данными, используйщийся в данной библиотеке имеет заголовок с параметрами вида:
```
Id      DSET   HHMMSS     MSEC CHAN    A  CNTS    DT1X
             [hhmmss] [ms.µs ]      [dB]          [µs]
La Label  1: '06:51 Resume'
DT 26 Май 2016 г., Host Time: 6:51
LE         6 06:51:52 221,4381   13 50,5     3        
Ht         7 06:51:52 221,4581   14 61,4    44    20,0
...
```

### Пример чтения файла с данными:

```
from aelib import io


acoustic_emission_data = io.open_file("filename.txt")
```

Результатом выполнения указанного выше кода будет объект типа pandas.DataFrame, пустые места в строках значений будут заполнены NaN.

### Пример использования метода локации:

```
    from aelib import io, location
    
    
    # читаем файл с АЭ волнами
    data = io.open_file("waves.txt")
    
    # читаем файл с координатами датчиков
    coords = pd.read_csv("coords.txt", sep=" ")
    
    # Устанавливаем пороговые значения скорости волн в см/мс
    lower_threshold = 100
    upper_threshold = 500
    
    # Устанавливаем ширину разверстки объекта для учета прохождения сигнала через край
    width = 520
    
    # Задаем сколько датчиков, зафиксировавших волну, будут использоваться для рассчета
    events_n = 3
    
    # Задаем максимально возможное изменение скорости волны при распространении
    acc = 0.01

    located_points = location.localize(data, coords, lower_threshold, upper_threshold, width, events_n, acc)
```

Результат located_points - список точек потенциального расположения источника сигнала для каждой волны, содержащий в себе элементы вида: [x, y, speed].

## Дальнейшее развитие

1) Добавление модуля кластеризации (после оформления патента)
2) Построение графиков по результатам работы модулей
3) Расширение модулей
4) Скомпоновать пакет для Python






