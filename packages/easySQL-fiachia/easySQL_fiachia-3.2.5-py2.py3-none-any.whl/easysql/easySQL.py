import threading
from collections.abc import Iterable

import pymysql
from pymysql.cursors import Cursor

try:
    from .setting import char_list, database_table_engine, database_table_charset, type_used_long_1, type_used_long_2
    from .setting import mysql_type_to, int_list
except ImportError:
    from setting import char_list, database_table_engine, database_table_charset, type_used_long_1, type_used_long_2
    from setting import mysql_type_to, int_list

# 导入控制台颜色打印函数，包名'printf-fiachia'
try:
    from printf import printf, color

    print_error = printf.Format(_type=color.TYPE.ERROR).print
    print_warning = printf.Format(_type=color.TYPE.WARNING).print
    print_data = printf.Format(_type=color.TYPE.DATA).print
    print_success = printf.Format(_type=color.TYPE.SUCCESS).print
except ImportError:
    printf = color = None
    print_error = print
    print_warning = print
    print_data = print
    print_success = print

# 数据表属性查询
attribute_find_sql = """SELECT `column_name` from information_schema.columns where table_schema='%s' and table_name='%s' order By ORDINAL_POSITION"""
# 数据表表名查询
table_find_sql = """select `table_name` from information_schema.tables where table_schema='%s'"""


