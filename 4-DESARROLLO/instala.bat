CLS
@echo off
@echo INSTALANDO EL ENTORNO VIRTUAL
pip install virtualenv
@echo CREANDO EL ENTORNO VIRTUAL
python -m venv venv
@echo ACTIVANDO EL ENTORNO VIRTUAL

venv\Scripts\activate
@echo INSTALANDO DJANGO
python -m pip install Django==5.2
python.exe -m pip install --upgrade pip
@echo INSTALANDO REQUERIMIENTOS
pip install -r requirements.txt
call venv\Scripts\deactivate


@echo PROCESO DE INSTALACION FINALIZADO