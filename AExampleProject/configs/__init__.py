import os

__all__ = ["get_adapter_info", "get_db_info", "GlobalEnv","configs_dir"]

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configs_dir = os.path.join(root_path, "comfigs\\")


class GlobalEnv(object):
    sys_env = "ST"
    adapter_file_path, sys_file_path = None, None


def get_adapter_info():
    '''
    获取对应环境的系统配置信息文件路径，接口配置文件路径
    :return: 系统配置信息文件路径，接口配置文件路径
    '''
    env = GlobalEnv.sys_env
    sys_file_path = os.path.join(
        configs_dir, "adapter\\{}_info.json".format(env.lower()))
    adapter_file_path = os.path.join(configs_dir, "adapter\\adapter.json")
    GlobalEnv.sys_file_path, GlobalEnv.adapter_file_path = sys_file_path, adapter_file_path
    return sys_file_path, adapter_file_path


def get_db_info():
    '''
    获取对应环境的数据库配置信息文件路径
    :return: 数据库配置信息文件路径
    '''
    env = GlobalEnv.sys_env
    db_file_path = os.path.join(
        configs_dir, "dbinfo\\{}_dbinfo.json".format(env.lower()))
    return db_file_path


if __name__ == "__main__":
    print(configs_dir)
