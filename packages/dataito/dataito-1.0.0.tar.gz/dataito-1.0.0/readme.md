# DataITO

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

<center><img src="https://camo.githubusercontent.com/8ea5ab2f59ce09a175cb2fd87d0a75b86bde024cbb8b96a596f9d698a89dea15/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f707972696768742d4d49542d677265656e"><img src="https://camo.githubusercontent.com/036c3fa7badfd718f1d5f594921b9eeb0f3122a0529d3f4113aeb584cae74f1b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d646174612d626c7565"></center>

## 安装(install)

- 安装开发版（Install development version）

```python
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps dataito
```

- 安装稳定版（ Install stable version ）

```python
pip install dataito
```



## 使用手册 (中文版)

Python数据输入(Input)、转换(transform)、输出(output)，一行代码读取/转换多种格式的数据文件

dataito仅有三个函数，分别是<kbd>read()</kbd>、<kbd>transform()</kbd>、<kbd>save()</kbd>，具体参数及调用方式如下：



### 格式

- 目前支持的读取格式

  - txt
  - xlsx
  - csv
  - json（仅支持结构化数据）

- 目前支持的转换格式

  - dataframe (pandas)
  - array (numpy)
  - list

- 目前支持的保存格式

  - xlsx（目前仅支持保存为xlsx，在考虑是否要增加自定义格式保存功能）




### 调用方式

- read( )

  ```python
  read(filepath)
  ```

  注：只能读取支持的文件格式（建议filepath之前加个`r`，具体看example）

- transform( )

  ```python
  transform(data,'parameter')
  ```

  parameter中填写为需要转换的目标数据类型，其与type(data)获取的数据类型的关系如下：

  | type             | type(data)                            |
  | ---------------- | ------------------------------------- |
  | dataframe/pandas | <class 'pandas.core.frame.DataFrame'> |
  | array/numpy      | <class 'numpy.ndarray'>               |
  | list             | <class 'list'>                        |

  

  ```python
  >>> data= dataito.transform(data,'dataframe')
  >>> type(data) 
  <class 'pandas.core.frame.DataFrame'>
  >>> data= dataito.transform(data,'array')     
  >>> type(data)
  <class 'numpy.ndarray'>
  >>> data= dataito.transform(data,'list')      
  >>> type(data)
  <class 'list'>
  ```

  

- save( )

  ```
  save(filepath)
  ```

  （建议filepath之前加个`r`，具体看example）

  

- example

  ```python
  import dataito
  
  filepath = r'data/data.xlsx'				#读取支持格式的数据文件
  
  data = dataito.read(filepath)				#调用函数读取(读取其他支持的格式也是这个函数)
  data= dataito.transform(data,'dataframe')	#数据格式转换为想要的格式（转换为其他支持的格式也是这个）
  dataito.save(data,r'D:\data\data.xlsx')		#保存在data文件夹（默认文件名为data）
  ```

  

## User manual (English version)

### format

Python data input (i), transform (t), output (o), a line of code to read / convert a variety of formats of data files

- Currently supported read formats

  - txt
  - xlsx
  - csv
  - json (only supports structured data)
- Currently supported conversion formats

  - dataframe
  - array (numpy)
  - list
- Currently supported save formats
  - xlsx ( it only supports saving as xlsx. We are considering whether to add the function of saving in custom format.)



### Call mode

- read( )

  ```python
  read(filepath)
  ```

  Note: only the supported file formats can be read (it is recommended to add `r` before filepath, see example for details)

- transform( )

  ```python
  transform(data,'parameter')
  ```

  parameter is the target data type to be converted, and its relationship with the data type obtained by type (data) is as follows:

  | type             | type(data)                            |
  | ---------------- | ------------------------------------- |
  | dataframe/pandas | <class 'pandas.core.frame.DataFrame'> |
  | array/numpy      | <class 'numpy.ndarray'>               |
  | list             | <class 'list'>                        |

  

  ```python
  >>> data= dataito.transform(data,'dataframe')
  >>> type(data) 
  <class 'pandas.core.frame.DataFrame'>
  >>> data= dataito.transform(data,'array')     
  >>> type(data)
  <class 'numpy.ndarray'>
  >>> data= dataito.transform(data,'list')      
  >>> type(data)
  <class 'list'>
  ```

  

- save( )

  ```
  save(filepath)
  ```

   (it is recommended to add `r` before filepath, see example for details)

  

- example

  ```python
  import dataito
  
  filepath = r'data/data.xlsx'				#Read data files in supported formats
  data = dataito.read(filepath)				#Call the function to read (read other supported formats as well as this function)
  data= dataito.transform(data,'dataframe')	#Convert the data format to the desired format (and other supported formats)
  dataito.save(data,r'D:\data\data.xlsx')		#Save in the data folder (the default file name is data). If the path is not written, the file is saved in the root directory
  ```
  
  

