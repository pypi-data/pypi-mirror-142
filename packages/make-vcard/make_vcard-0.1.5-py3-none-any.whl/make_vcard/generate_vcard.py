from .read_file import read_file_xlsx_data

# BEGIN:VCARD
# VERSION:3.0
# N;CHARSET=UTF-8:{n}
# FN;CHARSET=UTF-8:{n}
# TEL;TYPE=CELL:{dh}
# NOTE;CHARSET=UTF-8:{c}
# EMAIL:邮箱地址
# END:VCARD
class Vcard:
    def __init__(self):
        self._vcard = {}

    def set_data(self, **kwds):
        '''
        set_data(
            n="名字",
            tel=电话,
            note="备注"
        )
        '''
        # print(kwds)
        if kwds:
            for k in kwds:
                kf = "set_{}".format(k.lower())
                # print(kf)
                if hasattr(self, kf):
                    getattr(self, kf)(kwds[k])
        return self

    def _set(self, data, k, txt):
        if data:
            self._vcard[k] = txt.format(data)
            
        return self

    def set_n(self, data):
        return self._set(data, "N", "N;CHARSET=UTF-8:{}\n")

    def set_fn(self, data):
        return self._set(data, "FN", "FN;CHARSET=UTF-8:{}\n")

    def set_tel(self, data):
        return self._set(data, "TEL", "TEL;TYPE=CELL:{}\n")

    def set_note(self, data):
        return self._set(data, "NOTE", "NOTE;CHARSET=UTF-8:{}\n")

    def set_email(self, data):
        return self._set(data, "EMAIL", "EMAIL:{}\n")

    def _get_values(self):
        return self._vcard.values()

    def to_string(self):
        return "BEGIN:VCARD\nVERSION:3.0\n"+"".join(self._get_values())+"END:VCARD\n"


class VcardFile:
    def __init__(self) -> None:
        self._data = []

    def write(self, data):
        '''
        ds = {'N': 'name', 'FN': 'name', 'TEL': 12345, 'NOTE': 'XXXXX'}\n
        write(ds)
        ds = """BEGIN:VCARD\nVERSION:3.0\nFN;CHARSET=UTF-8:Name\nTEL;TYPE=CELL:12345\nEND:VCARD\n"""
        write(ds)
        '''
        if type(data) == str:
            self._data.append(data)
        elif type(data) == dict:
            self._data.append(Vcard().set_data(**data).to_string())
        return self


    def to_string(self):
        return "".join(self._data)


    def save(self, fn, fsuffix=".vcf", encoding="utf-8", callback=None):
        with open("{}{}".format(fn, fsuffix), "w", encoding=encoding) as f:
            if callable(callback):
                callback(f)
            if self._data:
                f.write(self.to_string())
        print("文件保存完毕")


def make_vcard(inputFileName, outputFileName):
    datas = read_file_xlsx_data(inputFileName)
    f = VcardFile()
    for data in datas:
        f.write(data)
    f.save(outputFileName)

