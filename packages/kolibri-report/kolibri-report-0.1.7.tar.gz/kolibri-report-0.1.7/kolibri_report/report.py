# Importing the packages
import streamlit as st,requests,pandas as pd,io,os,json,numpy as np,seaborn as sns
import datetime as d,calendar
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
from kolibri.backend import models
from abc import ABC,abstractmethod

class KolibriImplements(ABC):
    """
    This is a abstract method for report implementation.
    """
    @abstractmethod
    def data(self):
        return NotImplementedError

    @abstractmethod
    def visualise(self):
        return NotImplementedError

    @abstractmethod
    def modelAnalysis(self):
        return NotImplementedError
    
    @abstractmethod
    def featureInteraction(self):
        return NotImplementedError

class Report(KolibriImplements):
    """
    A class which creates us the dashboard for our model and plots all the score and graph.
    """
    def __init__(self,data=None,model_interpreter=None,model_directory=None,X_test=None, X_train=None, y_test=None, y_train=None, x_val=None, y_val=None):
        """A constructor which takes the data, model_interpreter and the trainer as important parameter and 

        Args:
            data (Dataframe, optional): Pandas Dataframe(Dataset). Defaults to None.
            model_interpreter (ModelLoader, optional) : A model loader where we fetch all the training and test data Defaults to None.
            model_directory (String, optional): Directory path to fetch metetajson file. Defaults to None.
            X_test (List, optional): Defaults to None.
            X_train (List, optional): Defaults to None.
            y_test (List, optional): Defaults to None.
            y_train (List, optional): Defaults to None.
            x_val (List, optional): Defaults to None.
            y_val (List, optional): Defaults to None.
        """
        self.dataset = data
        self.model_directory = model_directory
        self.model_interpreter = model_interpreter
        self.X_test, self.X_train, self.y_test, self.y_train,self.x_val,self.y_val = X_test, X_train, y_test, y_train,x_val,y_val
        self.pathDict = dict() # Dictionary to store path of the created temporary file

