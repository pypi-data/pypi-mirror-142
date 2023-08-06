"""Model summary: This is the model summary
"""
from kolibri_report.report import Report
from kolibri.model_trainer import ModelTrainer,ModelConfig
from kolibri.model_loader import ModelLoader
import os
from kolibri.datasets import get_data

data = get_data('amazon')

confg = {}
confg['do-lower-case'] = True
confg['language'] = 'en'
confg['filter-stopwords'] = True
confg["model"] = 'RandomForestClassifier'
confg["n_estimators"] = 100
confg['output-folder'] = '/Users/aneruthmohanasundaram/Documents/koli_report_test'
confg['pipeline']= ['WordTokenizer', 'TFIDFFeaturizer', 'SklearnEstimator']
confg['evaluate-performance'] = True

X = data.reviewText.values.tolist()
y = data.Positive.values.tolist()

trainer = ModelTrainer(ModelConfig(confg))

# I need to check if the train file is present in that location [model_direc]
    # not present train the model and not present train the model
# option 2
# operator overiding
while 1:
    trainer.fit(X, y)
    train = False
    model_directory = trainer.persist(confg['output-folder'], fixed_model_name="Cache Test")
else:
    model_directory = '/Users/aneruthmohanasundaram/Documents/koli_report_test/Cache Test'

model_interpreter = ModelLoader.load(os.path.join(confg['output-folder'], 'Cache Test'))

app_report = Report(data,model_interpreter,model_directory)
app_report.run()

# if __name__ == "__main__":
#     import sys
#     # sys.argv
#     pass