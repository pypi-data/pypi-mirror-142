import ast


class Config:
    def __init__(self, filename: str) -> None:
        if filename.endswith('.set'):
            self.__filename = filename
        else:
            raise Exception('File of such format are not supported')

        with open(self.__filename, 'r', encoding='utf-8') as cfg:
            self.__congif_data = cfg.read()
        if not self.__congif_data.endswith('\n'):
            with open(self.__filename, 'a') as cfg:
                cfg.write('\n')

    def get_section(self, section: str) -> dict:
        self.__section_args = []
        self.__section_dict = {}
        self.__section_index = -1
        with open(self.__filename, 'r', encoding='utf-8') as cfg:
            self.__congif_data = cfg.read()
            self.__config_data_list = self.__congif_data.split('\n')

        if self.__config_data_list.count(section) > 1:
            raise Exception('Multiple sections have the same name')
        else:
            self.__list_counter = 0
            for line in self.__config_data_list:
                if line.startswith('<') and section in line and '>' in line:
                    self.__section_index = self.__list_counter
                self.__list_counter += 1

            if self.__section_index == -1:
                raise Exception('Section not found')
            else:
                for i in range(self.__section_index + 1, len(self.__config_data_list)):
                    if not self.__config_data_list[i].startswith('<'):
                        if self.__config_data_list[i]:
                            # print(self.__config_data_list[i])
                            self.__section_args.append(self.__config_data_list[i])
                    else:
                        break
                # print(self.__section_args)
                for item in self.__section_args:
                    key, value = str(item).split('=')
                    self.__section_dict.update({key.strip(): ast.literal_eval(value.strip())})
                # print(self.__section_dict)
                return self.__section_dict
