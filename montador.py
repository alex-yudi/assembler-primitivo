# Aluno: Alex Yudi Toma
import textwrap
end_inicio_memoria = 0x00400000

def gera_cod_op(inst):
    fam_r = ["sll", "srl", "jr", "mfhi", "mflo", "mult", "multu", "div", "divu", "add", "addu", "sub", "subu", "and", "or","slt","sltu"]
    mul = "mul"
    fam_i = [
        {
        "nome":"beq",
        "cod_op":"000100"
        }, 
        {
        "nome":"bne",
        "cod_op":"000101"
        },
        {
        "nome":"addi",
        "cod_op":"001000"
        },
        {
        "nome":"addiu",
        "cod_op":"001001"
        },
        {
        "nome":"slti",
        "cod_op":"001010"
        },
        {
        "nome":"sltiu",
        "cod_op":"001011"
        },
        {
        "nome":"andi",
        "cod_op":"001100"
        },
        {
        "nome":"ori",
        "cod_op":"001101"
        },
        {
        "nome":"lui",
        "cod_op":"001111"
        },
        {
        "nome":"lw",
        "cod_op":"100011"
        },
        {
        "nome":"sw",
        "cod_op":"101011"
        }
    ]
    fam_j = [
        {
        "nome":"j",
        "cod_op":"000010"
        },
        {
        "nome":"jal",
        "cod_op":"000011"
        }
    ]
    
    if(inst in fam_r):
        return "000000"
    
    if(inst == mul):
        return "011100"
   
    for i in fam_i:
        if(i['nome'] == inst):
            return i["cod_op"]
    
    for i in fam_j:
        if(i['nome'] == inst):
            return i["cod_op"]

def verifica_familia_cod_op(cod_op):
    fam_op = ""
    fam_i = ["000100", "000101", "001000", "001001", "001010", "001011", "001100", "001101", "001111", "100011", "101011"]
    
    if(cod_op == "000000" or cod_op == "011100"):
        fam_op = "R"
    elif(cod_op == "000010" or cod_op == "000011"):
        fam_op = "J"
    elif(cod_op in fam_i):
        fam_op = "I"

    return fam_op

def retorna_bin_funct_r(funct):
    fam_r = [
        {
        "nome":"sll",
        "funct":"000000"
        },
        {
        "nome":"srl",
        "funct":"000010"
        },
        {
        "nome":"jr",
        "funct":"001000"
        },
        {
        "nome":"mfhi",
        "funct":"010000"
        },
        {
        "nome":"mflo",
        "funct":"010010"
        },
        {
        "nome":"mult",
        "funct":"011000"
        },
        {
        "nome":"multu",
        "funct":"011001"
        },
        {
        "nome":"div",
        "funct":"011010"
        },
        {
        "nome":"divu",
        "funct":"011011"
        },
        {
        "nome":"add",
        "funct":"100000"
        },
        {
        "nome":"addu",
        "funct":"100001"
        },
        {
        "nome":"sub",
        "funct":"100010"
        },
        {
        "nome":"subu",
        "funct":"100011"
        },
        {
        "nome":"and",
        "funct":"100100"
        },
        {
        "nome":"or",
        "funct":"100101"
        },
        {
        "nome":"slt",
        "funct":"101010"
        },
        {
        "nome":"sltu",
        "funct":"101011"
        },
        {
        "nome":"mul",
        "funct":"000010"
        }
    ]

    for i in fam_r:
        if(i['nome'] == funct):
            return i['funct']

