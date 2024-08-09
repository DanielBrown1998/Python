def criar_saudacao(nome):
    def saudacao(age):
        return f'Olá, {nome}, {age}!'
    return saudacao
saudacao = criar_saudacao('Daniel')
print(saudacao(26))  # Olá, Daniel!
#
# The function criar_saudacao() returns a function saudacao() that uses the name parameter from the outer function.
#
# This is a closure in action. A closure is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used later when the function is invoked and the defining scope is no longer available.
#
# In this case, the free variable is the name parameter of the criar_saudacao() function. The saudacao() function retains the value of name even after the criar_saudacao() function has finished executing.
#
# This allows the saudacao() function to use the name parameter from the outer function when it is called later.
#
# Closures are a powerful feature in Python that allows you to create functions that can capture and retain the context in which they were created.
#
# You can use closures to create functions that have access to variables from the enclosing scope, even after the scope has finished executing.
#
# This can be useful for creating functions that generate other functions, or for creating functions that have access to shared state that is hidden from the outside world.
#
# In this example, the criar_saudacao() function creates a closure that generates personalized greetings for different names. The saudacao() function retains the name parameter from the criar_saudacao() function, allowing it to generate greetings with the specified name.     
#
