# Вариант 17 — калькулятор среднего балла

Python-проект с автоматическими unit-тестами в GitHub Actions.
Программа принимает оценки от 0 до 100 и вычисляет средний балл.
Требуется Python 3.10 или новее; CI использует Python 3.13.
Внешние библиотеки не нужны; unittest входит в Python.

## Запуск на Windows

Откройте терминал в папке проекта:

```powershell
py grades.py
```

Введите `80 90 100`. Результат: `Средний балл: 90.00`.

## Проверка проекта

```powershell
py -m pip install -r requirements.txt
py -m compileall -q grades.py tests
py -m unittest discover -s tests -v
```

Последняя команда должна показать `Ran 8 tests` и `OK`.
Compileall проверяет синтаксис и компилирует исходники в байт-код.
Это учебный этап Build; он не создаёт установщик или exe-файл.

## Файлы

- grades.py — приложение и функция average_score.
- tests/test_grades.py — 8 unit-тестов.
- requirements.txt — описание отсутствия сторонних зависимостей.
- .github/workflows/ci.yml — конфигурация CI.
- INSTRUCTIONS_RU.txt — инструкция для Windows.
- REPORT_DRAFT.txt — основа отчёта, которую нужно дополнить результатами.

## Автоматизация

Push, Pull Request или ручной запуск запускают Python CI.
Build устанавливает зависимости и компилирует Python-файлы.
Test запускается только после успешного Build благодаря `needs: build`.
Каждый job работает в отдельном окружении, поэтому получает код и Python заново.
При ошибке команды job завершается с ошибкой. Развёртывание приложения не настроено:
для этого задания реализован базовый CI-конвейер сборки и тестирования.

## Проверяемые сценарии

1. Среднее нескольких оценок.
2. Одна оценка.
3. Границы 0 и 100.
4. Округление до двух знаков.
5. Пустой список.
6. Оценки вне диапазона.
7. Некорректные типы значений.
8. NaN и бесконечность.

## Источники

https://docs.github.com/en/actions/tutorials/build-and-test-code/python
https://github.com/actions/setup-python
https://github.com/actions/checkout
https://docs.python.org/3/library/unittest.html