class DatabaseSql:
    """
    数据库类
    """

    def __init__(self, _database_name=None, _user="root", _passwd="123456", _host="localhost", _port=3306, **kwargs):
        """
        :param _database_name: [str/None] 数据库名
        :param _user: [str] 用户名
        :param _passwd: [int/str] 用户密码
        :param _host: [str] 连接地址
        :param _port: [str] 连接端口
        :param kwargs: [dict] 其他参数，详见注释

        :key bind_address: [str/None] 当有多个网络接口时，指定其中一个hostname/IP
        :key unix_socket: [str/None] 使用unix连接而不是TCP/IP
        :key read_timeout: [int/None] 读超时
        :key write_timeout: [int/None] 写超时
        :key charset: [str] 使用的字符集
        :key sql_mode: [str/None] 使用的SQL_MODE
        :key read_default_file: [str/None] 指定一个ini/cnf配置文件并读取
        :key conv: [dict/None] 使用转换字典提供类型的自定义编组和解编组，具体参见转换器
        :key use_unicode: [bool] 是否使用unicode字符
        :key client_flag: [int] 发送自定义标记
        :key cursorclass: [Cursor] 自定义游标类
        :key init_command: [str/None] 建立连接时使用的初始命令
        :key connect_timeout: [int] 连接超时，范围[1, 31536000]，默认10
        :key ssl: [dict/None] 类似于mysql_ssl_set()参数的字典
        :key ssl_ca: [str/None] PEM-格式CA证书的文件路径
        :key ssl_cert: [str/None] PEM-格式client证书的文件路径
        :key ssl_disabled: [bool/None] 是否禁用TLS
        :key ssl_key: [str/None] PEM-格式client证书私钥的文件路径
        :key ssl_verify_cert: [bool/None] 是否检查服务器证书的有效性
        :key ssl_verify_identity: [bool/None] 是否检查服务器的身份
        :key read_default_group: [str/None] 配置文件中要读取的Group
        :key autocommit: [bool] 是否自动提交，默认否
        :key local_infile: [bool] 是否启用"本地加载数据"，默认否
        :key max_allowed_packet: [int] 最大数据包的大小，默认16MB，仅用于限制"本地加载数据"数据包小于默认值(16KB)
        :key defer_connect: [bool] 是否延迟连接，不直接连接而是等待连接回复，默认否
        :key auth_plugin_map: [dict/None] （试验） 要处理插件的插件名。
            使用该类需要Connection作为构造参数和以认证数据包为基础的认证方法。
            对于对话框插件，可以使用提示符（echo，prompt）方法（如果没有认证方法）用于返回字符串。
        :key server_public_key: [str/None] SHA256认证插件公钥值
        :key binary_prefix: [bool] 是否在字节和字节数组上添加"_binary"前缀
        :key compress: 不支持
        :key named_pipe: 不支持

        :return:
        """
        self.database = _database_name
        self.user = _user
        self.passwd = _passwd
        self.host = _host
        self.port = _port
        self.kwargs = kwargs

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        if value is None or isinstance(value, str):
            self.__database = value
        else:
            self.__database = str(value)

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if isinstance(value, str):
            self.__user = value
        else:
            self.__user = str(value)

    @property
    def passwd(self):
        return self.__passwd

    @passwd.setter
    def passwd(self, value):
        if isinstance(value, str):
            self.__passwd = value
        else:
            self.__passwd = str(value)

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        if isinstance(value, str):
            self.__host = value
        else:
            self.__host = str(value)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = int(value)

    def connect(self):
        root_con = pymysql.connect(
            host=self.host, user=self.user, passwd=self.passwd, db=None, port=self.port, **self.kwargs)
        cursor = root_con.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS %s""" % self.database)
        root_con.commit()
        cursor.close()
        root_con.close()
        return pymysql.connect(
            host=self.host, user=self.user, passwd=self.passwd, db=self.database, port=self.port, **self.kwargs
        )

    def __str__(self):
        return self.database

    def __repr__(self):
        return self.database

    def __eq__(self, other):
        if isinstance(other, DatabaseSql):
            if other.database == self.database and other.host == self.host:
                return True
        return False


class TableSql:
    """
    数据表类
    """

    def __init__(self, _table_name, _engine="InnoDB", _charset="utf8mb4"):
        """
        :param _table_name: [str] 表名
        :param _engine: [str] 引擎
        :param _charset: [str] 字符集
        :return: 无
        """
        self.table = _table_name
        self.engine = _engine
        self.charset = _charset
        self.attribute = list()
        self.attribute_info_list = list()
        self.primary_keys = list()

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = str(value)

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value):
        if value in database_table_engine:
            self.__engine = value
        else:
            print_warning("未找到对应的引擎，使用默认引擎。")
            self.__engine = "InnoDB"

    @property
    def charset(self):
        return self.__charset

    @charset.setter
    def charset(self, value):
        if value in database_table_charset:
            self.__charset = value
        else:
            print_warning("未找到对应字符集，使用默认字符集。")

    def copy(self):
        copy_result = TableSql(
            self.table,
            _engine=self.engine,
            _charset=self.charset
        )
        copy_result.attribute_info_list = self.attribute_info_list.copy()
        copy_result.primary_keys = self.primary_keys.copy()
        return copy_result

    def reset(self, _tableSql_table):
        """
        将值替换为目标数据表（方便等于操作）
        """
        if isinstance(_tableSql_table, TableSql):
            self.table = _tableSql_table.table
            self.engine = _tableSql_table.engine
            self.charset = _tableSql_table.charset
            self.attribute_info_list = _tableSql_table.attribute_info_list
            self.primary_keys = _tableSql_table.primary_keys
        else:
            print_error("%s无法替换为%s" % (self.table, _tableSql_table))

    def add_attribute(
            self,
            _attribute_name: str,
            _attribute_type: str,
            _attribute_long=None,
            default=None,
            is_not_null=False,
            is_primary_key=False,
            is_auto=False,
            is_unique=False,
            is_unsigned=False
    ):
        """
        添加字段
        :param _attribute_name: [str] 字段名
        :param _attribute_type: [str] 字段类型
        :param _attribute_long: [int] or [tuple, list] 字段长度
        :param default: 字段默认值
        :param is_not_null: 字段非空设置
        :param is_primary_key: 字段主键设置
        :param is_auto: 字段自增设置
        :param is_unique: 字段非空设置
        :param is_unsigned: 字段无符号设置
        :return: 无
        """
        if _attribute_type.upper() in char_list:
            if default is not None:
                default = '"%s"' % default
        elif _attribute_type.upper() in type_used_long_1:
            if isinstance(_attribute_long, int):
                pass
            else:
                print_warning("%s: 该字段需要输入一位长度，目前默认值为255" % _attribute_type)
                _attribute_long = 255
        elif _attribute_type.upper() in type_used_long_2:
            if _attribute_long is None:
                print_warning("%s: 该字段需要输入二位长度，目前默认值为(5,2)" % _attribute_type)
                _attribute_long = (5, 2)
            elif isinstance(_attribute_long, int):
                print_warning("%s: 该字段需要输入二位长度，目前默认值为(%s,2)" % (_attribute_type, _attribute_long))
                _attribute_long = (_attribute_long, 2)
            elif isinstance(_attribute_long, Iterable):
                _attribute_long = [
                    long_temp for long_temp in _attribute_long if isinstance(long_temp, int)
                ]
                if len(_attribute_long) == 2:
                    pass
                else:
                    print_warning("%s: 该字段需要输入二位长度，目前默认值为(5,2)" % _attribute_type)
                    _attribute_long = (5, 2)
            else:
                print_warning("%s: 该字段需要输入二位长度，目前默认值为(5,2)" % _attribute_type)
                _attribute_long = (5, 2)
        else:
            if _attribute_long is not None:
                print_warning("%s: 该字段不需要输入长度" % _attribute_type)
            _attribute_long = None
        self.attribute.append(_attribute_name)
        self.attribute_info_list.append({
            "name": _attribute_name,
            "type": _attribute_type,
            "long": _attribute_long,
            "notnull": is_not_null,
            "primarykey": is_primary_key,
            "auto": is_auto,
            "unique": is_unique,
            "unsigned": is_unsigned,
            "default": default
        })
        if is_primary_key:
            self.primary_keys.append(_attribute_name)

    def create_language(self):
        """
        生成创建表语句
        :return: SQL语句（str）
        """
        _create_language = ""
        for attribute in self.attribute_info_list:
            if attribute["long"] is None:
                _create_language += "`%s` %s" % (attribute["name"], attribute["type"])
            elif isinstance(attribute["long"], int):
                _create_language += "`%s` %s(%s)" % (attribute["name"], attribute["type"], attribute["long"])
            else:
                _create_language += "`%s` %s(%s,%s)" % (
                    attribute["name"], attribute["type"], attribute["long"][0], attribute["long"][1])

            if attribute["type"].upper() in int_list:
                if attribute["unsigned"]:
                    _create_language += " UNSIGNED"
                if attribute["auto"]:
                    _create_language += " AUTO_INCREMENT"

            if attribute["notnull"] and not attribute["primarykey"]:
                _create_language += " NOT NULL"

            if attribute["unique"]:
                _create_language += " UNIQUE"

            if attribute["default"] is not None:
                _create_language += " DEFAULT %s" % attribute["default"]
            _create_language += ","
        if self.primary_keys:
            _create_language += "PRIMARY KEY("
            for primary_key in self.primary_keys:
                _create_language += "`%s`," % primary_key
        if _create_language != "":
            _create_language = _create_language[:-1] + ")"
            _create_language_temp = """CREATE TABLE %s (%s)ENGINE=%s DEFAULT CHARSET=%s""" % (
                self.table, _create_language, self.engine, self.charset)
        else:
            _create_language_temp = """CREATE TABLE %s ENGINE=%s DEFAULT CHARSET=%s""" % (
                self.table, self.engine, self.charset)
        return _create_language_temp

    def __str__(self):
        return self.table

    def __repr__(self):
        return self.__str__()

    def belong(self, tableSql_table):
        """
        判断数据表类型归属
        用于创建数据表时判断重复问题
        所有非主键的字段全属于另一个表
        :param tableSql_table:
        :return:
        """
        if isinstance(tableSql_table, TableSql):
            for attribute in self.attribute_info_list:
                if not attribute["primarykey"]:
                    if attribute not in tableSql_table.attribute_info_list:
                        return False
            return True
        else:
            return False

    def belong_list(self, *tableSql_list):
        for table in tableSql_list:
            if self.belong(table):
                return True
        return False

    def add_same_table_list(self, *tableSql_list):
        if self.belong_list(*tableSql_list):
            return tableSql_list
        else:
            for tableSql_temp_i in tableSql_list:
                if tableSql_temp_i.belong(self):
                    tableSql_temp_i.reset(self)
                    return tableSql_list
            tableSql_list += (self,)
            return tableSql_list


def add_table_list(tableSql_list_1: list or tuple, tableSql_list_2: list):
    """
    :param tableSql_list_1:
    :param tableSql_list_2: 添加之前确保该列表符合唯一
    :return:
    """
    for tableSQL_table in tableSql_list_1:
        tableSql_list_2 = tableSQL_table.add_same_table_list(*tableSql_list_2)
    return tableSql_list_2


class DataSql:
    """
    数据类
    """

    def __init__(self, _database, _table_name, _attribute=None, _key_list=None, _datas=None, find_info=None):
        """
        :param _database: [DatabaseSql] 数据库
        :param _table_name: [str] 数据表名
        :param _attribute: [tuple/list/Cursor] 数据表字段
        :param _datas: [tuple/list] 数据
        :param find_info: [any]] 查找范围，转变成list[dict]格式
        :return: 无
        """
        self.database = _database
        self.table = _table_name
        self.pri_key_list = _key_list
        self.attribute = _attribute
        self.value_list = _datas
        self.find_info = find_info

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        if value is None:
            self.__database = DatabaseSql()
        elif isinstance(value, DatabaseSql):
            self.__database = value
        else:
            print_error("数据库字段数据种类错误")

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        if value is None:
            self.__attribute = list()
        elif isinstance(value, Cursor):
            if self.table:
                value.execute(attribute_find_sql % (self.database.database, self.table))
                results = value.fetchall()
                value.execute(
                    """SHOW KEYS FROM `%s` WHERE Key_name = 'PRIMARY'""" % self.table)
                self.__pri_key_list = list(
                    map(
                        lambda x: x[4],
                        value.fetchall()
                    )
                )
                self.__attribute = list(map(lambda x: x[0], results))
            else:
                self.__attribute = list()
        elif isinstance(value, Iterable):
            self.__attribute = list(value)
        else:
            print_error("属性字段数据种类错误")

    def add_attribute(self, value):
        if value is None:
            pass
        elif isinstance(value, str):
            self.__attribute.append(value)
        elif isinstance(value, Iterable):
            self.__attribute.extend(list(value))
        else:
            print_error("属性字段数据种类错误")

    @property
    def value_list(self):
        return self.__value_list

    @property
    def data_list(self):
        if not self.__data_list:
            self.data_list = True
        return self.__data_list

    @value_list.setter
    def value_list(self, value):
        if value is None:
            self.__value_list = list()
            self.__data_list = list()
        elif isinstance(value, Iterable):
            if value:
                self.__value_list = list(value)
                self.__data_list = list()
            else:
                self.__data_list = list()
                self.__value_list = list()
        else:
            print_error("属性字段数据种类错误")

    @data_list.setter
    def data_list(self, value):
        if value:
            if self.attribute:
                self.__data_list = list(
                    map(lambda x: {self.attribute[i]: x[i] for i in range(len(self.attribute))}, self.value_list)
                )
            else:
                self.__data_list = list(
                    map(lambda x: {"attr_%s" % i: x[i] for i in range(len(self.value_list[0]))}, self.value_list)
                )
        else:
            self.__data_list = list()

    def add_value(self, value):
        if value:
            self.__value_list.append(tuple(value))

    def add_values(self, values):
        if values:
            self.__value_list.extend(values)

    @property
    def pri_key_list(self):
        return self.__pri_key_list

    @pri_key_list.setter
    def pri_key_list(self, value):
        if value:
            if isinstance(value, bool):
                cur = self.database.connect().cursor()
                cur.execute(
                    """SHOW KEYS FROM `%s` WHERE Key_name = 'PRIMARY'""" % self.table)
                self.__pri_key_list = list(
                    map(
                        lambda x: x[4],
                        cur.fetchall()
                    )
                )
                cur.close()
            elif isinstance(value, Iterable):
                self.__pri_key_list = list(value)
        else:
            self.__pri_key_list = []

    @property
    def find_info_pri_key(self):
        if self.pri_key_list:
            return self.get_dic(*self.pri_key_list)
        return []

    @property
    def find_info(self):
        return self.__find_info

    @find_info.setter
    def find_info(self, value):
        if value is None:
            self.__find_info = []
        elif isinstance(value, str):
            if value.lower() == "pri":
                cur = self.database.connect().cursor()
                cur.execute(
                    """SHOW KEYS FROM `%s` WHERE Key_name = 'PRIMARY'""" % self.table)
                primary_key_list = list(
                    map(
                        lambda x: x[4],
                        cur.fetchall()
                    )
                )
                cur.close()
                for primary_key_temp in primary_key_list:
                    if primary_key_temp not in self.attribute:
                        raise AttributeError("没有找到对应的主键数据")
                self.__find_info = self.get_dic(*primary_key_list)
            else:
                self.__find_info = _find_info_read(value)
        elif isinstance(value, dict):
            self.__find_info = []
            if value:
                self.find_info.append(value)
        elif isinstance(value, Iterable):
            self.__find_info = []
            for find_info_temp_dict in value:
                if isinstance(find_info_temp_dict, dict):
                    if find_info_temp_dict:
                        self.__find_info.append(find_info_temp_dict)
                else:
                    raise TypeError("find_info列表需要字典格式数据")
        else:
            raise TypeError("数据库字段数据种类错误")

    def __str__(self):
        return self.table

    def show(self):
        """
        展示数据

        :return:
        """
        if self.is_empty():
            print_warning("没有数据")
        else:
            print_data(self.attribute)
            for data_line in self.value_list:
                print_data(data_line)

    def add(self, data_dataSql):
        """
        数据集加，只支持相同字段的数据集

        :param data_dataSql: [DataSql]
        :return:
        """
        if isinstance(data_dataSql, DataSql):
            if self.database == data_dataSql.database and self.table == data_dataSql.table:
                if self.find_info and data_dataSql.find_info:
                    is_need_warning_print = True
                    for find_info_temp in data_dataSql.find_info:
                        if find_info_temp in self.find_info:
                            if is_need_warning_print:
                                print_warning("将会对数据去重，请注意后续操作")
                                is_need_warning_print = False
                        else:
                            self.find_info.append(find_info_temp)
                    all_value_list = list(set(data_dataSql.value_list + self.value_list))
                    self.value_list = all_value_list
                else:
                    raise OverflowError("对拥有全数据的数据表无需使用add")
            else:
                raise AttributeError("Not same table")
        else:
            raise TypeError("Not DataSql.")

    def first(self):
        if self.value_list:
            return self.data_list[0]
        else:
            return {}

    def get(self, *args):
        """
        获取对应字段的数据集

        :param args:
        :return:
        """
        if not args:
            return self.value_list
        elif len(args) == 1:
            return [
                data_line.get(args[0], None) for data_line in self.data_list
            ]
        else:
            return [
                [data_line.get(arg, None) for arg in args] for data_line in self.data_list
            ]

    # 仅限于单一key唯一
    def get_dic(self, *args, _model="LD", **kwargs) -> list or dict:
        """key_name=None, data_dic=None,
        获取以args属性为目标的数据集，可采用下列方式对数据集排布进行限制，不采用则使用正常排布

        模式LD(list-dict)为列表: [{key1=, key2=, .}, {key1=, key2=, .}]

        模式DL(dict-list)为字典: {key1=[],key2=[]}

        以上两种模式可以在后面添加参数使得原字段被重新命名：old_name = new_name

        模式Key(dict-by-key)为字典: {key1: value1, key2: value2 } value = {arg: get(arg) for arg in args} or get(arg)
        需要参数：key_name="key"

        默认为list-dict
        """
        if isinstance(_model, str):
            if _model == "LD":
                if args:
                    return list(
                        map(lambda x: {kwargs.get(arg, arg): x.get(arg, None) for arg in args}, self.data_list)
                    )
                else:
                    return list(
                        map(lambda x: {
                            kwargs.get(arg, arg): x.get(arg, None) for arg in self.attribute}, self.data_list)
                    )
            elif _model == "DL":
                if args:
                    return {
                        kwargs.get(attr, attr): list(
                            map(lambda x: x.get(attr, None), self.data_list)) for attr in args
                    }
                else:
                    return {
                        kwargs.get(attr, attr): list(
                            map(lambda x: x.get(attr, None), self.data_list)) for attr in self.attribute
                    }
            elif _model.lower() == "key":
                key_name = kwargs.get("key_name")
                data_index = 0

                def unique_id(name="no_key"):
                    """
                    获取唯一名称
                    """
                    nonlocal data_index
                    data_index += 1
                    return "%s_%s" % (name, data_index)

                if key_name:
                    if args:
                        if len(args) == 1:
                            return {
                                data_line.get(
                                    key_name, unique_id(key_name)
                                ): data_line.get(args[0], None) for data_line in self.data_list
                            }
                        else:
                            return {
                                data_line.get(
                                    key_name, unique_id(key_name)
                                ): {
                                    arg: data_line.get(arg, None) for arg in args if arg != key_name
                                } for data_line in self.data_list
                            }
                    else:
                        return {
                            data_line.get(
                                key_name, unique_id(key_name)
                            ): {
                                arg: data_line.get(arg, None) for arg in self.attribute if arg != key_name
                            } for data_line in self.data_list
                        }
                else:
                    print_warning("没有输入key值")
                    if args:
                        if len(args) == 1:
                            return {
                                unique_id(key_name): data_line.get(args[0], None) for data_line in self.data_list
                            }
                        else:
                            return {
                                unique_id(key_name): {
                                    arg: data_line.get(arg, None) for arg in args if arg != key_name
                                } for data_line in self.data_list
                            }
                    else:
                        return {
                            unique_id(key_name): {
                                arg: data_line.get(arg, None) for arg in self.attribute if arg != key_name
                            } for data_line in self.data_list
                        }
            elif _model.lower() == "dict":
                dict_input = kwargs.get("data_dict")
                if dict_input:
                    if args:
                        """
                        获取dict_input的结构然后代入
                        """
                        pass
                    else:
                        pass
                else:
                    print_warning("data_dict not find.")
                    return self.get_dic(*args, _model="key", key_name="not_find_dict")
            else:
                print_warning("没有找到对应模式，使用默认使用LD模式")
                return self.get_dic(*args, _model="LD", **kwargs)

    def read_file(self, filename, _encoding=None, _sep=" "):
        if self.is_empty():
            with open(filename, "r", encoding=_encoding) as f:
                first_line = f.readline()
                self.attribute = first_line.split(_sep)
                results = list()
                for data_line in f.readlines():
                    results.append(data_line.split(_sep))
                self.value_list = results
                f.close()
        else:
            print_error("该数据类非空，请使用空数据类读取")

    def is_empty(self):
        return not self.value_list

    def insert_sql(self, need_clear=False):
        temp_db = self.database.connect()
        temp_cur = temp_db.cursor()
        _insert_language_temp_0 = """INSERT INTO `%s` (`%s`) VALUES (""" % (
            self.table,
            "`,`".join(self.attribute)
        )
        _insert_language_temp_1 = "%s," * len(self.attribute)
        _insert_language = "%s%s)" % (_insert_language_temp_0, _insert_language_temp_1[:-1])
        try:
            if not self.is_empty():
                temp_cur.executemany(_insert_language, self.value_list)
                temp_db.commit()
                temp_cur.close()
                temp_db.close()
                if need_clear:
                    self.value_list = None
        except Exception as e:
            temp_db.rollback()
            print_error(e)
            print_error(_insert_language)
            temp_cur.close()
            temp_db.close()

    def update_sql(self, *args, need_clear=False):
        if args:
            for arg in args:
                if arg not in self.attribute:
                    print_error("没有找到对应字段，更新失败")
                    return
            arg_index = 0
            value_index_list = []
            temp_index_list = []
            for attr in self.attribute:
                if attr in args:
                    temp_index_list.append(arg_index)
                else:
                    value_index_list.append(arg_index)
                arg_index += 1
            value_index_list += temp_index_list
            temp_db = self.database.connect()
            temp_cur = temp_db.cursor()
            update_language_0 = "UPDATE `%s` SET " % self.table
            update_language_1 = "`=(%s),".join([attr for attr in self.attribute if attr not in args])
            update_language_2 = "`=(%s) and `".join(args)
            update_language = """%s`%s WHERE `%s""" % (
                update_language_0, update_language_1 + "`=(%s)", update_language_2 + "`=(%s)")
            if not self.is_empty():
                value_sort_by_arg = [tuple([
                    value_line[i] for i in value_index_list
                ]) for value_line in self.value_list]
                try:
                    temp_cur.executemany(update_language, value_sort_by_arg)
                    temp_db.commit()
                    temp_cur.close()
                    temp_db.close()
                    if need_clear:
                        self.value_list = None
                except Exception as e:
                    temp_db.rollback()
                    print_error(e)
                    print_error(update_language)
                    temp_cur.close()
                    temp_db.close()
            else:
                print_warning("没有找到要执行的数据")
        else:
            print_error("需要指定用于查询的字段在args里")

    def update(self):
        if self.pri_key_list:
            # 由于更改了数据因此原find_info失效，所以使用主键字典列表作为find_info
            self.find_info = self.find_info_pri_key
            self.update_sql(*self.pri_key_list, need_clear=False)
        else:
            print_error("没有设置主键，无法更新")


class MysqlThread(threading.Thread):
    def __init__(self, threadID, database, sql_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.database = database
        self.db = True
        self.sql_list = sql_list
        self.error_list = []

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        if isinstance(value, DatabaseSql):
            self.__database = value
        else:
            raise TypeError("MysqlThread必须使用Database类型的数据库")

    @property
    def cursor(self):
        return self.__cursor

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, value):
        if value is None:
            self.__db = None
            self.__cursor = None
        elif isinstance(value, bool):
            if value:
                self.__db = self.database.connect()
                self.__cursor = self.__db.cursor()
            else:
                self.__cursor.close()
                self.__db.close()
                self.__db = None
                self.__cursor = None
        else:
            print_error("<db>不能自行设置")

    def run(self):
        for sql_key, sql_value in self.sql_list:
            try:
                if sql_key != "sql":
                    self.cursor.executemany(sql_key, sql_value)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                self.error_list.append((sql_key, sql_value[0]))
        try:
            for sql_language in self.sql_list["sql"]:
                self.cursor.execute(sql_language)
            self.db.commit()
            return
        except:
            self.db.rollback()
        for sql_language in self.sql_list["sql"]:
            try:
                self.cursor.execute(sql_language)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                self.error_list.append(sql_language)
        self.db = False

    def get_error(self):
        threading.Thread.join(self)
        return self.error_list


class EasySql:
    """
    主功能类，利用前面结构类进行简化
    """

    def __init__(
            self, database=None, _database_name=None, _user=None, _passwd=None, _host=None, _port=None, **kwargs
    ):
        """
        初始化连接数据库，推荐使用数据库类构造后调用本函数

        :param database: [DatabaseSql/None] 数据库类，输入该类则不识别其他参数，其他参数的作用就是创建数据库类
        :param _database_name: [str/None]
        :param _user: [str/None]
        :param _passwd: [str/None]
        :param _host: [str/None]
        :param _port: [int/None]
        :param kwargs: 其他参数

        :return:
        """
        if isinstance(database, DatabaseSql):
            self.database = database
        else:
            if _user is None:
                _user = "root"
            if _passwd is None:
                _passwd = "123456"
            if _host is None:
                _host = "localhost"
            if _port is None:
                _port = 3306
            self.database = DatabaseSql(
                _database_name=_database_name,
                _user=_user,
                _passwd=_passwd,
                _host=_host,
                _port=_port,
                **kwargs
            )
        self.db = True
        self.sql_list = {
            "sql": [],
        }
        self.error_list = []
        self.thread_index = 0
        self.thread_dic = {}

    @property
    def cursor(self):
        return self.__cursor

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, value):
        if value is None:
            self.__db = None
            self.__cursor = None
        elif isinstance(value, bool):
            if value:
                self.__db = self.database.connect()
                self.__cursor = self.__db.cursor()
            else:
                self.__cursor.close()
                self.__db.close()
                self.__db = None
                self.__cursor = None
        else:
            print_error("<db>不能自行设置")

    def start(self):
        self.db = True

    def end(self):
        self.db = False

    def __del__(self):
        self.db = False

    def use(self, database_name):
        self.db = False
        self.database.database = database_name
        self.db = True

    def creat(self, *args, _table_name=None, _last_table_name=None, _child_deep=0, **kwargs):
        """
        根据字典创建数据表（可匹配JSON使用）只能创建简单表

        表名：输入则为输入，不输入则：1. 字典仅为1层时取第一层的键为表名 2. 1失败则使用默认名
        方式：若为纯字典格式，则直到最后一次分层前都是前一层为表，后一层为值嵌套，若为列表格式，则列表内的值为数据
        主键为默认生成的自增id
        args和kwargs只能输入一项，均输入会优先使用args而不使用kwargs
        暂时不确定是否通用以及没有使用deep

        :param args: json列表
        :param _table_name:
        :param _last_table_name:
        :param _child_deep: _child_deep = x(>0) :进行x次分层; _child_deep = 0 :不进行分层; _child_deep = x(<0) :直到无法分层
        :param kwargs: json字典或自定义字典
        :return:
        """
        __table_name = ""
        _child_deep = 0  # 暂未实现迭代
        if _table_name is None:
            __table_name = self.get_temp_table_name(_last_table_name)
        else:
            __table_name = str(_table_name)
        __table_name_id = "%s_id" % __table_name
        dataSql_data = DataSql(self.database, __table_name)
        dataSql_data.attribute = [__table_name_id]
        attribute_value_type_dict = dict()
        if args:
            """
            列表元素一定是数据集
            """
            _temp_index = 0
            for __dict_arg in args:
                if isinstance(__dict_arg, dict):
                    _temp_data_dict = dict()
                    for _key, _value in __dict_arg:
                        if _key not in dataSql_data.attribute and _value is not None:
                            dataSql_data.add_attribute(_key)
                            attribute_value_type_dict[_key] = get_mysql_type(_value)
                        if _child_deep == 0:
                            _temp_data_dict[_key] = _value
                        else:
                            if isinstance(_value, list):
                                """
                                使用args新构建一个表，并在之后该字段都使用该表储存，该字段储存对应主键，每次使用对应deep减1
                                """
                                _temp_data_dict[_key] = _value
                                pass
                            elif isinstance(_value, dict):
                                """
                                使用kwargs新构建一个表，并在之后该字段都使用该表储存，该字段储存对应主键，每次使用对应deep减1
                                """
                                _temp_data_dict[_key] = _value
                                pass
                            else:
                                _temp_data_dict[_key] = _value
                    dataSql_data.data_list.append(_temp_data_dict)
                    _temp_index += 1
                else:
                    print_warning("未能读取对应的数据格式，跳过该行")
        elif kwargs:
            """
            字典元素如果字段相似则仍为数据集，字典的键设为主键，如果不相似则为字段
            """
            _temp_index = 0
            for _key, _value in kwargs:
                _temp_data_dict = dict()
                if _key not in dataSql_data.attribute and _value is not None:
                    dataSql_data.add_attribute(_key)
                    attribute_value_type_dict[_key] = get_mysql_type(_value)
                if _child_deep == 0:
                    _temp_data_dict[_key] = _value
                else:
                    if isinstance(_value, list):
                        """
                        使用args新构建一个表，并在之后该字段都使用该表储存，该字段储存对应主键，每次使用对应deep减1
                        """
                        _temp_data_dict[_key] = _value
                        pass
                    elif isinstance(_value, dict):
                        """
                        使用kwargs新构建一个表，并在之后该字段都使用该表储存，该字段储存对应主键，每次使用对应deep减1
                        """
                        _temp_data_dict[_key] = _value
                        pass
                    else:
                        _temp_data_dict[_key] = _value
                dataSql_data.data_list.append(_temp_data_dict)
                _temp_index += 1
            pass
        else:
            print_error("没有可以使用的数据")
        # 创建数据表
        tableSql_table = TableSql(__table_name)
        tableSql_table.add_attribute(__table_name_id, "INT", is_primary_key=True)
        for _attribute_temp, _attribute_temp_type in attribute_value_type_dict:
            tableSql_table.add_attribute(_attribute_temp, _attribute_temp_type)
        _table_create_sql = tableSql_table.create_language()
        self.cursor.execute(_table_create_sql)
        self.db.commit()
        # 添加数据
        self.add(__table_name, data_dataSql=dataSql_data)

    def add(self, table_name="", data_dataSql=None, **kwargs):
        """
        添加数据

        :param table_name: [str] 数据表名
        :param data_dataSql: [DataSql/None] 添加整个数据集中的数据，与kwargs手动输入数据集冲突，不要同时使用
        :param kwargs: 字段=值 手动添加一条数据
        :return:
        """
        if isinstance(data_dataSql, DataSql):
            _insert_language_temp_0 = """INSERT INTO `%s` (`%s`) VALUES (""" % (
                table_name or data_dataSql.table,
                "`,`".join(data_dataSql.attribute)
            )
            _insert_language_temp_1 = "%s," * len(data_dataSql.attribute)
            _insert_language = "%s%s)" % (_insert_language_temp_0, _insert_language_temp_1[:-1])
            try:
                if not data_dataSql.is_empty():
                    self.cursor.executemany(_insert_language, data_dataSql.value_list)
                    self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                print_error(_insert_language)
            return
        else:
            _insert_language_temp_0 = """INSERT INTO `%s` (`%s`) VALUES (""" % (
                table_name,
                "`,`".join(kwargs.keys())
            )
            _insert_language_temp_1 = "%s," * len(kwargs)
            _insert_language = "%s%s)" % (_insert_language_temp_0, _insert_language_temp_1[:-1])
            self.add_sql(
                (_insert_language, [[value for value in kwargs.values()]])
            )

    def add_with_same_attr(self, table_name, *args, values=None):
        if table_name and args and isinstance(values, Iterable) and len(args) == len(values[0]):
            _insert_language_temp_0 = """INSERT INTO `%s` (`%s`) VALUES (""" % (
                table_name,
                "`,`".join(args)
            )
            _insert_language_temp_1 = "%s," * len(args)
            _insert_language = "%s%s)" % (_insert_language_temp_0, _insert_language_temp_1[:-1])
            try:
                self.cursor.executemany(_insert_language, values)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                print_error(_insert_language)

    def add_list(self, table_name, data_list_long=None, **kwargs):
        """
        添加数据列

        :param table_name: [str] 数据表名
        :param data_list_long: [int/None] 数据长度，推荐输入
        :param kwargs: 字段=[值1, 值2, ...] 手动添加多条数据，检测列表长度最多的数或手动输入，其他值自动扩展，推荐手动输入防止自动检测错误
        :return:
        """
        if not isinstance(data_list_long, int) or data_list_long <= 0:
            temp_len_len = {}
            for key, value in kwargs.items():
                if isinstance(value, (list, tuple)):
                    temp_len = len(value)
                    if temp_len in temp_len_len:
                        temp_len_len[temp_len] += [key]
                    else:
                        temp_len_len[temp_len] = [key]
            data_list_long = max(temp_len_len, key=lambda x: len(temp_len_len[x]))
            key_for_list = temp_len_len[data_list_long]
        else:
            key_for_list = list()
            for key, value in kwargs.items():
                if len(value) == data_list_long:
                    key_for_list.append(key)
        result_temp = []
        for index_temp in range(data_list_long):
            kwargs_temp = []
            for key in kwargs.keys():
                if key in key_for_list:
                    kwargs_temp.append(kwargs[key][index_temp])
                else:
                    kwargs_temp.append(kwargs[key])
            result_temp.append(tuple(kwargs_temp))
        self.add_with_same_attr(table_name, *kwargs.keys(), result_temp)

    def delete(self, table_name, data_dataSql=None, **kwargs):
        """
        删除数据

        :param table_name:
        :param data_dataSql:
        :param kwargs:
        :return:
        """
        if isinstance(data_dataSql, DataSql):
            if data_dataSql.find_info:
                _delete_language = """DELETE FROM `%s` WHERE%s""" % (
                    data_dataSql.table, _find_info("AND", p1=data_dataSql.find_info_pri_key))
            else:
                _delete_language = """DELETE FROM `%s`""" % data_dataSql.table
            self.add_sql(
                _delete_language
            )
        else:
            if kwargs:
                findInfo = _find_info(find_model="AND", **kwargs)
                _delete_language = """DELETE FROM `%s` WHERE%s""" % (table_name, findInfo)
            else:
                _delete_language = """DELETE FROM `%s`""" % table_name
            self.add_sql(
                _delete_language
            )

    def show(self, *args):
        """
        展示数据
        :param args:
        """

    def find(self, *args, table_name="", **kwargs):
        """
        查找数据

        :param table_name:
        :param kwargs:
        :return:
        """
        if not table_name:
            return
        select_str = "*" if not args else ",".join(args)
        if kwargs:
            find_info = _find_info(find_model="AND", **kwargs)
            _find_language = """SELECT %s FROM `%s` WHERE%s""" % (select_str, table_name, find_info)
            return_data = DataSql(
                self.database, table_name,
                _attribute=args or self.cursor,
                _datas=self.get_data(_find_language),
                find_info=kwargs)
        else:
            _find_language = """SELECT %s FROM `%s`""" % (select_str, table_name)
            return_data = DataSql(
                self.database, table_name,
                _attribute=args or self.cursor,
                _datas=self.get_data(_find_language),
                find_info=None)
        return_data.data_list = True
        return return_data

    def find_by_sql_str(self, *args, table_name="", sql_str=""):
        if not table_name:
            return
        select_str = "*" if not args else ",".join(args)

        if sql_str:
            return_data = DataSql(
                self.database,
                table_name,
                _attribute=args or self.cursor,
                _datas=self.get_data("""SELECT %s FROM `%s` WHERE %s""" % (select_str, table_name, sql_str)),
                find_info=sql_str
            )
        else:
            return_data = DataSql(
                self.database,
                table_name,
                _attribute=args or self.cursor,
                _datas=self.get_data("""SELECT %s FROM `%s`""" % (select_str, table_name)),
                find_info=None
            )
        return_data.data_list = True
        return return_data

    def update(self, table_name="", find_info=None, **update_datas):
        """
        :param table_name:
        :param find_info:
        :param update_datas:
        :return:
        """
        if not update_datas:
            print_warning("没有要更新的数据！")
            return
        if find_info is None:
            return self.add(table_name=table_name, **update_datas)
        else:
            _update_language = """UPDATE `%s` SET %s"""
            temp_update_language = """"""
            for key, value in update_datas.items():
                if isinstance(value, str):
                    temp_update_language += """`%s`="%s",""" % (key, value.replace('"', "'"))
                else:
                    temp_update_language += """`%s`=%s,""" % (key, value)
            if isinstance(find_info, str):
                if find_info:
                    if find_info[0] != " ":
                        find_info = " %s" % find_info
                    self.add_sql(
                        _update_language % (table_name, temp_update_language[:-1]) + """ WHERE%s""" % find_info
                    )
                else:
                    self.add_sql(
                        _update_language % (table_name, temp_update_language[:-1])
                    )
            # elif isinstance(find_info, DataSql):
            #     if find_info.find_info:
            #         self.add_sql(
            #             _update_language % (
            #                 find_info.table, temp_update_language[:-1]) + """ WHERE%s""" % _find_info(
            #                 "AND", p1=find_info.find_info_pri_key)
            #         )
            #
            #         find_info.update(**update_datas)
            #     else:
            #         self.add_sql(
            #             _update_language % (find_info.table, temp_update_language[:-1])
            #         )
            #
            #         find_info.update(**update_datas)
            elif isinstance(find_info, dict):
                if find_info:
                    self.add_sql(
                        _update_language % (
                            table_name,
                            temp_update_language[:-1]
                        ) + """ WHERE%s""" % _find_info(find_model="AND", **find_info)
                    )
                else:
                    self.add_sql(
                        _update_language % (
                            table_name,
                            temp_update_language[:-1]
                        ))
            else:
                print_error("未找到适用的更新值，请确认find_info值是否正确")

    def update_values(self, *args, table_name="", find_info=None, update_datas=None):
        if args and table_name and find_info and update_datas and isinstance(update_datas, Iterable):
            if isinstance(find_info, str):
                find_info_used = _find_info_read(find_info).keys()
            elif isinstance(find_info, dict):
                find_info_used = find_info.keys()
            elif isinstance(find_info, Iterable):
                find_info_used = find_info
            else:
                print_error("未找到适用的更新值，请确认find_info值是否正确")
                return
            update_language_0 = "UPDATE `%s` SET " % table_name
            update_language_1 = "`=(%s),".join(args)
            update_language_2 = "`=(%s) and `".join(find_info_used)
            update_language = """%s`%s WHERE `%s""" % (
                update_language_0, update_language_1 + "`=(%s)", update_language_2 + "`=(%s)")
            try:
                self.cursor.executemany(update_language, update_datas)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                print_error(update_language)

    def add_sql(self, *sql_list):
        """
        sql_list: str or list(sql, values)
        """
        for sql in sql_list:
            if isinstance(sql, str):
                self.sql_list["sql"].append(sql)
            elif isinstance(sql, dict):
                for sql_key, sql_values in sql.items():
                    self.add_sql((sql_key, sql_values))
            elif isinstance(sql, Iterable):
                if sql[0] in self.sql_list.keys():
                    self.sql_list[sql[0]].extend(sql[1])
                else:
                    self.sql_list[sql[0]] = sql[1]
            else:
                raise TypeError("无法识别sql语句")

    def show_sql(self, index: int = None):
        if index is None:
            print_data("%s\n".join(self.sql_list["sql"]))
        else:
            print_data("%s: %s" % (index, self.sql_list["sql"][index]))

    def delete_sql(self):
        self.sql_list = {
            "sql": []
        }

    def execute(self, sql: str):
        """
        执行并提交事务

        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print_error(e)
            print_error(sql)

    def commit(self):
        """
        批量执行并提交已储存事务

        :return:
        """
        for sql_key, sql_value in self.sql_list:
            try:
                if sql_key != "sql":
                    self.cursor.executemany(sql_key, sql_value)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                self.error_list.append((sql_key, sql_value[0]))
        try:
            for sql_language in self.sql_list["sql"]:
                self.cursor.execute(sql_language)
            self.db.commit()
        except:
            self.db.rollback()
        else:
            self.delete_sql()
            return
        for sql_language in self.sql_list["sql"]:
            try:
                self.cursor.execute(sql_language)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print_error(e)
                self.error_list.append(sql_language)
        self.delete_sql()

    # 不推荐创建太多，因为没有对数据库连接进行异步，因此可能报连接错误
    def commit_with_thread(self):
        """
        使用多线程批量执行已储存事务（sql语句不冲突才可使用），返回创建的线程，可自行阻塞
        不推荐创建太多，因为没有对数据库连接进行异步，因此可能报连接错误
        """
        print_warning("已创建线程连接数据库，这可能花费较长时间")
        thread_temp = MysqlThread(self.thread_index, self.database, self.sql_list)
        thread_temp.start()
        self.delete_sql()
        return thread_temp

    def get_data(self, sql: str):
        """
        查找事务并返回数据

        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.db.rollback()
            print_error(e)
            print_error(sql)
        else:
            return self.cursor.fetchall()

    def get_temp_table_name(self, _last_table_name=None):
        self.cursor.execute(table_find_sql % self.database.database)
        results = self.cursor.fetchall()
        table_name_list_temp = tuple(map(lambda x: x[0], results))
        __index_temp = 0
        __temp_table_name = "temp_table_name_" if _last_table_name is None else "%s_" % _last_table_name
        while True:
            __temp_name = "%s%s" % (__temp_table_name, __index_temp)
            if __temp_name in table_name_list_temp:
                __index_temp += 1
            else:
                return __temp_name

    def get_primary_key(self, table_name):
        primary_key_list = list(
            map(
                lambda x: x[4],
                self.get_data("""SHOW KEYS FROM `%s` WHERE Key_name = 'PRIMARY'""" % table_name)
            )
        )
        return primary_key_list

    def get_attribute(self, table_name):
        return list(map(lambda x: x[0], self.get_data(attribute_find_sql % (self.database.database, table_name))))

    def get_table_name(self):
        return list(map(lambda x: x[0], self.get_data(table_find_sql % self.database.database)))


def _find_info(find_model="AND", **keys):
    """
    合成条件语句

    :param find_model: ["AND"/"OR"]
    :param keys: [dict]
    :key types:
    - AND :
    - - _find_info("AND", key1=value1, key2=value2, ...): find key1=value1 and key2=value2 and ...
    - - [only one param can put list type]  _find_info("AND", key1=[value1, value2, ...], ...):
        find (key1=value1 and ...) or (key1=value2 and ...) or ...
    - - [only one param can put list type]  _find_info("AND", param1=[{key1=value1, key2=value2, ...}, {key1=value2, key3=value4, ...}], key4=value5, ...):
        find ((key1=value1 and key2=value2 and ...) or (key1=value2 and key3=value4 and ...) or ...) and key4=value5
    - OR :
    - - _find_info("OR", key1=value1, key2=value2, ...): find key1=value1 or key2=value2 or ...
    - - [param_name can be any str, and it is not used]
        _find_info("OR", param1={key1=value1, key2=value2, ...}, param2={key1=value2, key3=value4, ...}, ...):
        find (key1=value1 and key2=value2 and ...) or (key1=value2 and key3=value4 and ...) or ...
    :return:
    """
    if keys:
        find_info = ""
        if find_model == "AND":
            temp_or_key = None
            temp_or_list = None
            for find_key, find_value in keys.items():
                if isinstance(find_value, dict):
                    print_error("AND模式不支持该类型的数据！\n%s: %s" % (find_key, find_value))
                    raise TypeError
                elif isinstance(find_value, str):
                    find_info += """ `%s`=%s AND""" % (find_key, find_value.replace('"', "'"))
                elif isinstance(find_value, Iterable):
                    if temp_or_list is not None:
                        print_error("AND模式不支持多个参数使用list格式，如需要多个参数，请使用list[dict]格式")
                        raise TypeError
                    else:
                        temp_or_key = find_key
                        temp_or_list = find_value
                else:
                    find_info += """ `%s`=%s AND""" % (find_key, find_value)
            if temp_or_list:
                if isinstance(temp_or_list[0], dict):
                    or_find_info = ""
                    for or_value_i in temp_or_list:
                        if not isinstance(or_value_i, dict):
                            raise TypeError
                        or_find_info += find_info + _find_info(find_model="AND", **or_value_i) + " OR"
                    return or_find_info[:-3]
                else:
                    or_find_info = ""
                    for or_value_i in temp_or_list:
                        if isinstance(or_value_i, dict):
                            raise TypeError
                        if isinstance(or_value_i, str):
                            or_find_info += find_info + """ `%s`=%s OR""" % (temp_or_key, or_value_i.replace('"', "'"))
                        else:
                            or_find_info += find_info + """ `%s`=%s OR""" % (temp_or_key, or_value_i)
                    return or_find_info[:-3]
            else:
                return find_info and find_info[:-4]
        elif find_model == "OR":
            for find_key, find_value in keys.items():
                if isinstance(find_value, dict):
                    _find_info_temp_str = _find_info(find_model="AND", **find_value)
                    if _find_info_temp_str:
                        find_info += _find_info_temp_str + " OR"
                elif isinstance(find_value, str):
                    find_info += """ `%s`=%s OR""" % (find_key, find_value.replace('"', "'"))
                elif isinstance(find_value, Iterable):
                    print_error("AND模式不支持该类型的数据！\n%s: %s" % (find_key, find_value))
                    raise TypeError
                else:
                    find_info += """ `%s`=%s OR""" % (find_key, find_value)
            return find_info[:-3]
        else:
            print_error("只有AND或OR模式！")
            raise TypeError
    else:
        return ""


def _find_info_read(find_info_str):
    if isinstance(find_info_str, str):
        if find_info_str:
            find_info_list = find_info_str.split("OR")
            if len(find_info_list) == 1:
                find_info_list = find_info_list[0].split("AND")
                find_info_dict = dict()
                for find_info_split in find_info_list:
                    find_info_split.strip()
                    if find_info_split:
                        find_key, find_value = find_info_split.split("`=")
                        find_info_dict[find_key[:-1]] = __return_value(find_value)
                return [find_info_dict]
            else:
                find_info_return = list()
                for find_info_split in find_info_list:
                    find_info_split.strip()
                    if find_info_split:
                        find_info_return += _find_info_read(find_info_split)
                return find_info_return
        else:
            return {}
    else:
        raise TypeError("无法识别非字符串类型")


def _find_info_update(find_info_list=None, **find_info_kwargs):
    if find_info_list:
        if isinstance(find_info_list, Iterable):
            for find_info_dict in find_info_list:
                for update_key, update_value in find_info_kwargs.items():
                    if update_key in find_info_dict:
                        find_info_dict[update_key] = update_value
            return find_info_list
        else:
            raise TypeError("find_info must a list.")
    else:
        return [find_info_kwargs]


def __return_value(value: str):
    try:
        if value:
            if value[0] == '"':
                return value.strip('"')
            elif value.isdigit() or (value[0] == "-" and value[1:].isdigit()):
                return int(value)
            elif value == "True":
                return True
            elif value == "False":
                return False
            else:
                value_split = value.split(".")
                if len(value_split) == 2:
                    if (
                            value_split[0].isdigit() or (value_split[0][0] == "-" and value_split[0][1:].isdigit())
                    ) and value_split[1].isdigit():
                        return float(value)
                print_error("没有识别到对应值%s" % value)
                raise TypeError
        else:
            return None
    except Exception as e:
        print_error("转换失败\n%s" % e)
        raise TypeError


def get_mysql_type(value):
    return mysql_type_to.get(type(value), "VARCHAR")


def _chunks(list_split, num):
    _div, _mod = divmod(len(list_split), num)
    for i in range(num):
        _split = (_div + 1) * (i if i < _mod else _mod) + _div * (0 if i < _mod else i - _mod)
        yield list_split[_split:_split + (_div + 1 if i < _mod else _div)]


def _print_running(max_num=3):
    num = 0
    while True:
        yield "." * (num + 1)
        num = (num + 1) % max_num


if __name__ == "__main__":
    db = EasySql(_database_name=None, _passwd="123456")
    db.update_values("1", table_name="test", find_info=["1", "2"], update_datas=[(1, 2, 3), (3, 4, 5)])
    pass
