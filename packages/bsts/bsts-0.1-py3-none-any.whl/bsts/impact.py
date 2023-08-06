from .bsts import BSTS


class CausalImpact(object):
    def __init__(self, seasonality=None):
        self.model = BSTS(seasonality)

    def __call__(self, df, target_column, impact_index):
        y_train = df.loc[:impact_index, target_column].values
        X_train = df.loc[:impact_index].drop(target_column, axis=1).values
        y_test = df.loc[impact_index:, target_column].values
        X_test = df.loc[impact_index:].drop(target_column, axis=1).values
        self.model.fit(y_train, X_train)
        return self.model.plot_impact(y_test, X_test)
