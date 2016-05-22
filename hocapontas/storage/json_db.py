import json
import os.path
from shutil import copyfile


DB_PATH = os.path.join(os.path.expanduser('~'), '.ulf.json')
DB_BAK_PATH = os.path.join(os.path.expanduser('~'), '.ulf.json.bak')



class JsonDB:
    def read(self):
        data = '[]'
        try:
            with open(DB_PATH, 'r') as f:
                data = f.read()
        except FileNotFoundError:
            with open(DB_PATH, 'w') as f:
                f.write('[]')
        return json.loads(data)

    def write(self, item):
        copyfile(DB_PATH, DB_BAK_PATH)
        data = self.read()
        data.append(item)
        try:
            with open(DB_PATH, 'w') as f:
                json.dump(data, f, ensure_ascii=False)
            return True
        except IOError:
            # TODO: log
            return False

    def delete(self, item):
        copyfile(DB_PATH, DB_BAK_PATH)
        data = self.read()
        data.remove(item)
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    def update(self, item_id, item):
        copyfile(DB_PATH, DB_BAK_PATH)
        data = self.read()
        data[item_id] = item
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    def reset(self):
        if os.path.isfile(DB_PATH):
            copyfile(DB_PATH, DB_BAK_PATH)
        with open(DB_PATH, 'w') as f:
            f.write('[]')
