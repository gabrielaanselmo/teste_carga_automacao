import subprocess
import yaml

# Carregar configurações do arquivo config.yml
with open('config/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Parâmetros do JMeter a partir do arquivo config.yml
num_threads = config['jmeter']['num_threads']
ramp_up = config['jmeter']['ramp_up_period']
loop_count = config['jmeter']['loop_count']

# Caminho para o arquivo JMX do JMeter (onde você salvou o arquivo no seu projeto)
jmeter_test_plan = "jmeter/plano_teste.jmx"

# Caminho para o JMeter no sistema
jmeter_path = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\apache-jmeter-5.6.3\\bin\\jmeter.bat"

# Comando para rodar o JMeter com os parâmetros configurados
jmeter_command = [
    jmeter_path,
    "-n",  # Modo não-gráfico (headless)
    "-t", jmeter_test_plan,  # Caminho do plano de teste JMX
    "-Jthreads=" + str(num_threads),  # Número de usuários
    "-Jramp_up=" + str(ramp_up),  # Tempo de ramp-up
    "-Jloops=" + str(loop_count),  # Número de loops
    "-l", "logs\\jmeter_log.jtl"  # Salvar os logs em logs/jmeter_log.jtl
]

# Executar o JMeter
subprocess.run(jmeter_command)
