## Requirements

* Read the 'payments' document and register: agentes, contratantes, policies, and payments.
* Read the 'policies' document and register old payments with existing policy.
* See the list of payments for each policy.
* Append the new payments to the list of payments
* Compute the date of the last payments for each user.
* Compute the date of the next payments for each user.
* Compute the list of customers with monthly policy that has 5/4/3/2/1 days to pay.
* Compute the list of customers with non-monthly policy that has 5/4/3/2/1 days or 3/2/1 weeks to pay.
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
    * number -> payments.csv -> policy
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

✅ Read 'data' folder.
✅ Read 'insurance-app' folder.
✅ Open and read 'payments' file.
✅ Create a customer with idempotency.
✅ Create an agent with idempotency.
✅ Create a policy with idempotency.
✅ Create a validity with idempotency.
✅ Create a payment with idempotency.
✅ Create line objects.
✅ Create line objects with idempotency.
✅ Create all the payments with idempotency.
TODO: Create a CLI to load 'payments' file.
TODO: Read all the policies stored in the memory storage.
TODO: Get the list of payments for each policy.
TODO: Compute the next payment for each customer.
TODO: Compute the date of the last payments for each user.
TODO: Compute the date of the next payments for each user.
TODO: Compute the list of customers with monthly policy that has 5/4/3/2/1 days to pay.
TODO: Compute the list of customers with non-monthly policy that has 5/4/3/2/1 days or 3/2/1 weeks to pay.
TODO: Create a CLI to load 'policies' file.
TODO: Create an GUI to upload 'payments' file.
TODO: Create an GUI to upload 'policies' file.
TODO: Implement storage with CSV files in a 'db' folder.
TODO: Feed the storage with the 'policies' file.

## Ideas

* Use React, Electron, and Python to create a Desktop Application.
* Use React, FastAPI, and Firebase to create a Web Application.