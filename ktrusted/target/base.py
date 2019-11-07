

class Target:

    def __init__(self, table_name, data_stage):
        self.table_name = table_name
        self.data_stage = data_stage

    def save_to_s3(self):
        print("Saving files in " + self.data_stage + "/" + self.table_name)

    def apply_validate(self, df_result, expected_struct):
        return
