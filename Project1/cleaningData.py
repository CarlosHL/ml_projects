
class CleanData:

    def __init__(self, file_name):
        self.file_name = file_name

    def clean_data(self):
        """Cleans the data and writes it in a new file"""

        # data: POPULATION | PROFIT
        print "> Cleaning data"

        # open file
        file_content = open(self.file_name).readlines()


        # create cleaned file
        print "> Creating new file cleanData1.txt"
        new_file = open('cleanData1.txt','w')

        for line in file_content:
            new_line=line.replace(",", " ")
            new_file.write(new_line)

        new_file.close()
        data = open('cleanData1.txt', 'r')

        x_axis = [float(x.split(' ')[0]) for x in data.readlines()]
        data.close()
        data = open('cleanData1.txt', 'r')
        y_axis = [float(x.split(' ')[1]) for x in data.readlines()]
        print "> Data has been copied and cleaned to the new file"
        return x_axis, y_axis
