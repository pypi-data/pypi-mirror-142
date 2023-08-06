import os
from pathlib import Path

import pandas as pd
from mlpipeline_analyzer.suggest import PipelineSuggest


class TestPipelineSuggest:
    """
    Class that performs unit tests for the Pipeline Suggest module
    """

    def test_fit(self):
        """
        Test that the data is divided into train and test data before finding the best ML pipeline
        """
        data = pd.read_csv(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))), 'sample_data/income_classification.csv'))
        response = 'income'
        predictor = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                     'hours-per-week', 'native-country']

        problem_type = 'binary'
        objective = 'F1'

        ps = PipelineSuggest()
        ps.fit(data, response, predictor, problem_type, objective)

        assert (ps.x_train.shape[0] != 0) is True
        assert (ps.x_test.shape[0] != 0) is True
        assert (ps.y_train.shape[0] != 0) is True
        assert (ps.y_test.shape[0] != 0) is True

    def test_suggest_fe(self):
        """
        Test that the suggest function returns feature engineering steps of the best ML pipeline
        """
        data = pd.read_csv(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))), 'sample_data/income_classification.csv'))
        response = 'income'
        predictor = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                     'hours-per-week', 'native-country']

        problem_type = 'binary'
        objective = 'F1'

        ps = PipelineSuggest()
        ps.fit(data, response, predictor, problem_type, objective)

        best_fe = ps.suggest('fe')

        assert best_fe

    def test_suggest_model(self):
        """
        Test that the suggest function returns feature engineering steps of the best ML pipeline
        """
        data = pd.read_csv(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))), 'sample_data/income_classification.csv'))
        response = 'income'
        predictor = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                     'hours-per-week', 'native-country']

        problem_type = 'binary'
        objective = 'F1'

        ps = PipelineSuggest()
        ps.fit(data, response, predictor, problem_type, objective)

        best_model = ps.suggest('model')

        assert best_model

    def test_suggest_all(self):
        """
        Test that the suggest function returns feature engineering steps of the best ML pipeline
        """
        data = pd.read_csv(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))), 'sample_data/income_classification.csv'))
        response = 'income'
        predictor = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                     'hours-per-week', 'native-country']

        problem_type = 'binary'
        objective = 'F1'

        ps = PipelineSuggest()
        ps.fit(data, response, predictor, problem_type, objective)

        best_pipeline = ps.suggest()

        assert best_pipeline
