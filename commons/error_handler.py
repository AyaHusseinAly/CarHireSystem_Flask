from flask import jsonify

def Error_Handler(func):
    def Inner_Function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception::{func.__module__}::{func.__qualname__}::{func.__name__}::{str(e)}")
            response = jsonify({'error': str(e)})
            response.status_code = 500
            return response  
    return Inner_Function