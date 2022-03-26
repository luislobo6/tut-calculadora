import pytest
import sys
sys.path.append("../../")
import funciones as tf


def obtener_datos_integracion():
  return [(5,5,1.25,0.75,5),(8,"1.4",15,"3/8",137.475)]

@pytest.mark.parametrize("num_suma1, num_suma2, num_resta1, num_resta2, resultado", obtener_datos_integracion())
def test_integracion(num_suma1, num_suma2, num_resta1, num_resta2, resultado):
  assert tf.multiplicacion(tf.suma(num_suma1,num_suma2),tf.resta(num_resta1,num_resta2)) == resultado