parse_dates : boolean or list of ints or names or list of lists or dict, default False

boolean. True -> 解析索引
list of ints or names. e.g. If [1, 2, 3] -> 解析1,2,3列的值作为独立的日期列；
list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用
dict, e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"
infer_datetime_format : boolean, default False

如果设定为True并且parse_dates 可用，那么pandas将尝试转换为日期类型，如果可以转换，转换方法并解析。在某些情况下会快5~10倍。

keep_date_col : boolean, default False

如果连接多列解析日期，则保持参与连接的列。默认为False。

date_parser : function, default None

用于解析日期的函数，默认使用dateutil.parser.parser来做转换。Pandas尝试使用三种不同的方式解析，如果遇到问题则使用下一种方式。

1.使用一个或者多个arrays（由parse_dates指定）作为参数；

2.连接指定多列字符串作为一个列作为参数；

3.每行调用一次date_parser函数来解析一个或者多个字符串（由parse_dates指定）作为参数。

dayfirst : boolean, default False

DD/MM格式的日期类型

iterator : boolean, default False

返回一个TextFileReader 对象，以便逐块处理文件。

chunksize : int, default None

文件块的大小 https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

low_memory : boolean, default True

分块加载到内存，再低内存消耗中解析。但是可能出现类型混淆。确保类型不被混淆需要设置为False。或者使用dtype 参数指定类型。注意使用chunksize 或者iterator 参数分块读入会将整个文件读入到一个Dataframe，而忽略类型（只能在C解析器中有效）

memory_map : boolean, default False

如果使用的文件在内存内，那么直接map文件使用。使用这种方式可以避免文件再次进行IO操作