def retorna_end_bin_regist(registrador):
    fam_reg = [
        {
        "nome":"zero",
        "numero":"0",
        "bin":"00000"
        },
        {
        "nome":"at",
        "numero":"1",
        "bin":"00001"
        },
        {
        "nome":"v0",
        "numero":"2",
        "bin":"00010"
        },
        {
        "nome":"v1",
        "numero":"3",
        "bin":"00011"
        },
        {
        "nome":"a0",
        "numero":"4",
        "bin":"00100"
        },
        {
        "nome":"a1",
        "numero":"5",
        "bin":"00101"
        },
        {
        "nome":"a2",
        "numero":"6",
        "bin":"00110"
        },
        {
        "nome":"a3",
        "numero":"7",
        "bin":"00111"
        },
        {
        "nome":"t0",
        "numero":"8",
        "bin":"01000"
        },
        {
        "nome":"t1",
        "numero":"9",
        "bin":"01001"
        },
        {
        "nome":"t2",
        "numero":"10",
        "bin":"01010"
        },
        {
        "nome":"t3",
        "numero":"11",
        "bin":"01011"
        },
        {
        "nome":"t4",
        "numero":"12",
        "bin":"01100"
        },
        {
        "nome":"t5",
        "numero":"13",
        "bin":"01101"
        },
        {
        "nome":"t6",
        "numero":"14",
        "bin":"01110"
        },
        {
        "nome":"t7",
        "numero":"15",
        "bin":"01111"
        },
        {
        "nome":"s0",
        "numero":"16",
        "bin":"10000"
        },
        {
        "nome":"s1",
        "numero":"17",
        "bin":"10001"
        },
        {
        "nome":"s2",
        "numero":"18",
        "bin":"10010"
        },
        {
        "nome":"s3",
        "numero":"19",
        "bin":"10011"
        },
        {
        "nome":"s4",
        "numero":"20",
        "bin":"10100"
        },
        {
        "nome":"s5",
        "numero":"21",
        "bin":"10101"
        },
        {
        "nome":"s6",
        "numero":"22",
        "bin":"10110"
        },
        {
        "nome":"s7",
        "numero":"23",
        "bin":"10111"
        },
        {
        "nome":"t8",
        "numero":"24",
        "bin":"11000"
        },
        {
        "nome":"t9",
        "numero":"25",
        "bin":"11001"
        },
        {
        "nome":"sp",
        "numero":"29",
        "bin":"11101"
        },
        {
        "nome":"ra",
        "numero":"31",
        "bin":"11111"
        }
    ]
    for i in fam_reg:
        if(i['nome'] == registrador or i['numero'] == registrador):
            return i['bin']

def converte_decimal_binario(decimal, comprimento = 5, complemento_2 = True):
    if(complemento_2 and decimal < 0):
        num_pos = (1 << comprimento) + decimal
        bin = format(num_pos, f'0{comprimento}b')
        return bin
    return format(decimal, f'0{comprimento}b')

def converte_saida_bin_hex(string_binaria):
    parcelas = textwrap.wrap(string_binaria, width=4)
    valor_hex = ""

    for parcela in parcelas:
        parcela = hex(int(parcela, 2)).lstrip("0x").zfill(1)
        valor_hex = valor_hex + parcela

    return valor_hex


def gera_bin_fam_r(instrucao):
    partes = instrucao.split(" ")
    funct = partes[0]
    partes = instrucao.split("$")
    bin_funct = retorna_bin_funct_r(funct)

    # Cria o binário para deslocamentos
    if(funct == "sll" or funct == "srl"):
        rd = partes[1].rstrip(', ').rstrip(',')
        end_rd = retorna_end_bin_regist(rd)

        partes = partes[2].split(",")
        rt = partes[0].rstrip(', ').rstrip(',')
        end_rt = retorna_end_bin_regist(rt)
        shamt = partes[1]
        bin_shamt = converte_decimal_binario(int(shamt))

        return ("00000" + end_rt + end_rd + bin_shamt + bin_funct)
    # Cria o binário para jr
    elif(funct == "jr"):
        rs = partes[1]
        end_rs = retorna_end_bin_regist(rs)
        return (end_rs + "00000" + "00000" + "00000" + bin_funct)
    # Cria o binário para mfhi e mflo
    elif(funct == "mfhi" or funct == "mflo"):
        rd = partes[1]
        end_rd = retorna_end_bin_regist(rd)
        return ("00000" + "00000" + end_rd + "00000" + bin_funct)
    # Cria o binário para mult, multu, div e divu
    elif(funct == "mult" or funct == "multu" or funct == "div" or funct == "divu"):
        rs = partes[1].rstrip(', ').rstrip(',')
        end_rs = retorna_end_bin_regist(rs)
        rt = partes[2].rstrip(', ').rstrip(',')
        end_rt = retorna_end_bin_regist(rt)

        return (end_rs + end_rt + "00000" + "00000" + bin_funct)
    else:
        rd = partes[1].rstrip(', ').rstrip(',')
        end_rd = retorna_end_bin_regist(rd)

        rs = partes[2].rstrip(', ').rstrip(',')
        end_rs = retorna_end_bin_regist(rs)

        rt = partes[3].rstrip(', ').rstrip(',')
        end_rt = retorna_end_bin_regist(rt)

        return (end_rs + end_rt + end_rd + "00000" + bin_funct)

