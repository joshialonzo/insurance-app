## Requirements

* Read the 'payments' document and register: agentes, contratantes, polizas, and payments.
* Read the 'poliza' document and register old payments with existing poliza.
* See the list of payments for each poliza.
* Append the new payments to the list of payments
* Compute the date of the last payments for each user.
* Compute the date of the next payments for each user.
* Compute the list of customers with monthly poliza that has 5/4/3/2/1 days to pay.
* Compute the list of customers with non-monthly poliza that has 5/4/3/2/1 days or 3/2/1 weeks to pay.
* Create an UI to upload 'payments' file.
* Create an UI to upload 'policies' file.

## Input documents

* payments
* policies

## Models

* User
    * number
    * name

* Customer(User)
    * user
    * number
    * name -> payments.csv -> Contratante

* Agent(User)
    * user
    * number -> payments.csv -> Número de agente
    * name -> payments.csv -> Nombre de agente

* Policy
    * number -> payments.csv -> Poliza
    * contratante
    * periodicity -> payments.csv -> Forma de pago

* Validity
    * policy
    * periodicity
    * Start date -> payments.csv -> Inicio de Vigencia
    * End date -> payments.csv -> Fin de Vigencia

* Payment
    * Vigencia
    * Estatus -> payments.csv -> Estatus
    * Prima neta -> payments.csv -> Prima Neta
    * Date -> payments.csv -> Fecha Aplicación
    * Payment type -> payments.csv -> Conducto
    * Recargos -> payments.csv -> Recargos
    * Gastos de expedición -> payments.csv -> Gastos de expedición
    * Impuestos -> payments.csv -> Impuestos
    * Folio de endoso -> payments.csv -> Folio de Endoso
    * Prima total -> payments.csv -> Prima Total

* Report
    * name

* Report Item
    * Report
    * Description

## To Do list

* Read 'data' folder
* Read 'insurance-app' folder
* Open and read 'polizas' file
* Open and read 'payments' file
* Read all the 'polizas' columns
* Read all the 'payments' columns

## Ideas

* Use React Native for a Desktop application
* User React Native for a Web Application