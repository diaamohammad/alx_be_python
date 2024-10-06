def safe_divide(numerator, denominator):
    try:
      num = numerator
      denom = denominator

      result = num / denom
      
      return (f"result is {result}")
     
         
    except ZeroDivisionError:
       return ("Erorr:Cannot divide by zero!")

    except ValueError:
       return ("Error: Non-numeric input provided!")



