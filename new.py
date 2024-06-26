import xml.etree.ElementTree as ET 

tree = ET.parse('input.xml')
root = tree.getroot()

for book in root.findall('TcUnitOfMeasure'):
    e1 = book.find('unitOfMeasureName')
    e2 = book.find('unitOfMeasureSymbol')
    e3 = book.find('description')

    if e1 is not None and e2 is not None and e3 is not None:
        v1 = e1.text
        v2 = e2.text
        v3 = e3.text

        book.remove(e1)
        book.remove(e2)
        book.remove(e3)

        book.set('unitOfMeasureName', v1)
        book.set('unitOfMeasureSymbol', v2)
        book.set('description', v3)


tree.write('output.xml')