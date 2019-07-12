import arcpy,fileinput
workspace=r"C:/Users/White/Desktop/New folder"
arcpy.env.workspace = workspace
infile= r"C:\Users\White\Desktop\polygon.txt"
fc='polygon9.shp'
arcpy.CreateFeatureclass_management("C:/Users/White/Desktop/New folder",fc,"Polygon")
cursor = arcpy.da.InsertCursor(fc,["SHAPE@"])
array = arcpy.Array()
point = arcpy.Point()
for line in fileinput.input(infile):
    point.ID,point.X, point.Y = line.split()
    array.add(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
fileinput.close()
print('done')