"""File"""
import os
import sys


class vsvpack(object):
    def __init__(self, newParth, name):
        self.parth = newParth
        self.name = name

    def new(self, Overwite_text):  # Parth ,New pack name,Overwite_text
        # if (Parth_!=None):
        #    Os_Parth_Test = Parth_
        name_new = self.name
        Parth_ = self.parth
        # else:
        Os_Parth_Test = Parth_ + "/"
        Parth_Test = os.path.exists(Os_Parth_Test)
        skip_action = False
        if (Parth_Test == False):
            Parth_Test = os.path.exists(Os_Parth_Test)
            Ordner_new = os.makedirs(Os_Parth_Test)

        Parth_pack = Parth_ + "/" + name_new + ".pack"
        try:
            test_file = open(Parth_pack)
            # Do something with the file
        except IOError:
            test_file = open(Parth_pack, "w")
            test_file.write("@code=not_deletable")
            test_file.close()
        finally:
            test_file.close()

        filesize = os.path.getsize(Parth_pack)
        if filesize == 0:
            test_for_text = True
        else:
            test_for_text = False
            file2 = open(Parth_pack, "r")
            lines = file2.read().splitlines()
            if ("{}".format(lines[0]) == "@code=not_deletable"):
                skip_action = True

        if (Overwite_text == True):

            new = open(Parth_pack, "w")
            new.write("@code=not_deletable")
            new.close()
        elif (test_for_text == True):
            new = open(Parth_pack, "w")
            new.write("@code=not_deletable")
            new.close()
        elif (skip_action == False):
            print("Info:this file isnt empty if you wane use it,")
            print("use data.new_file(<Parth_>,<name_new>,True)")
            print("instead of data.new_file(<Parth_>,<name_new>,False)")

    def read(self, Name):  # parth_=file-phad ohne .pack

        Parth = self.parth + "\\" + self.name + ".pack"

        x = 0
        with open(Parth, 'r') as cp:
            for count, line in enumerate(cp):
                pass
        cp.close()
        y = 0
        file2 = open(Parth, "r")
        lines = file2.read().splitlines()
        # print(count)
        while (y <= count):
            text_ = "{}".format(lines[y])
            test_name, text_return = text_.split("=")
            if (test_name == Name):
                return text_return
                file2.close()
            y += 1
            file2.close()

    def add(self, Name_var, value):

        Parth = self.parth + "\\" + self.name + ".pack"

        x = 0
        if (Name_var == "@code"):
            print("ERROR: don't use @code")
            return
        with open(Parth, 'r') as cp:
            for count, line in enumerate(cp):
                pass
        cp.close()
        y = 0
        text_ = {}
        file2 = open(Parth, "r")
        lines = file2.read().splitlines()
        # print(count)

        if ("{}".format(lines[0]) == "@code=not_deletable"):

            while (y <= count):
                try:
                    text_[y] = "{}".format(lines[y])
                finally:
                    y += 1

            file2.close()
            file_w = open(Parth, "w")
            write_new_Var = True
            v = 0
            while (y >= 1):

                test_name, text_return = str(text_[v]).split("=")
                if (test_name == Name_var):
                    file_w.write(Name_var + "=" + value)
                    file_w.write("\n")
                    write_new_Var = False

                else:
                    file_w.write(str(text_[v]))
                    file_w.write("\n")
                y -= 1
                v += 1
            if (write_new_Var == True):
                write_ = Name_var + "=" + value
                file_w.write(write_)
                file_w.close()
        else:
            print(
                "WARNING: selected file is not declerated corecktly as '.pack' file,(in line 0 missing:@code=not_deletable)")

    def remove(self, Name_var_remove, ):
        Parth_ = self.parth
        Parth = Parth_ + "\\" + self.name + ".pack"
        if (Name_var_remove == "@code"):
            print("ERROR: don't use @code")
            return
        x = 0
        with open(Parth, 'r') as cp:
            for count, line in enumerate(cp):
                pass
        cp.close()
        y = 0
        w_ = 0

        text_ = {}
        file2 = open(Parth, "r")
        lines = file2.read().splitlines()

        # print(count)
        if ("{}".format(lines[0]) == "@code=not_deletable"):
            while (y <= count):
                try:
                    text_[w_] = "{}".format(lines[y])
                finally:
                    s = 1

                y += 1

                w_ += 1
            file2.close()
            file_w = open(Parth, "w")
            v = 0
            while (y >= 1):
                # print(y)
                # print(text_[y - 1])
                test_name, text_return = str(text_[v]).split("=")
                if (test_name != Name_var_remove):
                    w_ -= 1
                    file_w.write(str(text_[v]))
                    file_w.write("\n")

                v += 1
                y -= 1
        else:
            print(
                "WARNING: selected file is not declerated corecktly as '.pack'-file\n ,(in line 0 of the file missing:@code=not_deletable)")

    def aVoidValue(self):  # reduces Ram Usage,Destroys the Objects Usability
        del self.name
        del self.parth


class absoluteScriptFolderPath:
    # Note: .get must alwais be .get(__file__) ,else it won't work !!
    def get(self, type__file__):
        filepath = type__file__

        t = filepath.split("\\")
        removeName = filepath.split("\\")[-1]
        t.remove(removeName)
        usableFilePath = ""
        firstwhothout = False
        for word in t:
            if firstwhothout:
                usableFilePath = usableFilePath + "\\" + word
            else:
                usableFilePath = usableFilePath + word
                firstwhothout = True
        return usableFilePath