################################################### Helper Methods Starts ##########################################################

    @staticmethod
    def showNavBar():
        """
        A static method to show the navigation bar.
        """
        st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

        st.markdown("""
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #C5BAAF;-webkit-transition: all 0.4s ease;transition: all 0.4s ease;">
        <a class="navbar-brand" href="https://thingks.io" target="_blank" style="color:black;">Mentis</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav" style="text-align: center;">
            <ul class="navbar-nav" >
            <li class="nav-item" style="float: left;text-align: center;">
                <a class="nav-link" href="#" target="_blank" style="color:black;">Overview</a>
            </li>
            <li class="nav-item" style="float: left;text-align: center;">
                <a class="nav-link" href="#" target="_blank" style="color:black;">Model Analysis</a>
            </li>
            <li class="nav-item" style="float: left;text-align: center;">
                <a class="nav-link" href="#" target="_blank" style="color:black;">Feature Interaction</a>
            </li>
            <li class="nav-item" style="float: left;text-align: center;">
                <a class="nav-link" href="#" target="_blank" style="color:black;">Real Time Interaction</a>
            </li>
            </ul>
        </div>
        </nav>
        """, unsafe_allow_html=True)

        st.markdown("""
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script>
            $(window).scroll(function() {
                if ($(document).scrollTop() > 50) {
                    $('nav').addClass('transparent');
                } else {
                    $('nav').removeClass('transparent');
                }
                });
        </script>
        """, unsafe_allow_html=True)
        
    # @st.cache(persist=True,suppress_st_warning=True)
    def __convertTrainTestData(self):
        import pandas as pd
        # self.X_test, self.X_train, self.y_test, self.y_train = X_test, X_train, y_test, y_train

        # If the user provides list values then we convert it to dataframe

        X_test = pd.DataFrame(self.X_test)
        X_train = pd.DataFrame(self.X_train)
        y_test = pd.DataFrame(self.y_test)
        y_train = pd.DataFrame(self.y_train)
        x_val = pd.DataFrame(self.x_val)
        y_val = pd.DataFrame(self.y_val)
        return X_train,X_test,y_train,y_test,x_val,y_val

    '''def __storePath(self,datasetID):
        """A private method to store the path of the created temporary file where we will be storing the results in json format.

        Args:
            datasetID (string): Dataset ID to store the path of the created temporary file.
        
        Returns:
            pathDict (dict): path of the created temporary file
        """
        currentDate = datetime.today().strftime("%Y-%m-%d")
        tempPath = tempfile.mkdtemp(prefix="pre_",suffix=f"_{currentDate}") # Temporary file directory
        
        if datasetID not in self.pathDict:
            self.pathDict[datasetID] = []
            self.pathDict[datasetID].append(tempPath)
        else:
            self.pathDict[datasetID].append(tempPath)'''

    def __getAccessToken(self):
        """A method to fetch the access token

        Returns:
            string: access token
        """
        accessUrl = 'https://mentis.io/api/login/access-token'
        username = 'admin@mentis.io'
        password = 'qO1ULDO$eX5t'

        accReq = requests.post(accessUrl,headers={'accept': 'application/json','Content-Type': 'application/x-www-form-urlencoded'},data={'username':username, 'password':password})
        tok = accReq.json()['access_token']
        return tok

    def __fetchModels(self):
        """A API call where we fetch all the models present in cloud.

        Returns:
            json: request data in JSON format
        """
        req = None
        try:
            token = self.__getAccessToken() # A method to fetch the token
            headers = {'Accept': 'application/json','Authorization': f'Bearer {token}'}
            baseURL = 'https://mentis.io/api/models'
            req = requests.get(baseURL,headers=headers)
        except requests.exceptions.RequestException as e:
            print(e)
        return req.json()
    
    @st.cache(persist=True,suppress_st_warning=True)
    def __fetchAPIData(self,startDate,endDate):
        """An API to fetch the data from the clinet server

        Args:
            startDate (String): Start date
            endDate (String): End date

        Returns:
            JSON: Response data from the server
        """
        resp = None
        try:
            baseUrl = f'https://reporting.smartconnect.eu/reports/report.php?r=208&u1=OCTAPLUS-5CF9E62E-B74B-4644-8284-122CD03968C2&u2={startDate}&u3={endDate}&u4=Email&m=1&h=b6f7fc4e90c7e400571daebfdeada88225b0a80e&export=csv'        
            headers = CaseInsensitiveDict()
            headers['X-MYDBR-AUTH'] = '1'
            resp = requests.get(baseUrl,headers=headers,auth=HTTPBasicAuth('mentis', 'k2BcuV&66kmB'))
        except requests.exceptions.RequestException as e:
            print(e)
        return resp.text

    @st.cache(persist=True,suppress_st_warning=True)
    def __getInformation(self) -> tuple:
        """Reads the metajson file and fetches all the information required for the Overview tab.
        Returns:
            tuple: Returns kolibri version,date,time at which it executed and name of the model(s) used.
        """
        for i in os.listdir(self.model_directory):
            if i.endswith('.json'):
                fileOpen = self.model_directory+'/'+i
                f = open(fileOpen,'r')
                data = json.load(f)
                v = data['pipeline'][-1]['tunable']['model']['parameters']['estimators']['value']
                model_name = [i['class'].split('.')[-1] for i in v]
                kolibri_version = data['kolibri_version']
                trained_at,time_trained = data['trained_at'].split('-')
                time_finished = ":".join([time_trained[i:i+2] for i in range(0, len(time_trained), 2)])
                date = datetime.strptime(trained_at,'%Y%m%d').strftime('%d/%m/%Y')
        return (kolibri_version,date,time_finished,model_name)

    @st.cache(persist=True,suppress_st_warning=True)
    def __showVisualisation(self):
        X_train,X_test,y_train,y_test,x_val,y_val = self.__convertTrainTestData()
        st.title('Visualising our dataset!!')
        if len(self.dataset.select_dtypes(include=["float", 'int']).columns) > 2:
                st.write(''' #### Heatmap for our dataset''')
                sns.heatmap(self.dataset.corr(),cmap='Greens')
                st.pyplot()
                with st.expander("See explanation"):
                    st.write("""The chart above shows some numbers class present in our dataset.""")
        else:
            import pandas as pd
            for i in os.listdir(self.model_directory):
                if i.endswith('.json'):
                    fileOpen = self.model_directory+'/'+i
                    f = open(fileOpen,'r')
                    data = json.load(f)
                    target = data['pipeline'][-1]['fixed']['target']

            # if we choose the options we get our output result as list
            col1,col2,col3 = st.columns([3,3,3])
            with col1:
                st.write(''' #### Train set Class distribution''')
                ax = pd.DataFrame(y_train.value_counts()).T.squeeze().plot(kind='bar')
                for p in ax.patches:
                    width = p.get_width()
                    height = p.get_height()
                    x, y = p.get_xy() 
                    ax.annotate(f'{height}', (round(x + width/2,2), round(y + height*1.01,2)), ha='center')
                    ax.set_xticklabels(y_test[0].unique())
                    ax.xaxis.set_label_text('Class')
                st.pyplot()
                with st.expander("See explanation"):
                    st.write("""The chart above shows some numbers class present in our dataset.""")
            
            with col2:
                st.write(''' #### Test set Class distribution''')
                ax = pd.DataFrame(y_test.value_counts()).T.squeeze().plot(kind='bar')
                for p in ax.patches:
                    width = p.get_width()
                    height = p.get_height()
                    x, y = p.get_xy() 
                    ax.annotate(f'{height}', (round(x + width/2,2), round(y + height*1.01,2)), ha='center')
                    ax.set_xticklabels(y_test[0].unique())
                    ax.xaxis.set_label_text('Class')
                st.pyplot()
                with st.expander("See explanation"):
                    st.write("""The chart above shows some numbers class present in our dataset.""")
            
            with col3:
                st.write(''' #### Validation set Class distribution''')
                ax = pd.DataFrame(y_val.value_counts()).T.squeeze().plot(kind='bar')
                for p in ax.patches:
                    width = p.get_width()
                    height = p.get_height()
                    x, y = p.get_xy() 
                    ax.annotate(f'{height}', (round(x + width/2,2), round(y + height*1.01,2)), ha='center')
                    ax.set_xticklabels(y_test[0].unique())
                    ax.xaxis.set_label_text('Class')
                st.pyplot()
                with st.expander("See explanation"):
                    st.write("""The chart above shows some numbers class present in our dataset.""")

    @st.cache(persist=True,suppress_st_warning=True)
    def __fetchScores(self) -> tuple:
        """A method which fetch all the scores from the metajson file and plots all the result.
        Returns:
            tuple[DataFrame, DataFrame, DataFrame, Series]: Returns cf_matrix and all scores
        """
        for i in os.listdir(self.model_directory):
            if i.endswith('.json'):
                fileOpen = self.model_directory+'/'+i
                f = open(fileOpen,'r')
                data = json.load(f)
                dict_val = [i for i in data['pipeline'] if 'performace_scores' in i][0]
                confussionMatrix = pd.DataFrame(dict_val['performace_scores']['confusion_matrix'])
                class_report = pd.DataFrame(dict_val['performace_scores']['class_report'])
                class_report.drop(class_report.index[len(class_report)-1],inplace=True) # Droping support
                new_class_report = class_report.iloc[: ,0:len(self.dataset[data['pipeline'][0]['fixed']['target']].unique())]
                score_report = class_report.iloc[:, 2:]
                res_score = dict([(k,dict_val['performace_scores'][k]) for k in dict_val['performace_scores'].keys() if k not in ['confusion_matrix', 'class_report']])
                res_score = pd.Series(res_score)
        return confussionMatrix,new_class_report,score_report,res_score

    def __saveResponse(self,startDate,endDate):  
        """_summary_

        Args:
            startDate (String|Datetime): _description_
            endDate (String|Datetime): _description_

        Returns:
            :dataset: dataset with new index
            :path: Path of our dataset
        """
        response = self.__fetchAPIData(startDate,endDate)
        responseDf = pd.read_csv(io.StringIO(response)) # converting the response to a dataframe
        response = responseDf.replace({'<NA>':'Nil'})
        currentDir = os.getcwd() # Fetch the current working directory
        newDir = 'Data'
        pathNewDir = os.path.join(currentDir,newDir) # A new path to save the response data
        if not os.path.exists(pathNewDir): os.mkdir(pathNewDir) # Creating the directory to store all the data
        fileName = f'{pathNewDir}/{startDate}_{endDate}_responseData.csv'
        responseDf.to_csv(fileName,index=False)

        responseDf.Init = pd.to_datetime(responseDf.Init) # Converting our Init to a datetime index option to subset based on time range.
        # st.table(responseDf[:3])
        responseDf = responseDf.set_index(['Init']) # Changing the index of our data frame
        return responseDf,fileName
    
    @st.cache(persist=True,suppress_st_warning=True) # caching if we ge the same datasetID
    def __numberOfTimesTrained(self,datasetID):
        """A method to fetch number of time the model trained.

        Args:
        datasetID (String): ID of the dataset

        Returns:
            String: value for number of times the model trained
        """
        req = None
        try:
            token = self.__getAccessToken()
            headers = {'Accept': 'application/json','Authorization': f'Bearer {token}'}
            baseURL = f'https://mentis.io/api/datasets/{datasetID}/training_processes'
            req = requests.get(baseURL,headers=headers)
        except requests.exceptions.RequestException as e:
            print(e)
        return req.json()['total']

    @st.cache(persist=True,suppress_st_warning=True)
    def __displayModels(self):
        """A method to display all the models present in cloud.
        """
        resp = self.__fetchModels()
        modelDf = pd.DataFrame()
        modelName,baseAlgorithm,version,userName,date,timesTrained = [],[],[],[],[],[]
        dataset_id = set()
        # To fetch all model name
        for val in range(resp['total']):
            dataset_id.add(resp['items'][val]['dataset_id'])
            mName = '_'.join(resp['items'][val]['model_path'].split('_')[1:]) # To store the model name
            modelName.append(mName)

            # Adding the Base Algorithm to our list
            if not resp['items'][val]['train_config']:
                baseAlgorithm.append(resp['items'][val]['metadata']['pipeline'][-1]['tunable']['model']['value']['class'].split('.')[-1])
            else:
                baseAlgorithm.append(resp['items'][val]['train_config']['model'])
            
            # Adding the version of our model
            version.append(resp['items'][val]['version'])

            # Adding the username
            userName.append(os.environ.get("USER"))

            # Fetch date
            date.append(resp['items'][val]['creation_date'].split('T')[0])

            # Number of times trained even though the training fails or pratialy fails we consider it as a request so we return including that count
            timesTrained.append(self.__numberOfTimesTrained(resp['items'][val]['dataset_id']))
        
    @st.cache(persist=True,suppress_st_warning=True)
    def __requestCountLanguages(self,dataset):
        """A method to fetch the number of requests for language present in the dataset per dates.

        Args:
            dataset (DataFrame): _description_

        Returns:
            DataFrame: A dataframe containing the languages with the requests per date
        """
        st.title('Total request for all detected languages')
        langDict = {}
        for idx,val in dataset.iterrows():
            key = val['Detected Language']
            date = val['Init'].split(' ')[0]
            if val['Detected Libelle'] != np.nan and val['Reclassified Libelle'] == 'Nil':
                if key not in langDict:
                    langDict[key] = {}
                if date not in langDict[key]:
                    langDict[key][date] = 1
                else:
                        langDict[key][date] += 1
        del langDict[np.nan]
        c = pd.DataFrame(pd.concat({
        k: pd.DataFrame.from_dict(v, 'index') for k, v in langDict.items()
            }, 
            axis=0))
        c = c.reset_index()
        c.columns = ['Language','Date','Request']
        return c

    @st.cache(persist=True,suppress_st_warning=True)
    def __getNumberOfRequest(self,dataset):
        """A method to fetch the number of requests in the dataset per date.

        Args:
            dataset (DataFrame): _description_

        Returns:
            DataFrame: Total requests in the dataset per date
        """
        requestDict = dict()
        for idx,val in dataset.iterrows():
            dates = val['Init'].split(' ')[0]
            if val['Detected Libelle'] != np.nan and val['Reclassified Libelle'] == 'Nil':
                if dates not in requestDict:
                    requestDict[dates] = 1
                else:
                    requestDict[dates] += 1
        totReq = pd.DataFrame(sorted(requestDict.items()), columns=['Date', 'No. of requests'])
        return totReq
    
    # def __useMostRecentData(self,startDate,endDate):
    #     import glob
    #     pathNewDir = self.__saveResponse(startDate,endDate)
    #     list_of_files = glob.glob(f'{pathNewDir}/*')# * means all if need specific format then *.csv
    #     latest_file = sorted(list_of_files, key=os.path.getctime, reverse=True)
    #     return list_of_files
