# 🚀 Projeto de Automação de Testes de Performance com Selenium e JMeter

Este projeto é uma automação de testes de performance e funcionalidade utilizando **Selenium** para testes de interface de usuário e **JMeter** para testes de carga e desempenho. A aplicação usada para os testes é a **The Internet (HerokuApp)**.

## 🎯 Objetivo do Projeto

O objetivo é automatizar o teste de login da aplicação **The Internet (HerokuApp)**, medindo o desempenho do servidor ao processar múltiplas requisições de login simultâneas e verificar a funcionalidade correta da interface de usuário.

## 🛠️ Tecnologias Utilizadas

- **Selenium**: Para automação da interface de usuário.
- **JMeter**: Para simulação de múltiplos usuários e testes de carga.
- **Python**: Para script de automação com Selenium.

## 📂 Estrutura do Projeto

```bash
/teste_carga_automacao
    /scripts
        - script_selenium.py  # Script para automação do login com Selenium
        - rodar_jmeter.py  # Script para execução de testes JMeter em modo headless
    /jmeter
        - plano_teste.jmx  # Plano de teste JMeter
    /config
        - config.yml  # Arquivo de configuração para parâmetros de teste
    /logs
        - jmeter_log.jtl  # Logs gerados após execução do JMeter
    /relatorios
        # Relatórios de desempenho serão gerados aqui
    /drivers
        - chromedriver.exe  # WebDriver usado pelo Selenium
```