def gera_bin_fam_i(instrucao, linha_pc = 0, dicionario_labels = {}):
    partes = instrucao.split(" ")
    funct = partes[0]
    partes = instrucao.split("$")

    if(funct == "beq" or funct == "bne"):

        rs = partes[1].rstrip(', ').rstrip(',')
        end_rs = retorna_end_bin_regist(rs)

        partes = partes[2].split(",")
        rt = partes[0]
        end_rt = retorna_end_bin_regist(rt)

        imm = partes[1].lstrip(' ')
        imm = (dicionario_labels[str(imm)]['numero_linha'])
        imm = imm - linha_pc
        imm_bin = converte_decimal_binario(int(imm), 16, True)

        return (end_rs + end_rt + imm_bin)
    elif(funct == "lw" or funct == "sw"):
        rt_im = partes[1].split(",")
        rt = rt_im[0]
        end_rt = retorna_end_bin_regist(rt)

        imm = rt_im[1].rstrip('()').lstrip(' ')
        imm_bin = converte_decimal_binario(int(imm), 16)

        rs = partes[2].rstrip(')')
        end_rs = retorna_end_bin_regist(rs)

        return (end_rs + end_rt + imm_bin)
    elif(funct == "lui"):
        partes = partes[1].split(",")

        rt = partes[0]
        end_rt = retorna_end_bin_regist(rt)

        imm = partes[1].lstrip(' ')
        imm_bin = converte_decimal_binario(int(imm), 16)

        return ("00000" + end_rt + imm_bin)
    else:
        rt = partes[1].rstrip(', ').rstrip(',')
        end_rt = retorna_end_bin_regist(rt)

        partes = partes[2].split(",")
        rs = partes[0]
        end_rs = retorna_end_bin_regist(rs)

        imm = partes[1].lstrip(' ')
        imm_bin = converte_decimal_binario(int(imm), 16)

        return (end_rs + end_rt + imm_bin)

def gera_bin_fam_j(instrucao, dicionario_labels = {}):
    partes = instrucao.split(" ")
    linha_label = partes[1]
    linha_label = dicionario_labels[linha_label]['numero_linha']
    end = int(((4*(linha_label-1)) + end_inicio_memoria) / 4)
    end_bin = converte_decimal_binario(int(end), 26)
    return end_bin

def retira_comentarios_labels(instrucao):
    if('#' in instrucao):
        instrucao = instrucao.split('#')[0].strip()
    
    if(':' in instrucao):
        instrucao = instrucao.split(':')[1].lstrip(" ")

    instrucao = instrucao.strip()
    return instrucao


def geraBinFinal(instrucao, linha_atual = 0, dicionario_labels = {}):
    instrucao = retira_comentarios_labels(instrucao)
    linha_pc = linha_atual + 1
    if(instrucao == ""):
        return
    
    # Separa instrução e verifica família
    inst = instrucao.split(" ")
    inst = inst[0]
    cod_op = gera_cod_op(inst)
    fam_op = verifica_familia_cod_op(cod_op)

    # Gerando instrução binária
    if(fam_op == "R"):
        return cod_op + gera_bin_fam_r(instrucao)
    if(fam_op == "I"):
        return cod_op + gera_bin_fam_i(instrucao, linha_pc, dicionario_labels)
    if(fam_op == "J"):
        return cod_op + gera_bin_fam_j(instrucao, dicionario_labels)



import sys

