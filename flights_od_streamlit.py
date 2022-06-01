#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 06:35:37 2022

@author: kartiknarula
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_folium import st_folium
import folium


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

header_container = st.container()
DV = st.container()
EAD = st.container()
AnalysisQ1=st.container()
AnalysisQ2=st.container()
AnalysisQ3=st.container()
AnalysisQ4=st.container()

cd1=pd.read_csv('2007_January1.csv')
cd2=pd.read_csv('2007_January2.csv')
cd3=pd.read_csv('2007_January3.csv')
a=pd.concat([cd1, cd2])
a=pd.concat([a, cd3])

if 'type' not in st.session_state or 'a' not in st.session_state:
    st.session_state['type']='Categorical'
   # st.session_state['a']= pd.read_csv("2007_January.csv")   
    st.session_state['a']=a
    day_of_week={"DayOfWeek":[1,2,3,4,5,6,7], "Weekday":['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    w=pd.DataFrame(day_of_week)
    Month_name={"Month":[1,2,3,4,5,6,7,8,9,10,11,12], "Month_":["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]}
    m=pd.DataFrame(Month_name)
    st.session_state['a']=st.session_state['a'].merge(w, how='left', on='DayOfWeek')
    st.session_state['a']=st.session_state['a'].merge(m, how='left', on='Month')
    st.session_state['a'].drop(['Month', 'DayOfWeek'], axis=1)

with header_container:

	# for example a logo or a image that looks like a website header
	#st.image('/Users/kartiknarula/Downloads/streamlit template/logo.png')

	# different levels of text you can include in your app
	st.title("Are you ready to take off")
	#st.header("Flights Origin and Destination data")
	st.subheader("We are analyzing US domestic flight data for the January 2007")
	#st.write("check it for yourself, if you don't believe me")




 
    
 
#master_file=pd.concat(map(p, glob.glob("/Users/kartiknarula/Downloads/dataverse_files/Files/*.csv")))
#p=partial(pd.read_csv, encoding='latin-1')
#master_file=pd.concat(map(p, glob.glob("/Users/kartiknarula/Downloads/dataverse_files/flights_u/*.csv")))
#files=glog.glob("/Users/kartiknarula/Downloads/dataverse_files/flights_u/*.csv")


#l=['d_' + str(i) for i in range(2000, 2009)]

#d_dict={}
#for names in l:
 #   n=names.split('_')[1]
  #  data=pd.read_csv("/Users/kartiknarula/Downloads/dataverse_files/flights_u/"+str(n)+".csv", encoding='latin-1', usecols=['Year', 'Month', 'DayofMonth', 'DayOfWeek','DepTime', 'CRSDepTime', 'ArrTime','CRSArrTime','ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 'Distance', 'TaxiIn', 'TaxiOut','Cancelled', 'Diverted', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'], dtype='Int64')
   # d_dict[names]=data





with DV:
    st.title("Here's a sneak peak at the data!")
    st.write(st.session_state['a'].head(50))
    st.caption('There are 621,559 rows and 29 columns in the dataset')



types={'Categorical':['Origin', 'Dest', 'UniqueCarrier', 'FlightNum', 'Weekday', 'Month_'], 'Numerical':['ArrTime', 'CRSArrTime', 'DepDelay', 'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay' ]}
#column=st.selectbox('Select a column', t)
with EAD:
    st.title("Let's do some Exploratory Data Analaysis (EAD")
    radio=st.radio('Select the type of variable', ['Categorical', 'Numerical'])
    st.session_state['type']=radio
    box=st.selectbox('Select the variable to analyze', types[st.session_state['type']])
    #st.write(st.session_state)
    st.write(box)
    if st.session_state['type']=='Categorical':
        dist=pd.DataFrame(st.session_state['a'][box].value_counts()).head(50)
        st.bar_chart(dist)
    else:
        st.write(st.session_state['a'][box].describe())
        

cd_o=pd.read_csv('airports.dat', header=None)
cd_d=pd.read_csv('airports.dat', header=None)

cd_o.columns=['Id', 'Name_o', 'City_o', 'Country', 'IATA_o', 'ICAO', 'Latitude_o', 'Longitude_o', 'Altitude', 'TimeZone', 'DST', 'Tz database time zone', 'Type', 'Source'] 
cd_d.columns=['Id', 'Name_d', 'City_d', 'Country', 'IATA_d', 'ICAO', 'Latitude_d', 'Longitude_d', 'Altitude', 'TimeZone', 'DST', 'Tz database time zone', 'Type', 'Source']
    

        
cd_o_md=cd_o[['Name_o', 'City_o', 'IATA_o', 'Latitude_o', 'Longitude_o']]
cd_d_md=cd_d[['Name_d','City_d', 'IATA_d', 'Latitude_d', 'Longitude_d']]
        
        
a1=st.session_state['a'].merge(cd_o_md, how='left', left_on='Origin', right_on='IATA_o')
final_merge=a1.merge(cd_d_md, how='left', left_on='Dest', right_on='IATA_d')
        
        
        
final_merge['cd_o'] = list(zip(final_merge.Latitude_o, final_merge.Longitude_o))
final_merge['cd_d'] = list(zip(final_merge.Latitude_d, final_merge.Longitude_d))      
with AnalysisQ1:
  st.title('Which city had maximum number of flights for a given Origin Airport?')
  c1, c2=st.columns(2)
  Origin_City=c1.selectbox('Enter Origin City', final_merge.City_o.unique())
  Origin_Airport=c2.selectbox('Enter Airport', final_merge[final_merge['City_o']==Origin_City].IATA_o.unique()) 
  filtered=final_merge[final_merge['IATA_o']==Origin_Airport]
  map=folium.Map(location=[37.0902, -95.7129], zoom_start=3)
  values = filtered.cd_d.value_counts().keys().tolist()
  counts = filtered.cd_d.value_counts().tolist()
  st.caption('The size of the circular map reflects the number of flights at the destination for the selected location. The map is interactive and the points are clickable')
  for i in range(len(values)):
    folium.CircleMarker(location=values[i], color='Red',  fill=True,
      fill_color='crimson' ,popup=(filtered[filtered['cd_d']==values[i]].City_d.values[0] , counts[i]) ,radius=float(counts[i]*0.03)).add_to(map)
  # c=final_merge[final_merge['Origin']==str(Origin)].Dest.value_counts().head(5)
    #st.bar_chart(c)
   ## st.write(Origin)
  st_folium(map)
  
  
with AnalysisQ2:
  st.title('Which airport had the maximum average weather delay?')
  Q2_df=pd.pivot_table(final_merge, values='WeatherDelay', index=['IATA_o'], aggfunc='mean').reset_index()
  Q2_df=Q2_df.sort_values(by='WeatherDelay', ascending = False).head(5)
  fig2 = px.bar(Q2_df, x="IATA_o", y="WeatherDelay", title="Average Weather Delay by Airport", labels={'WeatherDelay':'Average Weather Delay (Minutes)', 'IATA_o':'Origin Airport'})
  st.plotly_chart(fig2)
  
with AnalysisQ3:
  st.title('Which carrier had the most number of flights?')
  Q3_df=final_merge.UniqueCarrier.value_counts().rename_axis('Carrier').reset_index(name='Number of Flights')
  fig3 = px.bar(Q3_df, x="Carrier", y="Number of Flights", title="Number of Flights by Carrier", labels={'CarrierDelay':'Average Carrier Delay (Minutes)', 'UniqueCarrier':'Carrier'})
  st.plotly_chart(fig3)
  
with AnalysisQ4:
  st.title('Which carrier had the greatest average delay?')
  Q4_df=pd.pivot_table(final_merge, values='CarrierDelay', index=['UniqueCarrier'] , aggfunc='mean').reset_index()
  fig4 = px.bar(Q4_df, x="UniqueCarrier", y="CarrierDelay", title="Average Carrier Delay", labels={'CarrierDelay':'Average Carrier Delay (Minutes)', 'UniqueCarrier':'Carrier'})
  st.plotly_chart(fig4)
