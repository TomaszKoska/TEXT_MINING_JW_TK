from databaseHelpers.CsvHelper import CsvHelper
from databaseHelpers.SqliteHelper import SqliteHelper

myHelper = CsvHelper(databesePath="D:/databases/csv/",delimiter=",")
#myHelper = SqliteHelper(databesePath="D:/databases/bazka1.db")

myHelper.start()
myHelper.createDocumentTable("pozdro") # w przypadku obu helperów taka sama komenda!
myHelper.close()  
