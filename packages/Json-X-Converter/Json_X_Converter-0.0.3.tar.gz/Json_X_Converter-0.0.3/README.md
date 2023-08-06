# Json_X_Converter

Under construction! Not ready for use yet! Currently experimenting and planning!

Developed by Snehal Borkar (c) 2022

## Examples of How To Use (Buggy Alpha Version)

Import classes

```python 
from Json_X_Converter.api_resp_flat  import ApiCallFlat
from Json_X_Converter.x_converter import XConverter

 
data=ApiCallFlat.api_call(url)
print(data)
df =ApiCallFlat.flatten_json(data)
print(df)

XConverter(df,"test.csv").df_csv()
```

Methods available in api_resp_flat module - ApiCallFlat class
api_call(url)-Call Api and returns json data
```python
ApiCallFlat.api_call(url)
```

flatten_json(data)- Take data of type <class: dict> as parameter flatten it and  converts to pandas dataframe
```python
ApiCallFlat.flatten_json(data)
```

api_callflat(url)- Take url  of type <class: str> make HTTP request, flatten response and convert to pandas dataframe
```python
ApiCallFlat.flatten_json(data)
```



Methods available in x_converter module - XConverter class

obj = XConverter(df,file_name)

obj.df_csv() 
obj.df_xml()
obj.df_html()
obj.df_pdf(html_filename)

 
