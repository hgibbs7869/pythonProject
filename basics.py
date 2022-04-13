from basics import mean, variance, covariance

def fit_single_linear_regression(x: list, y: list) -> dict:
    """
    Fits a single linear regression in the format y = mx + b
    :param x: list of predictor values
    :param y: list of target values
    :return: dict of {'m': float, 'b':float} where m is slope, b is y-intercept
    """
    m = covariance(data_x=x, data_y=y) / variance(data=x)
    b = mean(y) - m * mean(x)
    coefficients = {
        'm': m,
        'b': b
    }
    return coefficients

def predict_single_linear_regression(x: list, model: dict) -> list:
    """
    Utilizes model format y = mx + b where we are given predictors
    :param x: list of predictors
    :param model: dict of results of fit_single_linear_regression
    :return: list of predicted
    """
    predicted_y = [model['m' ] *i + model['b'] for i in x]
    return predicted_y
def mean (list):
    x_mean = sum(list) / len(list)
    return x_mean

def error(list,y):
    y_errors = [i - y for i in list]
    return y_errors

def variance(data: list) -> float:
    """
    Calculates the variance of a list of numeric values
    :param data: list of numeric values
    :return: float
    """
    data_mean = mean(data)
    sum_of_squares = sum((i - data_mean)**2 for i in data)
    return sum_of_squares


def std_dev (list, deg_of_freedom=1):
    sum_of_sqaures = variance(list)
    pvar = sum_of_sqaures / (len(list) - deg_of_freedom)
    sd = pvar ** 0.5
    return sd

def covariance (list):
    covar = 0.0
    data_x = list;
    data_y = list;
    x_mean = mean(data_x)
    y_mean = mean(data_y)
    for i in range(len(data_x)):
        covar += (data_x[i] - x_mean) * (data_y[i] - y_mean)
    return covar


