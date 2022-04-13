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
