# secure-erp

## Project created due to CodeCool IT course requirements
## Language: PYTHON (100%)

Complete file/catalogue structure is provided by the excercise. All functions _except those in `data_manager.py`_ are created from scratch.
The main idea is to not use any `import` in the whole project. The exception is `util.py` file where the both imports: `string` and `random` were allready provided by the supervisors.

#### Contributors:
1. Radosław Rocławski
2. Adrian Paszek
3. Damian Czyż
4. Sofia Savchenko

#### Directories and files structure:
```
secure-erp/
|
|-.gitignore
|-erp.py
|-README.md
---controller/
|   |
|   |-crm_controller.py
|   |-hr_controller.py
|   |-main_controller.py
|   |-sales_controller.py
|
---model/
|   |
|   |-data_manager.py
|   |-util.pl
|   ---crm/
|   |   |
|   |   |-crm.csv
|   |   |- crm.py
|   ---hr/
|   |   |
|   |   |-hr.csv
|   |   |-hr.py
|   ---sales/
|       |
|       |-sales.csv
|       |-sales.py
---view/
    |
    |-terminal.py
```

##### Copyright Group 2. March 2023. MIT License.
