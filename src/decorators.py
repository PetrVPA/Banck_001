

def log(filename = None):
    def my_log(func):
        def wrapper(*args, **kwargs):
            x = args[0]
            y = args[1]
            t = {**kwargs}
            out_message =''

            try:
                result = func(*args, **kwargs)
                return result
            except TypeError:
                out_message = "TypeError"
            except ValueError:
                out_message ="ValueError"
            except ZeroDivisionError:
                out_message ="ZeroDivisionError"
            if filename != None:
                file = open(filename, "a")
                if out_message == '':
                    file.write('my_function ok \n')
                else:
                    file.write(f'my_function error: {out_message}. Inputs: ({x}, {y}), {t}\n')
            else:
                if out_message == '':
                    print('my_function ok\n')
                else:
                    print(f'my_function error: {out_message}. Inputs: ({x}, {y}), {t}\n')



        return wrapper
    return my_log
