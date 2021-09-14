#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int sizeObject, temp, i;
	PyObject *obj;

	sizeObject = Py_SIZE(p);
	temp = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", sizeObject);
	printf("[*] Allocated = %d\n", temp);
	for (i = 0; i < sizeObject; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
