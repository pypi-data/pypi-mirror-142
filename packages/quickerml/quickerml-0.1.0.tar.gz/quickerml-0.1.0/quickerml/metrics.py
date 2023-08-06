from sklearn.metrics import mean_squared_error


def neg_root_mean_squared_error(y_true, y_pred):
    return -1 * mean_squared_error(y_true, y_pred, squared=False)
