#!/usr/bin/env python
# coding: utf-8

# In[43]:


#时间序列进行拟合预测：
import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from scipy import stats 
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
import statsmodels as sm
from statsmodels.tsa.arima.model import ARIMA
from  statsmodels.tsa.stattools  import  adfuller  as  ADF

class IoT_ARIMA:
    difNumber = 2
    def __init__(self,fileurl):
        self.fileURL = fileurl
 
    #载入数据，将JSON格式的数据转化成为DataFrame
    def DataLoad(self):
        json_data_list = []
        current_json_obj = ''
        with open(self.fileURL, 'r') as file:
            # 逐行读取文件内容
            lines = file.readlines()
            for line in lines:
                # 移除行两端的空白字符（空格、制表符、换行符等）
                line = line.strip()
                parsed_data = json.loads(line)
                json_data_list.append(parsed_data)

        df = pd.DataFrame(columns=["Time", "Value"])
        addindex = df.index.stop
    # 迭代 JSON 对象并将键和值添加到 DataFrame
        for obj in json_data_list:
            for key,value in obj.items():
                if value!='':
                    df.loc[addindex] = [key,value]
                    addindex += 1
        return df
    
    #权重插值，对时间序列进行插值：
    def InsertValue(self,Data):
        #降序排列,转化格式为标准格式
        sorted_Data = Data.sort_values(by='Time', ascending=True)
        sorted_Data['Value'] = sorted_Data['Value'].astype('int')
        sorted_Data['Time'] = pd.to_datetime(sorted_Data['Time'])
        sorted_Data.reset_index(drop=True,inplace=True) #删除掉原来的索引
        #查找数据的起点和终点值
        timeStart = sorted_Data['Time'][0]
        timeEnd = sorted_Data['Time'][len(sorted_Data)-1]
        if not (timeEnd.hour==0 and timeEnd.minute==0 and timeEnd.second==0):
            timeEnd += pd.Timedelta(days=1)
            timeEnd = timeEnd.replace(hour=0, minute=0, second=0)
        #设置一个时间序列：
        time_series = pd.date_range(start=timeStart, end=timeEnd, freq='20T')
        df = pd.DataFrame({'Time':time_series})
        df['Value'] = 0
        #遍历进行插值
        index = 0
        LENGTH = len(sorted_Data)
        for i in range(0,len(df)):
            if sorted_Data['Time'][index] == df['Time'][i]:
                df['Value'][i] = sorted_Data['Value'][index]
                index +=1
            elif sorted_Data['Time'][index] > df['Time'][i]:
                tmp1 = (sorted_Data['Time'][index] - df['Time'][i]).total_seconds()//60
                tmp2 = (df['Time'][i]-df['Time'][i-1]).total_seconds()//60
                value = (sorted_Data['Value'][index]*tmp1 + df['Value'][i-1]*tmp2)/(tmp1+tmp2)
                df['Value'][i] = value
            else:
                #可能会越界,因为右边界参照了sorted_Data 因此最终没啥问题
                count = 0
                value = 0
                while(index < LENGTH and sorted_Data['Time'][index] <= df['Time'][i]):
                    count += 1
                    value += sorted_Data['Value'][index] 
                    index += 1
                df['Value'][i] = value/count
        df.index = df['Time']
        return timeEnd,df
    
    #展示ARIMA模型的差分图
    def showDiff(self,df,col):
        font = {"size":15,
           "family":"fangsong"}
        matplotlib.rc("font",**font)
        matplotlib.rcParams['axes.unicode_minus']=False

        df["diff_1"] = df[col].diff(1)  #一阶差分
        df["diff_2"] = df["diff_1"].diff(1)  #二阶差分

        #平稳数据折线图
        plt.figure(figsize=(12,8))
        plt.subplot(3,1,1)
        plt.plot(df[col].values,label="源数据")
        plt.xlim(0,120)
        plt.legend()
        plt.subplot(3,1,2)
        plt.plot(df["diff_1"].values,c="darkgreen",label="一阶差分")
        plt.plot([0,120],[0,0],"--",c = "grey")
        plt.xlim(0,120)
        plt.legend()
        plt.subplot(3,1,3)
        plt.plot(df["diff_2"].values,c="tomato",label="二阶差分")
        plt.plot([0,120],[0,0],"--",c = "grey")
        plt.xlim(0,120)
        plt.legend()
        plt.show()

        #ACF PACF
        print("-"*30,"未平稳数据ACF与PACF","-"*30)
        fig = plt.figure(figsize=(12,8))
        ax1 = fig.add_subplot(211)
        fig = plot_acf(df[col], lags=40,ax = ax1)
        ax2 = fig.add_subplot(212)
        plot_pacf(df[col], lags=40,ax = ax2)
        plt.show()

        #一阶差分后的ACF PACF
        print("-"*30,"一阶差分数据ACF与PACF","-"*30)
        fig = plt.figure(figsize=(12,8))
        ax1 = fig.add_subplot(211)
        fig = plot_acf(df["diff_1"][1:].values, lags=40,ax = ax1)
        ax2 = fig.add_subplot(212)
        plot_pacf(df["diff_1"][1:], lags=40,ax = ax2)
        plt.show()

    #获取ARIMA模型的参数
    def getpdq(self,Data):
        #未差分平稳性检测（ADF检验、单位根检验）
        #p d q
        p = 0
        d = 0
        q = 0
        if ADF(Data["Value"])[1] < 0.05 :
            d = 0
        elif ADF(Data["diff_1"][1:])[1] < 0.05:
            d = 1
        else:
            d = 2
        maxarg = 4
        train_results = sm.tsa.stattools.arma_order_select_ic(Data['Value'], ic=['aic', 'bic'], trend='c', max_ar=maxarg, max_ma=maxarg)
        aic = train_results.aic_min_order
        bic = train_results.bic_min_order
        #AIC更加倾向于预测，因此选择AIC准则
        p,q = aic
        return p,d,q
    
    #传入DataFrame的数据，起始时间和想要预测的天数，返回最终的JSON数据
    def myARIMA(self,Data,pretimeStart,day,p = 0,d = 0,q = 0):
        model = ARIMA(Data['Value'], order=(p, d, q))
        results = model.fit()
        pretimeEnd = pretimeStart + pd.Timedelta(days=day)
        predict_dta = results.predict(pretimeStart, pretimeEnd, dynamic=True)
        predict_dta = pd.DataFrame({"Value":predict_dta})
        Data_Trans = dict(zip(map(str,predict_dta.index), predict_dta["Value"].values))
        JSData = json.dumps(Data_Trans)
        return JSData

    #展示模型生成的可视化拟合效果
    def showFitting(self,Data,p,d,q):
        model = ARIMA(Data['Value'], order=(p,d,q))
        results = model.fit()
        predict_sunspots = results.predict(steps=100,dynamic=False)
        print(predict_sunspots)
        fig, ax = plt.subplots(figsize=(12, 8))
        ax = Data['Value'].plot(ax=ax)
        predict_sunspots.plot(ax=ax)
        plt.show()
        
    #调用最终的拟合函数
    def Predict(self,day):
        df = self.DataLoad()  #读取数据
        timeEnd,InsertDF = self.InsertValue(df)  #进行插值运算
        self.showDiff(InsertDF,"Value") #差分运算
        p,d,q = self.getpdq(InsertDF) #获取模型的参数
        JSData = self.myARIMA(InsertDF,timeEnd,day,p,d,q)
        return JSData
    
    #模型调用测试函数
def test():
    #这个路径是需要修改的：
    pressureURL = r'D:/Files/SoftWare_5/物联网/组队项目/2024IoTData/pressure.txt'
    #传入文件路径对类进行初始化
    IoTpress = IoT_ARIMA(pressureURL)
    #设置想要的天数,这里假设预测7天 ； 希望预测未来的天数
    day = 7   
    js = IoTpress.Predict(day)  #这是一个JSON数据，可以直接返回给前端
    print(js)
    
if __name__ == "main":
    test()


# In[44]:

#测试 in jupyter notebook
# pressureURL = r'D:/Files/SoftWare_5/物联网/组队项目/2024IoTData/pressure.txt'
# IoTpress = IoT_ARIMA(pressureURL)
#     #设置想要的天数,这里假设预测7天
# day = 7
# IoTpress.Predict(day)


# In[ ]:




