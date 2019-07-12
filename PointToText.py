import arcpy
arcpy.env.workspace = r'C:\Users\White\Documents\ArcGIS\Packages\ZooEscape_FE482E01-9AF3-4166-AA7C-0FE71F8457BA\zooescape.gdb'
cursor = arcpy.da.SearchCursor('FieldSightings_Lola',["OID@",'SHAPE@XY'])
txt= open(r"C:\Users\White\Desktop\polygon.txt","w")
rowNumbers = arcpy.GetCount_management('FieldSightings_Lola')
for row in cursor:
    OID= row[0]
    x,y=row[1]
    txt.write("{0} {1} {2}\n".format(OID,x,y))
txt.close()
txt= open(r"C:\Users\White\Desktop\polygon.txt")
lines=txt.readlines()
txt.close()
txt= open(r"C:\Users\White\Desktop\polygon.txt","a")
num=int(rowNumbers[0])+1
firstline = lines[0]
firstline.rstrip()
print(firstline)
txt.write(firstline.replace("1",str(num),1))
txt.close()
print(lines)
print('done')
