## Простейший язык формульных выражений.
Я думаю, что язык выражений в табличных процессорах мог бы выглядеть так:

```
expr = 1 if sum({8.05, 9, -0.5, 2e-3}) > 3 else 0
1
expr = avr({100, 1000, 5000})
2033.3333333333333
expr = pow(2, 0.5) == 2^.5
True
```