from AExampleProject.configs import root_path,GlobalEnv
from AExampleProject.transaction.jsonunit import JsonUnit
import os


class TransactionBase():
    def __init__(self):
        self.adapter_file_path = GlobalEnv.adapter_file_path
        self.sys_file_path = GlobalEnv.sys_file_path

    def load_tra_msg(self, trn_name: str):
        try:
            template_path=os.path.join(root_path,"configs\\template")
            full_path=os.listdir(template_path)
            if "{}.json".format(trn_name) in full_path:
                json_path=os.path.join(template_path,"{}.json".format(trn_name))
                return JsonUnit.get_jsonfile_content(json_path)
        except:
            pass



if __name__ == "__main__":
    GlobalEnv.sys_env = "UAT"
    a = TransactionBase().load_tra_msg("msg_template1")
    print(a)
