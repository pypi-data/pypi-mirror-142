# 데코레이터
def check_dtype(function):
    def check(self, X, y):
        if X.shape[0] != y.shape[0]:
          print("The size of X and y is not same!")
          return
        for dtype in X.dtypes: 
          if not dtype in [float, int]: 
            print("There is a columns which not int or float!")
            return
        function(X, y)
    return check

