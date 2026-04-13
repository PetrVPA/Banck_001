

def log(filename = None):
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
