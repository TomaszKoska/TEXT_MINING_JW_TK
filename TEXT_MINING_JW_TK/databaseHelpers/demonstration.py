from databaseHelpers.SqliteHelper import SqliteHelper

myHelper = SqliteHelper("D:/databases/testDlaJacka.db")
myHelper.start()
myHelper.createArticleTable("MY_ARTICLE")
myHelper.createArticleTable("MY_ARTICLE2")
myHelper.createArticleTable("MY_ARTICLE3")
myHelper.saveDocument()
myHelper.close()
