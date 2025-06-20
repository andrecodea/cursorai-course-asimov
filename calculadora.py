import streamlit as st

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro"
    return x / y

st.title("Calculadora Estilo Windows")

# Inicializa o estado da calculadora na sessão
if 'input' not in st.session_state:
    st.session_state.input = '0'
    st.session_state.first_operand = None
    st.session_state.operator = None
    st.session_state.waiting_for_second_operand = False

# Visor da calculadora
st.text_input("Visor", value=st.session_state.input, disabled=True, key="visor")

# Função para processar os cliques nos botões
def handle_click(value):
    if value == ' \\* ':
        value = '*'
    elif value == ' \\+ ':
        value = '+'
    elif value == ' \\- ':
        value = '-'

    if value in list('0123456789.'):
        if st.session_state.waiting_for_second_operand:
            st.session_state.input = value
            st.session_state.waiting_for_second_operand = False
        else:
            if st.session_state.input == '0' and value != '.':
                st.session_state.input = value
            elif value == '.' and '.' in st.session_state.input:
                pass  # Impede múltiplos pontos decimais
            else:
                st.session_state.input += value

    elif value in ['+', '-', '*', '/']:
        # Se o usuário clicar em um operador quando um cálculo já pode ser feito,
        # calcula o resultado parcial antes de registrar o novo operador.
        if st.session_state.first_operand is not None and not st.session_state.waiting_for_second_operand:
            handle_click('=')

        # Permite trocar o operador se o segundo número ainda não foi digitado
        if st.session_state.waiting_for_second_operand:
            st.session_state.operator = value
            return
            
        try:
            st.session_state.first_operand = float(st.session_state.input)
            st.session_state.operator = value
            st.session_state.waiting_for_second_operand = True
        except ValueError:
            st.session_state.input = "Erro"

    elif value == '=':
        if st.session_state.first_operand is None or st.session_state.operator is None or st.session_state.waiting_for_second_operand:
            return
        
        try:
            second_operand = float(st.session_state.input)
            
            ops = {'+': somar, '-': subtrair, '*': multiplicar, '/': dividir}
            result = ops[st.session_state.operator](st.session_state.first_operand, second_operand)

            # Formata o resultado para remover ".0" de inteiros
            if isinstance(result, float) and result.is_integer():
                st.session_state.input = str(int(result))
            else:
                st.session_state.input = str(round(result, 8)) # Arredonda para evitar dízimas

            st.session_state.first_operand = result # Mantém o resultado para operações encadeadas
            st.session_state.operator = None
            st.session_state.waiting_for_second_operand = True
        except (ValueError, ZeroDivisionError):
            st.session_state.input = "Erro"

    elif value == 'C':
        st.session_state.input = '0'
        st.session_state.first_operand = None
        st.session_state.operator = None
        st.session_state.waiting_for_second_operand = False

# Layout dos botões em uma grade
button_rows = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', ' \\* '),
    ('1', '2', '3', ' \\- '),
    ('C', '0', '.', ' \\+ ')
]

for row in button_rows:
    cols = st.columns(4)
    for i, label in enumerate(row):
        cols[i].button(label, on_click=handle_click, args=(label,), use_container_width=True)

# Botão de igualdade separado para dar mais destaque
st.button('=', on_click=handle_click, args=('=',), use_container_width=True)
