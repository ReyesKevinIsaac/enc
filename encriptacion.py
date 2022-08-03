from cryptography.fernet import Fernet

dato=input() ## Dato
key=Fernet.generate_key() 
oCifrado = Fernet(key)
d_encriptado=oCifrado.encrypt(str.encode(dato))  ## Encriptación
    
d_desencriptado_b = oCifrado.decrypt(d_encriptado) ## Desencriptación

print('Encriptado: ',d_encriptado)
print()
print('Desencriptado: ',d_desencriptado_b)
