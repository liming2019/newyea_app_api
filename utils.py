import json
import app
import pymysql


# 读取json文件数据并返回列表类型的数据
def read_param_data(file, method_name):
    data_list = []
    file_path = app.base_path + '/data/{}'.format(file)
    with open(file_path, encoding='utf-8') as f:
        # 读取json文件并转换为dict对象
        json_data = json.load(f)
        # 获取某个接口（key)的所有测试数据
        test_data = json_data.get(method_name)

        # 遍历列表
        for i in test_data:
            data_list.append(tuple(i.values()))
        return data_list


# 对响应数据进行断言
def assert_response(self, response, status_code, code, text):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(code, response.json().get("code"))
    if text is not None:
        self.assertEqual(text, response.json().get("text"))


class DBUtils:
    __conn = None
    __cursor = None

    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(user=app.db_user, password=app.db_password, host=app.db_localhost,
                                         port=app.db_localhost, database=app.db_database)
            return cls.__conn

    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    @classmethod
    def exe_sql(cls, sql):
        try:
            cursor = cls.__get_cursor()
            cursor.execute(sql)
            if sql.split()[0].lower() == 'select':
                return cursor.fetchall()
            else:
                cls.__cursor.commit()
                return cursor.rowcount
        except Exception as e:
            cls.__conn.rollback()
            print(e)
        finally:
            cls.__close_cursor()
            cls.__close_conn()

    @classmethod
    def __close_cursor(cls):
        if cls.__cursor is not None:
            cls.__cursor.close()
            cls.__cursor = None

    @classmethod
    def __close_conn(cls):
        if cls.__conn is not None:
            cls.__conn.close()
            cls.__conn = None
