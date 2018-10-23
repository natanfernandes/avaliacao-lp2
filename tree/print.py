from csv import reader
from contextlib import redirect_stdout
from collections import namedtuple
from anytree import Node, RenderTree
node_geral = Node('Raiz')
node_cod_geral = ""
node_cod_especifica = ""
node_cod_detalhada = ""
node_detalhes = ""
Entrada = namedtuple("Entrada", "cod_geral area_geral cod_especifica area_especifica cod_detalhada area_detalhada codigo rotulo")
with open("dataset.csv", encoding="utf-8") as csvfile:
  with open("tree.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        cod_geral = ""
        cod_especifica = ""
        cod_detalhada = ""
        cod = ""
        csvfile.readline()
        for line in reader(csvfile, delimiter=";"):
            entrada = Entrada(*line)
            if entrada.cod_geral != cod_geral:
                #print("==== Área geral: {} {}".format(entrada.cod_geral, entrada.area_geral))
                node_cod_geral = Node(entrada.cod_geral +" - "+entrada.area_geral,parent=node_geral)
                cod_geral = entrada.cod_geral
            if entrada.cod_especifica != cod_especifica:
                cod_especifica = entrada.cod_especifica
                #print("---- Área específica: {} {}".format(entrada.cod_especifica, entrada.area_especifica))
                node_cod_especifica = Node(entrada.cod_especifica+" - "+entrada.area_especifica, parent=node_cod_geral)
            if entrada.cod_detalhada != cod_detalhada:
                cod_detalhada = entrada.cod_detalhada

                #print("++++ Área detalhada: {} {}".format(entrada.cod_detalhada, entrada.area_detalhada))
                node_cod_detalhada = Node(entrada.cod_detalhada + " - "+ entrada.area_detalhada, parent=node_cod_especifica)
            if cod != entrada.codigo:
                cod = entrada.codigo
                node_detalhes = Node(entrada.codigo + " - " + entrada.rotulo,parent = node_cod_detalhada)
        for pre, _, node in RenderTree(node_geral):
            print("%s%s" % (pre, node.name))
            #print("{} {}".format(entrada.codigo, entrada.rotulo))