## Description

The current process consist of a person (Nora) sending a text message via Whatsapp to all the chilean employees, the message contains today's menu with the different alternatives for lunch. 

> Hola!  
> Dejo el menú de hoy :)
>
> Opción 1: Pastel de choclo, Ensalada y Postre  
> Opción 2. Arroz con nugget de pollo, Ensalada y Postre  
> Opción 3: Arroz con hamburguesa, Ensalada y Postre  
> Opción 4: Ensalada premium de pollo y Postre  
>
> Tengan lindo día!

With the new system, Nora should be able to:

- Create a menu for a specific date.
- Send a Slack reminder with today's menu to all chilean employees (this process needs to be asynchronous).

The employees should be able to:

- Choose their preferred meal (until 11 AM CLT).
- Specify customizations (e.g. no tomatoes in the salad).

Nora should be the only user to be able to see what the Cornershop employees have requested, and to create and edit today's menu. The employees should be able to specify what they want for lunch but they shouldn't be able to see what others have requested. 

NOTE: The slack reminders must contain an URL to today's menu with the following pattern https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (an UUID), this page must not require authentication of any kind.

## Aspects to be evaluated

Since the system is very simple (yet powerful in terms of yumminess) we'll be evaluating, besides functionality, these aspects:

- Testing
- Documentation
- Software design
- Programming style
- Appropriate framework use

## Aspects to be ignored

- Visual design of the solution
- Deployment of the solution

## Restrictions

- The usage of Django's admin is forbidden.