################################################### Helper Methods Ends ##########################################################

################################################### Overview Tab Starts ##########################################################
    @st.cache(persist=True,suppress_st_warning=True)
    def data(self):
        '''
        This method displays description of the model, Model Version​,Kolibri Version​,Owner​ and Trained at​.
        '''
        modelDict = {
            "Model Name" : '',
            "Trained At" : '',
            "Model Version" : '',
            "Base Algorithm" : '',
            "Number of times used" : '',
            "Average Request per day" : '',
            "Number of times trained" : '',
            "Last time used" : '',
            "User name" : ''
        }
        kolibri_version,date,time_finished,model_name = self.__getInformation()
        md = models.get_classification_model(model_name)
        nameList = [md["parameters"]["estimators"]["value"][i]["name"] for i in range(len(md["parameters"]["estimators"]["value"]))]
        modelDict['Model Name'] = model_name
        modelDict['Model Version'] = kolibri_version
        modelDict['Trained At'] = time_finished
        modelDict['Base Algorithm'] = ','.join(nameList)
        modelDict["User name"] = os.environ.get("USER")
        modelDict['Last time used'] = date
        modelInfo = pd.Series(modelDict).to_frame().T
        st.table(modelInfo)

        # Displaying our dataset
        st.subheader('Our dataset')
        st.table(self.dataset[:5])
