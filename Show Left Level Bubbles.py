__author__='NguyenKhanhTien'
from Autodesk.Revit.DB import DatumEnds, Transaction, FilteredElementCollector, BuiltInCategory
from Autodesk.Revit.DB import View
from rpw.exceptions import RevitExceptions
from rpw import ui
doc = __revit__.ActiveUIDocument.Document
alllevels=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels)\
                    .WhereElementIsNotElementType()\
                    .ToElements()
view = doc.ActiveView

levels = []
selection = ui.Selection()
if selection:
    levels = selection
else:
    levels = alllevels

t=Transaction(doc,'Show Left Bubbles')
t.Start()
for level in levels:
    try:
        level.ShowBubbleInView(DatumEnds.End0, view)
        level.HideBubbleInView(DatumEnds.End1, view)
    except Exception:
	    pass
t.Commit()