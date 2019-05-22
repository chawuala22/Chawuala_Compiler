import basic
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import basic

class Aplicacion:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.ventana1.title("Chawala compiler")
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)        
        self.nombrearch = ""
        self.ventana1.mainloop()
        

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Abrir archivo", command=self.cargar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Compilar Programa", command=self.compilar)
        
        menubar1.add_cascade(label="Compilador", menu=opciones2)
            
    
    def salir(self):
        sys.exit()

    def guardar(self):
        self.nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("dan files",".dan"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def cargar(self):
        self.nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("dan files","*.dan"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)
    def compilar(self):
        
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "r", encoding="utf-8")
            for linea in archi1.readlines():
				ab=linea
				print(ab)
                main(linea)
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)


def main(text):
	
	result, error = basic.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)




aplicacion1=Aplicacion()