def ler_arquivo(nome_arquivo, tipo_saida):
    dicionario_instrucoes = {}
    qtde_total_instrucoes = 0

    # Leitura do arquivo para gerar os binários e hexadecimais
    try:
        with open(nome_arquivo, 'r') as arquivo:
            nome_arquivo_sem_extensao = nome_arquivo.split(".")[0]
            conteudo = arquivo.read()
            vetor_conteudo = conteudo.split("\n")
            dicionario_labels = {}
            contador_linhas = 0
            linha_atual = 0
            
            # Procurando por todas as labels e linhas que elas estão contidas
            for instrucao in vetor_conteudo:
                contador_linhas = contador_linhas + 1
                if(":" in instrucao):
                    label = instrucao.split(":")[0]
                    dicionario_labels[label] = {
                        "numero_linha": contador_linhas
                    }

            # Cria o diciário de instruções e a quantidade de vezes que elas são utilizadas no código
            for instrucao in vetor_conteudo:
                instrucao = retira_comentarios_labels(instrucao)
                if(instrucao == ""):
                    continue
                qtde_total_instrucoes += 1 
                instrucao = instrucao.split(" ")[0]
                if(instrucao in dicionario_instrucoes):
                    dicionario_instrucoes[instrucao]["quantidade_usada"] = dicionario_instrucoes[instrucao]["quantidade_usada"] + 1
                else:
                    dicionario_instrucoes[instrucao] = {
                    "quantidade_usada": 1
                    }
                
            
            if(tipo_saida == '-h'):
                with open(nome_arquivo_sem_extensao +".hex", "w") as arquivo_saida:
                    arquivo_saida.write("v2.0 raw\n")

            for instrucao in vetor_conteudo:
                if(instrucao == ""):
                    continue
                linha_atual = linha_atual + 1

                bin_final = geraBinFinal(instrucao, linha_atual, dicionario_labels) 
                
                if(tipo_saida == '-b' and bin_final != None):
                    with open(nome_arquivo_sem_extensao +".bin", "a") as arquivo_saida:
                        arquivo_saida.write(bin_final + "\n")

                if(tipo_saida == '-h' and bin_final != None):
                    hex_final = converte_saida_bin_hex(bin_final)
                    with open(nome_arquivo_sem_extensao +".hex", "a") as arquivo_saida:
                        arquivo_saida.write(hex_final + "\n")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo '{nome_arquivo}'.")

    # Leitura do arquivo com os ciclos e instruções, para cálculo de CPI
    try:
        with open("ciclos_instrucoes.csv", 'r') as arquivo:
            conteudo = arquivo.read()
            vetor_conteudo = conteudo.split("\n")
            vetor_conteudo = vetor_conteudo[1:]
            dicionario_ciclos_instrucoes = {}
            cpi_medio = 0

            for instrucao in vetor_conteudo:
                if(instrucao == ""):
                    continue
                dicionario_ciclos_instrucoes[instrucao.split(",")[0]] = {
                    "ciclos": instrucao.split(",")[1]
                }

            if(qtde_total_instrucoes == 0):
                print("Não foi possível calcular o CPI médio, pois não há instruções no código.")
                return
            
            print("Quantidade por tipo de instruções: ")
            for instrucao in dicionario_instrucoes:
                print(f"{instrucao}: {dicionario_instrucoes[instrucao]['quantidade_usada']}")
                cpi_medio += int(dicionario_ciclos_instrucoes[instrucao]['ciclos']) * dicionario_instrucoes[instrucao]['quantidade_usada']
            
            cpi_medio = cpi_medio / qtde_total_instrucoes
            
            print('\n')

            print("CPI médio: " + str(cpi_medio))


    except FileNotFoundError:
        print(f"Erro: O arquivo 'ciclos_instrucoes.csv' não foi encontrado.")
    except IOError:
        print(f"Erro: Não foi possível ler o arquivo 'ciclos_instrucoes.csv'.")

if __name__ == "__main__":
    tipo_saida = '-b'
    nome_arquivo = sys.argv[1]

    if(len(sys.argv) > 2):
        tipo_saida = sys.argv[2]

    ler_arquivo(nome_arquivo, tipo_saida)