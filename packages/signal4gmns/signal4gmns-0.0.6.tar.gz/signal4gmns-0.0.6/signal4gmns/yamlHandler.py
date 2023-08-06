import yaml

class YamlHandler:

    def __init__(self,file,encoding = 'utf-8'):
         self.file = file
         self.encoding = encoding

    def get_ymal_data(self):
        with open(self.file,encoding=self.encoding) as f:
            data = yaml.load(f.read(),Loader=yaml.FullLoader)
        return data

    def write_yaml(self,data):
        with open(self.file,'w',encoding=self.encoding) as f:
            yaml.dump(data,stream=f,allow_unicode = True)

    def get_default_config_dic(self):
        config={'PHF': 1.0,'default_c_Min': 60.0,'f_lu': 1.0,'f_hv': 1.0,'l_value': 12.0,'minGreenTime': 12,'t_AR': 2,'t_L': 4,
't_Yellow': 4,'x_c_Input': 0.99,'x_c_output': 0.9,'y_StageMax': 1,'start_time_in_min': 420,'end_time_in_min': 480,'default_volume_filled_by_code': True,'use_reference_cycle_length': True}
        return config
