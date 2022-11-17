import xml.etree.ElementTree as ET
# hemos creado un fichero pyton que crea un xml

students = ET.Element("students")
student = ET.SubElement(students, "student")
nodo1 = ET.SubElement(student, "name", name="Javier")
nodo1.text = "Me llamo Javier"
ET.SubElement(student, "surname", surname="Miranda").text = "Mi primer apellido es Miranda"
ET.SubElement(student, "email", email="emirand20").text = "Mi correo es emirand20@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948A").text = "Mi dni es 24578948A"
arbol = ET.ElementTree(students)

nodo2 = ET.SubElement(student, "name", name="Raul")
nodo2.text = "Me llamo Raul"
ET.SubElement(student, "surname", surname="Rufo").text = "Mi primer apellido es Rufo"
ET.SubElement(student, "email", email="rrufo").text = "Mi correo es rrufo@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948B").text = "Mi dni es 24578948B"
arbol = ET.ElementTree(students)
arbol.write("creaXML.xml")

nodo2 = ET.SubElement(student, "name", name="Guillem")
nodo2.text = "Me llamo Raul"
ET.SubElement(student, "surname", surname="Guillem").text = "Mi primer apellido es Fernandez"
ET.SubElement(student, "email", email="ggillem").text = "Mi correo es gguillem@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948B").text = "Mi dni es 24578948B"
arbol = ET.ElementTree(students)
arbol.write("creaXML.xml")

nodo2 = ET.SubElement(student, "name", name="Luis")
nodo2.text = "Me llamo Raul"
ET.SubElement(student, "surname", surname="Luis").text = "Mi primer apellido es Garcia"
ET.SubElement(student, "email", email="luis").text = "Mi correo es luis@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948B").text = "Mi dni es 24578948B"
arbol = ET.ElementTree(students)
arbol.write("creaXML.xml")

nodo2 = ET.SubElement(student, "name", name="Matias")
nodo2.text = "Me llamo Raul"
ET.SubElement(student, "surname", surname="Matias").text = "Mi primer apellido es Fernandez"
ET.SubElement(student, "email", email="matias").text = "Mi correo es matias@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948B").text = "Mi dni es 24578948B"
arbol = ET.ElementTree(students)
arbol.write("creaXML.xml")

nodo2 = ET.SubElement(student, "name", name="Laura")
nodo2.text = "Me llamo Raul"
ET.SubElement(student, "surname", surname="Garcia").text = "Mi primer apellido es Garcia"
ET.SubElement(student, "email", email="matias").text = "Mi correo es laura@jaumebalmes.net"
ET.SubElement(student, "dni", dni="24578948B").text = "Mi dni es 24578948B"
arbol = ET.ElementTree(students)
arbol.write("creaXML.xml")


ET.dump(students)