################################################### Overview Tab Ends ############################################################
    
################################################### Class distribution Taxonmloy Starts ##########################################################
    @st.cache(persist=True,suppress_st_warning=True)
    def visualise(self):
        self.__showVisualisation()
################################################### Class distribution Taxonmloy Ends ############################################################    
    
################################################### Model Analysis Tab Starts ##########################################################               
    def modelAnalysis(self):
        """This is a function where it plots all the score analysis such as precision,recall,f1-score and 
        accuracy.
        """
        # To print all models presnt in a dataframe
        self.__displayModels()
        confussionMatrix,class_report,score_report,res_score = self.__fetchScores()
        col1,col2= st.columns(2)
        with col1:
            st.write(''' #### Confusion Matix for our dataset''')
            sns.heatmap(confussionMatrix/np.sum(confussionMatrix), annot=True, fmt='.2%')
            st.pyplot()
            with st.expander("See explanation"):
                st.write("""A random text about confusion matrix""")
        
        with col2:
            st.write(''' #### Class Report for our dataset''')
            ax1 = class_report.plot(kind='bar',figsize=(6,6))
            for p in ax1.patches:
                width = p.get_width()
                height = p.get_height()
                x, y = p.get_xy() 
                ax1.annotate(f'{height:.0%}', (round(x + width/2,2), round(y + height*1.02,2)), ha='center')
            st.pyplot()
            with st.expander("See explanation"):
                st.write("""A random text about confusion matrix""")

        col3,col4= st.columns(2)
        with col3:
            st.write(''' #### Accuracy,Macro Average and Weighted Average for our dataset''')
            ax1 = res_score.plot(kind='bar', color=['black', 'red', 'green', 'blue', 'coral','limegreen','darkkhaki','thistle','chocolate','peru','darkgoldenrod','steelblue'])
            for p in ax1.patches:
                width1 = p.get_width()
                height1 = p.get_height()
                x1, y1 = p.get_xy() 
                ax1.annotate(f'{height1:.0%}', (round(x1 + width1/2,2), round(y1 + height1*1.02,2)), ha='center')
            st.pyplot()
            with st.expander("See explanation"):
                st.write("""A random text about confusion matrix""")
