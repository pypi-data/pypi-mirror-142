class Averaging:
    def __init__(self):
        import pandas as pd
        import numpy as np
        from sklearn.ensemble import VotingRegressor

        pass

    def set_base_models(self):
          import pandas as pd
          import numpy as np
          from sklearn.ensemble import VotingRegressor

          """
          Lets the user set multiple user defined base models. 
          
          Note: The models the user wishes to use have to be imported separately. 
          
          Parameters
          ----------
          base_model: user defined base models. 
          
          Example
          -------
          >>> from Ensemble_Learning import Average_weight_Ensemble
          >>> awe = Average_weight_Ensemble()
          >>> awe.set_base_models()
          >>> base_model =[('rfr', RandomForestRegressor()), 
          ('knn', KNeighborsRegressor()), ('lr', LinearRegression())]
      
          """
          self.base_model =[]

          return print("[('rfr', RandomForestRegressor()), ('knn', KNeighborsRegressor()), ('lr', LinearRegression())]")

    def get_Averaging_technique(self,base_model,train_X,train_y,test_X):
             import pandas as pd
             import numpy as np
             from sklearn.ensemble import VotingRegressor
             """
             Averages out the performance of each model and builds
             a new model as output based on the average. 
             
             Parameters
             ----------
             base_model: models set as the base models for averaging.
             train_X: input train data.
             test_X: input test data.
             train_y: output train data.
             test_y: output test data. 
             
             Example
             -------
             >>> from Ensemble_Learning import Average_weight_Ensemble
             >>> awe = Average_weight_Ensemble()
             >>> y_test_pred = awe.get_Averaging_technique(base_model= base_model,
                                          train_X=x_train,
                                          train_y= y_train,
                                          test_X=x_test)
                                          
             """
             self.base_model = base_model
             self.train_X = train_X
             self.test_X  = test_X 
             self.train_y = train_y
             vt = VotingRegressor(estimators=self.base_model)
             vt.fit(self.train_X,self.train_y)
             return vt.predict(self.test_X)

Averaging.__doc__

class weighted_Averaging:
    def __init__(self):
          pass

    def get_weighted_Avg_technique(self,base_model,train_X,train_y,test_X,weights):
             import pandas as pd
             import numpy as np
             from sklearn.ensemble import VotingRegressor

             """
             Averages out the performance of each model based on weights
             and builds a new model as output. 
             
             Parameters
             ----------
             base_model: models set as the base models for averaging.
             train_X: input train data.
             test_X: input test data.
             train_y: output train data.
             test_y: output test data.
             weights: weights obtained from the models.
             
             Example
             -------
             >>> from Ensemble_Learning import Average_weight_Ensemble
             >>> awe = Average_weight_Ensemble()
             >>> summary.weights.values
             >>> ypred_test = awe.get_weighted_Avg_technique(base_model= base_models,
                                            train_X=x_train,
                                            train_y= y_train,
                                            test_X=x_test,
                                            weights= weights1)
             """
             self.base_model = base_model
             self.train_X = train_X
             self.test_X  = test_X 
             self.train_y = train_y
             self.weights  = weights
             vt = VotingRegressor(estimators=self.base_model,weights=self.weights)
             vt.fit(self.train_X,self.train_y)
             return vt.predict(self.test_X)
      
weighted_Averaging.__doc__

class Rank_weighted:
    def __init__(self):
          pass

    def get_weights(self,threshold,base_model,train_X,test_X,train_y,test_y):
            import pandas as pd
            import numpy as np
            """
            Gives the weights of the user defined models based on their accuracies. 
            
            Parameters
            ----------
            threshold: minimum accuracy expected from the models.
            base_model: models statisfying the threshold. 
            train_X: input train data.
            test_X: input test data.
            train_y: output train data.
            test_y: output test data.
            
            Example
            -------
            >>> from Ensemble_Learning import Average_weight_Ensemble
            >>> awe = Average_weight_Ensemble()
            >>> summary = awe.get_weights(threshold= 0.5,
                          base_model= base_models,
                          train_X= x_train,
                          test_X= x_test,
                          train_y= y_train,
                          test_y= y_test)
                          
            """
            self.threshold  = threshold
            self.base_model = base_model
            self.train_X    = train_X
            self.test_X     = test_X
            self.train_y    = train_y
            self.test_y     = test_y
            self.results = self.accuracy_filter(self.threshold,self.base_model,self.train_X,self.test_X,self.train_y,self.test_y)
            self.results = self.results.sort_values("accuracy",ascending=False)
            self.new     = [self.f for self.f in np.arange(1,self.results.shape[0]+1)]
            self.new.sort(reverse=True) 
            self.results['weights'] = self.new /np.sum(self.new)
            return self.results

    def get_rank_weighted_technique(self,base_model,train_X,train_y,test_X,weights):
             import pandas as pd
             import numpy as np
             from sklearn.ensemble import VotingRegressor

             """
             Averages out the performance of each model based on weights
             and builds a new model as output. 
             
             Parameters
             ----------
             base_model: models set as the base models for averaging.
             train_X: input train data.
             test_X: input test data.
             train_y: output train data.
             test_y: output test data.
             weights: weights obtained from the models.
             
             Example
             -------
             >>> from Ensemble_Learning import Average_weight_Ensemble
             >>> awe = Average_weight_Ensemble()
             >>> summary.weights.values
             >>> ypred_test = awe.get_weighted_Avg_technique(base_model= base_models,
                                            train_X=x_train,
                                            train_y= y_train,
                                            test_X=x_test,
                                            weights= weights1)
             """
             self.base_model = base_model
             self.train_X = train_X
             self.test_X  = test_X 
             self.train_y = train_y
             self.weights  = weights
             vt = VotingRegressor(estimators=self.base_model,weights=self.weights)
             vt.fit(self.train_X,self.train_y)
             return vt.predict(self.test_X)

Rank_weighted.__doc__