# Аналіз продуктивності алгоритмів сортування

## Вступ

У цьому проекті ми емпірично аналізуємо та порівнюємо продуктивність трьох алгоритмів сортування: сортування злиттям, сортування вставками та Timsort, який є гібридним алгоритмом, що поєднує в собі сортування злиттям і сортування вставками. Метою є оцінка їх ефективності за часом виконання на різних наборах даних.

## Методологія

Ми провели експерименти, використовуючи модуль `timeit` в Python для вимірювання часу виконання кожного алгоритму сортування на різних наборах даних. Ми тестували алгоритми як на малих, так і на великих масивах, щоб спостерігати їх поведінку в різних сценаріях.

## Результати

1. **Сортування злиттям**:
   - Сортування злиттям демонструє стабільну продуктивність на різних наборах даних з часовою складністю O(n log n). Воно ефективно працює навіть на великих масивах завдяки своєму підходу "розділі й володарюй".
   - Результати замірів:
     - Розмір масиву: 1000
       - Час сортування: 0.0106 с
     - Розмір масиву: 10000
       - Час сортування: 0.1123 с
     - Розмір масиву: 100000
       - Час сортування: 1.348 с

2. **Сортування вставками**:
   - Сортування вставками має квадратичну часову складність (O(n^2)), що робить його менш ефективним на великих наборах даних порівняно з сортуванням злиттям та Timsort. Проте воно працює краще на практично впорядкованих або невеликих наборах даних завдяки своєму адаптивному характеру.
   - Результати замірів:
     - Розмір масиву: 1000
       - Час сортування: 0.0919 с
     - Розмір масиву: 10000
       - Час сортування: 8.9401 с
     - Розмір масиву: 100000
       - Час сортування: 922.9744 с

3. **Timsort**:
   - Timsort перевершує як сортування злиттям, так і сортування вставками на всіх наборах даних. Його гібридний підхід поєднує переваги сортування злиттям і сортування вставками, що призводить до ефективного сортування з часовою складністю O(n log n). Адаптивний характер Timsort дозволяє ефективно обробляти різноманітні типи даних.
   - Результати замірів:
     - Розмір масиву: 1000
       - Час сортування: 0.00008 с
     - Розмір масиву: 10000
       - Час сортування: 0.00098 с
     - Розмір масиву: 100000
       - Час сортування: 0.0125 с

## Висновок

Емпіричний аналіз підтверджує, що Timsort значно ефективніший за сортування злиттям та сортування вставками в більшості випадків. Його комбінація алгоритмів сортування забезпечує універсальне та високоефективне рішення для сортування, що пояснює, чому вбудовані функції сортування Python (`sorted` та `sort`) базуються на Timsort. Програмісти зазвичай віддають перевагу використанню цих вбудованих функцій, а не реалізації алгоритмів сортування з нуля через переваги Timsort у продуктивності та адаптивності.

Загалом, переваги продуктивності Timsort підкреслюють важливість використання ефективних вбудованих алгоритмів для сортування, особливо у програмуванні на Python.

## Рузультати моїх замірів
| Розмір масиву | Час сортування злиттям | Час сортування вставками | Час сортування Timsort |
|--------------|-------------------------|---------------------------|-------------------------|
| 1000         | 0.0106 с                | 0.0919 с                  | 0.00008 с               |
| 10000        | 0.1123 с                | 8.9401 с                  | 0.00098 с               |
| 100000       | 1.348 с                 | 922.9744 с                | 0.0125 с                |