################################################### Model Analysis Tab Ends ############################################################    
    
################################################### Feature Interaction Tab Starts ##########################################################
    @st.cache(persist=True,suppress_st_warning=True)
    def featureInteraction(self):
        """Checking our feature how it interacts with other feature. We provde you a dropbox 
        functionality and then you can analyse the interactn fo the features.
        """
        pass
################################################### Feature Interaction Tab Ends ##########################################################

################################################### Real Time Tracking Starts ##########################################################
    # Using the API we access and fetch the data
    @st.cache(persist=True,suppress_st_warning=True)
    def showResponse(self):
        from datetime import time
        """A method to show the response in a certain date range and time range.
        """
        rowSlider,_,dateSlider = st.columns(3)
        startTime,endTime = None,None

        # Tab to choose the time range to fetch the data.
        with rowSlider:
            values = st.slider('Select a range of values',value=(time(0, 30), time(3, 30)))
            startTime,endTime = values

        # Tab to choose the start date and end date.
        with dateSlider:
            startDate = d.date(datetime.today().year, datetime.today().month, 1)
            date = d.datetime.now()
            month_end_date = d.datetime(date.year,date.month,1) + d.timedelta(days=calendar.monthrange(date.year,date.month)[1] - 1)
            d3 = st.date_input("Please select the date range to fetch the data", [startDate,month_end_date.date()])
            startDate,endDate = d3
            endDate += d.timedelta(days=1) # Incrementing the date to fetch data
        
        response = self.__fetchAPIData(startDate,endDate) # response from server within a specified date range.
        subsetTimeDf,filePath = self.__saveResponse(startDate,endDate)
        df = pd.read_csv(filePath) # dataset without headers
        df['Reclassified Libelle'] = df['Reclassified Libelle'].replace({np.nan:'Nil'}) # changing nan to Nil
        subsetTimeDf = subsetTimeDf.between_time(startTime,endTime)
        
        st.title("Total Request per date for all detected languages")
        st.table(self.__getNumberOfRequest(df))
        st.table(self.__requestCountLanguages(df))
        st.title("Dataset based on time series")
        st.table(subsetTimeDf[:5])
################################################### Real Time Tracking Ends ##########################################################
    def run(self):
        """A method to run the real time tracking.
        """
        st.page_config = st.set_page_config(
                page_title="Kolibri report",
                layout="wide",
            )
        st.set_option('deprecation.showPyplotGlobalUse', False)
        '''self.showNavBar() # To display navigation bar
        self.data() # Ovireview tab
        self.visualise() # Extra Info {yet to think about this tab}
        self.modelAnalysis() # Model analysis tab'''
        self.showResponse() # A method to show the response of our client data.
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)