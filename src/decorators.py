

def log(filename = None):
    '''
    Функция выполняет логирование обертываемой функции в файл если указано имя файла или консоль если имя не передается.
    В лог записывается то что операция выполнена успешно ("my_function ok\n"), либо сообщает тип ошибки и введенные
    переменные при неудачном выполнении обертываемой функции, например
    (my_function error: TypeError. Inputs: (6, t), {})
    :param filename: задается имя файла для логирования оборачиваемой функции
    return result возвращает результат обертываемой функции
    out_message сообщение в лог об операции успешной либо с ошибкой
    :return:
    '''
    def my_log(func):
        def wrapper(*args, **kwargs):
            x = args[0]
            y = args[1]
            t = {**kwargs}
            try:
                result = func(*args, **kwargs)

            except TypeError:
                out_message = "TypeError"
            except ValueError:
                out_message = "ValueError"
            except ZeroDivisionError:
                out_message = "ZeroDivisionError"
            except UnboundLocalError:
                out_message = "UnboundLocalError"
            else:
                out_message = "my_function ok\n"

            if filename != None:
                file = open(filename, "w")
                if out_message != "my_function ok\n":
                    file.write(f'my_function error: {out_message}. Inputs: ({x}, {y}), {t}\n')
                else:
                    file.write('my_function ok\n')
                    return result
                file.close()

            else:
                if out_message != "my_function ok\n":
                    print(f'my_function error: {out_message}. Inputs: ({x}, {y}), {t}\n')

                else:
                    print('my_function ok\n')
                    return result

        return wrapper
    return my_log
